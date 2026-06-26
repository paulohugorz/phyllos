"""
Seed de dados de referência no banco SQLite.

Carrega todas as evidências curadas de reference_data.py e EPD ground truth
para o banco, calcula os agregados por fibra.

Uso:
    python3 -m impact_collector.flows.seed_reference_data
"""

from __future__ import annotations
import logging
import sys
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)


def run_seed() -> None:
    # Adicionar raiz do projeto ao path para importar app.*
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    if root not in sys.path:
        sys.path.insert(0, root)

    from app.core.database import SessionLocal, engine, run_migrations
    from app.models import models  # noqa: F401 — garante que as tabelas são registradas no Base

    # Criar tabelas novas (create_all é idempotente)
    from app.core.database import Base
    Base.metadata.create_all(bind=engine)
    run_migrations()

    from impact_collector.sources.reference_data import REFERENCE_DATA, get_reference_evidences
    from impact_collector.sources.epd_international import EPD_GROUND_TRUTH
    from impact_collector.models import ImpactEvidence as CollectorEvidence, ImpactSource
    from impact_collector.loaders.sqlite_loader import (
        save_evidences_to_db,
        update_impact_material_aggregate,
    )

    db = SessionLocal()
    total_saved = 0
    fiber_ids: set[str] = set()

    try:
        # ── 1. Evidências de referência curadas ──────────────────────────
        for fibra_id, entries in REFERENCE_DATA.items():
            evidences = []
            for entry in entries:
                if not any([entry.get("co2eq_kg_por_kg"), entry.get("agua_l_por_kg"), entry.get("energia_mj_por_kg")]):
                    continue

                source = ImpactSource(
                    tipo="pdf",
                    nome=entry["fonte"],
                    ano_publicacao=entry.get("ano"),
                    acesso_aberto=True,
                )
                ev = CollectorEvidence(
                    fibra_id=fibra_id,
                    source=source,
                    co2eq_kg_por_kg=entry.get("co2eq_kg_por_kg"),
                    agua_l_por_kg=entry.get("agua_l_por_kg"),
                    energia_mj_por_kg=entry.get("energia_mj_por_kg"),
                    escopo_lca=entry.get("escopo"),
                    metodologia_acv=entry.get("metodologia"),
                    regiao_origem=entry.get("regiao"),
                    ano_referencia=entry.get("ano"),
                    confianca=entry.get("confianca", "media"),
                    validado_humano=(entry.get("confianca") == "alta"),
                    extraction_model="manual",
                )
                evidences.append(ev)

            if evidences:
                saved = save_evidences_to_db(db, evidences)
                total_saved += saved
                fiber_ids.add(fibra_id)
                logger.info("Referência: %s — %d/%d salvas", fibra_id, saved, len(evidences))

        # ── 2. EPD ground truth Lenzing ──────────────────────────────────
        for fibra_id, gt in EPD_GROUND_TRUTH.items():
            source = ImpactSource(
                tipo="pdf",
                nome=gt["fonte"],
                acesso_aberto=True,
                ano_publicacao=2023,
            )
            ev = CollectorEvidence(
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
            saved = save_evidences_to_db(db, [ev])
            total_saved += saved
            fiber_ids.add(fibra_id)

        # ── 3. Recalcular agregados para todas as fibras atualizadas ─────
        for fibra_id in fiber_ids:
            update_impact_material_aggregate(db, fibra_id)

        logger.info("Seed concluído: %d evidências inseridas em %d fibras", total_saved, len(fiber_ids))

    finally:
        db.close()

    return total_saved


if __name__ == "__main__":
    run_seed()
