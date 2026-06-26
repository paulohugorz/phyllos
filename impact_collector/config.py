"""Configuração central do pipeline — carrega de variáveis de ambiente."""

from __future__ import annotations
import os

# Claude API para extração estruturada
ANTHROPIC_API_KEY: str | None = os.getenv("ANTHROPIC_API_KEY")
EXTRACTION_MODEL = os.getenv("IMPACT_EXTRACTION_MODEL", "claude-haiku-4-5-20251001")

# Rate limits (req/seg)
OPENALEX_RATE_LIMIT = 10  # sem autenticação; 100 com mailto
SEMANTIC_SCHOLAR_RATE_LIMIT = 1  # conservador sem API key
LCA_COMMONS_RATE_LIMIT = 5

# Email para APIs que pedem identificação (OpenAlex, Unpaywall)
CONTACT_EMAIL = os.getenv("PHYLLOS_CONTACT_EMAIL", "paulohugorz@gmail.com")

# Diretório de cache local de PDFs
PDF_CACHE_DIR = os.getenv("IMPACT_PDF_CACHE_DIR", "/tmp/phyllos_impact_pdfs")

# Limite de artigos por coleta (ajustável para testes)
MAX_ARTICLES_PER_FIBER = int(os.getenv("IMPACT_MAX_ARTICLES", "20"))

# Fibras prioritárias Sprint 1
PRIORITY_FIBERS = [
    "algodao_convencional",
    "algodao_organico",
    "poliester_reciclado",
    "lyocell_tencel",
    "linho",
    "la",
]

# Termos de busca por fibra (inglês para APIs internacionais)
FIBER_SEARCH_TERMS: dict[str, list[str]] = {
    "algodao_convencional": [
        "life cycle assessment cotton",
        "LCA conventional cotton environmental impact",
        "cotton fiber carbon footprint",
        "environmental impact cotton production",
    ],
    "algodao_organico": [
        "life cycle assessment organic cotton",
        "organic cotton LCA environmental",
        "organic cotton water footprint",
    ],
    "poliester_reciclado": [
        "life cycle assessment recycled polyester",
        "rPET fiber LCA carbon footprint",
        "recycled PET textile environmental impact",
    ],
    "lyocell_tencel": [
        "life cycle assessment lyocell",
        "Tencel lyocell environmental impact LCA",
        "lyocell fiber carbon water footprint",
        "MMCF man-made cellulosic fiber LCA",
    ],
    "linho": [
        "life cycle assessment flax linen fiber",
        "linen flax LCA environmental impact",
        "flax fiber water footprint carbon",
    ],
    "la": [
        "life cycle assessment wool fiber",
        "wool LCA GWP carbon footprint",
        "merino wool environmental impact",
    ],
}

# Aliases de normalização de nomes de fibras
FIBER_ALIASES: dict[str, list[str]] = {
    "algodao_convencional": [
        "conventional cotton", "cotton fiber", "cotton fibre",
        "algodao convencional", "cotton (conventional)", "upland cotton",
    ],
    "algodao_organico": [
        "organic cotton", "GOTS cotton", "cotton (organic)",
        "algodao organico",
    ],
    "poliester_reciclado": [
        "recycled polyester", "rPET", "recycled PET", "post-consumer polyester",
        "poliester reciclado", "polyester (recycled)", "recycled poly",
    ],
    "lyocell_tencel": [
        "lyocell", "Tencel", "TENCEL", "lyocell fiber", "lyocell fibre",
        "Tencel lyocell", "lyocell (Lenzing)", "MMCF lyocell",
    ],
    "linho": [
        "flax", "linen", "flax fiber", "flax fibre", "linen fiber",
        "linho", "lin", "lin textile",
    ],
    "la": [
        "wool", "merino wool", "virgin wool", "la", "lã",
        "sheep wool", "fleece", "worsted wool",
    ],
}
