from __future__ import annotations

from dataclasses import asdict, dataclass


class DppCalculationError(ValueError):
    pass


@dataclass(frozen=True)
class DppCalculationInput:
    area_peca_m2: float
    perda_corte_pct: float
    gramatura_g_m2: float
    agua_litros_kg: float
    energia_kwh_kg: float
    carbono_kgco2e_kg: float


@dataclass(frozen=True)
class DppCalculationResult:
    area_total_requerida_m2: float
    area_perdida_m2: float
    peso_peca_kg: float
    agua_peca_litros: float
    energia_peca_kwh: float
    carbono_peca_kgco2e: float
    status_evidencia: str = "calculado"
    label_publica: str = "Estimativa calculada com fator medio ou declarado."

    def as_dict(self) -> dict:
        return asdict(self)


def _positive(name: str, value: float) -> float:
    if value is None:
        raise DppCalculationError(f"{name} e obrigatorio")
    value = float(value)
    if value < 0:
        raise DppCalculationError(f"{name} nao pode ser negativo")
    return value


def calculate_dpp_indicators(data: DppCalculationInput | dict) -> DppCalculationResult:
    if isinstance(data, dict):
        data = DppCalculationInput(**data)

    area_peca = _positive("area_peca_m2", data.area_peca_m2)
    if area_peca == 0:
        raise DppCalculationError("area_peca_m2 deve ser maior que zero")

    perda_pct = _positive("perda_corte_pct", data.perda_corte_pct)
    if perda_pct >= 100:
        raise DppCalculationError("perda_corte_pct deve ser menor que 100")

    gramatura_kg_m2 = _positive("gramatura_g_m2", data.gramatura_g_m2) / 1000
    if gramatura_kg_m2 == 0:
        raise DppCalculationError("gramatura_g_m2 deve ser maior que zero")

    agua_litros_kg = _positive("agua_litros_kg", data.agua_litros_kg)
    energia_kwh_kg = _positive("energia_kwh_kg", data.energia_kwh_kg)
    carbono_kgco2e_kg = _positive("carbono_kgco2e_kg", data.carbono_kgco2e_kg)

    perda_decimal = perda_pct / 100
    area_total = area_peca / (1 - perda_decimal)
    area_perdida = area_total - area_peca
    peso = area_total * gramatura_kg_m2

    return DppCalculationResult(
        area_total_requerida_m2=round(area_total, 6),
        area_perdida_m2=round(area_perdida, 6),
        peso_peca_kg=round(peso, 6),
        agua_peca_litros=round(peso * agua_litros_kg, 6),
        energia_peca_kwh=round(peso * energia_kwh_kg, 6),
        carbono_peca_kgco2e=round(peso * carbono_kgco2e_kg, 6),
    )
