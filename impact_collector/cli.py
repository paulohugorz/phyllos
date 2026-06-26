"""
CLI do Impact Collector — execução via linha de comando.

Uso:
    python -m impact_collector.cli
    python -m impact_collector.cli --fibers lyocell_tencel linho
    python -m impact_collector.cli --sources epd lca_commons --dry-run
    python -m impact_collector.cli --report
"""

from __future__ import annotations
import argparse
import json
import sys
import os


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PHYLLOS Impact Collector — coleta de dados de impacto de matérias-primas têxteis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Coletar todas as fibras prioritárias (sem LLM)
  python -m impact_collector.cli --sources epd lca_commons

  # Coletar lyocell com LLM (requer ANTHROPIC_API_KEY)
  python -m impact_collector.cli --fibers lyocell_tencel --sources epd openalex

  # Ver relatório das evidências já coletadas
  python -m impact_collector.cli --report

  # Dry run (não salva)
  python -m impact_collector.cli --dry-run
        """,
    )

    parser.add_argument(
        "--fibers",
        nargs="+",
        metavar="FIBRA_ID",
        help="Fibras a coletar. Padrão: todas as prioritárias.",
    )
    parser.add_argument(
        "--sources",
        nargs="+",
        choices=["openalex", "epd", "lca_commons"],
        default=["epd", "lca_commons"],
        help="Fontes a usar. Padrão: epd lca_commons (sem LLM).",
    )
    parser.add_argument(
        "--max-articles",
        type=int,
        default=10,
        help="Máximo de artigos por fibra no OpenAlex. Padrão: 10.",
    )
    parser.add_argument(
        "--output",
        default="produto/catalogo-impacto/evidencias-coletadas.jsonl",
        help="Caminho do arquivo de saída JSONL.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Executar sem salvar resultados.",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Exibir relatório das evidências já coletadas e sair.",
    )
    parser.add_argument(
        "--list-fibers",
        action="store_true",
        help="Listar fibras disponíveis e sair.",
    )

    args = parser.parse_args()

    # Relatório de evidências existentes
    if args.report:
        from impact_collector.loaders.json_loader import generate_summary_report
        report = generate_summary_report(args.output)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return

    # Listar fibras
    if args.list_fibers:
        from impact_collector.config import PRIORITY_FIBERS, FIBER_SEARCH_TERMS
        print("Fibras prioritárias do Sprint 1:")
        for fid in PRIORITY_FIBERS:
            terms = FIBER_SEARCH_TERMS.get(fid, [])
            print(f"  {fid} ({len(terms)} termos de busca)")
        return

    # Verificar API key se OpenAlex com LLM
    if "openalex" in args.sources:
        if not os.getenv("ANTHROPIC_API_KEY"):
            print(
                "AVISO: ANTHROPIC_API_KEY não configurada.\n"
                "A coleta via OpenAlex vai encontrar artigos mas não vai extrair dados numéricos.\n"
                "Configure: export ANTHROPIC_API_KEY=sk-ant-...\n"
                "Ou use --sources epd lca_commons para coletar sem LLM.\n",
                file=sys.stderr,
            )

    from impact_collector.flows.main_flow import collect_material_impact

    evidences = collect_material_impact(
        fibers=args.fibers,
        sources=args.sources,
        max_articles=args.max_articles,
        output_path=args.output,
        dry_run=args.dry_run,
    )

    if args.dry_run:
        print(f"\nDry run: {len(evidences)} evidências encontradas (não salvas).")
        for ev in evidences[:5]:
            print(f"  {ev.fibra_id}: CO2={ev.co2eq_kg_por_kg} | confiança={ev.confianca}")
        if len(evidences) > 5:
            print(f"  ... e mais {len(evidences) - 5}")


if __name__ == "__main__":
    main()
