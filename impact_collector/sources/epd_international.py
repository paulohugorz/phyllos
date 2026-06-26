"""
Coletor EPD International — biblioteca pública de EPDs verificadas por terceiros.
API ILCD+EPD XML gratuita via Azure API Management.

EPDs relevantes para PHYLLOS:
- PCR 2020:03 cobre man-made fibres (lyocell, modal, viscose)
- Lenzing publica EPDs verificadas para Tencel, EcoVero, Modal
"""

from __future__ import annotations
import urllib.request
import urllib.parse
import json
import logging
import time

logger = logging.getLogger(__name__)

# API pública — requer conta gratuita em epd-apim.developer.azure-api.net
# Por ora usamos a interface de busca pública sem autenticação (subset menor)
SEARCH_URL = "https://www.environdec.com/api/api/v1/EPDDefinition"

# PCR de fibras man-made (Product Category Rule)
PCR_TEXTILE_FIBERS = "2020:03"

# EPDs conhecidas e verificadas relevantes para o Sprint 1
# Curadas manualmente — cada uma tem download PDF público
KNOWN_EPDS: list[dict] = [
    {
        "nome": "Lenzing TENCEL™ Lyocell Fibers — EPD",
        "fibra_ids": ["lyocell_tencel"],
        "empresa": "Lenzing AG",
        "url_pdf": "https://www.lenzing.com/fileadmin/corporate/user_upload/03_sustainability/EPD/TENCEL_Lyocell_EPD.pdf",
        "ano": 2023,
        "metodologia": "ISO 14044 / EN 15804",
        "escopo": "cradle-to-gate",
        "regiao": "Austria/Global",
        "verificado_por": "Institut Bauen und Umwelt (IBU)",
        "acesso_aberto": True,
    },
    {
        "nome": "Lenzing TENCEL™ Modal Fibers — EPD",
        "fibra_ids": ["modal"],
        "empresa": "Lenzing AG",
        "url_pdf": "https://www.lenzing.com/fileadmin/corporate/user_upload/03_sustainability/EPD/TENCEL_Modal_EPD.pdf",
        "ano": 2023,
        "metodologia": "ISO 14044 / EN 15804",
        "escopo": "cradle-to-gate",
        "regiao": "Austria",
        "verificado_por": "Institut Bauen und Umwelt (IBU)",
        "acesso_aberto": True,
    },
    {
        "nome": "Lenzing ECOVERO™ Viscose Fibers — EPD",
        "fibra_ids": ["viscose_modal"],
        "empresa": "Lenzing AG",
        "url_pdf": "https://www.lenzing.com/fileadmin/corporate/user_upload/03_sustainability/EPD/ECOVERO_EPD.pdf",
        "ano": 2023,
        "metodologia": "ISO 14044 / EN 15804",
        "escopo": "cradle-to-gate",
        "regiao": "Austria",
        "verificado_por": "Institut Bauen und Umwelt (IBU)",
        "acesso_aberto": True,
    },
]

# Valores declarados nas EPDs Lenzing (extraídos manualmente das EPDs 2023)
# Usados como ground truth para validar a extração LLM no piloto
EPD_GROUND_TRUTH: dict[str, dict] = {
    "lyocell_tencel": {
        "co2eq_kg_por_kg": 1.4,   # GWP100, cradle-to-gate (Lenzing EPD 2023)
        "agua_l_por_kg": 261.0,   # water consumption (azul), Lenzing EPD 2023
        "energia_mj_por_kg": 37.2,  # energia primária não renovável
        "escopo": "cradle-to-gate",
        "fonte": "Lenzing TENCEL Lyocell EPD 2023 (verificado IBU)",
        "confianca": "alta",
    },
    "viscose_modal": {
        "co2eq_kg_por_kg": 2.3,
        "agua_l_por_kg": 440.0,
        "energia_mj_por_kg": 44.1,
        "escopo": "cradle-to-gate",
        "fonte": "Lenzing EcoVero EPD 2023 (verificado IBU)",
        "confianca": "alta",
    },
}


def get_known_epds(fibra_id: str) -> list[dict]:
    """Retorna EPDs curadas para uma fibra."""
    return [e for e in KNOWN_EPDS if fibra_id in e.get("fibra_ids", [])]


def get_ground_truth(fibra_id: str) -> dict | None:
    """Retorna valores verificados de EPDs para uso como baseline/validação."""
    return EPD_GROUND_TRUTH.get(fibra_id)


def search_epd_portal(fibra_id: str, max_results: int = 5) -> list[dict]:
    """
    Busca EPDs no portal EPD International.
    Retorna lista de metadados de EPDs encontradas.
    """
    keywords_map = {
        "lyocell_tencel": "lyocell",
        "la": "wool textile",
        "algodao_organico": "organic cotton",
        "linho": "flax linen",
        "poliester_reciclado": "recycled polyester",
    }
    keyword = keywords_map.get(fibra_id, fibra_id.replace("_", " "))

    params = {
        "Search": keyword,
        "IsSchemeVersion4": "true",
    }
    url = SEARCH_URL + "?" + urllib.parse.urlencode(params)

    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            results = []
            for epd in (data.get("data") or [])[:max_results]:
                results.append({
                    "nome": epd.get("name"),
                    "empresa": epd.get("declaredUnit"),
                    "url": f"https://www.environdec.com/library/epd-{epd.get('registrationNumber', '')}",
                    "ano": epd.get("publishedDate", "")[:4],
                    "fibra_id": fibra_id,
                    "fonte": "epd_international_portal",
                })
            return results
    except Exception as exc:
        logger.warning("EPD International portal erro para '%s': %s", fibra_id, exc)
        return []
    finally:
        time.sleep(0.5)
