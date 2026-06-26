"""
Serviço de catálogo de fatores de impacto ambiental.

Cadeia de lookup unificada (por ordem de prioridade):
  1. Normalização de alias → fibra_id canônico
  2. SQLite impact_materials (Sprint 2 — dados verificados, confiança alta/media)
  3. JSON fatores-genericos-v0.json (fallback, confiança media/baixa)

Resultado: obter_fibra() funciona com qualquer forma de entrada — fibra_id canônico,
alias em qualquer língua, variação de nome comercial.

Conversão padrão: energia_mj_por_kg → energia_kwh_kg  (1 MJ = 0.27778 kWh)
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

_MJ_TO_KWH = 0.27778

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
    # Sprint 2: de onde veio o dado
    origem_dado: str = "json_catalogo"   # "sqlite_sprint2" | "json_catalogo"
    co2eq_range: tuple[float, float] | None = None
    agua_range: tuple[float, float] | None = None

    @property
    def energia_kwh_por_kg(self) -> float:
        return round(self.energia_mj_por_kg * _MJ_TO_KWH, 6)


@dataclass
class DetalheBlend:
    fibra_id: str
    nome_pt: str
    percentual: float
    co2eq_kg_por_kg: float
    agua_l_por_kg: float
    energia_mj_por_kg: float
    confianca: str
    fonte: str
    origem_dado: str


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
    detalhes: list[DetalheBlend]
    aviso: Optional[str]


# ── Normalização de aliases ─────────────────────────────────────────────────

def _normalize_id(raw: str) -> str:
    """
    Resolve qualquer forma de entrada para o fibra_id canônico.
    Usa o dicionário de aliases do impact_collector.
    Retorna o raw original em lowercase+snake se não encontrar alias.
    """
    try:
        from impact_collector.normalizers.aliases import normalize_fiber_name
        resolved = normalize_fiber_name(raw)
        if resolved:
            return resolved
    except ImportError:
        pass
    # Fallback: lowercase + underscores
    return raw.lower().strip().replace(" ", "_").replace("-", "_")


# ── Lookup SQLite (Sprint 2) ────────────────────────────────────────────────

def _lookup_sqlite(fibra_id: str) -> FatorFibra | None:
    """
    Consulta impact_materials no SQLite.
    Retorna None se tabela não existir ou fibra não encontrada.
    """
    try:
        from app.core.database import SessionLocal
        from app.models.models import ImpactMaterial
    except Exception:
        return None

    try:
        db = SessionLocal()
        m = db.query(ImpactMaterial).filter_by(fibra_id=fibra_id).first()
        db.close()
    except Exception as exc:
        logger.debug("SQLite lookup falhou para %s: %s", fibra_id, exc)
        return None

    if not m or not m.co2eq_kg_por_kg_agg:
        return None

    energia_mj = m.energia_mj_por_kg_agg or 0.0
    agua = m.agua_l_por_kg_agg or 0.0

    return FatorFibra(
        fibra_id=fibra_id,
        nome_pt=m.nome_pt or fibra_id,
        categoria=m.categoria or "desconhecida",
        origem="sqlite_sprint2",
        co2eq_kg_por_kg=m.co2eq_kg_por_kg_agg,
        agua_l_por_kg=agua,
        energia_mj_por_kg=energia_mj,
        confianca=m.confianca_agg or "media",
        fonte=f"banco_phyllos_sprint2 ({m.n_evidencias or 0} evidências)",
        metodologia="mediana de evidências coletadas de fontes abertas",
        certificacoes_compativeis=[],
        nota_curadoria=f"Dado agregado de {m.n_evidencias or 0} evidências. Atualizado em {m.atualizado_em or 'N/A'}.",
        origem_dado="sqlite_sprint2",
        co2eq_range=(m.co2eq_range_min, m.co2eq_range_max) if m.co2eq_range_min else None,
        agua_range=(m.agua_range_min, m.agua_range_max) if m.agua_range_min else None,
    )


# ── Lookup JSON ─────────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _carregar_catalogo(caminho: str) -> dict:
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def _catalog_path() -> str:
    env = os.getenv("CATALOGO_IMPACTO_PATH")
    return env if env else str(_DEFAULT_CATALOG)


_JSON_ID_FALLBACKS: dict[str, str] = {
    # canonical fibra_id → fibra_id que existe no JSON
    "poliamida_nylon_virgem": "nylon_6",
    "la":                     "la_virgem",
}


def _lookup_json(fibra_id: str) -> FatorFibra | None:
    """Busca no JSON — por fibra_id exato; tenta fallback canônico se não achar."""
    try:
        data = _carregar_catalogo(_catalog_path())
    except FileNotFoundError:
        return None

    lookup_ids = {fibra_id}
    if fibra_id in _JSON_ID_FALLBACKS:
        lookup_ids.add(_JSON_ID_FALLBACKS[fibra_id])

    for raw in data.get("fibras", []):
        if raw.get("fibra_id") in lookup_ids:
            fator = _to_fator(raw)
            # Normaliza o fibra_id retornado para o canônico pedido
            if fator.fibra_id != fibra_id:
                fator = FatorFibra(
                    fibra_id=fibra_id,
                    nome_pt=fator.nome_pt,
                    categoria=fator.categoria,
                    origem=fator.origem,
                    co2eq_kg_por_kg=fator.co2eq_kg_por_kg,
                    agua_l_por_kg=fator.agua_l_por_kg,
                    energia_mj_por_kg=fator.energia_mj_por_kg,
                    confianca=fator.confianca,
                    fonte=fator.fonte,
                    metodologia=fator.metodologia,
                    certificacoes_compativeis=fator.certificacoes_compativeis,
                    nota_curadoria=fator.nota_curadoria,
                    origem_dado="json_catalogo",
                )
            return fator

    return None


def _to_fator(raw: dict) -> FatorFibra:
    ind = raw["indicadores"]
    return FatorFibra(
        fibra_id=raw["fibra_id"],
        nome_pt=raw["nome_pt"],
        categoria=raw["categoria"],
        origem=raw.get("origem", "generica"),
        co2eq_kg_por_kg=ind["co2eq_kg_por_kg"]["valor"],
        agua_l_por_kg=ind["agua_l_por_kg"]["valor"],
        energia_mj_por_kg=ind["energia_mj_por_kg"]["valor"],
        confianca=ind["co2eq_kg_por_kg"]["confianca"],
        fonte=ind["co2eq_kg_por_kg"]["fonte"],
        metodologia=raw.get("metodologia", "estimativa_generica"),
        certificacoes_compativeis=raw.get("certificacoes_compativeis", []),
        nota_curadoria=raw.get("nota_curadoria", ""),
        origem_dado="json_catalogo",
    )


# ── Interface pública ────────────────────────────────────────────────────────

def listar_fibras() -> list[FatorFibra]:
    """Lista todas as fibras do JSON. Enriquece com dados do SQLite quando disponíveis."""
    data = _carregar_catalogo(_catalog_path())
    result = []
    seen: set[str] = set()
    for raw in data.get("fibras", []):
        fid = raw.get("fibra_id")
        if not fid or fid in seen:
            continue
        seen.add(fid)
        sqlite_fator = _lookup_sqlite(fid)
        result.append(sqlite_fator if sqlite_fator else _to_fator(raw))
    return result


def obter_fibra(fibra_id_or_name: str) -> FatorFibra:
    """
    Retorna fatores de impacto de uma fibra por ID canônico, alias ou nome comercial.

    Cadeia de lookup:
      1. normalize_fiber_name() → fibra_id canônico
      2. SQLite impact_materials (dados verificados Sprint 2)
      3. JSON fatores-genericos-v0.json (fallback)
      4. CatalogoImpactoError se não encontrado

    Exemplos aceitos:
      "algodao_convencional", "cotton", "Algodão", "TENCEL™", "rPET",
      "lyocell_tencel", "recycled polyester", "lã merino", "Econyl"
    """
    fibra_id = _normalize_id(fibra_id_or_name)

    # Tentar SQLite primeiro
    fator = _lookup_sqlite(fibra_id)
    if fator:
        return fator

    # Fallback JSON
    fator = _lookup_json(fibra_id)
    if fator:
        return fator

    # Se o id original era diferente do normalizado, tentar o original também
    if fibra_id_or_name.lower() != fibra_id:
        fator = _lookup_json(fibra_id_or_name.lower())
        if fator:
            return fator

    # Listar disponíveis para mensagem de erro útil
    try:
        data = _carregar_catalogo(_catalog_path())
        ids_json = [f["fibra_id"] for f in data.get("fibras", [])]
    except Exception:
        ids_json = []

    raise CatalogoImpactoError(
        f"Fibra '{fibra_id_or_name}' não encontrada (id normalizado: '{fibra_id}'). "
        f"Disponíveis no JSON: {ids_json}. "
        "Dica: aceita aliases — tente 'cotton', 'rPET', 'TENCEL', 'lã', etc."
    )


def calcular_blend(composicao: list[dict]) -> FatoresBlend:
    """
    Calcula fatores ponderados pela fração mássica para uma composição de fibras.

    Aceita como chave 'fibra_id' qualquer formato:
      - ID canônico: "algodao_convencional"
      - Alias: "cotton", "rPET", "TENCEL™", "lã merino"
      - Nome PT/EN: "Algodão Orgânico", "Recycled Polyester"

    Chave da composicao: 'fibra_id' (str) + 'percentual' (float, 0–100).
    Soma dos percentuais deve ser 100 (tolerância ±0.5).
    """
    if not composicao:
        raise CatalogoImpactoError("composicao não pode ser vazia")

    total_pct = sum(item.get("percentual", 0) for item in composicao)
    if abs(total_pct - 100) > 0.5:
        raise CatalogoImpactoError(
            f"Soma dos percentuais deve ser 100 (recebido: {total_pct:.1f})"
        )

    co2_sum = agua_sum = energia_sum = 0.0
    fibras_usadas: list[str] = []
    confiancas: list[str] = []
    fontes: list[str] = []
    detalhes: list[DetalheBlend] = []

    for item in composicao:
        raw_id = item.get("fibra_id") or item.get("fibra") or ""
        percentual = float(item.get("percentual", 0))

        if percentual < 0 or percentual > 100:
            raise CatalogoImpactoError(f"Percentual inválido para '{raw_id}': {percentual}")
        if percentual == 0:
            continue

        fator = obter_fibra(raw_id)
        fracao = percentual / 100.0

        co2_sum     += fator.co2eq_kg_por_kg    * fracao
        agua_sum    += fator.agua_l_por_kg      * fracao
        energia_sum += fator.energia_mj_por_kg  * fracao

        fibras_usadas.append(f"{fator.fibra_id} ({percentual}%)")
        confiancas.append(fator.confianca)
        fontes.append(fator.origem_dado)

        detalhes.append(DetalheBlend(
            fibra_id=fator.fibra_id,
            nome_pt=fator.nome_pt,
            percentual=percentual,
            co2eq_kg_por_kg=fator.co2eq_kg_por_kg,
            agua_l_por_kg=fator.agua_l_por_kg,
            energia_mj_por_kg=fator.energia_mj_por_kg,
            confianca=fator.confianca,
            fonte=fator.fonte,
            origem_dado=fator.origem_dado,
        ))

    # Confiança do blend = pior entre as fibras
    _ordem = {"baixa": 0, "media": 1, "alta": 2}
    confianca_final = min(confiancas, key=lambda c: _ordem.get(c, 0))

    # Metodologia: melhor fonte disponível
    if "sqlite_sprint2" in fontes:
        metodologia = "banco_phyllos (evidências coletadas de fontes abertas verificadas)"
        fonte_label = "banco_phyllos_sprint2 + catalogo_phyllos_v0"
    else:
        metodologia = "estimativa_generica"
        fonte_label = "catalogo_phyllos_v0 (higg_msi_2023 / ecoinvent_3.9)"

    avisos: list[str] = []
    if confianca_final == "baixa":
        avisos.append(
            "Uma ou mais fibras têm confiança 'baixa' — dado de estimativa ou literatura não verificada. "
            "Para DPP público, substitua pelo laudo do fornecedor."
        )
    elif confianca_final == "media":
        avisos.append(
            "Fatores genéricos — não calibrados para origem específica. "
            "Para maior precisão, use dados verificados do fornecedor."
        )

    return FatoresBlend(
        co2eq_kg_por_kg=round(co2_sum, 6),
        agua_l_por_kg=round(agua_sum, 6),
        energia_mj_por_kg=round(energia_sum, 6),
        energia_kwh_por_kg=round(energia_sum * _MJ_TO_KWH, 6),
        confianca=confianca_final,
        metodologia=metodologia,
        fonte=fonte_label,
        fibras_usadas=fibras_usadas,
        detalhes=detalhes,
        aviso=" | ".join(avisos) if avisos else None,
    )
