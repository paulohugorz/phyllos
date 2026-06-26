"""Gerador de Variações de Modelagem — 2000+ SKUs.

Popula `moldes_variacoes` com combinações de:
  (molde_base × tamanho × tipo_tecido × elasticidade × grau_ajuste)

Cada SKU tem todos os campos preenchidos:
  - variações de construção (comprimento, decote, manga, fechamento, cós)
  - medidas de molde pré-calculadas (corporal + folga)
  - descrição em linguagem natural + tags para matching semântico

Também adiciona medidas de masculino e infantil à tabela_medidas_padrao.

Uso:
  python data/gerar_variacoes.py
"""

import sys, os, json, math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import SessionLocal, engine, Base
from app.models.models import (
    MoldeBase, MoldeVariacao, TabelaMedidasPadrao,
)

Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# 1. Tabelas de medidas adicionais (masculino + infantil)
# ---------------------------------------------------------------------------

TAMANHOS_MASC = ["36","38","40","42","44","46","48","50","52","54"]
TAMANHOS_INF  = ["2","4","6","8","10","12","14","16"]   # anos

MEDIDAS_MASC_PLANO = {
    "busto":              [92, 96,100,104,108,112,116,120,124,128],
    "cintura":            [74, 78, 82, 86, 90, 94, 98,102,106,110],
    "quadril":            [90, 94, 98,102,106,110,114,118,122,126],
    "pescoco":            [38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
    "altura_corpo":       [43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
    "costas":             [36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
    "ombro":              [13,13.5,14,14.5,15,15.5,16,16.5,17,17.5],
    "altura_cava":        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "largura_braco":      [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    "comp_manga_comprida":[60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    "comp_manga_curta":   [22,22.5,23,23.5,24,24.5,25,25.5,26,26.5],
    "punho_camisa":       [20,20.5,21,21.5,22,22.5,23,23.5,24,24.5],
    "altura_gancho":      [26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
    "comp_calca":         [96, 98,100,102,104,106,108,110,112,114],
    "comp_joelho":        [55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
    "largura_joelho":     [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    "largura_tornozelo":  [22,22.5,23,23.5,24,24.5,25,25.5,26,26.5],
}

MEDIDAS_INF_PLANO = {
    "busto":              [52, 56, 60, 64, 68, 73, 79, 84],
    "cintura":            [50, 52, 54, 57, 60, 63, 66, 68],
    "quadril":            [56, 60, 65, 70, 75, 80, 87, 93],
    "ombro":              [ 7, 7.5,  8, 8.5,  9, 9.5, 10,10.5],
    "costas":             [22, 24, 26, 28, 30, 32, 34, 36],
    "altura_corpo":       [25, 28, 31, 34, 37, 40, 43, 46],
    "altura_cava":        [10, 11, 12, 13, 14, 15, 16, 17],
    "largura_braco":      [15, 16, 17, 18, 19, 20, 21, 22],
    "comp_manga_comprida":[25, 30, 35, 40, 45, 50, 54, 57],
    "comp_manga_curta":   [ 8, 10, 12, 13, 14, 15, 16, 17],
    "altura_gancho":      [16, 18, 20, 22, 24, 26, 28, 30],
    "comp_joelho":        [25, 30, 35, 40, 45, 50, 55, 60],
    "comp_calca":         [45, 52, 60, 68, 76, 84, 90, 96],
    "largura_joelho":     [20, 22, 24, 26, 28, 30, 32, 34],
    "largura_tornozelo":  [12, 13, 14, 15, 16, 17, 18, 19],
}


def seed_medidas_extras(db):
    existing = db.query(TabelaMedidasPadrao).filter_by(genero="masculino").count()
    if existing:
        print("  Medidas masculino/infantil já existem. Pulando.")
        return

    rows = []
    for ponto, valores in MEDIDAS_MASC_PLANO.items():
        for tam, val in zip(TAMANHOS_MASC, valores):
            rows.append(TabelaMedidasPadrao(
                genero="masculino", tipo_tecido="plano", elasticidade="plano",
                tamanho=tam, ponto_medida=ponto, valor_cm=float(val), fonte="extrapolado_mukai",
            ))
    for ponto, valores in MEDIDAS_INF_PLANO.items():
        for tam, val in zip(TAMANHOS_INF, valores):
            rows.append(TabelaMedidasPadrao(
                genero="infantil", tipo_tecido="plano", elasticidade="plano",
                tamanho=tam, ponto_medida=ponto, valor_cm=float(val), fonte="padrao_br_inf",
            ))
    db.bulk_save_objects(rows)
    db.commit()
    print(f"  Inseridas {len(rows)} medidas adicionais (masculino + infantil).")


# ---------------------------------------------------------------------------
# 2. Lookup de medidas corporais
# ---------------------------------------------------------------------------

def build_medidas_lookup(db):
    rows = db.query(TabelaMedidasPadrao).all()
    return {
        (r.genero, r.tipo_tecido, r.elasticidade, r.tamanho, r.ponto_medida): r.valor_cm
        for r in rows
    }


def get_body(lkp, genero, tipo, elasticidade, tamanho, ponto):
    return lkp.get((genero, tipo, elasticidade, tamanho, ponto))


# ---------------------------------------------------------------------------
# 3. Folgas de vestibilidade por (grau_ajuste, categoria, ponto)
# Simplificado — valores canônicos do método Mukai
# ---------------------------------------------------------------------------

FOLGAS = {
    # (grau_ajuste, categoria, ponto): folga_total_cm
    ("compression", None,     "busto"):   -4.0,
    ("compression", None,     "cintura"): -2.0,
    ("compression", None,     "quadril"): -4.0,
    ("compression", None,     "gancho"):  -1.0,
    ("fitted",      None,     "busto"):    2.0,
    ("fitted",      None,     "cintura"):  1.0,
    ("fitted",      None,     "quadril"):  2.0,
    ("fitted",      None,     "gancho"):   1.0,
    ("semi",        None,     "busto"):    4.0,
    ("semi",        None,     "cintura"):  2.0,
    ("semi",        None,     "quadril"):  4.0,
    ("semi",        None,     "gancho"):   2.0,
    ("relaxed",     None,     "busto"):    8.0,
    ("relaxed",     None,     "cintura"):  4.0,
    ("relaxed",     None,     "quadril"):  6.0,
    ("relaxed",     None,     "gancho"):   3.0,
    ("oversized",   None,     "busto"):   16.0,
    ("oversized",   None,     "cintura"):  8.0,
    ("oversized",   None,     "quadril"): 12.0,
    ("oversized",   None,     "gancho"):   4.0,
    # ombro e costas têm folga pequena ou nenhuma
    ("semi",        None,     "ombro"):    0.0,
    ("fitted",      None,     "ombro"):    0.0,
    ("relaxed",     None,     "ombro"):    0.5,
    ("oversized",   None,     "ombro"):    1.0,
    ("compression", None,     "ombro"):    0.0,
    # cava
    ("compression", None,     "altura_cava"): -0.5,
    ("fitted",      None,     "altura_cava"):  0.0,
    ("semi",        None,     "altura_cava"):  0.5,
    ("relaxed",     None,     "altura_cava"):  1.0,
    ("oversized",   None,     "altura_cava"):  2.0,
}


def folga(grau_ajuste, categoria, ponto):
    return (
        FOLGAS.get((grau_ajuste, categoria, ponto))
        or FOLGAS.get((grau_ajuste, None, ponto))
        or 0.0
    )


def med(lkp, genero, tipo, elasticidade, tamanho, ponto, grau_ajuste, categoria):
    v = get_body(lkp, genero, tipo, elasticidade, tamanho, ponto)
    if v is None:
        return None
    f = folga(grau_ajuste, categoria, ponto)
    return round(v + f, 1)


# ---------------------------------------------------------------------------
# 4. Comprimento total do molde por categoria + variante de comprimento
# ---------------------------------------------------------------------------

def calc_comprimento(categoria, subcategoria, comprimento_opt, body_vals):
    """Retorna o comprimento total do molde em cm."""
    def bv(ponto):
        return body_vals.get(ponto)

    if categoria == "manga":
        if subcategoria in ("curta", "baby_look", "petala"):
            return bv("comp_manga_curta")
        if subcategoria == "bufante":
            return (bv("comp_manga_curta") or 18) + 5
        return bv("comp_manga_comprida")

    if categoria == "saia":
        jlh = bv("comp_joelho") or 55
        map_ = {
            "micro":  38.0,
            "curta":  45.0,
            "joelho": jlh,
            "midi":   round(jlh + 15, 1),
            "longa":  90.0,
            "maxi":   110.0,
        }
        return map_.get(comprimento_opt, jlh + 15)

    if categoria == "blusa":
        ac = bv("altura_corpo") or 43
        map_ = {
            "cropped": round(ac - 8, 1),
            "normal":  round(ac + 5, 1),
            "longa":   round(ac + 15, 1),
        }
        return map_.get(comprimento_opt, round(ac + 5, 1))

    if categoria in ("camisa", "componente"):
        ac = bv("altura_corpo") or 43
        return round(ac + 10, 1)

    if categoria == "casaco":
        ac = bv("altura_corpo") or 43
        map_ = {
            "bolero":   round(ac - 5, 1),
            "quadril":  round(ac + 15, 1),
            "joelho":   (bv("comp_joelho") or 55) + (ac or 0),
            "longo":    round((bv("comp_joelho") or 55) + ac + 20, 1),
        }
        return map_.get(comprimento_opt, round(ac + 15, 1))

    if categoria == "vestido":
        ac = bv("altura_corpo") or 43
        jlh = bv("comp_joelho") or 55
        map_ = {
            "curta":  round(ac + 30, 1),
            "joelho": round(ac + jlh - 8, 1),
            "midi":   round(ac + jlh + 8, 1),
            "longa":  round(ac + 90, 1),
            "maxi":   round(ac + 110, 1),
        }
        return map_.get(comprimento_opt, round(ac + jlh - 8, 1))

    if categoria == "calca":
        cc = bv("comp_calca") or 95
        jlh = bv("comp_joelho") or 55
        map_ = {
            "bermuda": round(jlh - 8, 1),
            "capri":   round(cc * 0.72, 1),
            "7_8":     round(cc * 0.875, 1),
            "comprida": cc,
        }
        return map_.get(comprimento_opt, cc)

    return None


# ---------------------------------------------------------------------------
# 5. Descrição natural e tags por SKU
# ---------------------------------------------------------------------------

FIT_PT = {
    "compression": "de compressão",
    "fitted":      "justa",
    "semi":        "semi-ajustada",
    "relaxed":     "folgada",
    "oversized":   "ampla (oversized)",
}

TECIDO_PT = {
    ("plano",  "plano"): "tecido plano",
    ("malha",  "baixa"): "malha de baixa elasticidade",
    ("malha",  "media"): "malha de média elasticidade",
    ("malha",  "alta"):  "malha de alta elasticidade",
}

FIT_TAGS = {
    "compression": ["compressao","comprimida","segunda pele","justo","ajustado","sem folga"],
    "fitted":      ["justa","ajustada","justo","ajustado","colado","molda o corpo"],
    "semi":        ["semi ajustada","confortavel","padrao","nem justo nem folgado"],
    "relaxed":     ["folgada","confortavel","casual","soltinha","sem apertar","ampla"],
    "oversized":   ["oversized","largo","muito folgado","grande","extra ampla","boxy"],
}

COMP_TAGS = {
    "micro":   ["mini","curtissima","muito curta"],
    "curta":   ["curta","acima do joelho","short"],
    "joelho":  ["joelho","ate o joelho","knee length"],
    "midi":    ["midi","abaixo do joelho","medio","meio"],
    "longa":   ["longa","comprida","long","maxi","ate o tornozelo"],
    "maxi":    ["maxi","maxima","muito longa","ate o chao"],
    "cropped": ["cropped","curta","boxy","ombligo","barriga"],
    "normal":  ["basica","padrao","normal","comprimento padrao"],
    "quadril": ["quadril","hip","ate o quadril"],
    "bolero":  ["bolero","curta","cintura"],
    "comprida":["comprida","inteira","longa"],
    "bermuda": ["bermuda","short","curta","acima do joelho"],
    "capri":   ["capri","3 quartos","abaixo do joelho"],
    "7_8":     ["sete oitavos","7/8","abaixo da canela"],
    "joelho":  ["joelho","ate o joelho"],
}

COS_TAGS = {
    "alto":    ["cintura alta","high waist","taille haute"],
    "medio":   ["cintura media","cintura natural","padrao"],
    "baixo":   ["cintura baixa","low waist","hip bone"],
    "elastico":["elastico","confortavel","sem cos rigido","jersey"],
    "nenhum":  [],
}

CONTEXTO_USO = {
    "base-saia-reta":              ["casual","social","trabalho","versátil"],
    "base-saia-lapis":             ["social","executivo","elegante","lapis","ajustada"],
    "base-saia-gode":              ["festa","romantico","rodada","godê"],
    "base-saia-evase-classica":    ["casual","jovial","evasê"],
    "base-saia-longa-babados":     ["festa","romantico","babados","longa"],
    "base-saia-pregueada":         ["social","casual","pregueada","clássico"],
    "base-saia-sino":              ["festa","jovial","sino","volume"],
    "base-blusa-basica":           ["casual","versátil","basica","dia a dia"],
    "base-blusa-basica-pences":    ["social","elegante","ajustada","busto"],
    "base-regata":                 ["casual","verao","esporte","academia","funcional"],
    "base-regata-alcinhas":        ["casual","verao","festa","praia"],
    "base-blusa-transpassada":     ["casual","social","transpassada","wrap"],
    "base-blusa-gola-degage":      ["festa","sensual","degage","ombros"],
    "base-blusa-manga-japonesa":   ["casual","confortavel","kimono","dolman","ampla"],
    "base-top-corpete":            ["festa","sensual","corpete","bustier"],
    "base-blusa-cigana":           ["casual","boho","cigana","franzido"],
    "base-manga-curta":            ["casual","verao","componente","manga"],
    "base-manga-longa":            ["social","inverno","componente","manga"],
    "base-manga-raglan":           ["esporte","casual","raglan","componente"],
    "base-manga-baby-look":        ["casual","jovial","baby look","curta","stretch"],
    "base-manga-petala":           ["festa","elegante","petala","tulipa","decorativa"],
    "base-manga-bufante":          ["festa","romantico","bufante","franzido","volume"],
    "base-manga-alfaiataria":      ["social","executivo","alfaiataria","terno"],
    "base-manga-ordinaria":        ["casual","esporte","manga dois panos"],
    "base-camisa-fem-social":      ["social","executivo","trabalho","formal","colarinho"],
    "base-camisa-fem-pences":      ["social","elegante","ajustada","pences"],
    "base-camisa-fem-palas":       ["social","casual","palas","costas"],
    "base-gola-ordinaria":         ["componente","gola","colarinho"],
    "base-camisa-fem-bata":        ["casual","boho","bata","ampla","nervuras"],
    "base-blazer-dois-botoes":     ["social","executivo","trabalho","blazer","formal"],
    "base-bolero":                 ["festa","elegante","bolero","curto"],
    "base-sobretudo":              ["inverno","elegante","sobretudo","casaco longo"],
    "base-sobretudo-transpassado": ["inverno","casual","transpassado","wrap casaco"],
    "base-vestido-basico":         ["casual","versátil","vestido","dia a dia"],
    "base-vestido-tubo-pences":    ["social","elegante","festa","tubinho","pences"],
    "base-vestido-tubo-recortes":  ["social","elegante","recortes","princesa","tubinho"],
    "base-vestido-evase-recortes": ["casual","social","evasê","recortes","princesa"],
    "base-vestido-envelope":       ["casual","social","envelope","wrap","transpassado"],
    "base-vestido-trapezio":       ["casual","jovial","trapezio","A-line","solto"],
    "base-vestido-chemisier":      ["casual","social","chemisier","camisa","botoes"],
    "base-vestido-evase-pregas":   ["casual","social","evasê","pregas","volume"],
    "base-vestido-tomara":         ["festa","verao","sensual","tomara que caia","aterrado"],
    "base-vestido-drapeado":       ["festa","elegante","drapeado","assimetrico"],
    "base-vestido-frente-unica":   ["festa","elegante","frente unica","one shoulder"],
    "base-calca-comprida":         ["casual","versátil","calca","dia a dia"],
    "base-calca-pregas":           ["social","executivo","pregas","formal"],
    "base-calca-pantalona":        ["casual","social","pantalona","wide leg","ampla"],
    "base-calca-bolsos":           ["casual","funcional","bolsos","utilitario"],
    "base-calca-flare":            ["casual","boho","flare","bootcut","sino"],
    "base-calca-cos-baixo":        ["casual","jovial","low rise","cintura baixa"],
    "base-calca-pijama":           ["confort","casa","pijama","elastico","casa"],
    "base-camisa-masc-social":     ["social","executivo","formal","masculino","colarinho"],
    "base-calca-masc-social":      ["social","executivo","formal","masculino","social"],
    "base-blazer-masc":            ["social","executivo","formal","masculino","blazer"],
    "base-vestido-inf-evase":      ["infantil","menina","casual","evasê"],
    "base-vestido-inf-princesa":   ["infantil","menina","festa","princesa"],
    "base-bermuda-inf-menino":     ["infantil","menino","casual","bermuda"],
}


def gerar_descricao(nome, tamanho, tipo_tecido, elasticidade, grau_ajuste,
                    comprimento, decote, manga, fechamento, cos, genero):
    tecido_str = TECIDO_PT.get((tipo_tecido, elasticidade), tipo_tecido)
    fit_str = FIT_PT.get(grau_ajuste, grau_ajuste)
    partes = [nome, f"tamanho {tamanho}", f"em {tecido_str}", f"modelagem {fit_str}"]
    if comprimento and comprimento not in ("nenhum", "normal"):
        partes.append(f"comprimento {comprimento}")
    if decote and decote not in ("nenhum",):
        partes.append(f"decote {decote}")
    if manga and manga not in ("nenhum", "sem_manga"):
        partes.append(f"manga {manga}")
    if cos and cos not in ("nenhum",):
        partes.append(f"cós {cos}")
    if genero in ("masculino", "infantil"):
        partes.append(genero)
    return ", ".join(partes) + "."


def gerar_tags(base, tamanho, tipo_tecido, elasticidade, grau_ajuste,
               comprimento, decote, cos, manga, fechamento):
    t = set()
    t.add(base.categoria)
    if base.subcategoria:
        t.add(base.subcategoria)
    # palavras do nome da peça
    for w in base.nome.lower().split():
        if len(w) > 2:
            t.add(w)
    t.add(str(tamanho))
    t.add(tipo_tecido)
    t.add(elasticidade)
    if tipo_tecido == "malha":
        t.update(["malha", "stretch", "elastico"])
    else:
        t.update(["plano", "tecido plano"])
    t.add(grau_ajuste)
    t.update(FIT_TAGS.get(grau_ajuste, []))
    if comprimento:
        t.add(comprimento)
        t.update(COMP_TAGS.get(comprimento, []))
    if decote and decote not in ("nenhum",):
        t.add(decote)
    if cos and cos not in ("nenhum",):
        t.add(cos)
        t.update(COS_TAGS.get(cos, []))
    if manga and manga not in ("nenhum",):
        t.add(manga)
    if fechamento and fechamento not in ("nenhum",):
        t.add(fechamento)
    t.add(base.genero)
    t.update(CONTEXTO_USO.get(base.codigo, []))
    t.discard("")
    return json.dumps(sorted(t), ensure_ascii=False)


# ---------------------------------------------------------------------------
# 6. Configurações de variação por molde base
# (comprimento, decote, manga, fechamento, cos)
# ---------------------------------------------------------------------------

# Variantes de comprimento por molde (None = não aplica)
COMPRIMENTO_POR_MOLDE = {
    "base-saia-reta":              "midi",
    "base-saia-lapis":             "joelho",
    "base-saia-gode":              "midi",
    "base-saia-evase-classica":    "joelho",
    "base-saia-longa-babados":     "longa",
    "base-saia-pregueada":         "midi",
    "base-saia-sino":              "midi",
    "base-blusa-basica":           "normal",
    "base-blusa-basica-pences":    "normal",
    "base-regata":                 "normal",
    "base-regata-alcinhas":        "normal",
    "base-blusa-transpassada":     "normal",
    "base-blusa-gola-degage":      "normal",
    "base-blusa-manga-japonesa":   "normal",
    "base-top-corpete":            "cropped",
    "base-blusa-cigana":           "normal",
    "base-manga-curta":            "curta",
    "base-manga-longa":            "longa",
    "base-manga-raglan":           "longa",
    "base-manga-baby-look":        "curta",
    "base-manga-petala":           "curta",
    "base-manga-bufante":          "curta",
    "base-manga-alfaiataria":      "longa",
    "base-manga-ordinaria":        "longa",
    "base-camisa-fem-social":      "normal",
    "base-camisa-fem-pences":      "normal",
    "base-camisa-fem-palas":       "normal",
    "base-gola-ordinaria":         None,
    "base-camisa-fem-bata":        "normal",
    "base-blazer-dois-botoes":     "quadril",
    "base-bolero":                 "bolero",
    "base-sobretudo":              "joelho",
    "base-sobretudo-transpassado": "joelho",
    "base-vestido-basico":         "joelho",
    "base-vestido-tubo-pences":    "joelho",
    "base-vestido-tubo-recortes":  "joelho",
    "base-vestido-evase-recortes": "midi",
    "base-vestido-envelope":       "joelho",
    "base-vestido-trapezio":       "midi",
    "base-vestido-chemisier":      "joelho",
    "base-vestido-evase-pregas":   "midi",
    "base-vestido-tomara":         "curta",
    "base-vestido-drapeado":       "joelho",
    "base-vestido-frente-unica":   "joelho",
    "base-calca-comprida":         "comprida",
    "base-calca-pregas":           "comprida",
    "base-calca-pantalona":        "comprida",
    "base-calca-bolsos":           "comprida",
    "base-calca-flare":            "comprida",
    "base-calca-cos-baixo":        "comprida",
    "base-calca-pijama":           "comprida",
    "base-camisa-masc-social":     "normal",
    "base-calca-masc-social":      "comprida",
    "base-blazer-masc":            "quadril",
    "base-vestido-inf-evase":      "joelho",
    "base-vestido-inf-princesa":   "midi",
    "base-bermuda-inf-menino":     "bermuda",
}

DECOTE_POR_MOLDE = {
    "base-saia-reta": None, "base-saia-lapis": None, "base-saia-gode": None,
    "base-saia-evase-classica": None, "base-saia-longa-babados": None,
    "base-saia-pregueada": None, "base-saia-sino": None,
    "base-blusa-basica": "redondo",
    "base-blusa-basica-pences": "redondo",
    "base-regata": "redondo",
    "base-regata-alcinhas": "v",
    "base-blusa-transpassada": "v",
    "base-blusa-gola-degage": "degage",
    "base-blusa-manga-japonesa": "redondo",
    "base-top-corpete": "quadrado",
    "base-blusa-cigana": "redondo",
    "base-manga-curta": None, "base-manga-longa": None, "base-manga-raglan": None,
    "base-manga-baby-look": None, "base-manga-petala": None, "base-manga-bufante": None,
    "base-manga-alfaiataria": None, "base-manga-ordinaria": None,
    "base-camisa-fem-social": "colarinho",
    "base-camisa-fem-pences": "colarinho",
    "base-camisa-fem-palas": "colarinho",
    "base-gola-ordinaria": "colarinho",
    "base-camisa-fem-bata": "redondo",
    "base-blazer-dois-botoes": "lapela",
    "base-bolero": "redondo",
    "base-sobretudo": "lapela",
    "base-sobretudo-transpassado": "v",
    "base-vestido-basico": "redondo",
    "base-vestido-tubo-pences": "redondo",
    "base-vestido-tubo-recortes": "redondo",
    "base-vestido-evase-recortes": "redondo",
    "base-vestido-envelope": "v",
    "base-vestido-trapezio": "redondo",
    "base-vestido-chemisier": "colarinho",
    "base-vestido-evase-pregas": "redondo",
    "base-vestido-tomara": "quadrado",
    "base-vestido-drapeado": "v",
    "base-vestido-frente-unica": "assimetrico",
    "base-calca-comprida": None, "base-calca-pregas": None, "base-calca-pantalona": None,
    "base-calca-bolsos": None, "base-calca-flare": None,
    "base-calca-cos-baixo": None, "base-calca-pijama": None,
    "base-camisa-masc-social": "colarinho",
    "base-calca-masc-social": None,
    "base-blazer-masc": "lapela",
    "base-vestido-inf-evase": "redondo",
    "base-vestido-inf-princesa": "redondo",
    "base-bermuda-inf-menino": None,
}

MANGA_POR_MOLDE = {
    "base-saia-reta": None, "base-saia-lapis": None, "base-saia-gode": None,
    "base-saia-evase-classica": None, "base-saia-longa-babados": None,
    "base-saia-pregueada": None, "base-saia-sino": None,
    "base-blusa-basica": "sem_manga",
    "base-blusa-basica-pences": "sem_manga",
    "base-regata": "sem_manga",
    "base-regata-alcinhas": "sem_manga",
    "base-blusa-transpassada": "sem_manga",
    "base-blusa-gola-degage": "sem_manga",
    "base-blusa-manga-japonesa": "integrada",
    "base-top-corpete": "sem_manga",
    "base-blusa-cigana": "sem_manga",
    "base-manga-curta": None,
    "base-manga-longa": None,
    "base-manga-raglan": None,
    "base-manga-baby-look": None,
    "base-manga-petala": None,
    "base-manga-bufante": None,
    "base-manga-alfaiataria": None,
    "base-manga-ordinaria": None,
    "base-camisa-fem-social": "longa",
    "base-camisa-fem-pences": "longa",
    "base-camisa-fem-palas": "longa",
    "base-gola-ordinaria": None,
    "base-camisa-fem-bata": "sem_manga",
    "base-blazer-dois-botoes": "longa",
    "base-bolero": "curta",
    "base-sobretudo": "longa",
    "base-sobretudo-transpassado": "longa",
    "base-vestido-basico": "sem_manga",
    "base-vestido-tubo-pences": "sem_manga",
    "base-vestido-tubo-recortes": "sem_manga",
    "base-vestido-evase-recortes": "sem_manga",
    "base-vestido-envelope": "sem_manga",
    "base-vestido-trapezio": "sem_manga",
    "base-vestido-chemisier": "curta",
    "base-vestido-evase-pregas": "sem_manga",
    "base-vestido-tomara": "sem_manga",
    "base-vestido-drapeado": "sem_manga",
    "base-vestido-frente-unica": "sem_manga",
    "base-calca-comprida": None, "base-calca-pregas": None, "base-calca-pantalona": None,
    "base-calca-bolsos": None, "base-calca-flare": None,
    "base-calca-cos-baixo": None, "base-calca-pijama": None,
    "base-camisa-masc-social": "longa",
    "base-calca-masc-social": None,
    "base-blazer-masc": "longa",
    "base-vestido-inf-evase": "sem_manga",
    "base-vestido-inf-princesa": "sem_manga",
    "base-bermuda-inf-menino": None,
}

FECHAMENTO_POR_MOLDE = {
    "base-saia-reta": "zipper_lateral", "base-saia-lapis": "zipper_lateral",
    "base-saia-gode": "zipper_lateral", "base-saia-evase-classica": "zipper_lateral",
    "base-saia-longa-babados": "elastico", "base-saia-pregueada": "zipper_lateral",
    "base-saia-sino": "elastico",
    "base-blusa-basica": "nenhum", "base-blusa-basica-pences": "nenhum",
    "base-regata": "nenhum", "base-regata-alcinhas": "nenhum",
    "base-blusa-transpassada": "amarracao",
    "base-blusa-gola-degage": "nenhum",
    "base-blusa-manga-japonesa": "nenhum",
    "base-top-corpete": "zipper_traseiro",
    "base-blusa-cigana": "elastico",
    "base-manga-curta": "nenhum", "base-manga-longa": "nenhum",
    "base-manga-raglan": "nenhum", "base-manga-baby-look": "nenhum",
    "base-manga-petala": "nenhum", "base-manga-bufante": "nenhum",
    "base-manga-alfaiataria": "nenhum", "base-manga-ordinaria": "nenhum",
    "base-camisa-fem-social": "botoes", "base-camisa-fem-pences": "botoes",
    "base-camisa-fem-palas": "botoes",
    "base-gola-ordinaria": "nenhum",
    "base-camisa-fem-bata": "nenhum",
    "base-blazer-dois-botoes": "botoes",
    "base-bolero": "nenhum",
    "base-sobretudo": "botoes", "base-sobretudo-transpassado": "amarracao",
    "base-vestido-basico": "zipper_traseiro",
    "base-vestido-tubo-pences": "zipper_traseiro",
    "base-vestido-tubo-recortes": "zipper_traseiro",
    "base-vestido-evase-recortes": "zipper_traseiro",
    "base-vestido-envelope": "amarracao",
    "base-vestido-trapezio": "zipper_traseiro",
    "base-vestido-chemisier": "botoes",
    "base-vestido-evase-pregas": "zipper_traseiro",
    "base-vestido-tomara": "elastico",
    "base-vestido-drapeado": "zipper_lateral",
    "base-vestido-frente-unica": "zipper_lateral",
    "base-calca-comprida": "zipper_frente",
    "base-calca-pregas": "zipper_frente",
    "base-calca-pantalona": "zipper_frente",
    "base-calca-bolsos": "zipper_frente",
    "base-calca-flare": "zipper_frente",
    "base-calca-cos-baixo": "zipper_frente",
    "base-calca-pijama": "elastico",
    "base-camisa-masc-social": "botoes",
    "base-calca-masc-social": "zipper_frente",
    "base-blazer-masc": "botoes",
    "base-vestido-inf-evase": "zipper_traseiro",
    "base-vestido-inf-princesa": "zipper_traseiro",
    "base-bermuda-inf-menino": "elastico",
}

COS_POR_MOLDE = {
    "base-saia-reta": "medio", "base-saia-lapis": "medio",
    "base-saia-gode": "medio", "base-saia-evase-classica": "medio",
    "base-saia-longa-babados": "elastico", "base-saia-pregueada": "medio",
    "base-saia-sino": "elastico",
    "base-blusa-basica": None, "base-blusa-basica-pences": None,
    "base-regata": None, "base-regata-alcinhas": None,
    "base-blusa-transpassada": None, "base-blusa-gola-degage": None,
    "base-blusa-manga-japonesa": None, "base-top-corpete": None,
    "base-blusa-cigana": "elastico",
    "base-manga-curta": None, "base-manga-longa": None, "base-manga-raglan": None,
    "base-manga-baby-look": None, "base-manga-petala": None, "base-manga-bufante": None,
    "base-manga-alfaiataria": None, "base-manga-ordinaria": None,
    "base-camisa-fem-social": None, "base-camisa-fem-pences": None,
    "base-camisa-fem-palas": None, "base-gola-ordinaria": None,
    "base-camisa-fem-bata": None,
    "base-blazer-dois-botoes": None, "base-bolero": None,
    "base-sobretudo": None, "base-sobretudo-transpassado": None,
    "base-vestido-basico": None, "base-vestido-tubo-pences": None,
    "base-vestido-tubo-recortes": None, "base-vestido-evase-recortes": None,
    "base-vestido-envelope": None, "base-vestido-trapezio": None,
    "base-vestido-chemisier": None, "base-vestido-evase-pregas": None,
    "base-vestido-tomara": "elastico", "base-vestido-drapeado": None,
    "base-vestido-frente-unica": None,
    "base-calca-comprida": "medio", "base-calca-pregas": "medio",
    "base-calca-pantalona": "medio", "base-calca-bolsos": "medio",
    "base-calca-flare": "medio", "base-calca-cos-baixo": "baixo",
    "base-calca-pijama": "elastico",
    "base-camisa-masc-social": None, "base-calca-masc-social": "medio",
    "base-blazer-masc": None,
    "base-vestido-inf-evase": None, "base-vestido-inf-princesa": None,
    "base-bermuda-inf-menino": "elastico",
}


# ---------------------------------------------------------------------------
# 7. Plano de geração de SKUs
# ---------------------------------------------------------------------------

TAMANHOS_PLANO_FEM  = ["36","38","40","42","44","46","48","50","52","54","56","58","60","62"]
TAMANHOS_MALHA_FEM  = ["36","38","40","42","44","46"]   # PP P M G GG EGG
TAMANHO_LABEL_MALHA = {"36":"PP","38":"P","40":"M","42":"G","44":"GG","46":"EGG"}

# (categoria, genero, tipo_tecido, elasticidade) → lista de fits
FITS_POR_GRUPO = {
    ("saia",       "feminino",  "plano",  "plano"):  ["fitted","semi","relaxed"],
    ("blusa",      "feminino",  "plano",  "plano"):  ["fitted","semi","relaxed"],
    ("blusa",      "feminino",  "malha",  "media"):  ["fitted"],
    ("blusa",      "feminino",  "malha",  "alta"):   ["fitted"],
    ("manga",      "feminino",  "plano",  "plano"):  ["semi"],
    ("camisa",     "feminino",  "plano",  "plano"):  ["semi","relaxed"],
    ("componente", "feminino",  "plano",  "plano"):  ["semi"],
    ("casaco",     "feminino",  "plano",  "plano"):  ["relaxed","oversized"],
    ("vestido",    "feminino",  "plano",  "plano"):  ["fitted","semi","relaxed"],
    ("vestido",    "feminino",  "malha",  "media"):  ["fitted"],
    ("vestido",    "feminino",  "malha",  "alta"):   ["fitted"],
    ("calca",      "feminino",  "plano",  "plano"):  ["fitted","semi","relaxed"],
    ("calca",      "feminino",  "malha",  "media"):  ["semi","relaxed"],
    ("calca",      "feminino",  "malha",  "alta"):   ["compression","fitted"],
    ("camisa",     "masculino", "plano",  "plano"):  ["semi","relaxed"],
    ("calca",      "masculino", "plano",  "plano"):  ["semi","relaxed"],
    ("casaco",     "masculino", "plano",  "plano"):  ["relaxed","oversized"],
    ("vestido",    "infantil",  "plano",  "plano"):  ["semi","relaxed"],
    ("calca",      "infantil",  "plano",  "plano"):  ["semi","relaxed"],
}

# Padrões que suportam malha (by categoria+genero - usamos grupos acima)
SUPORTA_MALHA = {
    ("blusa", "feminino"):   ["media","alta"],
    ("vestido", "feminino"): ["media","alta"],
    ("calca", "feminino"):   ["media","alta"],
}

# Padrões que NÃO suportam malha (overrides)
NAO_SUPORTA_MALHA = {
    "base-manga-petala", "base-manga-bufante", "base-manga-alfaiataria",
    "base-manga-raglan", "base-bolero", "base-sobretudo",
    "base-sobretudo-transpassado", "base-blazer-dois-botoes",
    "base-gola-ordinaria",
    # vestidos muito estruturados
    "base-vestido-drapeado", "base-vestido-frente-unica",
}

# Vestidos que fazem sentido em malha alta
VESTIDOS_MALHA_ALTA = {
    "base-vestido-tubo-pences", "base-vestido-tubo-recortes",
    "base-vestido-tomara", "base-vestido-basico",
}


def tamanho_label(tamanho, tipo_tecido, elasticidade):
    """Retorna o label de tamanho para o código do SKU."""
    if tipo_tecido == "malha":
        return TAMANHO_LABEL_MALHA.get(tamanho, tamanho)
    return tamanho


def sku_codigo(base_codigo, tamanho, tipo_tecido, elasticidade, grau_ajuste):
    slug = base_codigo.removeprefix("base-")
    tam  = tamanho_label(tamanho, tipo_tecido, elasticidade)
    tec  = "plano" if tipo_tecido == "plano" else f"malha-{elasticidade[0]}"
    return f"{slug}-{tam}-{tec}-{grau_ajuste}"


def planos_de_geracao(base):
    """Retorna lista de (tamanho, tipo_tecido, elasticidade, fits[]) para um molde base."""
    cat = base.categoria
    gen = base.genero
    plans = []

    # Tecido plano — todos os gêneros têm plano
    tam_plano = (TAMANHOS_MASC if gen == "masculino"
                 else TAMANHOS_INF if gen == "infantil"
                 else TAMANHOS_PLANO_FEM)
    fits_plano = FITS_POR_GRUPO.get((cat, gen, "plano", "plano"), [])
    if fits_plano:
        for t in tam_plano:
            for fit in fits_plano:
                plans.append((t, "plano", "plano", fit))

    # Malha — apenas feminino, apenas categorias suportadas
    if gen == "feminino":
        elasticidades = SUPORTA_MALHA.get((cat, gen), [])
        for elast in elasticidades:
            if base.codigo in NAO_SUPORTA_MALHA:
                continue
            if elast == "alta" and cat == "vestido" and base.codigo not in VESTIDOS_MALHA_ALTA:
                continue
            fits_malha = FITS_POR_GRUPO.get((cat, gen, "malha", elast), [])
            for t in TAMANHOS_MALHA_FEM:
                for fit in fits_malha:
                    plans.append((t, "malha", elast, fit))

    return plans


# ---------------------------------------------------------------------------
# 8. Execução
# ---------------------------------------------------------------------------

def gerar():
    db = SessionLocal()
    try:
        # Verificar se já foi populado
        existing = db.query(MoldeVariacao).count()
        if existing:
            print(f"Variações já existem ({existing} SKUs). Use --force para recriar.")
            return

        # Seed de medidas extras
        print("Verificando medidas masculino/infantil...")
        seed_medidas_extras(db)

        # Carregar lookup de medidas
        print("Carregando tabela de medidas...")
        lkp = build_medidas_lookup(db)

        # Carregar todos os moldes base
        bases = db.query(MoldeBase).all()
        print(f"Moldes base encontrados: {len(bases)}")

        batch = []
        total = 0
        erros = []

        for base in bases:
            plans = planos_de_geracao(base)

            for (tamanho, tipo_tecido, elasticidade, grau_ajuste) in plans:
                cat = base.categoria

                # Medidas corporais para este SKU
                def bv(ponto):
                    return lkp.get((base.genero, tipo_tecido, elasticidade, tamanho, ponto))

                body_vals = {
                    p: bv(p) for p in [
                        "busto","cintura","quadril","ombro","costas",
                        "largura_braco","altura_cava","comp_manga_comprida",
                        "comp_manga_curta","altura_gancho","comp_calca",
                        "comp_joelho","largura_joelho","largura_tornozelo",
                        "altura_corpo",
                    ]
                }

                # Variantes de construção (padrões por molde)
                comp_opt   = COMPRIMENTO_POR_MOLDE.get(base.codigo)
                decote_val = DECOTE_POR_MOLDE.get(base.codigo)
                manga_val  = MANGA_POR_MOLDE.get(base.codigo)
                fech_val   = FECHAMENTO_POR_MOLDE.get(base.codigo)
                cos_val    = COS_POR_MOLDE.get(base.codigo)

                # Medidas de molde
                def mm(ponto):
                    return med(lkp, base.genero, tipo_tecido, elasticidade,
                               tamanho, ponto, grau_ajuste, cat)

                busto_m  = mm("busto")   if cat not in ("saia", "calca") else None
                cintura_m = mm("cintura")
                quadril_m = mm("quadril")
                ombro_m  = mm("ombro")   if cat not in ("saia", "calca") else None
                costas_m = mm("costas")  if cat not in ("saia", "calca") else None
                braco_m  = mm("largura_braco") if cat not in ("saia", "calca") else None
                cava_m   = mm("altura_cava") if cat not in ("saia", "calca") else None
                gancho_m = mm("altura_gancho") if cat in ("calca",) else None
                joelho_m = mm("largura_joelho") if cat in ("calca",) else None
                torn_m   = mm("largura_tornozelo") if cat in ("calca",) else None

                # Comprimento total
                comp_cm = calc_comprimento(cat, base.subcategoria, comp_opt, body_vals)

                # SKU code
                codigo = sku_codigo(base.codigo, tamanho, tipo_tecido, elasticidade, grau_ajuste)

                # Descrição natural
                descricao = gerar_descricao(
                    base.nome, tamanho_label(tamanho, tipo_tecido, elasticidade),
                    tipo_tecido, elasticidade, grau_ajuste,
                    comp_opt, decote_val, manga_val, fech_val, cos_val, base.genero
                )

                # Tags
                tags_json = gerar_tags(
                    base, tamanho_label(tamanho, tipo_tecido, elasticidade),
                    tipo_tecido, elasticidade, grau_ajuste,
                    comp_opt, decote_val, cos_val, manga_val, fech_val
                )

                batch.append(MoldeVariacao(
                    codigo=codigo,
                    molde_base_id=base.id,
                    tamanho=tamanho_label(tamanho, tipo_tecido, elasticidade),
                    tipo_tecido=tipo_tecido,
                    elasticidade=elasticidade,
                    grau_ajuste=grau_ajuste,
                    genero=base.genero,
                    comprimento=comp_opt,
                    decote=decote_val,
                    manga=manga_val,
                    fechamento=fech_val,
                    cos=cos_val,
                    busto_molde=busto_m,
                    cintura_molde=cintura_m,
                    quadril_molde=quadril_m,
                    ombro_molde=ombro_m,
                    costas_molde=costas_m,
                    largura_braco_molde=braco_m,
                    altura_cava_molde=cava_m,
                    comprimento_total_molde=comp_cm,
                    gancho_molde=gancho_m,
                    largura_joelho_molde=joelho_m,
                    largura_tornozelo_molde=torn_m,
                    descricao_natural=descricao,
                    tags=tags_json,
                ))
                total += 1

                # Flush em lotes de 500
                if len(batch) >= 500:
                    db.bulk_save_objects(batch)
                    db.commit()
                    print(f"  {total} SKUs inseridos...")
                    batch = []

        if batch:
            db.bulk_save_objects(batch)
            db.commit()

        print(f"\nGeração concluída: {total} SKUs criados.")

        # Estatísticas
        from sqlalchemy import func as sqlfunc
        print("\n=== DISTRIBUIÇÃO POR CATEGORIA ===")
        from app.models.models import MoldeVariacao as MV
        from sqlalchemy.orm import joinedload
        for cat, cnt in (
            db.query(MoldeBase.categoria, sqlfunc.count(MV.id))
            .join(MV, MV.molde_base_id == MoldeBase.id)
            .group_by(MoldeBase.categoria)
            .all()
        ):
            print(f"  {cat:15} {cnt:5} SKUs")

        print("\n=== POR TIPO DE TECIDO ===")
        for tec, cnt in db.query(MV.tipo_tecido, sqlfunc.count()).group_by(MV.tipo_tecido).all():
            print(f"  {tec:10} {cnt} SKUs")

        print("\n=== POR GRAU DE AJUSTE ===")
        for ga, cnt in db.query(MV.grau_ajuste, sqlfunc.count()).group_by(MV.grau_ajuste).all():
            print(f"  {ga:15} {cnt} SKUs")

        print(f"\nTotal: {db.query(MV).count()} SKUs no banco.")

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    import sys
    force = "--force" in sys.argv
    if force:
        db = SessionLocal()
        db.query(MoldeVariacao).delete()
        db.commit()
        db.close()
        print("SKUs anteriores removidos.")
    gerar()
