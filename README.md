# Phyllos — Motor de Moldes / Fashion OS

Repositório operacional da marca Phyllos. A premissa vigente e estreita: o MVP imediato e o **Parametric Pattern Engine** da PHYLLOS Create. O Fashion OS continua como infraestrutura tecnica e sistema de agentes, mas agora serve primeiro a um loop verificavel: parametros estruturados + medidas + tecido -> molde 2D parametrizado -> SVG/PDF A4 -> prova fisica. Linguagem natural entra depois, como camada sobre a engine validada.

## Backend — Como rodar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs
```

## Comandos Claude

```text
/gerar-molde calca reta, cintura alta, tecido plano com 3% elastano, medidas...
/nova-colecao coleção cápsula de calças femininas confortáveis e elegantes
/criar-peca calça preta com aparência de alfaiataria e mobilidade total
/gerar-foto-produto imagem de apoio para explicar a peça, se necessario
```

## Fluxo operacional

Motor de Moldes: Playbook -> Medidas -> Tecido -> Parametros -> Pattern Engine -> PatternValidator -> SVG/PDF A4 -> Prova fisica -> Feedback -> Ajuste numerico -> Beta users -> Captacao.

Fashion OS amplo: permanece como infraestrutura para colecoes, fichas, imagens, producao e comercial quando o motor estiver validado.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `.claude/agents/` | agentes de moda, produto, negocio e tecnologia alinhados ao Motor de Moldes |
| `.claude/commands/` | `/gerar-molde`, `/nova-colecao`, `/criar-peca`, `/gerar-foto-produto` |
| `app/` | FastAPI + SQLite |
| `moldes/` | interface publicada do catalogo/motor de moldes |
| `js/catalogo-moldes.js` | catalogo de moldes para a interface |
| `docs/planejamento/estrategia-motor-moldes-v1.md` | estrategia vigente do MVP |
| `docs/planejamento/risk-scope-review-mvp.md` | auditoria CTO/Product/Engenharia de Modelagem para revisar escopo |
| `templates/` | Ficha técnica, ordem de produção, checklist de qualidade |
| `prompts/` | Croquis técnicos, fotografia editorial |
| `collections/` | Base inicial de peças (CSV) |
| `docs/` | Roadmap, modelagem, estrategia e decisoes |
| `assets/` | Personas e modelos digitais |
