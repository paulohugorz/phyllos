"""
Normalização de nomes de fibras — dicionário de aliases.

Converte qualquer variação de nome de material para o fibra_id canônico do sistema PHYLLOS.
Usado pelo pipeline de extração LLM para mapear "material_identificado" para fibra_id.
"""

from __future__ import annotations
import re

# fibra_id canônico → lista de aliases (case-insensitive)
_ALIASES: dict[str, list[str]] = {
    "algodao_convencional": [
        "cotton", "conventional cotton", "cotton fiber", "cotton fibre",
        "algodão convencional", "algodao convencional", "algodão", "algodao",
        "cotton (conventional)", "upland cotton", "gossypium hirsutum",
        "cotton yarn", "cotton fabric", "cotone", "coton conventionnel",
        "baumwolle", "algodon",
    ],
    "algodao_organico": [
        "organic cotton", "cotton (organic)", "gots cotton",
        "algodão orgânico", "algodao organico", "certified organic cotton",
        "bio-baumwolle", "coton biologique", "organik pamuk",
    ],
    "poliester_virgem": [
        "polyester", "virgin polyester", "pet fiber", "pet fibre",
        "poliéster virgem", "poliester virgem", "polyethylene terephthalate",
        "pet", "virgin pet", "polyester (virgin)", "polyester yarn",
        "polyester fabric", "pef", "poliester",
    ],
    "poliester_reciclado": [
        "recycled polyester", "rpet", "recycled pet", "post-consumer polyester",
        "poliéster reciclado", "poliester reciclado", "recycled polyester fiber",
        "recycled polyester fibre", "polyester (recycled)", "recycled poly",
        "bottle-to-fiber polyester", "pcr polyester", "r-pet", "eco polyester",
    ],
    "lyocell_tencel": [
        "lyocell", "tencel", "tencel lyocell", "lyocell fiber", "lyocell fibre",
        "tencel fiber", "lyocell (lenzing)", "mmcf lyocell", "tencel™",
        "cellulosic lyocell", "man-made cellulosic fiber lyocell",
        "liocell", "lyocell fabric",
    ],
    "viscose_modal": [
        "viscose", "rayon", "modal", "viscose rayon", "modal fiber",
        "ecovero", "eco vero", "tencel modal", "lenzing modal",
        "viscose/rayon", "viscose fiber", "viscose fibre",
        "bamboo viscose", "bamboo rayon", "bamboo fiber",
        "modal (lenzing)",
    ],
    "cupro": [
        "cupro", "cupra", "cuprammonium", "bemberg", "cuprammonium rayon",
        "cupro fiber", "cupro fibre",
    ],
    "pla_biopolimero": [
        "pla", "polylactic acid", "poly lactic acid", "biopolymer pla",
        "pla fiber", "pla fibre", "corn fiber", "corn pla",
        "pla biopolimero", "biopolimero pla", "pla (corn)",
    ],
    "linho": [
        "linen", "flax", "flax fiber", "flax fibre", "linen fiber",
        "linho", "lin", "linho (flax)", "european flax",
        "lin (flax)", "flax linen", "linen fabric",
    ],
    "la": [
        "wool", "merino wool", "virgin wool", "sheep wool",
        "lã", "la", "laine", "woll", "lana",
        "merino", "fleece", "worsted wool", "worsted",
        "new wool", "raw wool", "zq merino", "responsible wool",
    ],
    "poliamida_nylon_virgem": [
        "nylon", "polyamide", "virgin nylon", "nylon 6", "nylon 6,6",
        "polyamide 6", "pa6", "pa66", "nylon fiber", "poliamida virgem",
        "nylon (virgin)", "nylon fabric",
    ],
    "poliamida_reciclada": [
        "recycled nylon", "recycled polyamide", "econyl",
        "poliamida reciclada", "nylon (recycled)",
        "recycled nylon 6", "rpas6", "r-nylon",
    ],
    "elastano_spandex": [
        "elastane", "spandex", "lycra", "elastano",
        "elastane fiber", "spandex fiber", "polyurethane fiber",
        "elasthan", "elastane/spandex", "stretch fiber",
    ],
    "canamo": [
        "hemp", "hemp fiber", "hemp fibre", "cânhamo", "canamo",
        "industrial hemp", "cannabis sativa fiber",
    ],
    "la_cashmere": [
        "cashmere", "kashmir", "cashmere wool", "kaschmirwolle",
        "cachemire", "lã cashmere",
    ],
    "seda": [
        "silk", "natural silk", "seda", "seide", "soie",
        "mulberry silk", "spider silk", "seda natural",
    ],
    "algodao_reciclado": [
        "recycled cotton", "post-consumer cotton", "cotton (recycled)",
        "algodão reciclado", "algodao reciclado", "regenerated cotton",
    ],
}

# Índice invertido: alias → fibra_id
_ALIAS_INDEX: dict[str, str] = {}
for _fid, _aliases in _ALIASES.items():
    for _alias in _aliases:
        _ALIAS_INDEX[_alias.lower().strip()] = _fid
    # O próprio fibra_id como alias
    _ALIAS_INDEX[_fid.lower().strip()] = _fid


def normalize_fiber_name(raw_name: str) -> str | None:
    """
    Converte um nome de fibra (qualquer língua) para o fibra_id canônico.

    Retorna None se nenhum alias for encontrado.

    Exemplos:
        normalize_fiber_name("Recycled PET") → "poliester_reciclado"
        normalize_fiber_name("TENCEL™ Lyocell") → "lyocell_tencel"
        normalize_fiber_name("Lã Merino") → "la"
    """
    if not raw_name:
        return None

    cleaned = raw_name.lower().strip()
    cleaned = re.sub(r"[™®©]", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # Busca exata
    if cleaned in _ALIAS_INDEX:
        return _ALIAS_INDEX[cleaned]

    # Busca por substring (nome composto que contém o alias)
    # Mínimo 4 chars para evitar falsos positivos como "la" ⊂ "pla"
    for alias, fid in _ALIAS_INDEX.items():
        if len(alias) >= 4 and (alias in cleaned or cleaned in alias):
            return fid

    return None


def get_aliases(fibra_id: str) -> list[str]:
    """Retorna todos os aliases de um fibra_id."""
    return _ALIASES.get(fibra_id, [])


def list_all_fiber_ids() -> list[str]:
    """Retorna todos os fibra_ids com aliases definidos."""
    return list(_ALIASES.keys())
