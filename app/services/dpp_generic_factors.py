"""Generic impact factors for DPP pilot (August 2026).

Sources:
- Water: Ecoinvent 3.9 / Chapagain & Hoekstra (2004) for cotton
- Energy: Ecoinvent 3.9 process datasets
- Carbon: IPCC AR6 GWP100 characterisation factors

All values are per kg of material as produced (cradle-to-gate, global average).
Marked as open-source generic estimates — not a substitute for supplier LCA data.
"""

from __future__ import annotations

METHODOLOGY_TAG = (
    "estimativa genérica — Ecoinvent 3.9 + IPCC AR6 GWP100, fonte aberta. "
    "Não substitui ACV por fornecedor ou auditoria independente."
)

# Keys align with composicao_fibras[].fibra normalised values
GENERIC_FACTORS: dict[str, dict[str, float]] = {
    # ── Fibras naturais ──────────────────────────────────────────────────
    "algodao_convencional": {
        "agua_litros_kg": 10_000.0,
        "energia_kwh_kg": 55.0,
        "carbono_kgco2e_kg": 5.9,
    },
    "algodao_organico": {
        "agua_litros_kg": 6_000.0,
        "energia_kwh_kg": 50.0,
        "carbono_kgco2e_kg": 3.7,
    },
    "linho": {
        "agua_litros_kg": 6_400.0,
        "energia_kwh_kg": 10.0,
        "carbono_kgco2e_kg": 1.7,
    },
    "viscose_modal": {
        "agua_litros_kg": 2_000.0,
        "energia_kwh_kg": 25.0,
        "carbono_kgco2e_kg": 3.0,
    },
    # ── Fibras sintéticas ────────────────────────────────────────────────
    "poliester_virgem": {
        "agua_litros_kg": 71.0,
        "energia_kwh_kg": 125.0,
        "carbono_kgco2e_kg": 9.5,
    },
    "poliester_reciclado": {
        "agua_litros_kg": 35.0,
        "energia_kwh_kg": 59.0,
        "carbono_kgco2e_kg": 3.8,
    },
    "poliamida_nylon_virgem": {
        "agua_litros_kg": 70.0,
        "energia_kwh_kg": 139.0,
        "carbono_kgco2e_kg": 14.4,
    },
    "poliamida_reciclada": {
        "agua_litros_kg": 40.0,
        "energia_kwh_kg": 70.0,
        "carbono_kgco2e_kg": 7.2,
    },
    "elastano_spandex": {
        "agua_litros_kg": 25.0,
        "energia_kwh_kg": 141.0,
        "carbono_kgco2e_kg": 16.0,
    },
    # ── Blends comuns em performance ─────────────────────────────────────
    # Valores ponderados: 78% poliéster reciclado + 22% elastano
    "blend_78_poliester_reciclado_22_elastano": {
        "agua_litros_kg": 33.0,
        "energia_kwh_kg": 77.4,
        "carbono_kgco2e_kg": 6.5,
    },
    # 90% poliamida reciclada + 10% elastano
    "blend_90_poliamida_reciclada_10_elastano": {
        "agua_litros_kg": 38.5,
        "energia_kwh_kg": 77.0,
        "carbono_kgco2e_kg": 8.1,
    },
}

SOURCE_LABELS = {
    "agua": "Ecoinvent 3.9 — estimativa genérica por material",
    "energia": "Ecoinvent 3.9 — estimativa genérica por material",
    "carbono": "IPCC AR6 GWP100 — estimativa genérica por material",
}


def get_factors(material_key: str) -> dict[str, float] | None:
    """Return generic factors for a material key, or None if unknown."""
    return GENERIC_FACTORS.get(material_key)


def apply_generic_factors(ficha_data: dict, material_key: str) -> dict:
    """Fill impact factor fields from generic table if not already set.

    Only overwrites fields that are absent (None or missing).
    Never silently replaces supplier-declared data.
    """
    factors = GENERIC_FACTORS.get(material_key)
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
    """Compute weighted average factors from a composicao_fibras list.

    Each entry: {"fibra": str, "pct": float}
    Returns None if any material is unknown.
    """
    total_pct = sum(f.get("pct", 0) for f in fibers)
    if abs(total_pct - 100) > 0.1:
        return None

    agua = energia = carbono = 0.0
    for entry in fibers:
        key = entry.get("fibra", "")
        pct = entry.get("pct", 0) / 100
        factors = GENERIC_FACTORS.get(key)
        if factors is None:
            return None
        agua += factors["agua_litros_kg"] * pct
        energia += factors["energia_kwh_kg"] * pct
        carbono += factors["carbono_kgco2e_kg"] * pct

    return {
        "agua_litros_kg": round(agua, 2),
        "energia_kwh_kg": round(energia, 2),
        "carbono_kgco2e_kg": round(carbono, 2),
    }
