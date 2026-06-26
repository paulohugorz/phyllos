"""Coletor OpenAlex — 250M artigos, API pública sem chave."""

from __future__ import annotations
import time
import urllib.request
import urllib.parse
import json
import logging
from impact_collector.config import CONTACT_EMAIL, OPENALEX_RATE_LIMIT, FIBER_SEARCH_TERMS
from impact_collector.models import ImpactSource

logger = logging.getLogger(__name__)

BASE_URL = "https://api.openalex.org/works"


def _get(url: str) -> dict:
    """HTTP GET simples com identificação no User-Agent (boa prática OpenAlex)."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"PHYLLOS-ImpactCollector/1.0 (mailto:{CONTACT_EMAIL})",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def search_lca_articles(
    fibra_id: str,
    max_results: int = 20,
    open_access_only: bool = True,
) -> list[ImpactSource]:
    """
    Busca artigos de LCA para uma fibra via OpenAlex.

    Retorna apenas artigos com PDF disponível quando open_access_only=True.
    """
    terms = FIBER_SEARCH_TERMS.get(fibra_id, [])
    if not terms:
        logger.warning("Nenhum termo de busca para fibra: %s", fibra_id)
        return []

    sources: list[ImpactSource] = []
    seen_dois: set[str] = set()
    per_page = min(max_results, 25)

    for term in terms:
        if len(sources) >= max_results:
            break

        base_filter = "open_access.is_oa:true" if open_access_only else ""
        params: dict[str, str] = {
            "search": term,
            "per-page": str(per_page),
            "select": "id,doi,title,publication_year,primary_location,open_access,authorships,best_oa_location",
            "mailto": CONTACT_EMAIL,
        }
        if base_filter:
            params["filter"] = base_filter

        url = BASE_URL + "?" + urllib.parse.urlencode(params)
        logger.info("OpenAlex query: %s", term)

        try:
            data = _get(url)
        except Exception as exc:
            logger.error("OpenAlex erro na busca '%s': %s", term, exc)
            time.sleep(2)
            continue

        for work in data.get("results", []):
            doi = work.get("doi")
            if doi and doi in seen_dois:
                continue
            if doi:
                seen_dois.add(doi)

            pdf_url = _extract_pdf_url(work)
            source = ImpactSource(
                tipo="api",
                nome="OpenAlex",
                url=pdf_url or work.get("id"),
                doi=doi,
                titulo=work.get("title"),
                autores=_extract_authors(work),
                ano_publicacao=work.get("publication_year"),
                journal=_extract_journal(work),
                acesso_aberto=work.get("open_access", {}).get("is_oa", False),
                licenca=work.get("open_access", {}).get("oa_url"),
            )
            sources.append(source)

            if len(sources) >= max_results:
                break

        time.sleep(1 / OPENALEX_RATE_LIMIT)

    logger.info("OpenAlex: %d fontes encontradas para %s", len(sources), fibra_id)
    return sources


def _extract_pdf_url(work: dict) -> str | None:
    """Tenta extrair URL de PDF acessível do registro OpenAlex."""
    best = work.get("best_oa_location") or {}
    if best.get("pdf_url"):
        return best["pdf_url"]
    primary = work.get("primary_location") or {}
    return primary.get("pdf_url")


def _extract_authors(work: dict) -> list[str]:
    authors = []
    for authorship in work.get("authorships", [])[:5]:
        name = authorship.get("author", {}).get("display_name")
        if name:
            authors.append(name)
    return authors


def _extract_journal(work: dict) -> str | None:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    return source.get("display_name")
