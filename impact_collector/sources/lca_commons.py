"""Coletor Federal LCA Commons (USDA/NREL) — banco LCA americano, API gratuita."""

from __future__ import annotations
import urllib.request
import urllib.parse
import json
import logging
import time

logger = logging.getLogger(__name__)

# API pública — requer chave gratuita via api.data.gov
# Sem chave funciona mas com rate limit menor
BASE_URL = "https://www.lcacommons.gov/lca-collaboration/search/datasets"
PROCESS_URL = "https://www.lcacommons.gov/lca-collaboration"

# Mapeamento de fibra_id para termos de busca no LCA Commons
FIBER_QUERY_MAP: dict[str, list[str]] = {
    "algodao_convencional": ["cotton", "cotton fiber", "conventional cotton"],
    "algodao_organico": ["organic cotton"],
    "poliester_reciclado": ["recycled polyester", "rPET", "PET recycled"],
    "lyocell_tencel": ["lyocell", "cellulosic fiber", "viscose"],
    "linho": ["flax", "linen"],
    "la": ["wool", "sheep"],
}

# Datasets conhecidos do USLCI que cobrem têxteis
KNOWN_USLCI_DATASETS = [
    {
        "nome": "USLCI — Nylon 6 Production",
        "fibra_ids": ["poliamida_nylon_virgem"],
        "url": "https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public",
        "doi": None,
        "ano": 2023,
        "metodologia": "TRACI 2.1 / ISO 14044",
        "regiao": "US",
    },
    {
        "nome": "USLCI — Polyethylene terephthalate (PET) resin production",
        "fibra_ids": ["poliester_virgem"],
        "url": "https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public",
        "doi": None,
        "ano": 2023,
        "metodologia": "TRACI 2.1 / ISO 14044",
        "regiao": "US",
    },
    {
        "nome": "USLCI — Cotton fiber production",
        "fibra_ids": ["algodao_convencional"],
        "url": "https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public",
        "doi": None,
        "ano": 2023,
        "metodologia": "TRACI 2.1 / ISO 14044",
        "regiao": "US",
    },
]


def get_known_datasets(fibra_id: str) -> list[dict]:
    """
    Retorna datasets conhecidos do USLCI para uma fibra.

    Para o Sprint 1 usamos datasets curados manualmente enquanto a API
    do LCA Commons não tem endpoint de busca por material bem documentado.
    """
    return [d for d in KNOWN_USLCI_DATASETS if fibra_id in d.get("fibra_ids", [])]


def fetch_dataset_metadata(fibra_id: str) -> list[dict]:
    """
    Tenta buscar via API do LCA Commons.
    Retorna lista de metadados de datasets encontrados.
    """
    terms = FIBER_QUERY_MAP.get(fibra_id, [])
    results = []

    for term in terms[:2]:  # limitar chamadas na API no piloto
        url = BASE_URL + "?" + urllib.parse.urlencode({
            "query": term,
            "page": 0,
            "pageSize": 10,
        })
        try:
            req = urllib.request.Request(
                url,
                headers={"Accept": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                for item in data.get("data", []):
                    results.append({
                        "nome": item.get("name"),
                        "uuid": item.get("uuid"),
                        "url": f"{PROCESS_URL}/{item.get('group','')}/{item.get('name','')}",
                        "fibra_id": fibra_id,
                        "fonte": "lca_commons_api",
                    })
        except Exception as exc:
            logger.warning("LCA Commons API erro para '%s': %s", term, exc)

        time.sleep(0.5)

    # Complementar com datasets curados
    results.extend(get_known_datasets(fibra_id))
    return results
