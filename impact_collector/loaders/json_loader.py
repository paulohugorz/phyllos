"""
Loader para JSON local — persiste evidências em arquivo JSONL para o Sprint 1.

No Sprint 2, será substituído/complementado pelo loader Supabase.
Formato: um JSON por linha (JSONL), fácil de ler incrementalmente.
"""

from __future__ import annotations
import json
import os
import logging
from datetime import datetime
from impact_collector.models import ImpactEvidence

logger = logging.getLogger(__name__)

DEFAULT_OUTPUT_PATH = "produto/catalogo-impacto/evidencias-coletadas.jsonl"


def _fingerprint(evidence: ImpactEvidence) -> str:
    """Hash simples para deduplicação — fibra + fonte + escopo."""
    import hashlib
    key = f"{evidence.fibra_id}|{evidence.source.nome}|{evidence.escopo_lca}|{evidence.co2eq_kg_por_kg}"
    return hashlib.md5(key.encode()).hexdigest()[:12]


def save_evidence(
    evidence: ImpactEvidence,
    output_path: str = DEFAULT_OUTPUT_PATH,
) -> bool:
    """Salva uma evidência no arquivo JSONL de saída. Retorna False se duplicata."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fp = _fingerprint(evidence)
    existing = load_evidences(output_path)
    if any(r.get("_fp") == fp for r in existing):
        logger.debug("Evidência duplicada ignorada: %s (%s)", evidence.fibra_id, fp)
        return False

    record = evidence.to_dict()
    record["salvo_em"] = datetime.utcnow().isoformat()
    record["_fp"] = fp

    with open(output_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    logger.debug("Evidência salva: %s — CO2: %s", evidence.fibra_id, evidence.co2eq_kg_por_kg)
    return True

    logger.debug("Evidência salva: %s — CO2: %s", evidence.fibra_id, evidence.co2eq_kg_por_kg)


def save_evidences(
    evidences: list[ImpactEvidence],
    output_path: str = DEFAULT_OUTPUT_PATH,
) -> int:
    """Salva lista de evidências ignorando duplicatas. Retorna quantas foram salvas."""
    saved = 0
    for ev in evidences:
        if ev.has_any_value() and save_evidence(ev, output_path):
            saved += 1
    logger.info("Salvas %d/%d evidências em %s", saved, len(evidences), output_path)
    return saved


def load_evidences(output_path: str = DEFAULT_OUTPUT_PATH) -> list[dict]:
    """Carrega todas as evidências salvas."""
    if not os.path.exists(output_path):
        return []
    records = []
    with open(output_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return records


def generate_summary_report(output_path: str = DEFAULT_OUTPUT_PATH) -> dict:
    """Gera relatório de sumário das evidências coletadas."""
    records = load_evidences(output_path)

    by_fiber: dict[str, list] = {}
    for r in records:
        fid = r.get("fibra_id", "desconhecida")
        by_fiber.setdefault(fid, []).append(r)

    summary = {
        "total_evidencias": len(records),
        "fibras_cobertas": len(by_fiber),
        "por_fibra": {},
        "gerado_em": datetime.utcnow().isoformat(),
    }

    for fibra_id, evs in by_fiber.items():
        co2_vals = [e["co2eq_kg_por_kg"] for e in evs if e.get("co2eq_kg_por_kg")]
        agua_vals = [e["agua_l_por_kg"] for e in evs if e.get("agua_l_por_kg")]
        confiancas = [e.get("confianca", "baixa") for e in evs]

        summary["por_fibra"][fibra_id] = {
            "n_evidencias": len(evs),
            "co2_media": round(sum(co2_vals) / len(co2_vals), 2) if co2_vals else None,
            "co2_min": min(co2_vals) if co2_vals else None,
            "co2_max": max(co2_vals) if co2_vals else None,
            "agua_media": round(sum(agua_vals) / len(agua_vals), 0) if agua_vals else None,
            "confianca_alta": confiancas.count("alta"),
            "confianca_media": confiancas.count("media"),
            "confianca_baixa": confiancas.count("baixa"),
        }

    return summary
