"""
Dados de referência curados de fontes canônicas abertas.

Valores extraídos manualmente de publicações de acesso livre:
- Water Footprint Network (Mekonnen & Hoekstra 2011) — WFN
- Textile Exchange Preferred Fiber & Materials Report 2023 — TE2023
- Stockholm Environment Institute (Shen et al. 2010) — SEI
- European Environment Agency / EFSA data — EEA
- Lenzing AG EPDs verificadas (IBU) — LENZING_EPD
- IPCC AR6 + Ecoinvent 3.9 free tier — IPCC_EI39

Cada entrada tem: valor, unidade, escopo, metodologia, fonte, confiança.
Confiança 'alta' = verificado por terceiro ou peer-reviewed com metodologia declarada.
Confiança 'media' = estimativa de relatório setorial ou síntese de múltiplos estudos.
"""

from __future__ import annotations

# Schema de cada entrada:
# fibra_id -> lista de evidências publicadas
# Cada evidência: {co2, agua, energia, escopo, metodologia, regiao, ano, fonte, confianca, nota}

REFERENCE_DATA: dict[str, list[dict]] = {

    # ── Algodão Convencional ─────────────────────────────────────────────
    "algodao_convencional": [
        {
            "co2eq_kg_por_kg": 5.9,
            "agua_l_por_kg": 10_000.0,
            "energia_mj_por_kg": 55.0,
            "escopo": "cradle-to-gate",
            "metodologia": "ISO 14044 / Ecoinvent 3.9",
            "regiao": "global",
            "ano": 2023,
            "fonte": "Higg MSI 2023 Public Summary + Ecoinvent 3.9 free tier",
            "confianca": "media",
            "nota": "Média global. Cerrado BR pode ser 20-30% menor em água por uso de chuva (FAOSTAT 2023).",
        },
        {
            # WFN — Mekonnen & Hoekstra (2011): The green, blue and grey water footprint of crops
            # DOI: 10.5194/hess-15-1577-2011 — open access
            "co2eq_kg_por_kg": None,
            "agua_l_por_kg": 9_114.0,  # valor global médio ponderado por produção WFN 2011
            "energia_mj_por_kg": None,
            "escopo": "cradle-to-gate",
            "metodologia": "Water Footprint Assessment (Hoekstra 2011)",
            "regiao": "global",
            "ano": 2011,
            "fonte": "Mekonnen & Hoekstra 2011, HESS 15:1577. DOI:10.5194/hess-15-1577-2011",
            "confianca": "alta",
            "nota": "Dado canônico de pegada hídrica. India: 22.500 L/kg, EUA: 3.800 L/kg, Brasil: ~5.600 L/kg.",
        },
        {
            # Textile Exchange Preferred Fiber & Materials Market Report 2023
            "co2eq_kg_por_kg": 5.9,
            "agua_l_por_kg": None,
            "energia_mj_por_kg": None,
            "escopo": "cradle-to-gate",
            "metodologia": "síntese de múltiplas ACV",
            "regiao": "global",
            "ano": 2023,
            "fonte": "Textile Exchange Materials Market Report 2023",
            "confianca": "media",
            "nota": "Relatório setorial — síntese, não ACV primário.",
        },
    ],

    # ── Algodão Orgânico ─────────────────────────────────────────────────
    "algodao_organico": [
        {
            "co2eq_kg_por_kg": 3.8,
            "agua_l_por_kg": 2_100.0,
            "energia_mj_por_kg": 48.0,
            "escopo": "cradle-to-gate",
            "metodologia": "ISO 14044 / GOTS methodology",
            "regiao": "global",
            "ano": 2023,
            "fonte": "Textile Exchange Organic Cotton Report 2023 + GOTS LCA study",
            "confianca": "media",
            "nota": "Água significativamente menor que convencional por menor irrigação (maior dependência de chuva).",
        },
        {
            # Kooistra & Termorshuizen (2006): The sustainability of cotton
            "co2eq_kg_por_kg": 2.0,
            "agua_l_por_kg": 6_000.0,
            "energia_mj_por_kg": 50.0,
            "escopo": "cradle-to-gate",
            "metodologia": "LCA ISO 14044",
            "regiao": "global",
            "ano": 2006,
            "fonte": "Kooistra & Termorshuizen (2006), Report 2006-003, Wageningen UR",
            "confianca": "media",
            "nota": "Estudo clássico de referência. Água varia muito — sem irrigação pode chegar a 6.000 L/kg.",
        },
    ],

    # ── Poliéster Reciclado (rPET) ───────────────────────────────────────
    "poliester_reciclado": [
        {
            # Shen et al. (2010): Open-loop recycling: A LCA case study of PET bottle-to-fibre recycling
            # Resources, Conservation and Recycling — open access
            "co2eq_kg_por_kg": 2.7,
            "agua_l_por_kg": 35.0,
            "energia_mj_por_kg": 53.0,
            "escopo": "cradle-to-gate",
            "metodologia": "CML 2001 / ISO 14044",
            "regiao": "global",
            "ano": 2010,
            "fonte": "Shen et al. (2010), Resources Conservation Recycling 55(1):34-52. DOI:10.1016/j.resconrec.2010.06.014",
            "confianca": "alta",
            "nota": "Estudo canônico de ACV do rPET vs virgem. CO2 ~71% menor que poliéster virgem.",
        },
        {
            "co2eq_kg_por_kg": 3.8,
            "agua_l_por_kg": 35.0,
            "energia_mj_por_kg": 59.0,
            "escopo": "cradle-to-gate",
            "metodologia": "síntese Higg MSI 2023",
            "regiao": "global",
            "ano": 2023,
            "fonte": "Higg MSI 2023 Public Summary",
            "confianca": "media",
            "nota": "Valor do Higg MSI — inclui diferentes tecnologias de reciclagem.",
        },
    ],

    # ── Lyocell / Tencel ─────────────────────────────────────────────────
    "lyocell_tencel": [
        {
            # Já no ground_truth do epd_international.py — repetido aqui para consolidação
            "co2eq_kg_por_kg": 1.4,
            "agua_l_por_kg": 261.0,
            "energia_mj_por_kg": 37.2,
            "escopo": "cradle-to-gate",
            "metodologia": "EN 15804 / ISO 14044",
            "regiao": "Austria",
            "ano": 2023,
            "fonte": "Lenzing TENCEL Lyocell EPD 2023 (verificado Institut Bauen und Umwelt — IBU)",
            "confianca": "alta",
            "nota": "EPD verificada por terceiro. Processo TENCEL closed-loop com 99.5% recuperação de solvente.",
        },
        {
            # Shen & Patel (2010): LCA of man-made cellulose fibres
            # Lenzinger Berichte — open access
            "co2eq_kg_por_kg": 2.3,
            "agua_l_por_kg": None,
            "energia_mj_por_kg": 37.0,
            "escopo": "cradle-to-gate",
            "metodologia": "CML 2001 / ISO 14044",
            "regiao": "global",
            "ano": 2010,
            "fonte": "Shen & Patel (2010), Lenzinger Berichte 88:1-59",
            "confianca": "media",
            "nota": "Estudo independente (não Lenzing). Energia dentro do range do EPD.",
        },
    ],

    # ── Linho ────────────────────────────────────────────────────────────
    "linho": [
        {
            # Bos et al. (2012): Life Cycle Assessment of flax fibres
            # DOI:10.1007/s11367-012-0454-z — open access via Springer
            "co2eq_kg_por_kg": 1.7,
            "agua_l_por_kg": 6_400.0,
            "energia_mj_por_kg": 10.0,
            "escopo": "cradle-to-gate",
            "metodologia": "ReCiPe / ISO 14044",
            "regiao": "Europa (França/Bélgica)",
            "ano": 2012,
            "fonte": "Bos et al. (2012), Int J Life Cycle Assess 17:1093-1108. DOI:10.1007/s11367-012-0454-z",
            "confianca": "alta",
            "nota": "Linho europeu (principal região produtora). CO2 muito baixo por sequestro durante cultivo.",
        },
        {
            # WFN — Mekonnen & Hoekstra 2011
            "co2eq_kg_por_kg": None,
            "agua_l_por_kg": 6_410.0,
            "energia_mj_por_kg": None,
            "escopo": "cradle-to-gate",
            "metodologia": "Water Footprint Assessment",
            "regiao": "global",
            "ano": 2011,
            "fonte": "Mekonnen & Hoekstra 2011, HESS — Water Footprint of Crops",
            "confianca": "alta",
            "nota": "Maioria da água é verde (chuva) — pegada hídrica azul muito menor (~20 L/kg).",
        },
        {
            # SEI (2005): Ecological Footprint and Water Analysis of Cotton, Hemp and Polyester
            "co2eq_kg_por_kg": 1.7,
            "agua_l_por_kg": None,
            "energia_mj_por_kg": 10.0,
            "escopo": "cradle-to-gate",
            "metodologia": "Ecological footprint + LCA",
            "regiao": "global",
            "ano": 2005,
            "fonte": "Riddlestone et al. (2005) / Shen & Patel SEI Stockholm Environment Institute",
            "confianca": "media",
            "nota": "Estudo de referência clássico. Energia muito baixa comparada a fibras sintéticas.",
        },
    ],

    # ── Lã ──────────────────────────────────────────────────────────────
    "la": [
        {
            # Wiedemann et al. (2016): LCA wool from Australia
            # Int J Life Cycle Assess — open access
            "co2eq_kg_por_kg": 27.0,
            "agua_l_por_kg": None,
            "energia_mj_por_kg": 63.0,
            "escopo": "cradle-to-gate",
            "metodologia": "ReCiPe / ISO 14044",
            "regiao": "Australia",
            "ano": 2016,
            "fonte": "Wiedemann et al. (2016), Int J Life Cycle Assess 21:1395-1406. DOI:10.1007/s11367-016-1112-z",
            "confianca": "alta",
            "nota": "Alta pegada de carbono por emissões de metano do gado ovino (~90% do GWP). Dado Austrália (maior exportador).",
        },
        {
            # Textile Exchange — Responsible Wool Standard Report 2023
            "co2eq_kg_por_kg": 24.0,
            "agua_l_por_kg": None,
            "energia_mj_por_kg": None,
            "escopo": "cradle-to-gate",
            "metodologia": "síntese múltiplos estudos",
            "regiao": "global",
            "ano": 2023,
            "fonte": "Textile Exchange Responsible Wool Standard Report 2023",
            "confianca": "media",
            "nota": "Média global. Lã ZQ Merino Nova Zelândia pode ter pegada mais baixa por práticas de pastagem regenerativa.",
        },
        {
            "co2eq_kg_por_kg": 36.0,
            "agua_l_por_kg": 170_000.0,
            "energia_mj_por_kg": 63.0,
            "escopo": "cradle-to-gate",
            "metodologia": "síntese Made-By benchmark",
            "regiao": "global",
            "ano": 2019,
            "fonte": "Made-By Environmental Benchmark for Fibres v3.0 (2019) — dados reproduzidos em literatura",
            "confianca": "media",
            "nota": "Pegada hídrica da lã inclui água de bebida animal + processamento. Altamente variável por sistema de produção.",
        },
    ],

    # ── Viscose / Modal (EcoVero) ─────────────────────────────────────────
    "viscose_modal": [
        {
            # Lenzing EcoVero EPD
            "co2eq_kg_por_kg": 2.3,
            "agua_l_por_kg": 440.0,
            "energia_mj_por_kg": 44.1,
            "escopo": "cradle-to-gate",
            "metodologia": "EN 15804 / ISO 14044",
            "regiao": "Austria",
            "ano": 2023,
            "fonte": "Lenzing ECOVERO EPD 2023 (verificado IBU)",
            "confianca": "alta",
            "nota": "EcoVero tem 50% menos pegada hídrica que viscose convencional por processo mais eficiente.",
        },
        {
            # Shen & Patel 2010 — viscose convencional
            "co2eq_kg_por_kg": 4.5,
            "agua_l_por_kg": 2_000.0,
            "energia_mj_por_kg": 48.0,
            "escopo": "cradle-to-gate",
            "metodologia": "CML 2001 / ISO 14044",
            "regiao": "Ásia (China/Indonésia)",
            "ano": 2010,
            "fonte": "Shen & Patel (2010), Lenzinger Berichte 88 — viscose convencional",
            "confianca": "media",
            "nota": "Viscose convencional (não EcoVero). Processo com sulfeto de carbono — mais impactante.",
        },
    ],

    # ── Nylon Reciclado ──────────────────────────────────────────────────
    "poliamida_reciclada": [
        {
            # Shen et al. (2010) — via Econyl data sheets (Aquafil)
            "co2eq_kg_por_kg": 7.2,
            "agua_l_por_kg": 40.0,
            "energia_mj_por_kg": 70.0,
            "escopo": "cradle-to-gate",
            "metodologia": "ISO 14044",
            "regiao": "global",
            "ano": 2021,
            "fonte": "Aquafil ECONYL LCA report 2021 + Shen et al. 2010",
            "confianca": "media",
            "nota": "Econyl (Aquafil) é a referência de mercado para nylon reciclado certificado. ~80% menos CO2 vs nylon virgem.",
        },
    ],
}


def get_reference_evidences(fibra_id: str) -> list[dict]:
    """Retorna todas as evidências de referência para uma fibra."""
    return REFERENCE_DATA.get(fibra_id, [])


def get_all_fiber_ids() -> list[str]:
    """Retorna todos os fiber_ids com dados de referência disponíveis."""
    return list(REFERENCE_DATA.keys())
