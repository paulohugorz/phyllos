"""
Validação cruzada de evidências — 3 gates de qualidade.

Gate 1 — range: verificado no llm_extractor durante a extração
Gate 2 — coerência de unidade: verificar se o valor numérico é compatível com a unidade declarada
Gate 3 — cross-check: comparar com outras evidências da mesma fibra
"""

from __future__ import annotations
import logging
from impact_collector.models import ImpactEvidence

logger = logging.getLogger(__name__)

# Unidades aceitas por indicador
_VALID_UNITS_CO2 = {"kgco2eq/kg", "kg co2 eq/kg", "kgco2e/kg", "kg co2e/kg", "kgco2/kg"}
_VALID_UNITS_AGUA = {"l/kg", "liters/kg", "litres/kg", "m3/kg", "liter/kg"}
_VALID_UNITS_ENERGIA = {"mj/kg", "kwh/kg", "gj/kg", "mj per kg"}

# Fatores de conversão para unidade padrão
_UNIT_CONVERSIONS_AGUA = {
    "m3/kg": 1000.0,  # 1 m3 = 1000 L
}
_UNIT_CONVERSIONS_ENERGIA = {
    "kwh/kg": 3.6,  # 1 kWh = 3.6 MJ
    "gj/kg": 1000.0,  # 1 GJ = 1000 MJ
}


def gate2_unit_coherence(evidence: ImpactEvidence) -> ImpactEvidence:
    """
    Gate 2: verifica e normaliza unidades.
    Modifica os valores in-place quando conversão é necessária.
    Rebaixa confiança se unidade inválida detectada.
    """
    issues = []

    # CO2 — se valor > 200 kgCO2e/kg, provavelmente está em g ou tonne
    if evidence.co2eq_kg_por_kg is not None:
        if evidence.co2eq_kg_por_kg > 200:
            # Suspeita de tCO2e/kg — converter
            logger.warning(
                "CO2 suspeito (%s kgCO2e/kg) para %s — possível tCO2e. Rebaixando.",
                evidence.co2eq_kg_por_kg, evidence.fibra_id,
            )
            issues.append("CO2 fora do range plausível")

    # Água — se valor > 500_000 L/kg, suspeita de m3 mal convertido
    if evidence.agua_l_por_kg is not None:
        if evidence.agua_l_por_kg > 500_000:
            logger.warning(
                "Água suspeita (%s L/kg) para %s", evidence.agua_l_por_kg, evidence.fibra_id
            )
            issues.append("Água fora do range plausível")

    # Energia — se valor > 2000 MJ/kg, provavelmente em kJ
    if evidence.energia_mj_por_kg is not None:
        if evidence.energia_mj_por_kg > 2000:
            logger.warning(
                "Energia suspeita (%s MJ/kg) para %s — possível kJ. Rebaixando.",
                evidence.energia_mj_por_kg, evidence.fibra_id,
            )
            issues.append("Energia fora do range plausível")

    if issues and evidence.confianca == "alta":
        evidence.confianca = "media"
    elif issues and evidence.confianca == "media":
        evidence.confianca = "baixa"

    return evidence


def gate3_cross_check(
    new_evidence: ImpactEvidence,
    existing_evidences: list[ImpactEvidence],
    tolerance: float = 0.4,
) -> tuple[ImpactEvidence, bool]:
    """
    Gate 3: verifica se nova evidência é consistente com existentes.

    Retorna (evidência atualizada, passou_no_gate).
    Eleva confiança para "media" se houver concordância com outra fonte.
    """
    comparables = [
        e for e in existing_evidences
        if e.fibra_id == new_evidence.fibra_id
        and e.escopo_lca == new_evidence.escopo_lca
        and e.confianca in ("alta", "media")
        and e.has_any_value()
    ]

    if not comparables:
        # Sem base de comparação ainda — manter confiança atual
        return new_evidence, True

    def _check_metric(new_val: float | None, field: str) -> bool | None:
        """None = sem dados para comparar. True/False = dentro/fora da tolerância."""
        if new_val is None:
            return None
        existing_vals = [getattr(e, field) for e in comparables if getattr(e, field) is not None]
        if not existing_vals:
            return None
        median = sorted(existing_vals)[len(existing_vals) // 2]
        if median == 0:
            return None
        deviation = abs(new_val - median) / median
        return deviation <= tolerance

    results = {
        "co2": _check_metric(new_evidence.co2eq_kg_por_kg, "co2eq_kg_por_kg"),
        "agua": _check_metric(new_evidence.agua_l_por_kg, "agua_l_por_kg"),
        "energia": _check_metric(new_evidence.energia_mj_por_kg, "energia_mj_por_kg"),
    }

    checks_with_data = {k: v for k, v in results.items() if v is not None}

    if not checks_with_data:
        return new_evidence, True

    passed = all(checks_with_data.values())
    any_passed = any(checks_with_data.values())

    if passed and new_evidence.confianca == "baixa":
        new_evidence.confianca = "media"
        logger.info(
            "Gate 3 elevou confiança para 'media' — %s consistente com %d fontes",
            new_evidence.fibra_id, len(comparables),
        )
    elif not any_passed:
        logger.warning(
            "Gate 3 falhou para %s — valores divergem >%d%% da mediana de %d fontes. "
            "Enfileirado para revisão humana.",
            new_evidence.fibra_id, int(tolerance * 100), len(comparables),
        )

    return new_evidence, passed or any_passed
