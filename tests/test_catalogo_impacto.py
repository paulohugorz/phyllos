"""Testes do serviço de catálogo de fatores de impacto."""

import pytest
from app.services.catalogo_impacto import (
    CatalogoImpactoError,
    calcular_blend,
    listar_fibras,
    obter_fibra,
    _MJ_TO_KWH,
)


def test_listar_fibras_retorna_10():
    assert len(listar_fibras()) == 10


def test_listar_fibras_tem_campos_obrigatorios():
    for f in listar_fibras():
        assert f.fibra_id
        assert f.co2eq_kg_por_kg > 0
        assert f.agua_l_por_kg > 0
        assert f.energia_mj_por_kg > 0


def test_obter_fibra_conhecida():
    f = obter_fibra("algodao_convencional")
    assert f.nome_pt == "Algodão Convencional"
    assert f.co2eq_kg_por_kg == 5.9
    assert f.agua_l_por_kg == 10000
    assert f.energia_mj_por_kg == 55


def test_conversao_energia_kwh():
    f = obter_fibra("algodao_convencional")
    assert abs(f.energia_kwh_por_kg - 55 * _MJ_TO_KWH) < 0.001


def test_obter_fibra_inexistente():
    with pytest.raises(CatalogoImpactoError, match="não encontrada"):
        obter_fibra("fibra_que_nao_existe")


def test_blend_puro_retorna_proprios_fatores():
    blend = calcular_blend([{"fibra_id": "linho", "percentual": 100}])
    f = obter_fibra("linho")
    assert blend.co2eq_kg_por_kg == f.co2eq_kg_por_kg
    assert blend.agua_l_por_kg == f.agua_l_por_kg


def test_blend_95_5_algodao_elastano():
    blend = calcular_blend([
        {"fibra_id": "algodao_convencional", "percentual": 95},
        {"fibra_id": "elastano_spandex",     "percentual": 5},
    ])
    esperado_co2 = round(5.9 * 0.95 + 26.0 * 0.05, 6)
    assert abs(blend.co2eq_kg_por_kg - esperado_co2) < 0.001
    assert blend.confianca == "media"
    assert blend.aviso is not None


def test_blend_soma_diferente_de_100_falha():
    with pytest.raises(CatalogoImpactoError, match="Soma"):
        calcular_blend([
            {"fibra_id": "algodao_convencional", "percentual": 60},
            {"fibra_id": "poliester_virgem",     "percentual": 30},
        ])


def test_blend_vazio_falha():
    with pytest.raises(CatalogoImpactoError):
        calcular_blend([])


def test_blend_fibra_inexistente_falha():
    with pytest.raises(CatalogoImpactoError):
        calcular_blend([{"fibra_id": "fibra_x", "percentual": 100}])


def test_blend_energia_kwh_consistente():
    blend = calcular_blend([{"fibra_id": "poliester_virgem", "percentual": 100}])
    assert abs(blend.energia_kwh_por_kg - blend.energia_mj_por_kg * _MJ_TO_KWH) < 0.001


def test_blend_tres_fibras():
    blend = calcular_blend([
        {"fibra_id": "algodao_organico",  "percentual": 70},
        {"fibra_id": "poliester_reciclado", "percentual": 25},
        {"fibra_id": "elastano_spandex",  "percentual": 5},
    ])
    esperado = round(3.8 * 0.70 + 3.8 * 0.25 + 26.0 * 0.05, 6)
    assert abs(blend.co2eq_kg_por_kg - esperado) < 0.001
