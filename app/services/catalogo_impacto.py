"""
Serviço de catálogo de fatores de impacto ambiental.

Carrega produto/catalogo-impacto/fatores-genericos-v0.json e calcula fatores
ponderados pela composição de fibras (blend). Os resultados são compatíveis
com DppCalculationInput (agua_litros_kg, energia_kwh_kg, carbono_kgco2e_kg).

Conversão: energia_mj_por_kg → energia_kwh_kg  (1 MJ = 0.27778 kWh)
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Optional

_MJ_TO_KWH = 0.27778

# Caminho padrão: raiz do projeto / produto/catalogo-impacto/fatores-genericos-v0.json
_DEFAULT_CATALOG = (
    Path(__file__).resolve().parent.parent.parent
    / "produto" / "catalogo-impacto" / "fatores-genericos-v0.json"
)


class CatalogoImpactoError(ValueError):
    pass


@dataclass(frozen=True)
class FatorFibra:
    fibra_id: str
    nome_pt: str
    categoria: str
    origem: str
    co2eq_kg_por_kg: float
    agua_l_por_kg: float
    energia_mj_por_kg: float
    confianca: str
    fonte: str
    metodologia: str
    certificacoes_compativeis: list[str]
    nota_curadoria: str

    @property
    def energia_kwh_por_kg(self) -> float:
        return round(self.energia_mj_por_kg * _MJ_TO_KWH, 6)


@dataclass(frozen=True)
class FatoresBlend:
    co2eq_kg_por_kg: float
    agua_l_por_kg: float
    energia_mj_por_kg: float
    energia_kwh_por_kg: float
    confianca: str
    metodologia: str
    fonte: str
    fibras_usadas: list[str]
    aviso: Optional[str]


@lru_cache(maxsize=1)
def _carregar_catalogo(caminho: str) -> dict:
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def _catalog_path() -> str:
    env = os.getenv("CATALOGO_IMPACTO_PATH")
    if env:
        return env
    return str(_DEFAULT_CATALOG)


def listar_fibras() -> list[FatorFibra]:
    data = _carregar_catalogo(_catalog_path())
    return [_to_fator(f) for f in data["fibras"]]


def obter_fibra(fibra_id: str) -> FatorFibra:
    data = _carregar_catalogo(_catalog_path())
    for f in data["fibras"]:
        if f["fibra_id"] == fibra_id:
            return _to_fator(f)
    ids_disponiveis = [f["fibra_id"] for f in data["fibras"]]
    raise CatalogoImpactoError(
        f"Fibra '{fibra_id}' não encontrada no catálogo. "
        f"Disponíveis: {ids_disponiveis}"
    )


def calcular_blend(composicao: list[dict]) -> FatoresBlend:
    """
    Calcula fatores de impacto ponderados para uma composição de fibras.

    composicao: lista de dicts com 'fibra_id' (str) e 'percentual' (float, 0–100)
    Soma dos percentuais deve ser 100 (tolerância ±0.5).

    Exemplo:
        [{"fibra_id": "algodao_convencional", "percentual": 95},
         {"fibra_id": "elastano_spandex", "percentual": 5}]
    """
    if not composicao:
        raise CatalogoImpactoError("composicao não pode ser vazia")

    total_pct = sum(item["percentual"] for item in composicao)
    if abs(total_pct - 100) > 0.5:
        raise CatalogoImpactoError(
            f"Soma dos percentuais deve ser 100 (recebido: {total_pct})"
        )

    co2_sum = 0.0
    agua_sum = 0.0
    energia_sum = 0.0
    fibras_usadas = []
    confiancas = []

    for item in composicao:
        fibra_id = item.get("fibra_id")
        percentual = float(item.get("percentual", 0))
        if percentual < 0 or percentual > 100:
            raise CatalogoImpactoError(
                f"Percentual inválido para '{fibra_id}': {percentual}"
            )
        if percentual == 0:
            continue

        fator = obter_fibra(fibra_id)
        fracao = percentual / 100.0

        co2_sum    += fator.co2eq_kg_por_kg    * fracao
        agua_sum   += fator.agua_l_por_kg      * fracao
        energia_sum += fator.energia_mj_por_kg * fracao

        fibras_usadas.append(f"{fibra_id} ({percentual}%)")
        confiancas.append(fator.confianca)

    # Confiança do blend = pior confiança entre as fibras usadas
    ordem = {"baixa": 0, "media": 1, "alta": 2}
    confianca_final = min(confiancas, key=lambda c: ordem.get(c, 0))

    aviso = None
    if confianca_final == "media":
        aviso = (
            "Fatores genéricos não calibrados para origem brasileira. "
            "Substitua por dado verificado do fornecedor para aumentar precisão."
        )

    return FatoresBlend(
        co2eq_kg_por_kg=round(co2_sum, 6),
        agua_l_por_kg=round(agua_sum, 6),
        energia_mj_por_kg=round(energia_sum, 6),
        energia_kwh_por_kg=round(energia_sum * _MJ_TO_KWH, 6),
        confianca=confianca_final,
        metodologia="estimativa_generica",
        fonte="catalogo_phyllos_v0 (higg_msi_2023 / ecoinvent_3.9)",
        fibras_usadas=fibras_usadas,
        aviso=aviso,
    )


def _to_fator(raw: dict) -> FatorFibra:
    ind = raw["indicadores"]
    return FatorFibra(
        fibra_id=raw["fibra_id"],
        nome_pt=raw["nome_pt"],
        categoria=raw["categoria"],
        origem=raw["origem"],
        co2eq_kg_por_kg=ind["co2eq_kg_por_kg"]["valor"],
        agua_l_por_kg=ind["agua_l_por_kg"]["valor"],
        energia_mj_por_kg=ind["energia_mj_por_kg"]["valor"],
        confianca=ind["co2eq_kg_por_kg"]["confianca"],
        fonte=ind["co2eq_kg_por_kg"]["fonte"],
        metodologia=raw.get("metodologia", "estimativa_generica"),
        certificacoes_compativeis=raw.get("certificacoes_compativeis", []),
        nota_curadoria=raw.get("nota_curadoria", ""),
    )
