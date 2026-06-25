"""Guidance for impact-factor source metadata used by DPP publication gates."""

IMPACT_FACTOR_SOURCE_GUIDANCE = {
    "agua_litros_kg": {
        "source_field": "fonte_agua_litros_kg",
        "public_label": "Fonte do fator de agua",
        "accepted_examples": (
            "laudo do fornecedor",
            "base setorial documentada, como Textile Exchange ou Higg MSI",
            "referencia hidrica documentada por material/processo",
        ),
    },
    "energia_kwh_kg": {
        "source_field": "fonte_energia_kwh_kg",
        "public_label": "Fonte do fator de energia",
        "accepted_examples": (
            "laudo do fornecedor",
            "base setorial documentada, como Higg MSI ou ecoinvent",
            "medicao declarada da etapa produtiva",
        ),
    },
    "carbono_kgco2e_kg": {
        "source_field": "fonte_carbono_kgco2e_kg",
        "public_label": "Fonte do fator de carbono",
        "accepted_examples": (
            "laudo do fornecedor",
            "base setorial documentada, como Higg MSI ou ecoinvent",
            "fator de emissao documentado, como IPCC ou GHG Protocol",
        ),
    },
}

BLOCKED_FACTOR_SOURCE_TERMS = (
    "proxy interno",
    "proxy de demonstracao",
    "demonstracao",
    "demo",
    "nao usar em piloto",
)
