# Phyllos — Fashion OS v1

Repositório operacional da marca Phyllos. Une o sistema de agentes Claude com o Fashion OS — software para criar, produzir e lançar moda com IA.

## Fashion OS — Como rodar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs
```

## Comandos Claude

```text
/nova-colecao coleção cápsula de calças femininas confortáveis e elegantes
/criar-peca calça preta com aparência de alfaiataria e mobilidade total
/gerar-foto-produto 10 fotos editoriais com modelos diversas
```

## Fluxo operacional

Estratégia → Pesquisa Criativa → Direção de Criação → Design Técnico → Sourcing → Compras → Custo → Modelagem → Ficha Técnica → Guia de Produção → Piloto → Materiais → Ordens → Produção → Qualidade → Acabamentos → PIM → Fotos → Conteúdos → Lançamentos → Vendas → Performance

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `.claude/agents/` | 22 agentes de pipeline de moda + 52 agentes de negócio |
| `.claude/commands/` | `/nova-colecao`, `/criar-peca`, `/gerar-foto-produto` |
| `app/` | FastAPI + SQLite (coleções, peças, fichas técnicas) |
| `templates/` | Ficha técnica, ordem de produção, checklist de qualidade |
| `prompts/` | Croquis técnicos, fotografia editorial |
| `collections/` | Base inicial de peças (CSV) |
| `docs/` | Roadmap e fluxo operacional |
| `assets/` | Personas e modelos digitais |
