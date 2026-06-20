# PHYLLOS CREATE - Risk & Scope Review do MVP

**Data:** 2026-06-11
**Origem:** auditoria CTO + Product + Engenharia de Modelagem
**Status:** insumo obrigatorio para avaliacao de escopo
**Documento relacionado:** `docs/planejamento/estrategia-motor-moldes-v1.md`

## 1. Avaliacao geral

| Criterio | Nota |
|---|---:|
| Produto | 9/10 |
| Mercado | 8/10 |
| Escopo MVP | 9,5/10 |
| Engenharia | 7/10 |
| Conhecimento de modelagem | 6/10 |
| Viabilidade tecnica | 8/10 |
| Sequencia de execucao | 8,5/10 |

**Nota geral:** 8,3/10.

O discovery esta bem direcionado, mas ainda subestima riscos tecnicos. O maior acerto e entender que a PHYLLOS nao deve construir um Audaces, Optitex ou CAD industrial. O produto certo para a V1 e mais proximo de **Canva + parametros + impressao domestica**: simples para usar, mas sustentado por uma engine geometrica confiavel.

## 2. Decisao de arquitetura

O MVP nao deve ser tratado como uma unica aplicacao. A PHYLLOS Create deve ser pensada como quatro ativos:

| Ativo | Funcao | Risco se ignorado |
|---|---|---|
| PHYLLOS Playbook | Regras de modelagem, folgas, tecidos, proporcoes e compatibilidades | conhecimento fica implicito e impossivel de escalar |
| PHYLLOS Engine | Motor parametrico, regras geometricas, SVG, PDF, DXF e validadores | interface bonita gera moldes incorretos |
| PHYLLOS Library | Moldes-base, componentes, metadados, versoes e compatibilidades | catalogo pequeno demais para virar ativo defensavel |
| PHYLLOS SaaS | Interface para usuario final | frontend nasce antes da logica e exige refatoracao |

Sequencia recomendada:

```text
Playbook -> Engine -> Library -> SaaS
```

## 3. Principio tecnico central

O produto nao deve manipular desenhos. Deve manipular parametros.

Exemplo:

```json
{
  "base": "saia_reta",
  "cintura_corpo": 76,
  "quadril_corpo": 104,
  "folga_quadril": 4,
  "comprimento": 62,
  "tecido": "plano_medio",
  "elasticidade": 0
}
```

O SVG, o PDF e o DXF sao consequencias desses parametros. O ativo real e a combinacao de parametros, regras e conhecimento de modelagem.

## 4. Mudancas recomendadas no escopo

### 4.1 Linguagem natural sai da V1

Linguagem natural e valiosa, mas e falsa prioridade para o MVP. O pedido "aumentar quadril 4 cm" pode significar aumentar lateral, gancho, entreperna, joelho ou redistribuir cintura. Sem engine geometrica e playbook, a IA tende a produzir molde bonito e incorreto.

**Decisao:** V1 deve usar formulario estruturado e parametros. Linguagem natural entra em V2/V3 como camada sobre a engine.

### 4.2 Calca nao deve ser a primeira peca

Calca envolve gancho, quadril, joelho, entreperna e equilibrio frente/costas. E uma das pecas mais dificeis da modelagem.

Nova ordem recomendada:

1. Saia reta.
2. Blusa basica.
3. Camiseta.
4. Vestido simples.
5. Calca reta.

### 4.3 Preview em tempo real sai da V1

Preview dinamico custa caro e agrega pouco antes da engine estar correta.

V1:

```text
Ajustar parametros -> Gerar SVG estatico -> Conferir -> Regenerar
```

V2:

```text
Preview dinamico / atualizacao em tempo real
```

### 4.4 PDF A4 nao e detalhe

PDF A4 com impressao domestica exige tesselation, margens, overlap, alinhamento, marcas de montagem e tolerancia a impressoras diferentes. Isso deve ser tratado como feature tecnica propria, com testes automatizados.

## 5. Vulnerabilidades e sugestoes

| # | Vulnerabilidade | Consequencia | Sugestao |
|---:|---|---|---|
| 1 | V1 tratada como aplicacao unica | refatoracao futura grande | separar Playbook, Engine, Library e SaaS |
| 2 | Linguagem natural cedo demais | molde plausivel mas incorreto | mover IA para V2/V3 |
| 3 | Conhecimento de modelagem implicito | motor inconsistente | criar `playbook.db` com regras, folgas e compatibilidades |
| 4 | Propagacao independente de medidas | alteracoes quebram outras partes | criar `dependency_graph` |
| 5 | Auto-intersecoes | SVG invalido ou spline invertida | criar validador geometrico |
| 6 | Componentes incompatíveis | costura impossivel | criar `compatibility_matrix` |
| 7 | Falta de versionamento | producao usa molde errado | versionar base, parametros e saida gerada |
| 8 | Biblioteca pequena | baixa defensabilidade | mirar biblioteca modular ampla, com componentes e metadados |
| 9 | Ausencia de modularizacao | explosao combinatoria | separar frente, costas, cos, bolso, manga, gola, punho etc. |
| 10 | Calca como primeira peca | complexidade alta cedo demais | iniciar por saia reta |
| 11 | Preview em tempo real | meses de engenharia precoce | gerar SVG estatico sob demanda |
| 12 | PDF A4 subestimado | impressao desalinhada | criar suite automatica de testes de paginacao |
| 13 | Medida corporal confundida com medida do molde | peca apertada ou larga | separar medida do corpo, folga e medida final do molde |
| 14 | Tecido pouco considerado | mesmo molde cai diferente | parametrizar tecido, elasticidade e gramatura |
| 15 | Consumo de tecido ausente | molde valido mas inviavel | criar estimador simples de encaixe/consumo |
| 16 | Grading aparecera cedo | usuarios pedem P/M/G/GG | preparar arquitetura para grade, mesmo sem expor na V1 |
| 17 | SVG tratado como produto | foco em desenho, nao em regra | tratar SVG como output derivado dos parametros |
| 18 | Falta de `PatternValidator` | evolucao quebra moldes | validar curvas, comprimentos, encaixes e limites |
| 19 | Ausencia de testes geometricos | regressao caotica | unit tests, golden patterns, visual diff e geometric tests |
| 20 | Risco de virar mini Audaces | produto pesado e lento | manter tese Canva da modelagem |

## 6. Epicos recomendados

| Epico | Nome | Objetivo |
|---|---|---|
| EPIC 0 | PHYLLOS Playbook | Codificar conhecimento de modelagem em regras, folgas, proporcoes e compatibilidades |
| EPIC 1 | Pattern Engine | Gerar molde parametrico a partir de medidas, tecido e base |
| EPIC 2 | Pattern Validator | Detectar intersecoes, encaixes impossiveis, limites e inconsistencias |
| EPIC 3 | Pattern Library | Organizar bases, componentes, metadados, tags e versoes |
| EPIC 4 | SVG/PDF Generator | Gerar SVG e PDF A4 imprimivel com marcas de montagem |
| EPIC 5 | Web SaaS | Interface simples para escolher base, preencher parametros e baixar saidas |
| EPIC 6 | Natural Language Layer | Converter linguagem natural em parametros estruturados |
| EPIC 7 | AI Composer | Combinar bases e componentes a partir de pedido textual |

## 7. Roadmap revisado

| Mes | Foco | Entrega |
|---:|---|---|
| 1 | Motor geometrico + SQLite + SVG | Saia reta parametrica com SVG estatico |
| 2 | Blusa basica + PDF A4 | gerador de PDF com tesselation e testes |
| 3 | Calca reta + validadores | 5 costureiras/modelistas validando saidas |
| 4 | Biblioteca modular | bases e componentes com compatibilidade |
| 5 | Historico, projetos e usuarios | versionamento e persistencia de trabalhos |
| 6 | Linguagem natural | camada textual sobre parametros ja confiaveis |

## 8. Vulnerabilidade mais critica

O discovery ainda assume que o problema e desenhar moldes. O verdadeiro problema e **codificar conhecimento de modelagem em regras matematicas confiaveis**.

Essa camada invisivel - PHYLLOS Playbook + PHYLLOS Engine - provavelmente representa mais de 80% do valor e da dificuldade tecnica da empresa.
