from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date


EVIDENCE_LABELS = {
    "ausente": "Nao informado pela marca",
    "declarado": "Declarado pela marca, nao auditado",
    "calculado": "Estimativa calculada com fator medio ou declarado",
    "documentado": "Documentado por arquivo de apoio",
    "verificado": "Verificado por terceiro",
}

REQUIRED_EVIDENCE_FIELDS = (
    "composicao_fibras",
    "area_peca_m2",
    "perda_corte_pct",
    "lote_quantidade",
    "gramatura_g_m2",
    "agua_peca_litros",
    "energia_peca_kwh",
    "carbono_peca_kgco2e",
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


def build_evidence_statuses(peca, ficha) -> dict[str, str]:
    statuses = {
        "composicao_fibras": "declarado" if ficha and ficha.composicao_fibras else "ausente",
        "area_peca_m2": "declarado" if peca.area_peca_m2 is not None else "ausente",
        "perda_corte_pct": "declarado" if peca.perda_corte_pct is not None else "ausente",
        "lote_quantidade": "declarado" if peca.lote_quantidade is not None else "ausente",
        "gramatura_g_m2": "declarado" if ficha and ficha.gramatura_g_m2 is not None else "ausente",
        "agua_peca_litros": "calculado" if ficha and ficha.agua_peca_litros is not None else "ausente",
        "energia_peca_kwh": "calculado" if ficha and ficha.energia_peca_kwh is not None else "ausente",
        "carbono_peca_kgco2e": "calculado" if ficha and ficha.pegada_carbono_kgco2e is not None else "ausente",
        "certificacoes": "documentado" if ficha and ficha.certificacoes else "ausente",
    }
    return statuses


def validate_dpp_publication(peca, ficha) -> DppValidationResult:
    errors = []
    warnings = []

    if not peca.gtin:
        errors.append("GTIN ou identificador publico obrigatorio para publicar DPP")
    if not ficha:
        errors.append("Ficha tecnica obrigatoria para publicar DPP")
    else:
        try:
            validate_fiber_composition(ficha.composicao_fibras)
        except ValueError as exc:
            errors.append(str(exc))
        warnings.extend(certification_warnings(ficha.certificacoes))

    for field, label in (
        ("area_peca_m2", "area da peca"),
        ("perda_corte_pct", "perda de corte"),
        ("lote_quantidade", "quantidade do lote"),
    ):
        value = getattr(peca, field, None)
        if value is None:
            errors.append(f"{label} obrigatoria para publicar DPP")

    for field, label in (
        ("gramatura_g_m2", "gramatura"),
        ("agua_litros_kg", "fator de agua"),
        ("energia_kwh_kg", "fator de energia"),
        ("carbono_kgco2e_kg", "fator de carbono"),
    ):
        value = getattr(ficha, field, None) if ficha else None
        if value is None:
            errors.append(f"{label} obrigatorio para publicar DPP")

    statuses = build_evidence_statuses(peca, ficha)
    missing = [field for field in REQUIRED_EVIDENCE_FIELDS if statuses.get(field) == "ausente"]
    for field in missing:
        errors.append(f"{field} sem evidencia minima")

    return DppValidationResult(
        can_publish=not errors,
        errors=errors,
        warnings=warnings,
        evidence_statuses=statuses,
    )
