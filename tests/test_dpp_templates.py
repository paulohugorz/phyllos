import hashlib
import unittest
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from app.validators.dpp_validators import EVIDENCE_LABELS


class DppTemplateTests(unittest.TestCase):
    def test_consumer_dpp_template_renders_with_minimum_context(self):
        templates_dir = Path(__file__).resolve().parents[1] / "app" / "templates"
        env = Environment(
            loader=FileSystemLoader(templates_dir),
            autoescape=select_autoescape(["html"]),
        )

        html = env.get_template("dpp_consumer.html").render({
            "peca_nome": "Camiseta Teste",
            "peca_codigo": "DPP-TEMPLATE",
            "peca_gtin": "7891234567890",
            "peca_uuid": "uuid-template",
            "peca_status": "publicado",
            "dpp_version": "1.0",
            "data_publicacao": None,
            "composicao": [],
            "certificacoes": [],
            "carbono_kgco2e": None,
            "agua_peca_litros": None,
            "energia_peca_kwh": None,
            "area_perdida_m2": None,
            "peso_peca_kg": None,
            "perda_corte_pct": None,
            "lote_quantidade": 100,
            "evidence_statuses": {},
            "evidence_labels": EVIDENCE_LABELS,
            "durabilidade_ciclos": None,
            "instrucoes_reparo": None,
            "instrucoes_fim_vida": None,
            "fornecedores": [],
            "total_cards": 3,
        })

        self.assertIn("Camiseta Teste", html)
        self.assertIn("DPP 1.0", html)
        self.assertIn("Indicadores aguardam ficha", html)
        self.assertIn("evidence-badge", html)

    def test_consumer_dpp_template_avoids_unverified_sustainability_claims(self):
        template = (
            Path(__file__).resolve().parents[1] / "app" / "templates" / "dpp_consumer.html"
        ).read_text(encoding="utf-8")

        forbidden_phrases = (
            "Credenciais de sustentabilidade",
            "Certificação de Origem",
            "Damos preferência a fibras comprovadamente duráveis",
        )
        for phrase in forbidden_phrases:
            self.assertNotIn(phrase, template)

        self.assertIn("Não substitui ACV auditada", template)

    def test_dpp_studio_matches_canonical_bundle_and_macro_flow(self):
        studio_path = Path(__file__).resolve().parents[1] / "phyllos" / "dpp-studio.html"
        studio_bytes = studio_path.read_bytes()
        studio = studio_bytes.decode("utf-8")

        self.assertEqual(
            hashlib.sha256(studio_bytes).hexdigest(),
            "560add24d6e31860fee858805644270b31e030b0a5d0d5ab273d21d52194b8c2",
        )
        for macro_step in ("Intenção", "Materiais", "Especificações", "Indicadores"):
            self.assertIn(macro_step, studio)

        self.assertNotIn("Publicar DPP e gerar QR", studio)
        self.assertNotIn("DPP publicado — QR ativo", studio)


if __name__ == "__main__":
    unittest.main()
