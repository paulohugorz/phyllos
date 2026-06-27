import unittest

from app.services.dpp_generic_factors import (
    GENERIC_FACTORS,
    METHODOLOGY_TAG,
    SOURCE_LABELS,
    apply_generic_factors,
    blend_factors_from_composition,
    get_factors,
)


class GetFactorsTests(unittest.TestCase):
    def test_known_material_returns_dict(self):
        f = get_factors("poliester_reciclado")
        self.assertIsNotNone(f)
        self.assertIn("agua_litros_kg", f)
        self.assertIn("energia_kwh_kg", f)
        self.assertIn("carbono_kgco2e_kg", f)

    def test_unknown_material_returns_none(self):
        self.assertIsNone(get_factors("material_inexistente"))

    def test_all_factors_are_positive(self):
        for material, factors in GENERIC_FACTORS.items():
            for key, value in factors.items():
                self.assertGreater(value, 0, f"{material}.{key} deve ser positivo")


class ApplyGenericFactorsTests(unittest.TestCase):
    def test_fills_empty_fields(self):
        result = apply_generic_factors({}, "algodao_convencional")
        self.assertEqual(result["agua_litros_kg"], 10_000.0)
        self.assertEqual(
            result["energia_kwh_kg"],
            GENERIC_FACTORS["algodao_convencional"]["energia_kwh_kg"],
        )
        self.assertEqual(result["carbono_kgco2e_kg"], 5.9)
        self.assertEqual(result["fonte_agua_litros_kg"], SOURCE_LABELS["agua"])
        self.assertEqual(result["metodologia_fatores_impacto"], METHODOLOGY_TAG)

    def test_does_not_overwrite_supplier_data(self):
        ficha = {
            "agua_litros_kg": 9999.0,
            "fonte_agua_litros_kg": "laudo do fornecedor XYZ",
        }
        result = apply_generic_factors(ficha, "algodao_convencional")
        self.assertEqual(result["agua_litros_kg"], 9999.0)
        self.assertEqual(result["fonte_agua_litros_kg"], "laudo do fornecedor XYZ")
        # energia e carbono ainda são preenchidos
        self.assertEqual(
            result["energia_kwh_kg"],
            GENERIC_FACTORS["algodao_convencional"]["energia_kwh_kg"],
        )

    def test_unknown_material_returns_unchanged(self):
        ficha = {"agua_litros_kg": None}
        result = apply_generic_factors(ficha, "fibra_desconhecida")
        self.assertIsNone(result["agua_litros_kg"])

    def test_does_not_mutate_input(self):
        original = {"agua_litros_kg": None}
        apply_generic_factors(original, "poliester_reciclado")
        self.assertIsNone(original["agua_litros_kg"])

    def test_methodology_not_overwritten_if_present(self):
        ficha = {"metodologia_fatores_impacto": "metodologia customizada do fornecedor"}
        result = apply_generic_factors(ficha, "poliester_reciclado")
        self.assertEqual(result["metodologia_fatores_impacto"], "metodologia customizada do fornecedor")


class BlendFactorsTests(unittest.TestCase):
    def test_pure_material_blend(self):
        fibers = [{"fibra": "poliester_reciclado", "pct": 100}]
        result = blend_factors_from_composition(fibers)
        self.assertIsNotNone(result)
        self.assertEqual(result["agua_litros_kg"], GENERIC_FACTORS["poliester_reciclado"]["agua_litros_kg"])

    def test_two_component_blend(self):
        fibers = [
            {"fibra": "poliester_reciclado", "pct": 78},
            {"fibra": "elastano_spandex", "pct": 22},
        ]
        result = blend_factors_from_composition(fibers)
        self.assertIsNotNone(result)
        expected_agua = round(
            0.78 * GENERIC_FACTORS["poliester_reciclado"]["agua_litros_kg"]
            + 0.22 * GENERIC_FACTORS["elastano_spandex"]["agua_litros_kg"],
            2,
        )
        self.assertAlmostEqual(result["agua_litros_kg"], expected_agua, places=1)

    def test_unknown_fiber_returns_none(self):
        fibers = [
            {"fibra": "poliester_reciclado", "pct": 80},
            {"fibra": "fibra_marciana", "pct": 20},
        ]
        self.assertIsNone(blend_factors_from_composition(fibers))

    def test_pct_not_summing_to_100_returns_none(self):
        fibers = [{"fibra": "poliester_reciclado", "pct": 50}]
        self.assertIsNone(blend_factors_from_composition(fibers))

    def test_methodology_tag_contains_version_info(self):
        self.assertIn("Ecoinvent 3.9", METHODOLOGY_TAG)
        self.assertIn("IPCC AR6", METHODOLOGY_TAG)


if __name__ == "__main__":
    unittest.main()
