"""
Endpoints do catálogo de fatores de impacto ambiental.

GET  /catalogo/fibras                   — lista todas as fibras disponíveis
GET  /catalogo/fibras/{fibra_id}        — detalhe de uma fibra
POST /catalogo/calcular-blend           — fatores ponderados por composição
POST /catalogo/calcular-peca            — indicadores por peça (blend + gramatura + área)
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.catalogo_impacto import (
    CatalogoImpactoError,
    calcular_blend,
    listar_fibras,
    obter_fibra,
)
from app.services.dpp_calculator import (
    DppCalculationError,
    DppCalculationInput,
    calculate_dpp_indicators,
)

router = APIRouter(prefix="/catalogo", tags=["Catálogo de Impacto"])


# ── Schemas ────────────────────────────────────────────────────────────

class FibraItem(BaseModel):
    fibra_id: str = Field(
        ...,
        example="algodao_convencional",
        description=(
            "ID canônico ou qualquer alias: 'cotton', 'rPET', 'TENCEL™', "
            "'lã merino', 'Recycled Polyester', etc."
        ),
    )
    percentual: float = Field(..., ge=0, le=100, example=95.0)


class BlendRequest(BaseModel):
    composicao: list[FibraItem] = Field(
        ...,
        min_length=1,
        example=[
            {"fibra_id": "algodao_convencional", "percentual": 95},
            {"fibra_id": "elastano_spandex", "percentual": 5},
        ],
    )

    @model_validator(mode="after")
    def validar_soma(self):
        total = sum(f.percentual for f in self.composicao)
        if abs(total - 100) > 0.5:
            raise ValueError(f"Soma dos percentuais deve ser 100 (recebido: {total})")
        return self


class PecaRequest(BlendRequest):
    gramatura_g_m2: float = Field(..., gt=0, example=180.0,
        description="Gramatura do tecido em g/m²")
    area_peca_m2: float = Field(..., gt=0, example=1.4,
        description="Área da peça já cortada em m²")
    perda_corte_pct: float = Field(default=15.0, ge=0, lt=100,
        description="Percentual de perda no corte (padrão: 15%)")


# ── Endpoints ──────────────────────────────────────────────────────────

@router.get("/fibras")
def listar():
    """Lista todas as fibras disponíveis no catálogo com seus fatores de impacto."""
    fibras = listar_fibras()
    return {
        "total": len(fibras),
        "fibras": [
            {
                "fibra_id": f.fibra_id,
                "nome_pt": f.nome_pt,
                "categoria": f.categoria,
                "origem": f.origem,
                "certificacoes_compativeis": f.certificacoes_compativeis,
                "indicadores": {
                    "co2eq_kg_por_kg":    f.co2eq_kg_por_kg,
                    "agua_l_por_kg":      f.agua_l_por_kg,
                    "energia_mj_por_kg":  f.energia_mj_por_kg,
                    "energia_kwh_por_kg": f.energia_kwh_por_kg,
                },
                "confianca": f.confianca,
                "fonte": f.fonte,
                "nota_curadoria": f.nota_curadoria,
            }
            for f in fibras
        ],
    }


@router.get("/fibras/{fibra_id}")
def detalhe_fibra(fibra_id: str):
    """Retorna os fatores de impacto de uma fibra específica."""
    try:
        f = obter_fibra(fibra_id)
    except CatalogoImpactoError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {
        "fibra_id": f.fibra_id,
        "nome_pt": f.nome_pt,
        "categoria": f.categoria,
        "origem": f.origem,
        "certificacoes_compativeis": f.certificacoes_compativeis,
        "indicadores": {
            "co2eq_kg_por_kg":    f.co2eq_kg_por_kg,
            "agua_l_por_kg":      f.agua_l_por_kg,
            "energia_mj_por_kg":  f.energia_mj_por_kg,
            "energia_kwh_por_kg": f.energia_kwh_por_kg,
        },
        "confianca": f.confianca,
        "fonte": f.fonte,
        "metodologia": f.metodologia,
        "nota_curadoria": f.nota_curadoria,
    }


@router.post("/calcular-blend")
def calcular_fatores_blend(body: BlendRequest):
    """
    Calcula os fatores de impacto ponderados para uma composição de fibras.

    Retorna fatores prontos para usar em /pecas/{codigo}/dpp/publicar
    (campos agua_litros_kg, energia_kwh_kg, carbono_kgco2e_kg da FichaTecnica).
    """
    try:
        blend = calcular_blend([f.model_dump() for f in body.composicao])
    except CatalogoImpactoError as e:
        raise HTTPException(status_code=422, detail=str(e))

    return {
        "composicao": [f.model_dump() for f in body.composicao],
        "fatores_blend": {
            "co2eq_kg_por_kg":    blend.co2eq_kg_por_kg,
            "agua_l_por_kg":      blend.agua_l_por_kg,
            "energia_mj_por_kg":  blend.energia_mj_por_kg,
            "energia_kwh_por_kg": blend.energia_kwh_por_kg,
        },
        "para_ficha_tecnica": {
            "carbono_kgco2e_kg": blend.co2eq_kg_por_kg,
            "agua_litros_kg":    blend.agua_l_por_kg,
            "energia_kwh_kg":    blend.energia_kwh_por_kg,
            "fonte_carbono_kgco2e_kg": blend.fonte,
            "fonte_agua_litros_kg":    blend.fonte,
            "fonte_energia_kwh_kg":    blend.fonte,
            "metodologia_fatores_impacto": blend.metodologia,
        },
        "detalhes_por_fibra": [
            {
                "fibra_id":           d.fibra_id,
                "nome_pt":            d.nome_pt,
                "percentual":         d.percentual,
                "co2eq_kg_por_kg":    d.co2eq_kg_por_kg,
                "agua_l_por_kg":      d.agua_l_por_kg,
                "energia_mj_por_kg":  d.energia_mj_por_kg,
                "co2_contribuicao":   round(d.co2eq_kg_por_kg * d.percentual / 100, 4),
                "confianca":          d.confianca,
                "fonte":              d.fonte,
                "origem_dado":        d.origem_dado,
            }
            for d in blend.detalhes
        ],
        "meta": {
            "fibras_usadas": blend.fibras_usadas,
            "confianca": blend.confianca,
            "metodologia": blend.metodologia,
            "fonte": blend.fonte,
            "aviso": blend.aviso,
        },
    }


@router.get("/fibras/{fibra_id}/evidencias")
def listar_evidencias(fibra_id: str, db: Session = Depends(get_db)):
    """
    Lista as evidências de impacto coletadas para uma fibra específica.

    Retorna todos os valores com rastreabilidade completa:
    fonte, metodologia, escopo, região, confiança e trecho original.
    Endpoint-chave para o DPP e para futuros clientes B2B do catálogo.
    """
    from app.models.models import ImpactEvidence, ImpactMaterial, ImpactSource

    material = db.query(ImpactMaterial).filter_by(fibra_id=fibra_id).first()
    evidences = (
        db.query(ImpactEvidence)
        .filter_by(fibra_id=fibra_id)
        .order_by(ImpactEvidence.confianca.desc(), ImpactEvidence.ano_referencia.desc())
        .all()
    )

    if not material and not evidences:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma evidência de impacto coletada para fibra '{fibra_id}'. "
                   "Execute o seed: python3 -m impact_collector.flows.seed_reference_data",
        )

    return {
        "fibra_id": fibra_id,
        "agregado": {
            "co2eq_kg_por_kg":     material.co2eq_kg_por_kg_agg  if material else None,
            "agua_l_por_kg":       material.agua_l_por_kg_agg    if material else None,
            "energia_mj_por_kg":   material.energia_mj_por_kg_agg if material else None,
            "co2eq_range":         [material.co2eq_range_min, material.co2eq_range_max] if material else None,
            "agua_range":          [material.agua_range_min,  material.agua_range_max]  if material else None,
            "confianca":           material.confianca_agg         if material else None,
            "n_evidencias":        material.n_evidencias          if material else len(evidences),
            "regra_agregacao":     material.regra_agregacao       if material else None,
            "atualizado_em":       material.atualizado_em.isoformat() if material and material.atualizado_em else None,
        },
        "evidencias": [
            {
                "id": ev.id,
                "co2eq_kg_por_kg":   ev.co2eq_kg_por_kg,
                "agua_l_por_kg":     ev.agua_l_por_kg,
                "energia_mj_por_kg": ev.energia_mj_por_kg,
                "escopo_lca":        ev.escopo_lca,
                "metodologia_acv":   ev.metodologia_acv,
                "regiao_origem":     ev.regiao_origem,
                "ano_referencia":    ev.ano_referencia,
                "confianca":         ev.confianca,
                "validado_humano":   ev.validado_humano,
                "extraction_model":  ev.extraction_model,
                "trecho_original":   ev.trecho_original,
                "nota_curadoria":    ev.nota_curadoria,
                "fonte": {
                    "nome":     ev.source.nome if ev.source else None,
                    "doi":      ev.source.doi  if ev.source else None,
                    "url":      ev.source.url  if ev.source else None,
                    "titulo":   ev.source.titulo if ev.source else None,
                    "journal":  ev.source.journal if ev.source else None,
                    "ano":      ev.source.ano_publicacao if ev.source else None,
                },
                "coletado_em": ev.criado_em.isoformat() if ev.criado_em else None,
            }
            for ev in evidences
        ],
        "meta": {
            "aviso": (
                "Valores com confiança 'media' são estimativas de síntese. "
                "Para claims legais no DPP, use apenas fontes com confiança 'alta' (EPD verificada ou LCA primário)."
            ) if any(ev.confianca == "media" for ev in evidences) else None,
        },
    }


@router.get("/impacto/resumo")
def resumo_banco_impacto(db: Session = Depends(get_db)):
    """
    Resumo do banco de dados de impacto — quantas fibras cobertas, distribuição de confiança.
    """
    from app.models.models import ImpactEvidence, ImpactMaterial

    materials = db.query(ImpactMaterial).all()
    total_ev = db.query(ImpactEvidence).count()
    alta = db.query(ImpactEvidence).filter_by(confianca="alta").count()
    media = db.query(ImpactEvidence).filter_by(confianca="media").count()
    baixa = db.query(ImpactEvidence).filter_by(confianca="baixa").count()

    return {
        "total_evidencias": total_ev,
        "fibras_cobertas": len(materials),
        "distribuicao_confianca": {"alta": alta, "media": media, "baixa": baixa},
        "fibras": [
            {
                "fibra_id":        m.fibra_id,
                "nome_pt":         m.nome_pt,
                "co2eq_agg":       m.co2eq_kg_por_kg_agg,
                "agua_agg":        m.agua_l_por_kg_agg,
                "n_evidencias":    m.n_evidencias,
                "confianca":       m.confianca_agg,
            }
            for m in sorted(materials, key=lambda x: x.fibra_id)
        ],
    }


@router.post("/calcular-peca")
def calcular_indicadores_peca(body: PecaRequest):
    """
    Calcula os indicadores ambientais completos de uma peça a partir da composição.

    Combina o catálogo de fatores com o cálculo de área/gramatura/perda
    e retorna os indicadores por peça (não por kg de fibra).
    """
    try:
        blend = calcular_blend([f.model_dump() for f in body.composicao])
    except CatalogoImpactoError as e:
        raise HTTPException(status_code=422, detail=str(e))

    try:
        result = calculate_dpp_indicators(DppCalculationInput(
            area_peca_m2=body.area_peca_m2,
            perda_corte_pct=body.perda_corte_pct,
            gramatura_g_m2=body.gramatura_g_m2,
            agua_litros_kg=blend.agua_l_por_kg,
            energia_kwh_kg=blend.energia_kwh_por_kg,
            carbono_kgco2e_kg=blend.co2eq_kg_por_kg,
        ))
    except DppCalculationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    return {
        "composicao": [f.model_dump() for f in body.composicao],
        "inputs": {
            "gramatura_g_m2":   body.gramatura_g_m2,
            "area_peca_m2":     body.area_peca_m2,
            "perda_corte_pct":  body.perda_corte_pct,
        },
        "fatores_blend_por_kg": {
            "co2eq_kg_por_kg":   blend.co2eq_kg_por_kg,
            "agua_l_por_kg":     blend.agua_l_por_kg,
            "energia_kwh_por_kg": blend.energia_kwh_por_kg,
        },
        "indicadores_por_peca": {
            "peso_peca_kg":        result.peso_peca_kg,
            "area_total_m2":       result.area_total_requerida_m2,
            "area_perdida_m2":     result.area_perdida_m2,
            "agua_peca_litros":    result.agua_peca_litros,
            "energia_peca_kwh":    result.energia_peca_kwh,
            "carbono_peca_kgco2e": result.carbono_peca_kgco2e,
        },
        "meta": {
            "fibras_usadas": blend.fibras_usadas,
            "confianca": blend.confianca,
            "metodologia": blend.metodologia,
            "fonte": blend.fonte,
            "aviso": blend.aviso,
            "status_evidencia": result.status_evidencia,
            "label_publica": result.label_publica,
        },
    }
