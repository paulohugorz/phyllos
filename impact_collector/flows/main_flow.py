"""
Flow principal do Impact Collector — orquestra coleta, parsing, extração e carga.

Sprint 1: OpenAlex + EPD International + LCA Commons
Sem Prefect no piloto — cron simples ou execução manual via CLI.
"""

from __future__ import annotations
import logging
import time
import os
from impact_collector.config import (
    PRIORITY_FIBERS,
    MAX_ARTICLES_PER_FIBER,
    PDF_CACHE_DIR,
)
from impact_collector.models import ImpactEvidence, ImpactSource
from impact_collector.sources.openalex import search_lca_articles
from impact_collector.sources.epd_international import (
    get_known_epds,
    get_ground_truth,
    search_epd_portal,
)
from impact_collector.sources.lca_commons import get_known_datasets, fetch_dataset_metadata
from impact_collector.parsers.pdf_parser import download_pdf, get_lca_chunks
from impact_collector.extractors.llm_extractor import extract_impact_from_text
from impact_collector.normalizers.confidence import gate2_unit_coherence, gate3_cross_check
from impact_collector.loaders.json_loader import save_evidences, generate_summary_report

logger = logging.getLogger(__name__)

# Nome amigável das fibras para prompts LLM
FIBER_NAMES_PT: dict[str, str] = {
    "algodao_convencional": "Algodão Convencional",
    "algodao_organico": "Algodão Orgânico",
    "poliester_reciclado": "Poliéster Reciclado (rPET)",
    "lyocell_tencel": "Lyocell / Tencel",
    "linho": "Linho (Flax)",
    "la": "Lã (Wool)",
}


def collect_material_impact(
    fibers: list[str] | None = None,
    sources: list[str] | None = None,
    max_articles: int | None = None,
    output_path: str = "produto/catalogo-impacto/evidencias-coletadas.jsonl",
    dry_run: bool = False,
) -> list[ImpactEvidence]:
    """
    Interface pública do coletor.

    Args:
        fibers: lista de fibra_ids. None = todas as prioritárias.
        sources: ["openalex", "epd", "lca_commons"] — None = todas.
        max_articles: sobrescreve MAX_ARTICLES_PER_FIBER do config.
        output_path: onde salvar as evidências em JSONL.
        dry_run: coleta mas não salva.

    Returns:
        Lista de ImpactEvidence coletadas e validadas.
    """
    fibers_to_collect = fibers or PRIORITY_FIBERS
    sources_to_use = set(sources or ["openalex", "epd", "lca_commons"])
    max_per_fiber = max_articles or MAX_ARTICLES_PER_FIBER

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    all_evidences: list[ImpactEvidence] = []

    for fibra_id in fibers_to_collect:
        fibra_nome = FIBER_NAMES_PT.get(fibra_id, fibra_id)
        logger.info("═══ Coletando: %s (%s) ═══", fibra_nome, fibra_id)
        fiber_evidences: list[ImpactEvidence] = []

        # ── Fonte 1: EPD International (dados de alta confiança, começar aqui) ──
        if "epd" in sources_to_use:
            fiber_evidences.extend(
                _collect_from_epd(fibra_id, fibra_nome)
            )

        # ── Fonte 2: LCA Commons (datasets curados americanos) ──
        if "lca_commons" in sources_to_use:
            fiber_evidences.extend(
                _collect_from_lca_commons(fibra_id, fibra_nome)
            )

        # ── Fonte 3: OpenAlex → download PDF → LLM extraction ──
        if "openalex" in sources_to_use:
            fiber_evidences.extend(
                _collect_from_openalex(fibra_id, fibra_nome, max_per_fiber, fiber_evidences)
            )

        # Gate 2 em todas as evidências da fibra
        fiber_evidences = [gate2_unit_coherence(e) for e in fiber_evidences]

        logger.info(
            "Fibra %s: %d evidências com dados válidos",
            fibra_id,
            sum(1 for e in fiber_evidences if e.has_any_value()),
        )
        all_evidences.extend(fiber_evidences)

    valid = [e for e in all_evidences if e.has_any_value()]
    logger.info("Total geral: %d evidências válidas em %d fibras", len(valid), len(fibers_to_collect))

    if not dry_run and valid:
        saved = save_evidences(valid, output_path)
        logger.info("%d evidências salvas em %s", saved, output_path)
        report = generate_summary_report(output_path)
        _print_summary(report)

    return valid


def _collect_from_epd(fibra_id: str, fibra_nome: str) -> list[ImpactEvidence]:
    """Carrega evidências de EPDs curadas + valores ground truth."""
    evidences = []

    # Valores ground truth das EPDs Lenzing (extraídos manualmente, confiança alta)
    gt = get_ground_truth(fibra_id)
    if gt:
        source = ImpactSource(
            tipo="pdf",
            nome=gt["fonte"],
            url=None,
            acesso_aberto=True,
        )
        ev = ImpactEvidence(
            fibra_id=fibra_id,
            source=source,
            co2eq_kg_por_kg=gt.get("co2eq_kg_por_kg"),
            agua_l_por_kg=gt.get("agua_l_por_kg"),
            energia_mj_por_kg=gt.get("energia_mj_por_kg"),
            escopo_lca=gt.get("escopo"),
            confianca=gt.get("confianca", "alta"),
            validado_humano=True,
            extraction_model="manual",
        )
        evidences.append(ev)
        logger.info("EPD ground truth carregado para %s (confiança: %s)", fibra_id, ev.confianca)

    # Metadados de EPDs disponíveis (para download manual posterior)
    known = get_known_epds(fibra_id)
    for epd in known:
        logger.info("EPD disponível para %s: %s (%s)", fibra_id, epd["nome"], epd.get("url_pdf", ""))

    return evidences


def _collect_from_lca_commons(fibra_id: str, fibra_nome: str) -> list[ImpactEvidence]:
    """Registra datasets disponíveis no LCA Commons como fontes rastreáveis."""
    evidences = []
    datasets = get_known_datasets(fibra_id)
    for ds in datasets:
        source = ImpactSource(
            tipo="bulk_dump",
            nome=ds["nome"],
            url=ds.get("url"),
            ano_publicacao=ds.get("ano"),
            acesso_aberto=True,
        )
        # LCA Commons requer processamento do arquivo ILCD/JSON-LD para extrair valores
        # No Sprint 1 registramos a fonte — valores serão extraídos no Sprint 2 via olca-ipc
        logger.info(
            "LCA Commons dataset registrado para %s: %s (extração no Sprint 2)",
            fibra_id, ds["nome"],
        )
    return evidences  # vazio no Sprint 1 — fonte registrada, dados no Sprint 2


def _collect_from_openalex(
    fibra_id: str,
    fibra_nome: str,
    max_articles: int,
    existing_evidences: list[ImpactEvidence],
) -> list[ImpactEvidence]:
    """Busca artigos no OpenAlex, baixa PDFs e extrai dados via LLM."""
    from impact_collector.config import ANTHROPIC_API_KEY

    evidences = []
    sources = search_lca_articles(fibra_id, max_results=max_articles)

    if not sources:
        logger.info("OpenAlex: nenhum artigo encontrado para %s", fibra_id)
        return []

    logger.info("OpenAlex: processando %d artigos para %s", len(sources), fibra_id)

    for source in sources:
        if not source.url or not source.acesso_aberto:
            logger.debug("Artigo sem PDF acessível: %s", source.titulo)
            continue

        # Download do PDF
        pdf_path = download_pdf(source.url, PDF_CACHE_DIR)
        if not pdf_path:
            continue

        # Extração de chunks relevantes
        text = get_lca_chunks(pdf_path)
        if not text.strip():
            logger.debug("Sem texto LCA extraído de: %s", source.titulo)
            continue

        # Extração via LLM (só se API key configurada)
        if not ANTHROPIC_API_KEY:
            logger.warning(
                "ANTHROPIC_API_KEY não configurada — pulando extração LLM. "
                "Configure a variável e reexecute."
            )
            break

        evidence = extract_impact_from_text(text, fibra_id, fibra_nome, source)

        if evidence and evidence.has_any_value():
            # Gate 3: cross-check com evidências existentes
            evidence, passed = gate3_cross_check(evidence, existing_evidences + evidences)
            evidences.append(evidence)

            logger.info(
                "✓ %s — CO2: %s kgCO2e/kg | Água: %s L/kg | Confiança: %s",
                fibra_id,
                evidence.co2eq_kg_por_kg,
                evidence.agua_l_por_kg,
                evidence.confianca,
            )

        # Rate limiting respeitoso
        time.sleep(0.5)

    return evidences


def _print_summary(report: dict) -> None:
    print("\n" + "═" * 60)
    print("RELATÓRIO DE COLETA — PHYLLOS Impact Collector")
    print("═" * 60)
    print(f"Total de evidências: {report['total_evidencias']}")
    print(f"Fibras cobertas:     {report['fibras_cobertas']}")
    print()

    for fibra_id, stats in report.get("por_fibra", {}).items():
        print(f"  {fibra_id}")
        print(f"    Evidências:   {stats['n_evidencias']}")
        if stats.get("co2_media"):
            print(f"    CO2 média:    {stats['co2_media']} kgCO2e/kg")
            print(f"    CO2 range:    {stats['co2_min']}–{stats['co2_max']}")
        if stats.get("agua_media"):
            print(f"    Água média:   {stats['agua_media']} L/kg")
        print(f"    Confiança:    alta={stats['confianca_alta']} "
              f"media={stats['confianca_media']} baixa={stats['confianca_baixa']}")
        print()

    print("═" * 60)
