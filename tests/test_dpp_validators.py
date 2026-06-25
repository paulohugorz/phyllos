import json
from types import SimpleNamespace
import unittest

from app.validators.dpp_validators import (
    validate_dpp_publication,
    validate_fiber_composition,
)


class DppValidatorTests(unittest.TestCase):
    def test_validate_fiber_composition_requires_100_percent_total(self):
        with self.assertRaisesRegex(ValueError, "100%"):
            validate_fiber_composition(json.dumps([
                {"fibra": "algodao", "pct": 80},
                {"fibra": "elastano", "pct": 10},
            ]))


    def test_validate_dpp_publication_accepts_minimum_evidence_after_calculation(self):
        peca = SimpleNamespace(
            gtin="7891234567890",
            area_peca_m2=1,
            perda_corte_pct=20,
            lote_quantidade=100,
        )
        ficha = SimpleNamespace(
            composicao_fibras=json.dumps([{"fibra": "algodao", "pct": 100}]),
            certificacoes=None,
            gramatura_g_m2=200,
            agua_litros_kg=100,
            energia_kwh_kg=10,
            carbono_kgco2e_kg=2,
            agua_peca_litros=25,
            energia_peca_kwh=2.5,
            pegada_carbono_kgco2e=0.5,
        )

        result = validate_dpp_publication(peca, ficha)

        self.assertTrue(result.can_publish)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.evidence_statuses["composicao_fibras"], "declarado")
        self.assertEqual(result.evidence_statuses["carbono_peca_kgco2e"], "calculado")


if __name__ == "__main__":
    unittest.main()
