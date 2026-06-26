"""
Extrator de dados de impacto via Claude Haiku.

Estratégia: chunking cirúrgico → só as seções com dados numéricos vão para o LLM.
Custo estimado: ~USD 0.003 por artigo.
"""

from __future__ import annotations
import json
import logging
import time
from impact_collector.models import ImpactEvidence, ImpactSource
from impact_collector.config import ANTHROPIC_API_KEY, EXTRACTION_MODEL

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Você é um extrator de dados de Avaliação de Ciclo de Vida (ACV/LCA) têxtil.
Extraia apenas valores numéricos de impacto ambiental que estejam EXPLICITAMENTE declarados no texto.
Regras:
- Não infira, não calcule, não interprete — só copie o que está no texto.
- Se o valor não estiver explícito, retorne null para esse campo.
- Retorne SOMENTE JSON válido, sem texto adicional antes ou depois.
- O campo confianca_extracao deve refletir a clareza do texto: "alta" para valores com unidade e metodologia declarados, "media" para valores numéricos sem toda a context, "baixa" para estimativas ou valores ambíguos."""

EXTRACTION_SCHEMA = """{
  "material_identificado": "<nome exato do material no texto, ou null>",
  "escopo_lca": "<cradle-to-gate|cradle-to-grave|gate-to-gate|outro|null>",
  "co2eq_kg_por_kg": {"valor": <float ou null>, "unidade": "<string>", "nota": "<contexto do texto>"},
  "agua_l_por_kg": {"valor": <float ou null>, "unidade": "<string>", "nota": "<contexto do texto>"},
  "energia_mj_por_kg": {"valor": <float ou null>, "unidade": "<string>", "nota": "<contexto do texto>"},
  "regiao_origem": "<pais/regiao declarado no texto, ou null>",
  "ano_referencia": <ano como inteiro, ou null>,
  "metodologia_acv": "<CML|ReCiPe|TRACI|ILCD|ISO14044|outro|null>",
  "confianca_extracao": "<alta|media|baixa>",
  "justificativa_confianca": "<frase curta explicando a confiança>",
  "trecho_com_dado": "<citação literal do trecho que contém o dado principal>"
}"""


def extract_impact_from_text(
    text: str,
    fibra_id: str,
    fibra_nome: str,
    source: ImpactSource,
) -> ImpactEvidence | None:
    """
    Usa Claude Haiku para extrair dados de impacto de um trecho de texto.

    Retorna ImpactEvidence ou None se nenhum dado encontrado.
    """
    if not ANTHROPIC_API_KEY:
        logger.error("ANTHROPIC_API_KEY não configurada. Configure a variável de ambiente.")
        return None

    if not text or len(text.strip()) < 100:
        logger.debug("Texto muito curto para extração: %d chars", len(text))
        return None

    user_prompt = f"""Texto do artigo (seções com dados de LCA):
--- INÍCIO ---
{text}
--- FIM ---

Material de interesse: {fibra_nome}
fibra_id no sistema PHYLLOS: {fibra_id}

Extraia os dados de impacto ambiental e retorne JSON no schema abaixo:
{EXTRACTION_SCHEMA}"""

    try:
        result = _call_claude_api(user_prompt)
    except Exception as exc:
        logger.error("Erro na chamada Claude API: %s", exc)
        return None

    if not result:
        return None

    return _parse_extraction_result(result, fibra_id, source)


def _call_claude_api(user_prompt: str) -> dict | None:
    """Chama a API da Anthropic e retorna o JSON extraído."""
    import urllib.request

    payload = {
        "model": EXTRACTION_MODEL,
        "max_tokens": 512,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_prompt}],
    }

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode(),
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as resp:
        response = json.loads(resp.read())

    content = response.get("content", [])
    if not content:
        return None

    text = content[0].get("text", "").strip()

    # Remover markdown code fences se presentes
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        logger.warning("JSON inválido retornado pelo LLM: %s\nTexto: %s", exc, text[:200])
        return None


def _parse_extraction_result(
    data: dict,
    fibra_id: str,
    source: ImpactSource,
) -> ImpactEvidence | None:
    """Converte JSON extraído em ImpactEvidence."""

    def _safe_float(obj: dict | None) -> float | None:
        if not obj:
            return None
        v = obj.get("valor")
        if v is None:
            return None
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    co2 = _safe_float(data.get("co2eq_kg_por_kg"))
    agua = _safe_float(data.get("agua_l_por_kg"))
    energia = _safe_float(data.get("energia_mj_por_kg"))

    if not any([co2, agua, energia]):
        logger.debug("Extração sem valores numéricos para %s", fibra_id)
        return None

    # Mapeamento de confiança LLM para enum do sistema
    confianca_map = {"alta": "alta", "media": "media", "baixa": "baixa"}
    confianca = confianca_map.get(
        str(data.get("confianca_extracao", "baixa")).lower(), "baixa"
    )

    # Validação de range mínima (Gate 1)
    if co2 and not _validate_co2_range(co2, fibra_id):
        logger.warning(
            "CO2 fora do range esperado para %s: %.2f — marcando confiança baixa",
            fibra_id, co2,
        )
        confianca = "baixa"

    escopo_raw = str(data.get("escopo_lca") or "").lower()
    escopo_map = {
        "cradle-to-gate": "cradle-to-gate",
        "cradle to gate": "cradle-to-gate",
        "cradle-to-grave": "cradle-to-grave",
        "cradle to grave": "cradle-to-grave",
        "gate-to-gate": "gate-to-gate",
        "gate to gate": "gate-to-gate",
    }
    escopo = escopo_map.get(escopo_raw)

    return ImpactEvidence(
        fibra_id=fibra_id,
        source=source,
        co2eq_kg_por_kg=co2,
        agua_l_por_kg=agua,
        energia_mj_por_kg=energia,
        escopo_lca=escopo,
        metodologia_acv=data.get("metodologia_acv"),
        regiao_origem=data.get("regiao_origem"),
        ano_referencia=data.get("ano_referencia"),
        trecho_original=data.get("trecho_com_dado"),
        confianca=confianca,
        extraction_model=EXTRACTION_MODEL,
    )


# Range esperado de CO2 por fibra (kgCO2e/kg) — usado no Gate 1
# Se o valor extraído estiver fora de 0.1x–5x o valor esperado, flaggear
_CO2_EXPECTED_RANGES: dict[str, tuple[float, float]] = {
    "algodao_convencional":  (1.0,  30.0),
    "algodao_organico":      (0.5,  20.0),
    "poliester_reciclado":   (0.5,  10.0),
    "lyocell_tencel":        (0.3,   8.0),
    "linho":                 (0.3,   8.0),
    "la":                    (5.0,  50.0),
    "poliester_virgem":      (3.0,  20.0),
    "nylon_virgem":          (5.0,  30.0),
    "viscose_modal":         (1.0,  10.0),
    "elastano_spandex":      (5.0,  40.0),
}
_DEFAULT_RANGE = (0.1, 100.0)


def _validate_co2_range(value: float, fibra_id: str) -> bool:
    low, high = _CO2_EXPECTED_RANGES.get(fibra_id, _DEFAULT_RANGE)
    return low <= value <= high
