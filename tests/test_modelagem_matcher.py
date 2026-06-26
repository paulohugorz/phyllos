from types import SimpleNamespace
import unittest

from app.services.modelagem_matcher import (
    build_molde_intent_spec,
    measurement_strategy,
    rank_variations,
    resolve_semantic_profile,
    select_representative_recommendations,
)


def make_variation(
    codigo,
    categoria,
    nome,
    subcategoria,
    grau_ajuste,
    tipo_tecido,
    descricao,
    tags="",
):
    return SimpleNamespace(
        codigo=codigo,
        descricao_natural=descricao,
        tags=tags,
        grau_ajuste=grau_ajuste,
        tipo_tecido=tipo_tecido,
        comprimento=None,
        decote=None,
        manga=None,
        fechamento=None,
        cos=None,
        molde_base=SimpleNamespace(
            codigo=f"base-{codigo}",
            nome=nome,
            categoria=categoria,
            subcategoria=subcategoria,
            descricao=descricao,
            notas_construcao=None,
        ),
    )


class ModelagemMatcherTests(unittest.TestCase):
    def test_resolves_macacao_folgado_alfaiataria_as_composite_reference(self):
        profile = resolve_semantic_profile("macação folgado tipo alfaitaria")

        self.assertEqual(profile.categoria_input, "macacao")
        self.assertEqual(profile.grau_ajuste, "relaxed")
        self.assertEqual(profile.tipo_tecido, "plano")
        self.assertTrue(profile.precisa_base_composta)
        self.assertIn("vestido", profile.categorias_referencia)
        self.assertIn("calca", profile.categorias_referencia)

    def test_ranks_body_and_lower_block_for_tailored_relaxed_jumpsuit(self):
        variations = [
            make_variation(
                "vestido-chemisier-m-plano-relaxed",
                "vestido",
                "Vestido Chemisier",
                "chemisier",
                "relaxed",
                "plano",
                "Vestido chemisier social de alfaiataria com corpo inteiro e botoes.",
            ),
            make_variation(
                "calca-pantalona-m-plano-relaxed",
                "calca",
                "Calca Pantalona",
                "pantalona",
                "relaxed",
                "plano",
                "Calca pantalona social ampla de alfaiataria.",
            ),
            make_variation(
                "legging-m-malha-fitted",
                "calca",
                "Legging",
                "legging",
                "fitted",
                "malha",
                "Legging esportiva justa em malha.",
            ),
            make_variation(
                "vestido-tubo-m-plano-fitted",
                "vestido",
                "Vestido Tubo",
                "tubo_pences",
                "fitted",
                "plano",
                "Vestido tubo social ajustado com pences.",
            ),
        ]

        profile, ranked = rank_variations("macacão folgado tipo alfaiataria", variations, limit=4)
        top_roles = {item.papel_referencia for item in ranked[:2]}

        self.assertEqual(profile.categoria_input, "macacao")
        self.assertEqual(top_roles, {"tronco_corpo_inteiro", "perna_gancho"})
        self.assertGreater(ranked[0].score, ranked[-1].score)
        self.assertNotEqual(ranked[0].variacao.codigo, "legging-m-malha-fitted")

    def test_measurement_strategy_warns_about_jumpsuit_specific_points(self):
        profile = resolve_semantic_profile("macacão folgado tipo alfaiataria")
        strategy = measurement_strategy(profile)

        self.assertEqual(strategy["tipo"], "base_composta")
        self.assertIn("gancho", strategy["mapa_medidas"]["perna"])
        self.assertTrue(any("sentado" in item for item in strategy["pontos_criticos"]))

    def test_builds_text_to_molde_spec_for_camp_collar_shirt(self):
        spec = build_molde_intent_spec("camisa camp collar de linho com manga curta")

        self.assertEqual(spec["versao"], "text_to_molde_v0")
        self.assertEqual(spec["perfil"]["categoria_input"], "camisa")
        self.assertEqual(spec["perfil"]["tipo_tecido"], "plano")
        self.assertIn("gola_camp", spec["componentes"])
        self.assertIn("manga_curta", spec["componentes"])
        self.assertIn("comprimento_manga", spec["medidas_obrigatorias"])
        self.assertIn("validar_compatibilidade_manga_cava", spec["validacoes_obrigatorias"])
        self.assertIn("validar_compatibilidade_gola_decote", spec["validacoes_obrigatorias"])

    def test_text_to_molde_spec_keeps_jumpsuit_as_composite(self):
        spec = build_molde_intent_spec("macacão folgado tipo alfaiataria")

        self.assertTrue(spec["perfil"]["precisa_base_composta"])
        self.assertIn("combinar_base_superior_com_base_inferior", spec["operacoes_geometricas"])
        self.assertIn("comprimento_torso", spec["medidas_obrigatorias"])
        self.assertIn("validar_gancho_em_pe_e_sentado", spec["validacoes_obrigatorias"])

    def test_composite_recommendations_keep_lower_block_even_with_many_torso_sizes(self):
        variations = [
            make_variation(
                f"vestido-tubo-{size}-plano-relaxed",
                "vestido",
                "Vestido Tubo",
                "tubo_pences",
                "relaxed",
                "plano",
                "Vestido tubo social de alfaiataria.",
            )
            for size in ("36", "38", "40", "42", "44", "46")
        ]
        variations.append(
            make_variation(
                "calca-pantalona-40-plano-relaxed",
                "calca",
                "Calca Pantalona",
                "pantalona",
                "relaxed",
                "plano",
                "Calca pantalona social ampla de alfaiataria.",
            )
        )

        profile, ranked = rank_variations("macacão folgado tipo alfaiataria", variations, limit=20)
        selected = select_representative_recommendations(profile, ranked, limit=3)

        self.assertIn("tronco_corpo_inteiro", {item.papel_referencia for item in selected})
        self.assertIn("perna_gancho", {item.papel_referencia for item in selected})


if __name__ == "__main__":
    unittest.main()
