"""Generic impact factors for DPP pilot.

Sources:
- Water: Ecoinvent 3.9 / Chapagain & Hoekstra (2004) for cotton
- Energy: Ecoinvent 3.9 process datasets
- Carbon: IPCC AR6 GWP100 characterisation factors
- Lenzing EPD 2023 for lyocell/modal/ecovero (verified, alta confiança)
- Aquafil Econyl LCA 2021 for recycled nylon
- SEI 2005 for hemp

All values are per kg of material as produced (cradle-to-gate, global average).
Keys align with fibra_id in catalogo-impacto/fatores-genericos-v0.json and
impact_collector/normalizers/aliases.py.
"""

from __future__ import annotations

METHODOLOGY_TAG = (
    "estimativa genérica — Ecoinvent 3.9 + IPCC AR6 GWP100, fonte aberta. "
    "Não substitui ACV por fornecedor ou auditoria independente."
)

# Keys: fibra_id canônico (alinhado com aliases.py e fatores-genericos-v0.json)
GENERIC_FACTORS: dict[str, dict[str, float]] = {
    # ── Fibras naturais vegetais ──────────────────────────────────────────
    "algodao_convencional": {
        "agua_litros_kg": 10_000.0,
        "energia_kwh_kg": 15.3,      # 55 MJ × 0.27778
        "carbono_kgco2e_kg": 5.9,
    },
    "algodao_organico": {
        "agua_litros_kg": 2_100.0,
        "energia_kwh_kg": 13.3,      # 48 MJ × 0.27778
        "carbono_kgco2e_kg": 3.8,
    },
    "algodao_reciclado": {
        "agua_litros_kg": 500.0,
        "energia_kwh_kg": 8.3,       # 30 MJ
        "carbono_kgco2e_kg": 1.5,
    },
    "linho": {
        "agua_litros_kg": 6_400.0,
        "energia_kwh_kg": 2.8,       # 10 MJ
        "carbono_kgco2e_kg": 1.7,
    },
    "canamo": {
        "agua_litros_kg": 300.0,
        "energia_kwh_kg": 3.3,       # 12 MJ
        "carbono_kgco2e_kg": 0.8,
    },
    "fibra_coco": {
        "agua_litros_kg": 100.0,
        "energia_kwh_kg": 2.2,       # 8 MJ
        "carbono_kgco2e_kg": 0.5,
    },
    # ── Fibras naturais animais ───────────────────────────────────────────
    "la":                    # alias canônico — mesmo que la_virgem no JSON
    {
        "agua_litros_kg": 170.0,
        "energia_kwh_kg": 17.5,      # 63 MJ
        "carbono_kgco2e_kg": 27.0,   # dado verificado Wiedemann 2016
    },
    "la_virgem": {           # mantido por retrocompatibilidade
        "agua_litros_kg": 170.0,
        "energia_kwh_kg": 17.5,
        "carbono_kgco2e_kg": 27.0,
    },
    "la_cashmere": {
        "agua_litros_kg": 1_200.0,
        "energia_kwh_kg": 51.4,      # 185 MJ
        "carbono_kgco2e_kg": 150.0,
    },
    "seda": {
        "agua_litros_kg": 1_500.0,
        "energia_kwh_kg": 41.7,      # 150 MJ
        "carbono_kgco2e_kg": 50.0,
    },
    # ── Fibras celulósicas regeneradas ───────────────────────────────────
    "lyocell_tencel": {
        "agua_litros_kg": 261.0,
        "energia_kwh_kg": 10.3,      # 37.2 MJ — Lenzing EPD 2023
        "carbono_kgco2e_kg": 1.4,    # alta confiança
    },
    "viscose_modal": {
        "agua_litros_kg": 440.0,     # EcoVero Lenzing EPD 2023 (alta)
        "energia_kwh_kg": 12.3,      # 44.1 MJ
        "carbono_kgco2e_kg": 2.3,
    },
    "cupro": {
        "agua_litros_kg": 600.0,
        "energia_kwh_kg": 13.9,      # 50 MJ
        "carbono_kgco2e_kg": 3.8,
    },
    # ── Fibras sintéticas petroquímicas ──────────────────────────────────
    "poliester_virgem": {
        "agua_litros_kg": 71.0,
        "energia_kwh_kg": 34.7,      # 125 MJ
        "carbono_kgco2e_kg": 9.5,
    },
    "poliester_reciclado": {
        "agua_litros_kg": 35.0,
        "energia_kwh_kg": 16.4,      # 59 MJ — Shen et al. 2010 (alta)
        "carbono_kgco2e_kg": 3.25,   # mediana Sprint 2 (2.7 Shen + 3.8 Higg)
    },
    "poliamida_nylon_virgem": {
        "agua_litros_kg": 230.0,     # nylon_6 do JSON
        "energia_kwh_kg": 33.3,      # 120 MJ
        "carbono_kgco2e_kg": 7.9,
    },
    "nylon_6": {             # retrocompatibilidade
        "agua_litros_kg": 230.0,
        "energia_kwh_kg": 33.3,
        "carbono_kgco2e_kg": 7.9,
    },
    "nylon_66": {
        "agua_litros_kg": 250.0,
        "energia_kwh_kg": 34.7,      # 125 MJ
        "carbono_kgco2e_kg": 8.1,
    },
    "poliamida_reciclada": {
        "agua_litros_kg": 40.0,
        "energia_kwh_kg": 19.4,      # 70 MJ — Econyl 2021
        "carbono_kgco2e_kg": 7.2,
    },
    "elastano_spandex": {
        "agua_litros_kg": 300.0,
        "energia_kwh_kg": 63.9,      # 230 MJ
        "carbono_kgco2e_kg": 26.0,
    },
    # ── Biopolímeros ──────────────────────────────────────────────────────
    "pla_biopolimero": {
        "agua_litros_kg": 120.0,
        "energia_kwh_kg": 15.0,      # 54 MJ
        "carbono_kgco2e_kg": 2.7,
    },
    # ── Blends pré-calculados comuns em activewear ────────────────────────
    # 78% poliéster reciclado + 22% elastano
    "blend_78_poliester_reciclado_22_elastano": {
        "agua_litros_kg": round(0.78 * 35.0 + 0.22 * 300.0, 1),   # 93.3
        "energia_kwh_kg": round(0.78 * 16.4 + 0.22 * 63.9, 2),    # 26.8
        "carbono_kgco2e_kg": round(0.78 * 3.25 + 0.22 * 26.0, 3), # 8.255
    },
    # 90% poliamida reciclada + 10% elastano
    "blend_90_poliamida_reciclada_10_elastano": {
        "agua_litros_kg": round(0.90 * 40.0 + 0.10 * 300.0, 1),   # 66.0
        "energia_kwh_kg": round(0.90 * 19.4 + 0.10 * 63.9, 2),    # 24.0
        "carbono_kgco2e_kg": round(0.90 * 7.2 + 0.10 * 26.0, 3),  # 9.08
    },
}

SOURCE_LABELS = {
    "agua":    "banco_phyllos / Ecoinvent 3.9 / WFN — estimativa por material",
    "energia": "banco_phyllos / Ecoinvent 3.9 / Lenzing EPD — estimativa por material",
    "carbono": "banco_phyllos / IPCC AR6 GWP100 / Lenzing EPD — estimativa por material",
}


def get_factors(material_key: str) -> dict[str, float] | None:
    """Retorna fatores genéricos para uma chave de material ou None se desconhecido."""
    # Tenta o key direto
    if material_key in GENERIC_FACTORS:
        return GENERIC_FACTORS[material_key]
    # Tenta normalizar via aliases
    try:
        from impact_collector.normalizers.aliases import normalize_fiber_name
        normalized = normalize_fiber_name(material_key)
        if normalized and normalized in GENERIC_FACTORS:
            return GENERIC_FACTORS[normalized]
    except ImportError:
        pass
    return None


def apply_generic_factors(ficha_data: dict, material_key: str) -> dict:
    """
    Preenche campos de impacto da ficha técnica a partir dos fatores genéricos.
    Não sobrescreve campos já definidos (dado do fornecedor tem precedência).
    """
    factors = get_factors(material_key)
    if not factors:
        return ficha_data

    out = dict(ficha_data)
    if out.get("agua_litros_kg") is None:
        out["agua_litros_kg"] = factors["agua_litros_kg"]
        out["fonte_agua_litros_kg"] = SOURCE_LABELS["agua"]
    if out.get("energia_kwh_kg") is None:
        out["energia_kwh_kg"] = factors["energia_kwh_kg"]
        out["fonte_energia_kwh_kg"] = SOURCE_LABELS["energia"]
    if out.get("carbono_kgco2e_kg") is None:
        out["carbono_kgco2e_kg"] = factors["carbono_kgco2e_kg"]
        out["fonte_carbono_kgco2e_kg"] = SOURCE_LABELS["carbono"]
    if out.get("metodologia_fatores_impacto") is None:
        out["metodologia_fatores_impacto"] = METHODOLOGY_TAG

    return out


def blend_factors_from_composition(fibers: list[dict]) -> dict[str, float] | None:
    """
    Calcula fatores ponderados pela fração mássica.

    Aceita 'fibra' ou 'fibra_id' como chave, e resolve aliases automaticamente.
    Entrada: [{"fibra": str, "pct": float}] ou [{"fibra_id": str, "percentual": float}]
    Retorna None se qualquer material for desconhecido.
    """
    total_pct = sum(f.get("pct", f.get("percentual", 0)) for f in fibers)
    if abs(total_pct - 100) > 0.1:
        return None

    agua = energia = carbono = 0.0
    for entry in fibers:
        key = entry.get("fibra") or entry.get("fibra_id", "")
        pct = entry.get("pct", entry.get("percentual", 0)) / 100
        factors = get_factors(key)
        if factors is None:
            return None
        agua    += factors["agua_litros_kg"] * pct
        energia += factors["energia_kwh_kg"] * pct
        carbono += factors["carbono_kgco2e_kg"] * pct

    return {
        "agua_litros_kg":    round(agua, 2),
        "energia_kwh_kg":    round(energia, 2),
        "carbono_kgco2e_kg": round(carbono, 2),
    }
