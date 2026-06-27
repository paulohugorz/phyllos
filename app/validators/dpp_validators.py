from __future__ import annotations

import json
import unicodedata
from dataclasses import dataclass
from datetime import date

from app.services.dpp_factor_sources import BLOCKED_FACTOR_SOURCE_TERMS


EVIDENCE_LABELS = {
    "ausente": "Nao informado pela marca",
    "declarado": "Declarado pela marca, nao auditado",
    "calculado": "Estimativa calculada com fator medio ou declarado",
    "documentado": "Documentado por arquivo de apoio",
    "verificado": "Verificado por terceiro",
}

REQUIRED_TIER1_FIELDS = (
    "sku_codigo",
    "nome_peca",
    "identificador_publico",
    "composicao_fibras",
    "pais_fabricacao",
    "instrucoes_cuidado",
    "instrucoes_fim_de_vida",
)

REQUIRED_FACTOR_SOURCE_FIELDS = (
    ("fonte_agua_litros_kg", "fonte do fator de agua", "agua_peca_litros"),
    ("fonte_energia_kwh_kg", "fonte do fator de energia", "energia_peca_kwh"),
    ("fonte_carbono_kgco2e_kg", "fonte do fator de carbono", "pegada_carbono_kgco2e"),
)

# unit_source obrigatorio para publicacao — rejeita se ausente
REQUIRED_UNIT_SOURCE_FIELDS = (
    ("agua_unit_source", "unidade da fonte do fator de agua (ex: L/kg ou m3/kg)"),
    ("energia_unit_source", "unidade da fonte do fator de energia (ex: kWh/kg ou MJ/kg)"),
)


@dataclass(frozen=True)
class DppValidationResult:
    can_publish: bool
    errors: list[str]
    warnings: list[str]
    evidence_statuses: dict[str, str]


def parse_json_list(raw: str | None, field_name: str) -> list:
    if not raw:
        return []
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{field_name} deve ser JSON valido") from exc
    if not isinstance(value, list):
        raise ValueError(f"{field_name} deve ser uma lista JSON")
    return value


def validate_fiber_composition(raw: str | None) -> list:
    fibers = parse_json_list(raw, "composicao_fibras")
    if not fibers:
        raise ValueError("composicao_fibras obrigatoria para publicar DPP")
    total = 0
    for item in fibers:
        if not isinstance(item, dict):
            raise ValueError("cada fibra deve ser um objeto")
        pct = item.get("pct")
        if pct is None:
            raise ValueError("cada fibra precisa de pct")
        total += float(pct)
    if abs(total - 100) > 0.01:
        raise ValueError("composicao_fibras deve somar 100%")
    return fibers


def certification_warnings(raw: str | None, today: date | None = None) -> list[str]:
    today = today or date.today()
    warnings = []
    for cert in parse_json_list(raw, "certificacoes"):
        validade = cert.get("validade") if isinstance(cert, dict) else None
        nome = cert.get("nome") or cert.get("tipo") if isinstance(cert, dict) else "certificacao"
        if not validade:
            continue
        try:
            expires_at = date.fromisoformat(str(validade))
        except ValueError:
            warnings.append(f"{nome}: validade em formato invalido")
            continue
        if expires_at < today:
            warnings.append(f"{nome}: certificado expirado")
    return warnings


def _has_text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _has_value(value) -> bool:
    return value is not None and value != ""


def _normalise_text(value: str) -> str:
    return unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()


def build_evidence_statuses(peca, ficha) -> dict[str, str]:
    has_public_identifier = any(
        _has_text(getattr(peca, field, None))
        for field in ("dpp_uuid", "gtin", "codigo")
    )
    has_country = bool(getattr(peca, "tem_pais_fabricacao", False)) or _has_text(
        getattr(peca, "pais_fabricacao", None)
    )
    statuses = {
        "sku_codigo": "declarado" if _has_text(getattr(peca, "codigo", None)) else "ausente",
        "nome_peca": "declarado" if _has_text(getattr(peca, "nome", None)) else "ausente",
        "identificador_publico": "declarado" if has_public_identifier else "ausente",
        "composicao_fibras": "declarado" if ficha and getattr(ficha, "composicao_fibras", None) else "ausente",
        "pais_fabricacao": "declarado" if has_country else "ausente",
        "instrucoes_cuidado": "declarado" if ficha and _has_text(getattr(ficha, "instrucoes_reparo", None)) else "ausente",
        "instrucoes_fim_de_vida": "declarado" if ficha and _has_text(getattr(ficha, "instrucoes_fim_de_vida", None)) else "ausente",
        "area_peca_m2": "declarado" if getattr(peca, "area_peca_m2", None) is not None else "ausente",
        "perda_corte_pct": "declarado" if getattr(peca, "perda_corte_pct", None) is not None else "ausente",
        "lote_quantidade": "declarado" if getattr(peca, "lote_quantidade", None) is not None else "ausente",
        "gramatura_g_m2": "declarado" if ficha and getattr(ficha, "gramatura_g_m2", None) is not None else "ausente",
        "agua_peca_litros": "calculado" if ficha and getattr(ficha, "agua_peca_litros", None) is not None else "ausente",
        "energia_peca_kwh": "calculado" if ficha and getattr(ficha, "energia_peca_kwh", None) is not None else "ausente",
        "carbono_peca_kgco2e": "calculado" if ficha and getattr(ficha, "pegada_carbono_kgco2e", None) is not None else "ausente",
        "certificacoes": "documentado" if ficha and getattr(ficha, "certificacoes", None) else "ausente",
        "fonte_agua_litros_kg": "declarado" if ficha and _has_text(getattr(ficha, "fonte_agua_litros_kg", None)) else "ausente",
        "fonte_energia_kwh_kg": "declarado" if ficha and _has_text(getattr(ficha, "fonte_energia_kwh_kg", None)) else "ausente",
        "fonte_carbono_kgco2e_kg": "declarado" if ficha and _has_text(getattr(ficha, "fonte_carbono_kgco2e_kg", None)) else "ausente",
    }
    return statuses


def validate_dpp_publication(peca, ficha) -> DppValidationResult:
    errors = []
    warnings = []
    reported_missing_fields = set()

    if not _has_text(getattr(peca, "codigo", None)):
        errors.append("SKU ou codigo interno obrigatorio para publicar DPP")
        reported_missing_fields.add("sku_codigo")
    if not _has_text(getattr(peca, "nome", None)):
        errors.append("nome da peca obrigatorio para publicar DPP")
        reported_missing_fields.add("nome_peca")
    if not any(_has_text(getattr(peca, field, None)) for field in ("dpp_uuid", "gtin", "codigo")):
        errors.append("identificador publico obrigatorio para publicar DPP")
        reported_missing_fields.add("identificador_publico")
    if not (getattr(peca, "tem_pais_fabricacao", False) or _has_text(getattr(peca, "pais_fabricacao", None))):
        errors.append("pais de fabricacao obrigatorio para publicar DPP")
        reported_missing_fields.add("pais_fabricacao")
    if not ficha:
        errors.append("Ficha tecnica obrigatoria para publicar DPP")
        reported_missing_fields.update({
            "composicao_fibras",
            "instrucoes_cuidado",
            "instrucoes_fim_de_vida",
        })
    else:
        try:
            validate_fiber_composition(getattr(ficha, "composicao_fibras", None))
        except ValueError as exc:
            errors.append(str(exc))
            reported_missing_fields.add("composicao_fibras")
        warnings.extend(certification_warnings(getattr(ficha, "certificacoes", None)))

        if not _has_text(getattr(ficha, "instrucoes_reparo", None)):
            errors.append("instrucoes de cuidado/lavagem obrigatorias para publicar DPP")
            reported_missing_fields.add("instrucoes_cuidado")
        if not _has_text(getattr(ficha, "instrucoes_fim_de_vida", None)):
            errors.append("instrucoes de fim de vida obrigatorias para publicar DPP")
            reported_missing_fields.add("instrucoes_fim_de_vida")

    has_tier2_input = any(
        _has_value(getattr(peca, field, None))
        for field in ("area_peca_m2", "perda_corte_pct", "lote_quantidade")
    ) or any(
        _has_value(getattr(ficha, field, None)) if ficha else False
        for field in (
            "gramatura_g_m2",
            "agua_litros_kg",
            "energia_kwh_kg",
            "carbono_kgco2e_kg",
            "agua_peca_litros",
            "energia_peca_kwh",
            "pegada_carbono_kgco2e",
        )
    )

    tier2_required_values = (
        ("area_peca_m2", "area da peca", peca),
        ("perda_corte_pct", "perda de corte", peca),
        ("gramatura_g_m2", "gramatura", ficha),
        ("agua_litros_kg", "fator de agua", ficha),
        ("energia_kwh_kg", "fator de energia", ficha),
        ("carbono_kgco2e_kg", "fator de carbono", ficha),
    )
    if has_tier2_input:
        missing_tier2 = [
            label
            for field, label, source in tier2_required_values
            if source is None or not _has_value(getattr(source, field, None))
        ]
        if missing_tier2:
            warnings.append(
                "Tier 2 incompleto; indicadores de agua, energia e carbono nao serao publicados: "
                + ", ".join(missing_tier2)
            )

    for field, label, impact_field in REQUIRED_FACTOR_SOURCE_FIELDS:
        value = getattr(ficha, field, None) if ficha else None
        impact_is_public = _has_value(getattr(ficha, impact_field, None)) if ficha else False
        if impact_is_public and not _has_text(value):
            errors.append(f"{label} obrigatoria para publicar DPP")
            continue
        source_text = _normalise_text(value) if _has_text(value) else ""
        if source_text and any(term in source_text for term in BLOCKED_FACTOR_SOURCE_TERMS):
            errors.append(f"{label} nao pode usar proxy de demonstracao para publicar DPP")

    # unit_source obrigatorio para cada fator publicado
    for unit_field, unit_label in REQUIRED_UNIT_SOURCE_FIELDS:
        factor_field = unit_field.replace("_unit_source", "_litros_kg") if "agua" in unit_field else unit_field.replace("_unit_source", "_kwh_kg")
        factor_is_public = _has_value(getattr(ficha, factor_field, None)) if ficha else False
        if factor_is_public and not _has_text(getattr(ficha, unit_field, None) if ficha else None):
            errors.append(f"{unit_label} obrigatoria para publicar fator de impacto")

    statuses = build_evidence_statuses(peca, ficha)
    for field in REQUIRED_TIER1_FIELDS:
        if statuses.get(field) == "ausente" and field not in reported_missing_fields:
            errors.append(f"{field} sem evidencia minima")

    return DppValidationResult(
        can_publish=not errors,
        errors=errors,
        warnings=warnings,
        evidence_statuses=statuses,
    )
