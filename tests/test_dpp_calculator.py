import unittest

from app.services.dpp_calculator import (
    DppCalculationError,
    DppCalculationInput,
    calculate_dpp_indicators,
)


class DppCalculatorTests(unittest.TestCase):
    def test_calculate_dpp_indicators_is_deterministic(self):
        result = calculate_dpp_indicators(DppCalculationInput(
            area_peca_m2=1,
            perda_corte_pct=20,
            gramatura_g_m2=200,
            agua_litros_kg=100,
            energia_kwh_kg=10,
            carbono_kgco2e_kg=2,
        ))

        self.assertEqual(result.area_total_requerida_m2, 1.25)
        self.assertEqual(result.area_perdida_m2, 0.25)
        self.assertEqual(result.peso_peca_kg, 0.25)
        self.assertEqual(result.agua_peca_litros, 25)
        self.assertEqual(result.energia_peca_kwh, 2.5)
        self.assertEqual(result.carbono_peca_kgco2e, 0.5)

    def test_calculate_dpp_indicators_rejects_cut_loss_at_or_above_100(self):
        with self.assertRaisesRegex(DppCalculationError, "perda_corte_pct"):
            calculate_dpp_indicators({
                "area_peca_m2": 1,
                "perda_corte_pct": 100,
                "gramatura_g_m2": 200,
                "agua_litros_kg": 100,
                "energia_kwh_kg": 10,
                "carbono_kgco2e_kg": 2,
            })

    def test_calculate_dpp_indicators_accepts_zero_cut_loss(self):
        result = calculate_dpp_indicators(DppCalculationInput(
            area_peca_m2=1,
            perda_corte_pct=0,
            gramatura_g_m2=200,
            agua_litros_kg=100,
            energia_kwh_kg=10,
            carbono_kgco2e_kg=2,
        ))

        self.assertEqual(result.area_total_requerida_m2, 1)
        self.assertEqual(result.area_perdida_m2, 0)
        self.assertEqual(result.peso_peca_kg, 0.2)


if __name__ == "__main__":
    unittest.main()
