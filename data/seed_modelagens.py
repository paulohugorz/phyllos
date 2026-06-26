"""Seed do Banco de Modelagens — fonte: Marlene Mukai, 3ª ed. 2015.

Popula:
  - moldes_base          (46 padrões de corte)
  - moldes_partes        (partes principais de cada molde)
  - moldes_derivacoes    (relações de derivação base → variação)
  - tabela_medidas_padrao (tabelas feminina plano 36-62 + malha média/alta)
  - reducao_malha        (percentuais de redução por elasticidade)
  - tecidos_indicados_molde (sugestões de tecido por categoria, p.8)
  - folgas_vestibilidade  (folgas por grau de ajuste)

Uso:
  cd /caminho/do/repo
  python data/seed_modelagens.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal, engine, Base
from app.models.models import (
    MoldeBase,
    MoldeParte,
    MoldeDerivacao,
    TabelaMedidasPadrao,
    ReducaoMalha,
    TecidoIndicadoMolde,
    FolgaVestibilidade,
)

Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# Catálogo de moldes base (Mukai 2015)
# ---------------------------------------------------------------------------

MOLDES_BASE = [
    # SAIAS (p.28-34)
    dict(codigo="base-saia-reta",           nome="Saia Reta",                      categoria="saia",    subcategoria="reta",         pagina_fonte=28, tipo_tecido="plano",  descricao="Molde básico de saia reta com cós. Base para variações de saia."),
    dict(codigo="base-saia-lapis",          nome="Saia Lápis",                     categoria="saia",    subcategoria="lapis",        pagina_fonte=29, tipo_tecido="plano",  descricao="Saia ajustada ao corpo, mais estreita no joelho."),
    dict(codigo="base-saia-gode",           nome="Saia Godê",                      categoria="saia",    subcategoria="gode",         pagina_fonte=30, tipo_tecido="plano",  descricao="Saia com corte em cunha que abre em godê. Requer tabela de raio (p.21)."),
    dict(codigo="base-saia-evase-classica", nome="Saia Evasê Clássica",            categoria="saia",    subcategoria="evase",        pagina_fonte=31, tipo_tecido="plano",  descricao="Saia com abertura gradual abaixo do quadril."),
    dict(codigo="base-saia-longa-babados",  nome="Saia Longa com Babados",         categoria="saia",    subcategoria="longa_babados", pagina_fonte=32, tipo_tecido="plano",  descricao="Saia longa com acabamento em babados."),
    dict(codigo="base-saia-pregueada",      nome="Saia Pregueada",                 categoria="saia",    subcategoria="pregueada",    pagina_fonte=33, tipo_tecido="plano",  descricao="Saia com pregas distribuídas a partir da cintura."),
    dict(codigo="base-saia-sino",           nome="Saia Sino",                      categoria="saia",    subcategoria="sino",         pagina_fonte=34, tipo_tecido="plano",  descricao="Saia com volume amplo em formato sino."),

    # BLUSAS E TOPS (p.36-44)
    dict(codigo="base-blusa-basica",        nome="Blusa Básica",                   categoria="blusa",   subcategoria="basica",       pagina_fonte=36, tipo_tecido="plano",  descricao="Molde base de blusa sem pences. Ponto de partida para a maioria das blusas."),
    dict(codigo="base-blusa-basica-pences", nome="Blusa Básica com Pences",        categoria="blusa",   subcategoria="basica_pences",pagina_fonte=37, tipo_tecido="plano",  descricao="Blusa básica com pences no busto para modelagem mais ajustada."),
    dict(codigo="base-regata",              nome="Regata",                         categoria="blusa",   subcategoria="regata",       pagina_fonte=38, tipo_tecido="plano",  descricao="Blusa sem manga com alças largas."),
    dict(codigo="base-regata-alcinhas",     nome="Regata com Alcinhas",            categoria="blusa",   subcategoria="regata_alcinhas", pagina_fonte=39, tipo_tecido="plano", descricao="Regata com alcinhas finas."),
    dict(codigo="base-blusa-transpassada",  nome="Blusa Transpassada",             categoria="blusa",   subcategoria="transpassada", pagina_fonte=40, tipo_tecido="plano",  descricao="Blusa com sobreposição de panos na frente. Sem botões."),
    dict(codigo="base-blusa-gola-degage",   nome="Blusa com Gola Degagê",          categoria="blusa",   subcategoria="gola_degage",  pagina_fonte=41, tipo_tecido="plano",  descricao="Blusa com gola degagê (ombros à mostra)."),
    dict(codigo="base-blusa-manga-japonesa",nome="Blusa Manga Japonesa",           categoria="blusa",   subcategoria="manga_japonesa", pagina_fonte=42, tipo_tecido="plano", descricao="Blusa com manga integrada ao corpo (kimono/dolman)."),
    dict(codigo="base-top-corpete",         nome="Top ou Corpete",                 categoria="blusa",   subcategoria="top",          pagina_fonte=43, tipo_tecido="plano",  descricao="Peça curta que cobre apenas o busto."),
    dict(codigo="base-blusa-cigana",        nome="Blusa Cigana",                   categoria="blusa",   subcategoria="cigana",       pagina_fonte=44, tipo_tecido="plano",  descricao="Blusa com elástico no busto e babados."),

    # MANGAS (p.47-54)
    dict(codigo="base-manga-curta",         nome="Manga Curta",                    categoria="manga",   subcategoria="curta",        pagina_fonte=47, tipo_tecido="ambos",  descricao="Manga montada clássica de comprimento curto."),
    dict(codigo="base-manga-longa",         nome="Manga Longa",                    categoria="manga",   subcategoria="longa",        pagina_fonte=48, tipo_tecido="ambos",  descricao="Manga montada clássica de comprimento longo."),
    dict(codigo="base-manga-raglan",        nome="Manga Raglan",                   categoria="manga",   subcategoria="raglan",       pagina_fonte=49, tipo_tecido="ambos",  descricao="Manga que se estende até o pescoço, sem costura no ombro."),
    dict(codigo="base-manga-baby-look",     nome="Manga Baby Look",                categoria="manga",   subcategoria="baby_look",    pagina_fonte=50, tipo_tecido="ambos",  descricao="Manga curta ajustada, característica de camisetas baby look."),
    dict(codigo="base-manga-petala",        nome="Manga Pétala ou Tulipa",         categoria="manga",   subcategoria="petala",       pagina_fonte=51, tipo_tecido="plano",  descricao="Manga decorativa com sobreposição em forma de pétala."),
    dict(codigo="base-manga-bufante",       nome="Manga Bufante ou Fofa",          categoria="manga",   subcategoria="bufante",      pagina_fonte=52, tipo_tecido="plano",  descricao="Manga franzida com volume pronunciado."),
    dict(codigo="base-manga-alfaiataria",   nome="Manga Alfaiataria para Blazer",  categoria="manga",   subcategoria="alfaiataria",  pagina_fonte=53, tipo_tecido="plano",  descricao="Manga com dois panos para blazer alfaiatado."),
    dict(codigo="base-manga-ordinaria",     nome="Manga Ordinária para Blazer",    categoria="manga",   subcategoria="ordinaria",    pagina_fonte=54, tipo_tecido="plano",  descricao="Manga com dois panos para blazer esportivo."),

    # CAMISAS FEMININAS (p.55-61)
    dict(codigo="base-camisa-fem-social",   nome="Camisa Feminina com Gola Colarinho", categoria="camisa", subcategoria="social",   pagina_fonte=55, tipo_tecido="plano",  descricao="Camisa feminina clássica com gola colarinho e abotoamento frontal."),
    dict(codigo="base-camisa-fem-pences",   nome="Camisa Feminina com Pences",     categoria="camisa",  subcategoria="pences",       pagina_fonte=58, tipo_tecido="plano",  descricao="Camisa feminina ajustada com pences no busto."),
    dict(codigo="base-camisa-fem-palas",    nome="Camisa Feminina com Palas",      categoria="camisa",  subcategoria="palas",        pagina_fonte=59, tipo_tecido="plano",  descricao="Camisa feminina com palas nas costas e/ou frente."),
    dict(codigo="base-gola-ordinaria",      nome="Gola Ordinária",                 categoria="componente", subcategoria="gola",     pagina_fonte=60, tipo_tecido="plano",  descricao="Gola colarinho básica, montada sobre pé-de-gola."),
    dict(codigo="base-camisa-fem-bata",     nome="Camisa Feminina Tipo Bata",      categoria="camisa",  subcategoria="bata",         pagina_fonte=61, tipo_tecido="plano",  descricao="Camisa feminina ampla com nervuras decorativas."),

    # CASACOS E EXTERIORES (p.62-67)
    dict(codigo="base-blazer-dois-botoes",  nome="Blazer de Dois Botões",          categoria="casaco",  subcategoria="blazer",       pagina_fonte=62, tipo_tecido="plano",  descricao="Blazer alfaiatado com dois botões e lapela."),
    dict(codigo="base-bolero",              nome="Bolero",                         categoria="casaco",  subcategoria="bolero",       pagina_fonte=63, tipo_tecido="plano",  descricao="Casaco curto que termina na cintura ou acima."),
    dict(codigo="base-sobretudo",           nome="Sobretudo",                      categoria="casaco",  subcategoria="sobretudo",    pagina_fonte=64, tipo_tecido="plano",  descricao="Casaco longo com botões frontais."),
    dict(codigo="base-sobretudo-transpassado", nome="Sobretudo Transpassado",      categoria="casaco",  subcategoria="sobretudo_transpassado", pagina_fonte=66, tipo_tecido="plano", descricao="Sobretudo com sobreposição dupla na frente."),

    # VESTIDOS (p.68-86)
    dict(codigo="base-vestido-basico",        nome="Vestido Básico",               categoria="vestido", subcategoria="basico",       pagina_fonte=68, tipo_tecido="plano",  descricao="Molde base de vestido sem pences. União de blusa básica e saia reta."),
    dict(codigo="base-vestido-tubo-pences",   nome="Vestido Tubo com Pences",      categoria="vestido", subcategoria="tubo_pences",  pagina_fonte=70, tipo_tecido="plano",  descricao="Vestido justo com pences no busto e/ou cintura."),
    dict(codigo="base-vestido-tubo-recortes", nome="Vestido Tubo com Recortes",    categoria="vestido", subcategoria="tubo_recortes",pagina_fonte=72, tipo_tecido="plano",  descricao="Vestido justo com recortes estruturais no lugar de pences."),
    dict(codigo="base-vestido-evase-recortes",nome="Vestido Evasê com Recortes",   categoria="vestido", subcategoria="evase_recortes",pagina_fonte=74,tipo_tecido="plano",  descricao="Vestido evasê com recortes princesa."),
    dict(codigo="base-vestido-envelope",      nome="Vestido Envelope",             categoria="vestido", subcategoria="envelope",     pagina_fonte=77, tipo_tecido="plano",  descricao="Vestido transpassado com sobreposição em V na frente."),
    dict(codigo="base-vestido-trapezio",      nome="Vestido Trapézio",             categoria="vestido", subcategoria="trapezio",     pagina_fonte=79, tipo_tecido="plano",  descricao="Vestido com silhueta trapezoidal, mais largo na barra."),
    dict(codigo="base-vestido-chemisier",     nome="Vestido Chemisier",            categoria="vestido", subcategoria="chemisier",    pagina_fonte=80, tipo_tecido="plano",  descricao="Vestido no estilo camisa com botões da gola à barra."),
    dict(codigo="base-vestido-evase-pregas",  nome="Vestido Evasê com Pregas",     categoria="vestido", subcategoria="evase_pregas", pagina_fonte=81, tipo_tecido="plano",  descricao="Vestido evasê com pregas distribuídas a partir da cintura."),
    dict(codigo="base-vestido-tomara",        nome="Vestido Tomara que Caia",      categoria="vestido", subcategoria="tomara",       pagina_fonte=82, tipo_tecido="plano",  descricao="Vestido sem alças com sustentação elástica no busto."),
    dict(codigo="base-vestido-drapeado",      nome="Vestido Drapeado",             categoria="vestido", subcategoria="drapeado",     pagina_fonte=83, tipo_tecido="plano",  descricao="Vestido com drapeamento lateral ou frontal."),
    dict(codigo="base-vestido-frente-unica",  nome="Vestido Frente Única",         categoria="vestido", subcategoria="frente_unica", pagina_fonte=85, tipo_tecido="plano",  descricao="Vestido com recorte assimétrico em frente única."),

    # CALÇAS (p.94-103)
    dict(codigo="base-calca-comprida",       nome="Calça Comprida Básica",        categoria="calca",   subcategoria="basica",       pagina_fonte=94, tipo_tecido="plano",  descricao="Molde base de calça feminina comprida. Base para todas as variações."),
    dict(codigo="base-calca-pregas",         nome="Calça com Pregas",             categoria="calca",   subcategoria="pregas",       pagina_fonte=96, tipo_tecido="plano",  descricao="Calça com pregas na frente, mais volume no gancho."),
    dict(codigo="base-calca-pantalona",      nome="Calça Pantalona",              categoria="calca",   subcategoria="pantalona",    pagina_fonte=97, tipo_tecido="plano",  descricao="Calça larga com perna ampla do quadril à barra."),
    dict(codigo="base-calca-bolsos",         nome="Calça com Bolsos",             categoria="calca",   subcategoria="bolsos",       pagina_fonte=98, tipo_tecido="plano",  descricao="Calça básica com bolsos laterais e/ou traseiros."),
    dict(codigo="base-calca-flare",          nome="Calça Flare",                  categoria="calca",   subcategoria="flare",        pagina_fonte=100, tipo_tecido="plano", descricao="Calça ajustada até o joelho, com abertura a partir daí."),
    dict(codigo="base-calca-cos-baixo",      nome="Calça de Cós Baixo e Médio",  categoria="calca",   subcategoria="cos_baixo",    pagina_fonte=101, tipo_tecido="plano", descricao="Variações de altura do cós: baixo (hip), médio e alto."),
    dict(codigo="base-calca-pijama",         nome="Calça Pijama",                 categoria="calca",   subcategoria="pijama",       pagina_fonte=102, tipo_tecido="plano", descricao="Calça larga com cós elástico, sem gancho estruturado."),

    # MASCULINO (p.105-115)
    dict(codigo="base-camisa-masc-social",   nome="Camisa Masculina Social",      categoria="camisa",  subcategoria="social_masc",  pagina_fonte=106, tipo_tecido="plano", genero="masculino", descricao="Camisa masculina com gola colarinho, punho e carcela."),
    dict(codigo="base-calca-masc-social",    nome="Calça Social Masculina com Pregas", categoria="calca", subcategoria="social_masc_pregas", pagina_fonte=110, tipo_tecido="plano", genero="masculino", descricao="Calça social masculina com pregas na frente."),
    dict(codigo="base-blazer-masc",          nome="Blazer Masculino",             categoria="casaco",  subcategoria="blazer_masc",  pagina_fonte=114, tipo_tecido="plano", genero="masculino", descricao="Blazer masculino estruturado."),

    # INFANTIL (p.116-128)
    dict(codigo="base-vestido-inf-evase",    nome="Vestido Infantil Evasê",       categoria="vestido", subcategoria="inf_evase",    pagina_fonte=117, tipo_tecido="plano", genero="infantil", descricao="Vestido infantil com silhueta evasê."),
    dict(codigo="base-vestido-inf-princesa", nome="Vestido Infantil Princesa",    categoria="vestido", subcategoria="inf_princesa", pagina_fonte=121, tipo_tecido="plano", genero="infantil", descricao="Vestido infantil com recorte princesa (saia godê)."),
    dict(codigo="base-bermuda-inf-menino",   nome="Bermuda Infantil para Menino", categoria="calca",   subcategoria="bermuda_inf",  pagina_fonte=125, tipo_tecido="plano", genero="infantil", descricao="Bermuda básica infantil masculina."),
]

# Partes de cada molde (nome, quantidade de corte, observações)
PARTES_POR_MOLDE = {
    "base-saia-reta":           [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro"), ("cos", 1, None)],
    "base-saia-lapis":          [("frente", 1, None), ("costas", 1, None), ("cos", 1, None)],
    "base-saia-gode":           [("cunha", 6, "número de cunhas pode variar"), ("cos", 1, None)],
    "base-saia-evase-classica": [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro"), ("cos", 1, None)],
    "base-saia-longa-babados":  [("frente", 1, None), ("costas", 1, None), ("babado", 1, "tirar em tira"), ("cos", 1, None)],
    "base-saia-pregueada":      [("frente", 1, "com marcação de pregas"), ("costas", 1, None), ("cos", 1, None)],
    "base-saia-sino":           [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro"), ("cos", 1, None)],

    "base-blusa-basica":        [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro")],
    "base-blusa-basica-pences": [("frente", 1, "com marcação de pences"), ("costas", 1, None)],
    "base-regata":              [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro")],
    "base-regata-alcinhas":     [("frente", 1, None), ("costas", 1, None), ("alcinha", 2, None)],
    "base-blusa-transpassada":  [("frente_direita", 1, None), ("frente_esquerda", 1, None), ("costas", 1, "cortar no dobro")],
    "base-blusa-gola-degage":   [("frente", 1, None), ("costas", 1, None)],
    "base-blusa-manga-japonesa":[("frente_manga", 1, "cortar no dobro — manga integrada"), ("costas_manga", 1, "cortar no dobro")],
    "base-top-corpete":         [("frente", 1, None), ("costas", 1, None)],
    "base-blusa-cigana":        [("corpo", 1, "cortar em tira circular"), ("babado", 1, None)],

    "base-manga-curta":         [("manga", 1, "cortar no dobro")],
    "base-manga-longa":         [("manga", 1, "cortar no dobro")],
    "base-manga-raglan":        [("manga_frente", 1, None), ("manga_costas", 1, None)],
    "base-manga-baby-look":     [("manga", 1, "cortar no dobro")],
    "base-manga-petala":        [("petala_superior", 1, None), ("petala_inferior", 1, None)],
    "base-manga-bufante":       [("manga", 1, "cortar mais larga para franzido")],
    "base-manga-alfaiataria":   [("manga_superior", 1, None), ("manga_inferior", 1, None)],
    "base-manga-ordinaria":     [("manga_superior", 1, None), ("manga_inferior", 1, None)],

    "base-camisa-fem-social":   [("frente", 2, "frente esq. e dir."), ("costas", 1, "cortar no dobro"), ("manga", 2, None), ("gola", 1, None), ("pe_de_gola", 1, None), ("carcela", 2, None), ("punho", 2, None)],
    "base-camisa-fem-pences":   [("frente", 2, "com pences"), ("costas", 1, None), ("manga", 2, None), ("punho", 2, None)],
    "base-camisa-fem-palas":    [("frente", 1, None), ("costas", 1, None), ("pala_costas", 1, None), ("manga", 2, None)],
    "base-gola-ordinaria":      [("gola", 2, "superior e inferior"), ("pe_de_gola", 1, None)],
    "base-camisa-fem-bata":     [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro"), ("nervuras", 4, "tiras para aplicar")],

    "base-blazer-dois-botoes":  [("frente", 2, "esq. e dir."), ("costas", 1, "cortar no dobro"), ("lapela", 2, None), ("manga_superior", 2, None), ("manga_inferior", 2, None), ("bolso", 2, None)],
    "base-bolero":              [("frente", 2, None), ("costas", 1, "cortar no dobro"), ("manga", 2, None)],
    "base-sobretudo":           [("frente", 2, None), ("costas", 1, "cortar no dobro"), ("manga_superior", 2, None), ("manga_inferior", 2, None)],
    "base-sobretudo-transpassado": [("frente", 2, "sobrepõe mais"), ("costas", 1, None), ("manga_superior", 2, None), ("manga_inferior", 2, None)],

    "base-vestido-basico":      [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro")],
    "base-vestido-tubo-pences": [("frente", 1, "com pences busto e cintura"), ("costas", 1, "com pence cintura")],
    "base-vestido-tubo-recortes": [("frente_centro", 1, None), ("frente_lateral", 2, None), ("costas_centro", 1, None), ("costas_lateral", 2, None)],
    "base-vestido-evase-recortes": [("frente_centro", 1, None), ("frente_lateral", 2, None), ("costas", 1, None)],
    "base-vestido-envelope":    [("frente_direita", 1, None), ("frente_esquerda", 1, None), ("costas", 1, "cortar no dobro")],
    "base-vestido-trapezio":    [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro")],
    "base-vestido-chemisier":   [("frente", 2, None), ("costas", 1, "cortar no dobro"), ("manga", 2, None), ("gola", 1, None)],
    "base-vestido-evase-pregas":[("frente", 1, "com marcação de pregas"), ("costas", 1, None)],
    "base-vestido-tomara":      [("frente", 1, None), ("costas", 1, None)],
    "base-vestido-drapeado":    [("frente", 1, "com excesso para drapeamento"), ("costas", 1, None)],
    "base-vestido-frente-unica":[("frente", 1, "assimétrica"), ("costas", 1, None)],

    "base-calca-comprida":      [("frente", 2, "2 peças simétricas"), ("costas", 2, None), ("cos", 1, None)],
    "base-calca-pregas":        [("frente", 2, "com marcação de pregas"), ("costas", 2, None), ("cos", 1, None)],
    "base-calca-pantalona":     [("frente", 2, "perna muito larga"), ("costas", 2, None), ("cos", 1, None)],
    "base-calca-bolsos":        [("frente", 2, None), ("costas", 2, None), ("bolso_lateral", 4, None), ("cos", 1, None)],
    "base-calca-flare":         [("frente", 2, "abertura a partir do joelho"), ("costas", 2, None), ("cos", 1, None)],
    "base-calca-cos-baixo":     [("frente", 2, None), ("costas", 2, None), ("cos", 1, "altura variável")],
    "base-calca-pijama":        [("frente", 2, "cortar no dobro"), ("costas", 2, None)],

    "base-camisa-masc-social":  [("frente", 2, None), ("costas", 1, "cortar no dobro"), ("pala_costas", 1, None), ("manga", 2, None), ("gola", 2, None), ("pe_de_gola", 1, None), ("punho", 2, None), ("carcela", 2, None)],
    "base-calca-masc-social":   [("frente", 2, "com pregas"), ("costas", 2, None), ("cos", 1, None)],
    "base-blazer-masc":         [("frente", 2, None), ("costas", 1, "cortar no dobro"), ("lapela", 2, None), ("manga_superior", 2, None), ("manga_inferior", 2, None)],

    "base-vestido-inf-evase":   [("frente", 1, "cortar no dobro"), ("costas", 1, "cortar no dobro")],
    "base-vestido-inf-princesa":[("frente_corpo", 1, None), ("costas_corpo", 1, None), ("saia_gode", 4, "cunhas")],
    "base-bermuda-inf-menino":  [("frente", 2, None), ("costas", 2, None), ("cos", 1, None)],
}

# Derivações (molde_origem → molde_derivado, tipo, descrição)
DERIVACOES = [
    ("base-blusa-basica",       "base-blusa-basica-pences",   "pence",       "Adicionar pences no busto para ajustar o volume"),
    ("base-blusa-basica",       "base-regata",                "encurtamento","Remover manga e reduzir alça para regata"),
    ("base-blusa-basica",       "base-regata-alcinhas",       "encurtamento","Versão com alcinhas finas no lugar de alças largas"),
    ("base-blusa-basica",       "base-top-corpete",           "encurtamento","Encurtar para terminar sob o busto"),
    ("base-blusa-basica",       "base-blusa-transpassada",    "sobreposicao","Adicionar sobreposição com amarração lateral"),
    ("base-blusa-basica",       "base-blusa-gola-degage",     "recorte",     "Baixar ombros e ampliar decote"),
    ("base-blusa-basica",       "base-blusa-manga-japonesa",  "integracao",  "Integrar manga ao corpo sem costura na cava"),
    ("base-blusa-basica-pences","base-blusa-cigana",          "franzido",    "Franzir a parte inferior e adicionar babado"),
    ("base-saia-reta",          "base-saia-lapis",            "ajustamento", "Apertar perna da calça abaixo do quadril"),
    ("base-saia-reta",          "base-saia-evase-classica",   "alargamento", "Abrir a partir do quadril progressivamente"),
    ("base-saia-reta",          "base-saia-pregueada",        "franzido",    "Adicionar pregas distribuídas na cintura"),
    ("base-saia-reta",          "base-saia-longa-babados",    "alargamento", "Alongar e adicionar babado na barra"),
    ("base-blusa-basica",       "base-vestido-basico",        "integracao",  "Unir blusa básica à saia reta para vestido"),
    ("base-vestido-basico",     "base-vestido-tubo-pences",   "pence",       "Adicionar pences para ajustar ao corpo"),
    ("base-vestido-tubo-pences","base-vestido-tubo-recortes", "recorte",     "Substituir pences por recortes princesa"),
    ("base-vestido-basico",     "base-vestido-trapezio",      "alargamento", "Abrir progressivamente da cintura à barra"),
    ("base-vestido-basico",     "base-vestido-evase-pregas",  "franzido",    "Adicionar pregas na cintura para volume"),
    ("base-vestido-basico",     "base-vestido-envelope",      "sobreposicao","Frente em sobreposição transpassada"),
    ("base-vestido-basico",     "base-vestido-chemisier",     "sobreposicao","Abotoamento frontal estilo camisa"),
    ("base-calca-comprida",     "base-calca-pregas",          "franzido",    "Adicionar pregas frontais"),
    ("base-calca-comprida",     "base-calca-pantalona",       "alargamento", "Alargar toda a perna"),
    ("base-calca-comprida",     "base-calca-flare",           "alargamento", "Alargar apenas abaixo do joelho"),
    ("base-calca-comprida",     "base-calca-pijama",          "alargamento", "Alargar e substituir cós por elástico"),
    ("base-blazer-dois-botoes", "base-bolero",                "encurtamento","Encurtar para terminar na cintura"),
    ("base-blazer-dois-botoes", "base-sobretudo",             "alargamento", "Alongar até o joelho ou abaixo"),
    ("base-sobretudo",          "base-sobretudo-transpassado","sobreposicao","Adicionar sobreposição dupla na frente"),
    ("base-camisa-fem-social",  "base-camisa-fem-pences",     "pence",       "Adicionar pences para caimento mais ajustado"),
    ("base-camisa-fem-social",  "base-camisa-fem-palas",      "recorte",     "Incluir palas nas costas e/ou frente"),
    ("base-camisa-fem-social",  "base-camisa-fem-bata",       "alargamento", "Ampliar e adicionar nervuras decorativas"),
    ("base-manga-longa",        "base-manga-bufante",         "franzido",    "Franzir topo e punho para volume"),
    ("base-manga-curta",        "base-manga-baby-look",       "ajustamento", "Reduzir largura para peça ajustada"),
    ("base-manga-longa",        "base-manga-alfaiataria",     "recorte",     "Dividir em pano superior e inferior"),
]

# ---------------------------------------------------------------------------
# Tabela de medidas padrão feminina — tecido PLANO (tamanhos 36 a 62)
# Fonte: Mukai 2015, p.11
# ---------------------------------------------------------------------------

TAMANHOS_PLANO = ["36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56", "58", "60", "62"]

MEDIDAS_FEM_PLANO = {
    "busto":              [82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126, 130, 134],
    "cintura":            [66, 70, 74, 78, 82,  86,  90,  94,  98, 102, 106, 110, 114, 118],
    "quadril":            [88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140],
    "altura_corpo":       [39, 40, 41, 42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52],
    "largura_braco":      [25, 26, 27, 28,  30,  32,  34,  36,  38,  39,  40,  41,  42,  43],
    "costas":             [34, 35, 36, 37,  38,  39,  39,  40,  40,  41,  42,  43,  44,  45],
    "ombro":              [11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5],
    "altura_cava":        [15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5],
    "altura_busto":       [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
    "separacao_busto":    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "comp_manga_comprida":[55, 56, 57, 58, 58.5, 59, 59.5, 60, 60.5, 61, 61.5, 62, 62.5, 63],
    "comp_manga_curta":   [16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5],
    "punho_camisa":       [14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5],
    "punho_blazer":       [25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30, 30.5, 31, 31.5],
    "altura_quadril":     [18, 19, 19, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22],
    "altura_gancho":      [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
    "comp_joelho":        [52, 53, 54, 55, 55, 56, 56, 57, 57, 58, 59, 60, 61, 62],
    "comp_calca":         [92, 93, 94, 95, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118],
    "largura_joelho":     [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    "largura_tornozelo":  [21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5],
}

# Tabela feminina malha MÉDIA elasticidade — redução 20% (tamanhos PP-EGG = 36-46)
# Fonte: Mukai 2015, p.12
TAMANHOS_MALHA = ["36", "38", "40", "42", "44", "46"]

MEDIDAS_FEM_MALHA_MEDIA = {
    "busto":              [66, 72, 78, 84, 90, 96],
    "cintura":            [60, 66, 72, 78, 84, 90],
    "quadril":            [70, 76, 82, 88, 94, 100],
    "ombro":              [8, 8.5, 9, 9.5, 10, 10.5],
    "costas":             [31, 33, 35, 37, 39, 41],
    "separacao_busto":    [14, 15.5, 17, 18.5, 20, 21.5],
    "altura_corpo":       [40, 42, 44, 46, 48, 50],
    "altura_cava":        [19, 19, 20.5, 21.5, 22.5, 23.5],
    "largura_braco":      [23, 25, 27, 29, 31, 33],
    "altura_busto":       [24, 24.5, 27, 28.5, 30.5, 31.5],
    "comp_manga_comprida":[54, 56, 58, 60, 62, 64],
    "punho_camisa":       [12.5, 13.5, 14, 15, 15.5, 16],
    "comp_manga_curta":   [16, 17, 18, 18.5, 19, 20],
    "altura_quadril":     [16.5, 17.5, 18.5, 19.5, 20.5, 21.5],
    "altura_gancho":      [23, 24, 25, 26, 27, 28],
    "comp_joelho":        [52, 54, 56, 58, 60, 62],
    "largura_joelho":     [28.5, 30, 31.5, 33, 34.5, 35],
    "largura_tornozelo":  [16.5, 18, 19, 20.5, 21.5, 22],
    "comp_calca":         [88, 91, 94, 97, 100, 103],
}

# Tabela feminina malha ALTA elasticidade — redução 30% (tamanhos PP-EGG = 36-46)
# Fonte: Mukai 2015, p.13
MEDIDAS_FEM_MALHA_ALTA = {
    "busto":              [58, 64, 70, 76, 82, 88],
    "cintura":            [46, 52, 58, 64, 70, 76],
    "quadril":            [62, 68, 74, 80, 86, 92],
    "ombro":              [7, 7.5, 8, 8.5, 9, 9.5],
    "costas":             [28, 30, 32, 34, 36, 38],
    "separacao_busto":    [12.5, 14, 15.5, 17, 19.5, 21],
    "altura_corpo":       [39, 41, 43, 45, 46, 48],
    "altura_cava":        [18, 18, 19.5, 20.5, 21.5, 22.5],
    "largura_braco":      [22, 24, 26, 28, 30, 32],
    "altura_busto":       [23.5, 24.5, 26.5, 28, 29.5, 31],
    "comp_manga_comprida":[53, 55, 57, 59, 61, 63],
    "punho_camisa":       [11.5, 12.5, 13, 14, 14.5, 15.5],
    "comp_manga_curta":   [15.5, 16, 16.5, 17, 17.5, 18],
    "altura_quadril":     [16, 17, 18, 19, 20, 21],
    "altura_gancho":      [22, 23, 24, 25, 26, 27],
    "comp_joelho":        [50.5, 52.5, 54.5, 56.5, 58.5, 60.5],
    "largura_joelho":     [24.5, 26, 27.5, 29, 30.5, 32],
    "largura_tornozelo":  [15.7, 17, 17.5, 19, 20.5, 22],
    "comp_calca":         [86, 89, 92, 95, 98, 101],
}

# ---------------------------------------------------------------------------
# Redução de malha por elasticidade (Mukai 2015, p.14)
# reducao_pct: % sobre a medida corporal  |  reducao_cm: valor fixo em cm
# ---------------------------------------------------------------------------

REDUCAO_MALHA = [
    # (elasticidade, ponto_medida, reducao_pct, reducao_cm, observacoes)
    ("baixa", "busto",               10.0, None, None),
    ("baixa", "cintura",             10.0, None, None),
    ("baixa", "quadril",             10.0, None, None),
    ("baixa", "largura_costas",       5.0, None, None),
    ("baixa", "separacao_busto",     10.0, None, None),
    ("baixa", "altura_blusa",        None, -1.0, None),
    ("baixa", "altura_cava",         None, -0.5, None),
    ("baixa", "largura_braco",       None, -1.0, None),
    ("baixa", "altura_busto",        None, -0.5, None),
    ("baixa", "comp_manga_comprida", None, -1.0, None),
    ("baixa", "punho",               10.0, None, None),
    ("baixa", "comp_manga_curta",    None, -0.5, None),
    ("baixa", "altura_quadril",      None, -0.5, None),
    ("baixa", "altura_gancho",       None, -1.0, None),
    ("baixa", "comp_joelho",         None, -1.0, None),
    ("baixa", "largura_joelho",      10.0, None, None),
    ("baixa", "largura_tornozelo",   10.0, None, None),
    ("baixa", "comp_calca",          None, -2.0, None),

    ("media", "busto",               20.0, None, None),
    ("media", "cintura",             20.0, None, None),
    ("media", "quadril",             20.0, None, None),
    ("media", "largura_costas",      15.0, None, None),
    ("media", "separacao_busto",     20.0, None, None),
    ("media", "altura_blusa",        None, -2.0, None),
    ("media", "altura_cava",         None, -1.0, None),
    ("media", "largura_braco",       None, -2.0, None),
    ("media", "altura_busto",        None, -1.0, None),
    ("media", "comp_manga_comprida", None, -2.0, None),
    ("media", "punho",               20.0, None, None),
    ("media", "comp_manga_curta",    None, -1.0, None),
    ("media", "altura_quadril",      None, -1.0, None),
    ("media", "altura_gancho",       None, -2.0, None),
    ("media", "comp_joelho",         None, -2.0, None),
    ("media", "largura_joelho",      20.0, None, None),
    ("media", "largura_tornozelo",   20.0, None, None),
    ("media", "comp_calca",          None, -4.0, None),

    ("alta",  "busto",               30.0, None, None),
    ("alta",  "cintura",             20.0, None, "cintura reduz apenas 20% mesmo em alta elasticidade"),
    ("alta",  "quadril",             30.0, None, None),
    ("alta",  "largura_costas",      25.0, None, None),
    ("alta",  "separacao_busto",     30.0, None, None),
    ("alta",  "altura_blusa",        None, -3.5, None),
    ("alta",  "altura_cava",         None, -1.5, None),
    ("alta",  "largura_braco",       None, -3.0, None),
    ("alta",  "altura_busto",        None, -1.5, None),
    ("alta",  "comp_manga_comprida", None, -3.0, None),
    ("alta",  "punho",               30.0, None, None),
    ("alta",  "comp_manga_curta",    None, -1.5, None),
    ("alta",  "altura_quadril",      None, -1.5, None),
    ("alta",  "altura_gancho",       None, -3.0, None),
    ("alta",  "comp_joelho",         None, -3.5, None),
    ("alta",  "largura_joelho",      30.0, None, None),
    ("alta",  "largura_tornozelo",   30.0, None, None),
    ("alta",  "comp_calca",          None, -6.0, None),
]

# ---------------------------------------------------------------------------
# Tecidos indicados por categoria (Mukai 2015, p.8)
# (categoria, nome_tecido, adequacao, observacoes)
# ---------------------------------------------------------------------------

TECIDOS_INDICADOS = [
    # Blusas leves
    ("blusa", "mousseline",    "ideal",      "Leve, fluido, semi-transparente"),
    ("blusa", "organdi",       "ideal",      "Leve, levemente estruturado"),
    ("blusa", "chiffon",       "ideal",      "Levíssimo, transparente"),
    ("blusa", "seda",          "ideal",      "Caimento excelente"),
    ("blusa", "crepe de seda", "ideal",      None),
    ("blusa", "satim",         "ideal",      None),
    ("blusa", "cambraia",      "ideal",      None),
    ("blusa", "viscose",       "ideal",      None),
    ("blusa", "cetim",         "ideal",      None),

    # Blazer
    ("casaco", "gabardine",    "ideal",      None),
    ("casaco", "lã inglesa",   "ideal",      None),
    ("casaco", "microfibra",   "ideal",      None),
    ("casaco", "Oxford",       "ideal",      None),
    ("casaco", "linho",        "ideal",      None),
    ("casaco", "brim",         "adequado",   None),
    ("casaco", "sarja",        "adequado",   None),
    ("casaco", "poliéster",    "adequado",   None),
    ("casaco", "tweed",        "ideal",      None),
    ("casaco", "veludo",       "ideal",      None),
    ("casaco", "jacquard",     "ideal",      None),
    ("casaco", "piquet",       "adequado",   None),

    # Calça e saia social
    ("calca",  "gabardine",    "ideal",      None),
    ("calca",  "lã inglesa",   "ideal",      None),
    ("calca",  "microfibra",   "ideal",      None),
    ("calca",  "tafetá",       "adequado",   None),
    ("calca",  "jacquard",     "adequado",   None),
    ("calca",  "Oxford",       "adequado",   None),
    ("calca",  "linho",        "ideal",      None),
    ("saia",   "gabardine",    "ideal",      None),
    ("saia",   "lã inglesa",   "ideal",      None),
    ("saia",   "microfibra",   "ideal",      None),
    ("saia",   "linho",        "ideal",      None),

    # Calça jeans
    ("calca",  "brim",         "ideal",      "Calça jeans"),
    ("calca",  "denim",        "ideal",      "Calça jeans"),
    ("calca",  "sarja",        "ideal",      "Calça jeans"),

    # Camisas
    ("camisa", "tricoline de algodão", "ideal", None),
    ("camisa", "algodão egípcio",      "ideal", None),
    ("camisa", "cambraia",             "ideal", None),
    ("camisa", "viscose",              "ideal", None),
    ("camisa", "popeline",             "ideal", None),
    ("camisa", "cetim",                "adequado", None),
    ("camisa", "seda",                 "ideal", None),

    # Vestidos tubinho
    ("vestido", "linho",       "ideal",      "Vestido tubinho"),
    ("vestido", "piquet",      "ideal",      "Vestido tubinho"),
    ("vestido", "neoprene",    "ideal",      "Vestido tubinho"),
    ("vestido", "gabardine",   "ideal",      "Vestido tubinho"),
    ("vestido", "crepe",       "ideal",      None),
    ("vestido", "jacquard",    "adequado",   None),
    ("vestido", "sarja",       "adequado",   None),
    ("vestido", "satim",       "ideal",      None),

    # Vestidos fluidos
    ("vestido", "crepe de seda","ideal",     "Vestido fluido"),
    ("vestido", "mousseline",  "ideal",      "Vestido fluido"),
    ("vestido", "chiffon",     "ideal",      "Vestido fluido"),
    ("vestido", "jérsei",      "ideal",      "Vestido fluido"),

    # Vestido de festa
    ("vestido", "crepe de seda","ideal",     "Vestido festa"),
    ("vestido", "shantung",    "ideal",      "Vestido festa"),
    ("vestido", "organza de seda", "ideal",  "Vestido festa"),
    ("vestido", "tule bordado","ideal",      "Vestido festa"),
    ("vestido", "veludo",      "ideal",      "Vestido festa"),
    ("vestido", "renda francesa","ideal",    "Forrar com acetato"),
    ("vestido", "brocado",     "ideal",      "Vestido festa"),
]

# ---------------------------------------------------------------------------
# Folgas de vestibilidade recomendadas
# Baseado no método Mukai: medida corporal / 4 + folga por quarto de molde
# ---------------------------------------------------------------------------

FOLGAS = [
    # (grau_ajuste, categoria_peca, ponto_medida, folga_total_cm, observacoes)
    ("compression", None,     "busto",   -4.0, "Para malha de alta elasticidade com redução adicional"),
    ("compression", None,     "cintura", -2.0, None),
    ("compression", None,     "quadril", -4.0, None),
    ("fitted",      "blusa",  "busto",    2.0, "Justo mas não comprime; método Mukai base"),
    ("fitted",      "blusa",  "cintura",  1.0, None),
    ("fitted",      "blusa",  "quadril",  2.0, None),
    ("fitted",      "calca",  "quadril",  2.0, None),
    ("fitted",      "calca",  "cintura",  1.0, None),
    ("fitted",      "calca",  "gancho",   1.0, None),
    ("fitted",      "vestido","busto",    2.0, None),
    ("fitted",      "vestido","cintura",  1.0, None),
    ("fitted",      "vestido","quadril",  2.0, None),
    ("semi",        "blusa",  "busto",    4.0, "Padrão Mukai para tecido plano sem elasticidade"),
    ("semi",        "blusa",  "cintura",  2.0, None),
    ("semi",        "blusa",  "quadril",  4.0, None),
    ("semi",        "calca",  "quadril",  4.0, None),
    ("semi",        "calca",  "cintura",  2.0, None),
    ("semi",        "calca",  "gancho",   2.0, None),
    ("semi",        "vestido","busto",    4.0, None),
    ("semi",        "vestido","cintura",  2.0, None),
    ("semi",        "vestido","quadril",  4.0, None),
    ("semi",        "saia",   "cintura",  2.0, None),
    ("semi",        "saia",   "quadril",  4.0, None),
    ("relaxed",     "blusa",  "busto",    8.0, None),
    ("relaxed",     "blusa",  "cintura",  4.0, None),
    ("relaxed",     "blusa",  "quadril",  6.0, None),
    ("relaxed",     "calca",  "quadril",  8.0, None),
    ("relaxed",     "calca",  "cintura",  4.0, None),
    ("relaxed",     "saia",   "cintura",  4.0, None),
    ("relaxed",     "saia",   "quadril",  6.0, None),
    ("oversized",   "blusa",  "busto",   16.0, None),
    ("oversized",   "blusa",  "cintura",  8.0, None),
    ("oversized",   "blusa",  "quadril", 12.0, None),
    ("oversized",   "casaco", "busto",   12.0, "Casaco usa folga maior para vestir sobre outras peças"),
    ("oversized",   "casaco", "quadril", 10.0, None),
]


# ---------------------------------------------------------------------------
# Execução do seed
# ---------------------------------------------------------------------------

def seed():
    db = SessionLocal()
    try:
        # Verificar se já foi populado
        if db.query(MoldeBase).count() > 0:
            print("Banco de modelagens já populado. Pulando seed.")
            return

        print("Inserindo moldes base...")
        codigo_to_id = {}
        for m in MOLDES_BASE:
            obj = MoldeBase(**m)
            db.add(obj)
            db.flush()
            codigo_to_id[m["codigo"]] = obj.id

        print("Inserindo partes dos moldes...")
        for codigo, partes in PARTES_POR_MOLDE.items():
            molde_id = codigo_to_id.get(codigo)
            if not molde_id:
                continue
            for nome, qtd, obs in partes:
                db.add(MoldeParte(molde_base_id=molde_id, nome=nome, quantidade_corte=qtd, observacoes=obs))

        print("Inserindo derivações...")
        for origem, derivado, tipo, descr in DERIVACOES:
            origem_id = codigo_to_id.get(origem)
            derivado_id = codigo_to_id.get(derivado)
            if origem_id and derivado_id:
                db.add(MoldeDerivacao(
                    molde_origem_id=origem_id,
                    molde_derivado_id=derivado_id,
                    tipo_transformacao=tipo,
                    descricao=descr,
                ))

        print("Inserindo tabela de medidas — feminino / plano...")
        for ponto, valores in MEDIDAS_FEM_PLANO.items():
            for tamanho, valor in zip(TAMANHOS_PLANO, valores):
                db.add(TabelaMedidasPadrao(
                    genero="feminino", tipo_tecido="plano", elasticidade="plano",
                    tamanho=tamanho, ponto_medida=ponto, valor_cm=float(valor),
                ))

        print("Inserindo tabela de medidas — feminino / malha média (20%)...")
        for ponto, valores in MEDIDAS_FEM_MALHA_MEDIA.items():
            for tamanho, valor in zip(TAMANHOS_MALHA, valores):
                db.add(TabelaMedidasPadrao(
                    genero="feminino", tipo_tecido="malha", elasticidade="media",
                    tamanho=tamanho, ponto_medida=ponto, valor_cm=float(valor),
                ))

        print("Inserindo tabela de medidas — feminino / malha alta (30%)...")
        for ponto, valores in MEDIDAS_FEM_MALHA_ALTA.items():
            for tamanho, valor in zip(TAMANHOS_MALHA, valores):
                db.add(TabelaMedidasPadrao(
                    genero="feminino", tipo_tecido="malha", elasticidade="alta",
                    tamanho=tamanho, ponto_medida=ponto, valor_cm=float(valor),
                ))

        print("Inserindo redução de malha...")
        for elasticidade, ponto, pct, cm, obs in REDUCAO_MALHA:
            db.add(ReducaoMalha(
                elasticidade=elasticidade, ponto_medida=ponto,
                reducao_pct=pct, reducao_cm=cm, observacoes=obs,
            ))

        print("Inserindo tecidos indicados por categoria...")
        for categoria, nome, adequacao, obs in TECIDOS_INDICADOS:
            db.add(TecidoIndicadoMolde(
                molde_base_id=None,
                categoria_peca=categoria,
                nome_tecido=nome,
                adequacao=adequacao,
                observacoes=obs,
            ))

        print("Inserindo folgas de vestibilidade...")
        for grau, cat, ponto, folga, obs in FOLGAS:
            db.add(FolgaVestibilidade(
                grau_ajuste=grau, categoria_peca=cat, ponto_medida=ponto,
                folga_total_cm=folga, observacoes=obs,
            ))

        db.commit()
        print("\nSeed concluído com sucesso.")
        print(f"  Moldes base:           {db.query(MoldeBase).count()}")
        print(f"  Partes de molde:       {db.query(MoldeParte).count()}")
        print(f"  Derivações:            {db.query(MoldeDerivacao).count()}")
        print(f"  Medidas padrão:        {db.query(TabelaMedidasPadrao).count()} registros")
        print(f"  Redução de malha:      {db.query(ReducaoMalha).count()} registros")
        print(f"  Tecidos indicados:     {db.query(TecidoIndicadoMolde).count()} registros")
        print(f"  Folgas vestibilidade:  {db.query(FolgaVestibilidade).count()} registros")

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    seed()
