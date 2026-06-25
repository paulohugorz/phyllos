"""
Endpoints do catálogo de fatores de impacto ambiental.

GET  /catalogo/fibras                   — lista todas as fibras disponíveis
GET  /catalogo/fibras/{fibra_id}        — detalhe de uma fibra
POST /catalogo/calcular-blend           — fatores ponderados por composição
POST /catalogo/calcular-peca            — indicadores por peça (blend + gramatura + área)
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, model_validator
from typing import Optional

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
    fibra_id: str = Field(..., example="algodao_convencional")
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
        "meta": {
            "fibras_usadas": blend.fibras_usadas,
            "confianca": blend.confianca,
            "metodologia": blend.metodologia,
            "fonte": blend.fonte,
            "aviso": blend.aviso,
        },
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
