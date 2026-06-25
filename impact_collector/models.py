"""Modelos de dados do pipeline — agnósticos de banco de dados."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal
from datetime import datetime


Confianca = Literal["alta", "media", "baixa"]
EscopoLCA = Literal["cradle-to-gate", "cradle-to-grave", "gate-to-gate", "outro"]
TipoFonte = Literal["api", "pdf", "bulk_dump", "scraping", "oai_pmh", "manual"]


@dataclass
class ImpactSource:
    tipo: TipoFonte
    nome: str
    url: str | None = None
    doi: str | None = None
    titulo: str | None = None
    autores: list[str] = field(default_factory=list)
    ano_publicacao: int | None = None
    journal: str | None = None
    acesso_aberto: bool = True
    licenca: str | None = None
    raw_storage_path: str | None = None
    coletado_em: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ImpactEvidence:
    fibra_id: str
    source: ImpactSource

    # Valores medidos (todos opcionais — artigo pode medir só um)
    co2eq_kg_por_kg: float | None = None
    agua_l_por_kg: float | None = None
    energia_mj_por_kg: float | None = None

    # Metadados do estudo
    escopo_lca: EscopoLCA | None = None
    metodologia_acv: str | None = None
    regiao_origem: str | None = None
    ano_referencia: int | None = None

    # Rastreabilidade
    pagina_referencia: str | None = None
    trecho_original: str | None = None

    # Qualidade
    confianca: Confianca = "baixa"
    validado_humano: bool = False

    # Extração
    extraction_model: str | None = None
    extraction_cost_usd: float | None = None

    def has_any_value(self) -> bool:
        return any([self.co2eq_kg_por_kg, self.agua_l_por_kg, self.energia_mj_por_kg])

    def to_dict(self) -> dict:
        return {
            "fibra_id": self.fibra_id,
            "co2eq_kg_por_kg": self.co2eq_kg_por_kg,
            "agua_l_por_kg": self.agua_l_por_kg,
            "energia_mj_por_kg": self.energia_mj_por_kg,
            "escopo_lca": self.escopo_lca,
            "metodologia_acv": self.metodologia_acv,
            "regiao_origem": self.regiao_origem,
            "ano_referencia": self.ano_referencia,
            "pagina_referencia": self.pagina_referencia,
            "trecho_original": self.trecho_original,
            "confianca": self.confianca,
            "extraction_model": self.extraction_model,
            "source_nome": self.source.nome,
            "source_url": self.source.url,
            "source_doi": self.source.doi,
            "source_titulo": self.source.titulo,
            "source_ano": self.source.ano_publicacao,
        }
