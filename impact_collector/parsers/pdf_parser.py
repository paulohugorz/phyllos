"""
Parser de PDF para extração de texto de artigos LCA.

Estratégia em camadas:
1. Detectar páginas/seções com dados numéricos (regex em LCA keywords)
2. Extrair apenas os chunks relevantes (reduz tokens LLM em 80-90%)
3. Retornar texto limpo por página
"""

from __future__ import annotations
import re
import logging
import os
import urllib.request

logger = logging.getLogger(__name__)

# Palavras-chave que indicam presença de dados de impacto numéricos
LCA_DATA_PATTERNS = [
    r"\d+[\.,]\d+\s*kg\s*CO2",
    r"GWP\s*[=:]\s*\d",
    r"global\s*warming\s*potential",
    r"carbon\s*footprint",
    r"water\s*(footprint|consumption|use)\s*[=:]\s*\d",
    r"\d+[\.,]\d+\s*[Ll]\/kg",
    r"energy\s*(consumption|use)\s*[=:]\s*\d",
    r"\d+[\.,]\d+\s*MJ\/kg",
    r"kgCO2.?eq",
    r"climate\s*change.*?\d+",
    r"Table\s+\d+.*?(impact|result|LCA|ACV)",
    r"cradle.to.(gate|grave)",
]

LCA_PATTERN_COMPILED = re.compile(
    "|".join(f"(?:{p})" for p in LCA_DATA_PATTERNS),
    re.IGNORECASE | re.DOTALL,
)


def download_pdf(url: str, cache_dir: str) -> str | None:
    """
    Baixa PDF de uma URL e salva em cache_dir.
    Retorna caminho local ou None se falhar.
    """
    os.makedirs(cache_dir, exist_ok=True)

    # Nome do arquivo baseado no hash da URL
    filename = re.sub(r"[^a-zA-Z0-9]", "_", url[-60:]) + ".pdf"
    filepath = os.path.join(cache_dir, filename)

    if os.path.exists(filepath):
        logger.debug("PDF em cache: %s", filepath)
        return filepath

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "PHYLLOS-ImpactCollector/1.0",
                "Accept": "application/pdf,*/*",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "pdf" not in content_type.lower() and not url.endswith(".pdf"):
                logger.warning("URL não retornou PDF: %s (Content-Type: %s)", url, content_type)
                return None
            with open(filepath, "wb") as f:
                f.write(resp.read())
        logger.info("PDF baixado: %s → %s", url, filepath)
        return filepath
    except Exception as exc:
        logger.warning("Falha ao baixar PDF %s: %s", url, exc)
        return None


def extract_relevant_chunks(pdf_path: str, max_pages: int = 30) -> list[dict]:
    """
    Extrai chunks de texto relevantes de um PDF.

    Retorna lista de dicts com:
        page: int
        text: str
        has_lca_data: bool
        snippet: str (primeiros 200 chars para preview)
    """
    try:
        import fitz  # PyMuPDF
    except ImportError:
        logger.error("PyMuPDF não instalado. Execute: pip install pymupdf")
        return []

    chunks = []
    try:
        doc = fitz.open(pdf_path)
        n_pages = min(len(doc), max_pages)

        for page_num in range(n_pages):
            page = doc[page_num]
            text = page.get_text("text")

            if not text or len(text.strip()) < 50:
                continue

            has_lca = bool(LCA_PATTERN_COMPILED.search(text))
            chunks.append({
                "page": page_num + 1,
                "text": text,
                "has_lca_data": has_lca,
                "snippet": text[:200].replace("\n", " "),
                "char_count": len(text),
            })

        doc.close()
    except Exception as exc:
        logger.error("Erro ao processar PDF %s: %s", pdf_path, exc)
        return []

    lca_pages = sum(1 for c in chunks if c["has_lca_data"])
    logger.info(
        "PDF %s: %d páginas, %d com dados LCA",
        os.path.basename(pdf_path), len(chunks), lca_pages
    )
    return chunks


def get_lca_chunks(pdf_path: str) -> str:
    """
    Retorna texto concatenado apenas das páginas com dados LCA.
    Entrada direta para o extrator LLM.
    Limita a 8000 caracteres para controlar custo de tokens.
    """
    chunks = extract_relevant_chunks(pdf_path)
    relevant = [c["text"] for c in chunks if c["has_lca_data"]]

    if not relevant:
        # Sem páginas identificadas — usar abstract e conclusão (páginas 1 e última)
        all_texts = [c["text"] for c in chunks]
        relevant = all_texts[:2] + all_texts[-1:] if all_texts else []

    combined = "\n\n--- página ---\n\n".join(relevant)

    # Limite de tokens: ~8000 chars ≈ 2000 tokens — suficiente para Haiku
    if len(combined) > 8000:
        combined = combined[:8000] + "\n[... texto truncado para extração ...]"

    return combined
