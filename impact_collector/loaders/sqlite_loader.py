"""
Loader SQLite — persiste evidências nas tabelas impact_sources / impact_evidences / impact_materials.

Usa o engine do Fashion OS (SQLAlchemy + SQLite).
Sprint 3: trocar engine pelo Supabase Postgres sem mudar esta interface.
"""

from __future__ import annotations
import json
import logging
import statistics
from datetime import datetime

from sqlalchemy.orm import Session

from impact_collector.models import ImpactEvidence as CollectorEvidence
from impact_collector.normalizers.aliases import get_aliases

logger = logging.getLogger(__name__)

# Nomes amigáveis por fibra_id
_FIBER_NAMES: dict[str, tuple[str, str]] = {
    "algodao_convencional": ("Algodão Convencional", "natural_vegetal"),
    "algodao_organico":     ("Algodão Orgânico", "natural_vegetal"),
    "poliester_virgem":     ("Poliéster Virgem", "sintetica_petroleo"),
    "poliester_reciclado":  ("Poliéster Reciclado (rPET)", "sintetica_reciclada"),
    "lyocell_tencel":       ("Lyocell / Tencel", "mmcf"),
    "viscose_modal":        ("Viscose / Modal / EcoVero", "mmcf"),
    "linho":                ("Linho (Flax)", "natural_vegetal"),
    "la":                   ("Lã (Wool)", "natural_animal"),
    "poliamida_nylon_virgem": ("Nylon Virgem (PA6/PA66)", "sintetica_petroleo"),
    "poliamida_reciclada":  ("Nylon Reciclado (Econyl)", "sintetica_reciclada"),
    "elastano_spandex":     ("Elastano / Spandex", "sintetica_petroleo"),
    "canamo":               ("Cânhamo (Hemp)", "natural_vegetal"),
}


def _get_or_create_source(db: Session, evidence: CollectorEvidence):
    """Retorna ImpactSource existente ou cria novo."""
    from app.models.models import ImpactSource as OrmSource

    src = evidence.source
    # Buscar por DOI (mais estável) ou por nome+url
    if src.doi:
        existing = db.query(OrmSource).filter_by(doi=src.doi).first()
        if existing:
            return existing

    existing = db.query(OrmSource).filter_by(nome=src.nome, url=src.url).first()
    if existing:
        return existing

    orm_src = OrmSource(
        tipo=src.tipo,
        nome=src.nome,
        doi=src.doi,
        url=src.url,
        titulo=src.titulo,
        autores=json.dumps(src.autores, ensure_ascii=False) if src.autores else None,
        ano_publicacao=src.ano_publicacao,
        journal=src.journal,
        acesso_aberto=src.acesso_aberto,
        licenca=src.licenca,
        raw_storage_path=src.raw_storage_path,
        status="coletado",
    )
    db.add(orm_src)
    db.flush()
    return orm_src


def save_evidence_to_db(db: Session, evidence: CollectorEvidence) -> bool:
    """
    Salva uma ImpactEvidence no banco SQLite.
    Retorna False se duplicata (por fingerprint).
    """
    from app.models.models import ImpactEvidence as OrmEvidence

    if not evidence.has_any_value():
        return False

    fp = _fingerprint(evidence)
    existing = db.query(OrmEvidence).filter_by(fingerprint=fp).first()
    if existing:
        logger.debug("Evidência duplicada ignorada: %s (%s)", evidence.fibra_id, fp)
        return False

    orm_src = _get_or_create_source(db, evidence)

    orm_ev = OrmEvidence(
        source_id=orm_src.id,
        fibra_id=evidence.fibra_id,
        fingerprint=fp,
        co2eq_kg_por_kg=evidence.co2eq_kg_por_kg,
        agua_l_por_kg=evidence.agua_l_por_kg,
        energia_mj_por_kg=evidence.energia_mj_por_kg,
        escopo_lca=evidence.escopo_lca,
        metodologia_acv=evidence.metodologia_acv,
        regiao_origem=evidence.regiao_origem,
        ano_referencia=evidence.ano_referencia,
        pagina_referencia=evidence.pagina_referencia,
        trecho_original=evidence.trecho_original,
        confianca=evidence.confianca,
        validado_humano=evidence.validado_humano,
        extraction_model=evidence.extraction_model,
        extraction_cost_usd=evidence.extraction_cost_usd,
    )
    db.add(orm_ev)
    return True


def save_evidences_to_db(db: Session, evidences: list[CollectorEvidence]) -> int:
    """Salva lista de evidências. Faz commit único no final. Retorna n salvas."""
    saved = 0
    for ev in evidences:
        if save_evidence_to_db(db, ev):
            saved += 1
    db.commit()
    logger.info("SQLite: %d/%d evidências salvas", saved, len(evidences))
    return saved


def update_impact_material_aggregate(db: Session, fibra_id: str) -> None:
    """
    Recalcula e upsert o ImpactMaterial agregado para uma fibra.

    Usa a mediana das evidências com confiança 'alta' ou 'media'
    e escopo 'cradle-to-gate'.
    """
    from app.models.models import ImpactEvidence as OrmEvidence, ImpactMaterial as OrmMaterial

    evidences = (
        db.query(OrmEvidence)
        .filter(
            OrmEvidence.fibra_id == fibra_id,
            OrmEvidence.confianca.in_(["alta", "media"]),
        )
        .all()
    )

    if not evidences:
        return

    co2_vals  = [e.co2eq_kg_por_kg  for e in evidences if e.co2eq_kg_por_kg  is not None]
    agua_vals = [e.agua_l_por_kg    for e in evidences if e.agua_l_por_kg    is not None]
    en_vals   = [e.energia_mj_por_kg for e in evidences if e.energia_mj_por_kg is not None]

    def _median(vals):
        return round(statistics.median(vals), 3) if vals else None

    def _min(vals):
        return min(vals) if vals else None

    def _max(vals):
        return max(vals) if vals else None

    has_alta = any(e.confianca == "alta" for e in evidences)
    confianca_agg = "alta" if has_alta else "media"

    nome_pt, categoria = _FIBER_NAMES.get(fibra_id, (fibra_id, "desconhecida"))
    aliases = get_aliases(fibra_id)

    material = db.query(OrmMaterial).filter_by(fibra_id=fibra_id).first()
    if not material:
        material = OrmMaterial(fibra_id=fibra_id)
        db.add(material)

    material.nome_pt             = nome_pt
    material.categoria           = categoria
    material.aliases_json        = json.dumps(aliases, ensure_ascii=False)
    material.co2eq_kg_por_kg_agg = _median(co2_vals)
    material.agua_l_por_kg_agg   = _median(agua_vals)
    material.energia_mj_por_kg_agg = _median(en_vals)
    material.co2eq_range_min     = _min(co2_vals)
    material.co2eq_range_max     = _max(co2_vals)
    material.agua_range_min      = _min(agua_vals)
    material.agua_range_max      = _max(agua_vals)
    material.confianca_agg       = confianca_agg
    material.n_evidencias        = len(evidences)
    material.regra_agregacao     = "mediana evidências confiança alta+media"
    material.atualizado_em       = datetime.utcnow()

    db.commit()
    logger.info(
        "ImpactMaterial atualizado: %s | CO2: %s | n=%d | confiança: %s",
        fibra_id, material.co2eq_kg_por_kg_agg, len(evidences), confianca_agg,
    )


def _fingerprint(evidence: CollectorEvidence) -> str:
    import hashlib
    key = (
        f"{evidence.fibra_id}|{evidence.source.nome}|"
        f"{evidence.escopo_lca}|{evidence.co2eq_kg_por_kg}|"
        f"{evidence.agua_l_por_kg}|{evidence.ano_referencia}"
    )
    return hashlib.md5(key.encode()).hexdigest()[:16]
