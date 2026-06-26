from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata


TOKEN_RE = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class SemanticProfile:
    raw: str
    normalized: str
    tokens: tuple[str, ...]
    categoria_input: str | None
    categorias_referencia: tuple[str, ...]
    grau_ajuste: str | None
    ajustes_alternativos: tuple[str, ...]
    tipo_tecido: str | None
    linguagem_construcao: str | None
    precisa_base_composta: bool
    componentes_detectados: tuple[str, ...]
    operacoes_geometricas: tuple[str, ...]
    validacoes_obrigatorias: tuple[str, ...]
    motivos: tuple[str, ...]
    alertas: tuple[str, ...]

    def as_dict(self) -> dict:
        return {
            "input": self.raw,
            "normalizado": self.normalized,
            "tokens": list(self.tokens),
            "categoria_input": self.categoria_input,
            "categorias_referencia": list(self.categorias_referencia),
            "grau_ajuste": self.grau_ajuste,
            "ajustes_alternativos": list(self.ajustes_alternativos),
            "tipo_tecido": self.tipo_tecido,
            "linguagem_construcao": self.linguagem_construcao,
            "precisa_base_composta": self.precisa_base_composta,
            "componentes_detectados": list(self.componentes_detectados),
            "operacoes_geometricas": list(self.operacoes_geometricas),
            "validacoes_obrigatorias": list(self.validacoes_obrigatorias),
            "motivos": list(self.motivos),
            "alertas": list(self.alertas),
        }


@dataclass(frozen=True)
class RankedVariation:
    variacao: object
    score: float
    motivos: tuple[str, ...]
    papel_referencia: str


def normalize_text(value: str | None) -> str:
    text = unicodedata.normalize("NFD", str(value or ""))
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-zA-Z0-9\s]", " ", text).lower()).strip()


def _contains_any(text: str, words: tuple[str, ...]) -> bool:
    return any(word in text for word in words)


def _tokenize(text: str) -> tuple[str, ...]:
    stopwords = {
        "a", "o", "os", "as", "de", "da", "do", "das", "dos", "um", "uma",
        "tipo", "com", "para", "que", "e", "ou", "mais", "menos",
    }
    return tuple(t for t in TOKEN_RE.findall(text) if t not in stopwords and len(t) > 1)


COMPONENT_KEYWORDS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("gola_camp", ("gola camp", "camp collar", "gola aberta")),
    ("gola_colarinho", ("colarinho", "gola social", "gola colarinho")),
    ("pe_de_gola", ("pe de gola", "stand collar")),
    ("manga_curta", ("manga curta", "short sleeve")),
    ("manga_longa", ("manga longa", "long sleeve")),
    ("manga_raglan", ("manga raglan", "raglan")),
    ("manga_bufante", ("manga bufante", "manga fofa", "bufante")),
    ("punho", ("punho", "cuff")),
    ("carcela", ("carcela", "placket")),
    ("vista_abertura", ("vista", "abotoamento", "botoes", "button")),
    ("bolso_faca", ("bolso faca", "bolso lateral", "slash pocket")),
    ("bolso_cargo", ("bolso cargo", "cargo pocket")),
    ("cos", ("cos", "waistband", "cintura alta", "elastico")),
    ("ziper", ("ziper", "fecho eclair", "zip")),
    ("pence", ("pence", "pences", "dart")),
    ("recorte_princesa", ("recorte princesa", "princess seam")),
    ("lapela", ("lapela", "lapel")),
)


def _keyword_found(normalized: str, tokens: tuple[str, ...], keyword: str) -> bool:
    if " " in keyword:
        return keyword in normalized
    return keyword in tokens


def _detect_components(normalized: str, tokens: tuple[str, ...]) -> tuple[str, ...]:
    componentes: list[str] = []
    for component, keywords in COMPONENT_KEYWORDS:
        if any(_keyword_found(normalized, tokens, keyword) for keyword in keywords):
            componentes.append(component)
    return tuple(componentes)


def _dedupe(items: list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return tuple(result)


def _geometry_operations(
    categoria_input: str | None,
    componentes: tuple[str, ...],
    precisa_base_composta: bool,
) -> tuple[str, ...]:
    operacoes: list[str] = []

    if precisa_base_composta:
        operacoes.extend([
            "combinar_base_superior_com_base_inferior",
            "mapear_comprimento_torso_antes_do_gancho",
            "preservar_eixo_centro_frente_centro_costas",
        ])
    elif categoria_input:
        operacoes.append(f"selecionar_base_{categoria_input}")

    if categoria_input in {"camisa", "casaco", "vestido", "blusa"}:
        operacoes.extend(["gerar_frente_costas", "marcar_linha_ombro_decote_cava"])
    if categoria_input == "calca":
        operacoes.extend(["gerar_frente_costas_calca", "marcar_gancho_joelho_barra"])
    if categoria_input == "saia":
        operacoes.extend(["gerar_frente_costas_saia", "marcar_cintura_quadril_barra"])

    if "gola_camp" in componentes:
        operacoes.extend(["abrir_decote_frente_para_gola_camp", "desenhar_gola_sem_pe_rigido"])
    if "gola_colarinho" in componentes:
        operacoes.extend(["desenhar_gola_e_pe_de_gola", "casar_gola_com_perimetro_decote"])
    if "pe_de_gola" in componentes:
        operacoes.append("desenhar_pe_de_gola_com_piques")
    if any(component.startswith("manga_") for component in componentes):
        operacoes.extend(["desenhar_manga_a_partir_da_cava", "casar_cabeca_da_manga_com_cava"])
    if "manga_curta" in componentes:
        operacoes.append("encurtar_manga_preservando_cabeca")
    if "manga_bufante" in componentes:
        operacoes.append("abrir_manga_para_volume_e_franzido")
    if "punho" in componentes:
        operacoes.append("adicionar_punho_e_pregas_de_manga")
    if "carcela" in componentes:
        operacoes.append("adicionar_abertura_de_carcela_com_reforco")
    if "vista_abertura" in componentes:
        operacoes.append("adicionar_vista_transpasse_e_marcacao_de_botoes")
    if "bolso_faca" in componentes:
        operacoes.append("adicionar_recorte_de_bolso_faca_espelho_e_saco")
    if "bolso_cargo" in componentes:
        operacoes.append("adicionar_painel_de_bolso_externo_com_reforco")
    if "cos" in componentes:
        operacoes.append("desenhar_cos_e_definir_transpasse_ou_elastico")
    if "ziper" in componentes:
        operacoes.append("reservar_margem_para_ziper_e_braguilha_ou_abertura")
    if "pence" in componentes:
        operacoes.append("distribuir_intake_de_pence_por_regiao")
    if "recorte_princesa" in componentes:
        operacoes.append("converter_pence_em_recorte_princesa")
    if "lapela" in componentes:
        operacoes.append("desenhar_quebra_de_lapela_revel_e_gola")

    return _dedupe(operacoes)


def _validation_gates(
    categoria_input: str | None,
    componentes: tuple[str, ...],
    precisa_base_composta: bool,
) -> tuple[str, ...]:
    validacoes = [
        "separar_medida_corporal_folga_e_medida_final",
        "declarar_linha_de_fio_por_parte",
        "declarar_margem_costura_por_operacao",
        "marcar_piques_dobras_e_pontos_de_controle",
    ]
    if precisa_base_composta:
        validacoes.extend([
            "validar_comprimento_torso_antes_do_corte",
            "validar_gancho_em_pe_e_sentado",
        ])
    if categoria_input == "calca":
        validacoes.append("validar_gancho_entreperna_joelho_e_barra")
    if categoria_input in {"camisa", "blusa", "casaco", "vestido"}:
        validacoes.append("validar_ombro_cava_e_linha_de_busto")
    if any(component.startswith("manga_") for component in componentes):
        validacoes.append("validar_compatibilidade_manga_cava")
    if any(component.startswith("gola_") or component == "pe_de_gola" for component in componentes):
        validacoes.append("validar_compatibilidade_gola_decote")
    if "bolso_faca" in componentes or "bolso_cargo" in componentes:
        validacoes.append("validar_abertura_volume_e_ordem_de_montagem_do_bolso")
    if "ziper" in componentes or "vista_abertura" in componentes:
        validacoes.append("validar_transpasse_fechamento_e_ordem_de_montagem")
    return _dedupe(validacoes)


def resolve_semantic_profile(query: str | None) -> SemanticProfile:
    normalized = normalize_text(query)
    tokens = _tokenize(normalized)
    motivos: list[str] = []
    alertas: list[str] = []

    categoria_input = None
    categorias_referencia: tuple[str, ...] = ()
    precisa_base_composta = False

    if _contains_any(normalized, ("macacao", "jumpsuit", "playsuit")):
        categoria_input = "macacao"
        categorias_referencia = ("vestido", "calca", "blusa", "camisa")
        precisa_base_composta = True
        motivos.append("macacao_detectado_como_peca_corpo_inteiro")
        alertas.append("macacao_exige_conferencia_de_torso_gancho_e_prova_sentada")
    elif _contains_any(normalized, ("calca", "pants", "trouser", "pantalona", "legging", "bermuda", "short")):
        categoria_input = "calca"
        categorias_referencia = ("calca",)
    elif _contains_any(normalized, ("vestido", "dress")):
        categoria_input = "vestido"
        categorias_referencia = ("vestido",)
    elif _contains_any(normalized, ("saia", "skirt")):
        categoria_input = "saia"
        categorias_referencia = ("saia",)
    elif _contains_any(normalized, ("camisa", "blusa", "top", "shirt", "blouse")):
        categoria_input = "camisa"
        categorias_referencia = ("camisa", "blusa")
    elif _contains_any(normalized, ("blazer", "casaco", "jaqueta", "sobretudo", "coat", "jacket")):
        categoria_input = "casaco"
        categorias_referencia = ("casaco",)

    grau_ajuste = None
    ajustes_alternativos: tuple[str, ...] = ()
    if _contains_any(normalized, ("muito folgado", "oversized", "maxi", "amplo demais")):
        grau_ajuste = "oversized"
        ajustes_alternativos = ("relaxed",)
        motivos.append("folga_alta_detectada")
    elif _contains_any(normalized, ("folgado", "folga", "solto", "solta", "amplo", "ampla", "relaxed")):
        grau_ajuste = "relaxed"
        ajustes_alternativos = ("oversized", "semi")
        motivos.append("folga_relaxed_detectada")
    elif _contains_any(normalized, ("ajustado", "justo", "slim", "fitted")):
        grau_ajuste = "fitted"
        ajustes_alternativos = ("semi",)
    elif _contains_any(normalized, ("semi", "regular", "normal")):
        grau_ajuste = "semi"
        ajustes_alternativos = ("relaxed",)

    linguagem_construcao = None
    tipo_tecido = None
    if _contains_any(normalized, ("alfaiataria", "alfaitaria", "alfaiatado", "social", "formal", "tailored", "tailoring")):
        linguagem_construcao = "alfaiataria"
        tipo_tecido = "plano"
        motivos.append("linguagem_de_alfaiataria_prefere_tecido_plano")
    elif _contains_any(normalized, ("malha", "jersey", "ribana", "moleton", "moletom")):
        tipo_tecido = "malha"
    elif _contains_any(normalized, ("plano", "crepe", "linho", "gabardine", "sarja", "tricoline")):
        tipo_tecido = "plano"

    componentes = _detect_components(normalized, tokens)
    operacoes = _geometry_operations(categoria_input, componentes, precisa_base_composta)
    validacoes = _validation_gates(categoria_input, componentes, precisa_base_composta)

    return SemanticProfile(
        raw=str(query or ""),
        normalized=normalized,
        tokens=tokens,
        categoria_input=categoria_input,
        categorias_referencia=categorias_referencia,
        grau_ajuste=grau_ajuste,
        ajustes_alternativos=ajustes_alternativos,
        tipo_tecido=tipo_tecido,
        linguagem_construcao=linguagem_construcao,
        precisa_base_composta=precisa_base_composta,
        componentes_detectados=componentes,
        operacoes_geometricas=operacoes,
        validacoes_obrigatorias=validacoes,
        motivos=tuple(motivos),
        alertas=tuple(alertas),
    )


def required_measurements(profile: SemanticProfile) -> tuple[str, ...]:
    medidas: list[str] = []
    categoria = profile.categoria_input

    if categoria == "macacao":
        medidas.extend([
            "busto", "cintura", "quadril", "ombro", "largura_costas",
            "cava", "comprimento_torso", "gancho", "entreperna", "joelho", "barra",
        ])
    elif categoria == "calca":
        medidas.extend(["cintura", "quadril", "gancho", "entreperna", "coxa", "joelho", "barra"])
    elif categoria == "saia":
        medidas.extend(["cintura", "quadril", "comprimento_saia", "barra"])
    elif categoria in {"camisa", "blusa", "casaco"}:
        medidas.extend(["busto", "cintura", "quadril", "ombro", "largura_costas", "cava", "comprimento_corpo"])
    elif categoria == "vestido":
        medidas.extend(["busto", "cintura", "quadril", "ombro", "cava", "comprimento_total"])

    if any(component.startswith("manga_") for component in profile.componentes_detectados):
        medidas.extend(["comprimento_manga", "largura_braco", "boca_manga"])
    if "punho" in profile.componentes_detectados:
        medidas.append("punho")
    if "gola_camp" in profile.componentes_detectados or "gola_colarinho" in profile.componentes_detectados:
        medidas.extend(["contorno_decote", "largura_pescoco"])
    if "cos" in profile.componentes_detectados:
        medidas.append("altura_cos")

    return _dedupe(medidas)


def build_molde_intent_spec(query: str | None) -> dict:
    profile = resolve_semantic_profile(query)
    return {
        "versao": "text_to_molde_v0",
        "status": "prototipo_tecnico_nao_molde_final",
        "input": profile.raw,
        "perfil": profile.as_dict(),
        "medidas_obrigatorias": list(required_measurements(profile)),
        "componentes": list(profile.componentes_detectados),
        "operacoes_geometricas": list(profile.operacoes_geometricas),
        "validacoes_obrigatorias": list(profile.validacoes_obrigatorias),
        "limites": [
            "nao_substitui_modelista_prova_fisica_ou_piloto",
            "nao_gera_molde_1_1_sem_medidas_completas",
            "toda_geometria_deve_declarar_folga_linha_de_fio_margem_e_piques",
        ],
    }


def _variation_text(variation: object) -> str:
    base = getattr(variation, "molde_base", None)
    fields = [
        getattr(variation, "codigo", None),
        getattr(variation, "descricao_natural", None),
        getattr(variation, "tags", None),
        getattr(variation, "grau_ajuste", None),
        getattr(variation, "tipo_tecido", None),
        getattr(variation, "comprimento", None),
        getattr(variation, "decote", None),
        getattr(variation, "manga", None),
        getattr(variation, "fechamento", None),
        getattr(variation, "cos", None),
        getattr(base, "codigo", None),
        getattr(base, "nome", None),
        getattr(base, "categoria", None),
        getattr(base, "subcategoria", None),
        getattr(base, "descricao", None),
        getattr(base, "notas_construcao", None),
    ]
    return normalize_text(" ".join(str(field) for field in fields if field))


def _reference_role(profile: SemanticProfile, category: str | None) -> str:
    if profile.categoria_input != "macacao":
        return "referencia_primaria"
    if category == "vestido":
        return "tronco_corpo_inteiro"
    if category == "calca":
        return "perna_gancho"
    if category in {"blusa", "camisa"}:
        return "tronco_superior"
    return "apoio"


def score_variation(variation: object, profile: SemanticProfile) -> RankedVariation:
    base = getattr(variation, "molde_base", None)
    category = normalize_text(getattr(base, "categoria", None)) or None
    subcategory = normalize_text(getattr(base, "subcategoria", None))
    text = _variation_text(variation)
    score = 0.0
    motivos: list[str] = []

    if profile.categoria_input == "macacao":
        if category == "vestido":
            score += 34
            motivos.append("usa_vestido_para_referencia_de_torso_cintura_quadril")
        elif category == "calca":
            score += 31
            motivos.append("usa_calca_para_referencia_de_perna_gancho_e_entreperna")
        elif category in {"blusa", "camisa"}:
            score += 18
            motivos.append("apoia_medidas_de_tronco_superior")
        else:
            score -= 12
    elif profile.categorias_referencia:
        if category in profile.categorias_referencia:
            score += 34
            motivos.append("categoria_compativel")
        else:
            score -= 16

    if profile.grau_ajuste:
        fit = normalize_text(getattr(variation, "grau_ajuste", None))
        if fit == profile.grau_ajuste:
            score += 24
            motivos.append(f"ajuste_{fit}")
        elif fit in profile.ajustes_alternativos:
            score += 13
            motivos.append(f"ajuste_alternativo_{fit}")
        elif profile.grau_ajuste in {"relaxed", "oversized"} and fit == "fitted":
            score -= 12

    if profile.tipo_tecido:
        fabric = normalize_text(getattr(variation, "tipo_tecido", None))
        if fabric == profile.tipo_tecido:
            score += 16
            motivos.append(f"tecido_{fabric}")
        elif profile.tipo_tecido == "plano" and fabric == "malha":
            score -= 9

    if profile.linguagem_construcao == "alfaiataria":
        alfaiataria_terms = (
            "alfaiataria", "alfaiatado", "social", "executivo", "formal",
            "blazer", "terno", "pregas", "chemisier", "pantalona", "tailored",
        )
        if _contains_any(text, alfaiataria_terms):
            score += 22
            motivos.append("linguagem_alfaiataria_encontrada")
        elif category in {"calca", "camisa", "casaco", "vestido"} and subcategory in {
            "social", "social_masc", "social_masc_pregas", "pences", "chemisier",
            "pregas", "pantalona", "blazer", "tubo_pences", "tubo_recortes",
        }:
            score += 18
            motivos.append("subcategoria_proxima_de_alfaiataria")

    token_hits = 0
    for token in profile.tokens:
        if token in text:
            token_hits += 1
    if token_hits:
        score += min(token_hits, 8) * 2.5
        motivos.append(f"{token_hits}_termos_do_usuario_encontrados")

    return RankedVariation(
        variacao=variation,
        score=round(score, 2),
        motivos=tuple(motivos),
        papel_referencia=_reference_role(profile, category),
    )


def rank_variations(query: str | None, variations: list[object], limit: int = 12) -> tuple[SemanticProfile, list[RankedVariation]]:
    profile = resolve_semantic_profile(query)
    ranked = [score_variation(variation, profile) for variation in variations]
    ranked.sort(key=lambda item: item.score, reverse=True)
    return profile, ranked[:limit]


def select_representative_recommendations(
    profile: SemanticProfile,
    ranked: list[RankedVariation],
    limit: int = 12,
) -> list[RankedVariation]:
    if not profile.precisa_base_composta:
        return ranked[:limit]

    selected: list[RankedVariation] = []
    used_keys: set[tuple] = set()

    def key_for(item: RankedVariation) -> tuple:
        base = getattr(item.variacao, "molde_base", None)
        return (
            item.papel_referencia,
            getattr(base, "codigo", None),
            getattr(item.variacao, "grau_ajuste", None),
            getattr(item.variacao, "tipo_tecido", None),
        )

    def add(item: RankedVariation) -> None:
        key = key_for(item)
        if key not in used_keys and len(selected) < limit:
            selected.append(item)
            used_keys.add(key)

    for role in ("tronco_corpo_inteiro", "perna_gancho", "tronco_superior"):
        candidate = next((item for item in ranked if item.papel_referencia == role and item.score > -10), None)
        if candidate:
            add(candidate)

    for item in ranked:
        if item.score <= -10 or len(selected) >= limit:
            break
        add(item)

    return selected


def measurement_strategy(profile: SemanticProfile) -> dict:
    if profile.categoria_input == "macacao":
        return {
            "tipo": "base_composta",
            "descricao": (
                "Macacao ainda nao deve depender de um unico molde quando a biblioteca SQL "
                "nao tiver base propria validada. Use referencia de vestido/blusa para torso "
                "e referencia de calca para perna, gancho e entreperna."
            ),
            "mapa_medidas": {
                "tronco": ["busto", "ombro", "costas", "cava", "comprimento_total"],
                "cintura_quadril": ["cintura", "quadril"],
                "perna": ["gancho", "entreperna", "joelho", "tornozelo"],
            },
            "pontos_criticos": [
                "validar gancho em pe e sentado",
                "conferir comprimento de torso antes de usar a medida final",
                "se a proposta for folgada, nao usar variacao fitted como referencia primaria",
            ],
        }

    return {
        "tipo": "base_unica",
        "descricao": "Usar a variacao mais bem pontuada como referencia inicial de medidas.",
        "mapa_medidas": {},
        "pontos_criticos": [],
    }
