# PHYLLOS - Premissas Historicas do Motor de Moldes

**Versao:** 1.0
**Data:** 2026-06-11
**Status:** referencia historica / modulo futuro
**Substituida no curto prazo por:** [dpp-integrado-strategic-premises.md](dpp-integrado-strategic-premises.md)
**Owner:** Founder Orchestrator

> Nota vigente em 2026-06-25: este documento registra a tese anterior de Motor de Moldes / Parametric Pattern Engine. Ele pode ser usado como base tecnica quando a tarefa envolver modelagem, fit, molde, graduacao ou integracao futura com CAD/arquivos de modelagem. Ele nao define o MVP da V1. A premissa vigente da PHYLLOS e DPP Integrado: ingestao de arquivos/especificacoes tecnicas, calculos, estados de evidencia, QR e flashcards.

Este documento orienta agentes da PHYLLOS somente quando a tarefa envolver especificamente modelagem, fichas tecnicas, molde, tecnologia futura de patternmaking ou contexto historico da tese anterior.

Ele nao prevalece sobre `dpp-integrado-strategic-premises.md`, `fashion-os-platform-specialization.md` ou o roadmap DPP vigente.

## 1. Decisao central historica

Na tese historica de 2026-06-11, o MVP imediato da PHYLLOS era o **Parametric Pattern Engine** da PHYLLOS Create.

O Fashion OS continua existindo como base tecnica e operacional mais ampla, mas deixa de ser o escopo principal de MVP. No curto prazo, ele deve servir ao Motor de Moldes: Fit Engine, Fabric Engine, Pattern Engine, banco de referencias, fichas e agentes existem para transformar **parametros estruturados** em molde 2D validavel.

O foco nao e "construir uma plataforma completa" nem interpretar qualquer frase livre do usuario. O foco e provar que uma pessoa consegue escolher uma base, informar medidas, tecido e parametros, e receber um molde tecnico cortavel, com coordenadas, curvas, margens, piques, linha de fio, sequencia operacional, SVG estatico e PDF A4. Linguagem natural entra depois, como camada sobre uma engine parametrica confiavel.

## 1.1 Arquitetura de produto

A PHYLLOS Create deve ser pensada como quatro ativos, nessa ordem:

1. **PHYLLOS Playbook:** regras de modelagem, folgas, proporcoes, tecidos, compatibilidades e criterios de prova.
2. **PHYLLOS Engine:** motor geometrico parametrico, validadores, SVG, PDF, DXF e testes.
3. **PHYLLOS Library:** bases, componentes, metadados, versionamento e matriz de compatibilidade.
4. **PHYLLOS SaaS:** interface simples para escolher base, preencher parametros e baixar saidas.

Sequencia de construcao:

```text
Playbook -> Engine -> Library -> SaaS
```

## 2. Produto

Categoria: **patternmaking engine**.

Promessa operacional:

> Da descricao ao molde. Sem software de CAD.

O motor recebe:

- formulario estruturado na V1; linguagem natural apenas em fase posterior;
- medidas corporais;
- tecido, elasticidade e caimento;
- tipo de peca e detalhes construtivos;
- preferencias de fit, folga e mobilidade.

O motor entrega:

- molde 2D parametrizado;
- coordenadas e curvas calculadas;
- margens de costura;
- piques e linha de fio;
- medidas finais por regiao;
- logica 3D -> 2D explicada;
- sequencia operacional;
- SVG para visualizacao;
- PDF A4 para impressao domestica;
- DXF como caminho posterior de producao.

Regra tecnica: o produto nao e o desenho. O produto e o conjunto de parametros, dependencias, regras e validacoes que gera o desenho.

## 3. ICP vigente

ICP primario:

- criador de moda independente;
- modelista freelance;
- alfaiate ou atelie pequeno;
- professor de modelagem;
- fundador de micro-marca.

Caracteristicas:

- opera com 1 a 5 pessoas;
- produz de 20 a 500 pecas por modelo;
- sente custo, prazo e dependencia de modelagem como gargalo;
- precisa de autonomia tecnica, nao de uma suite enterprise.

ICP secundario:

- marca media que quer acelerar rascunhos tecnicos antes do ajuste fino de modelista.

## 4. Escopo de MVP

O MVP deve provar um loop estreito:

1. usuario informa medidas e parametros de uma peca base;
2. motor calcula o molde;
3. sistema mostra SVG com partes do molde;
4. usuario exporta ou usa o arquivo para teste;
5. beta user corta/costura ou valida fisicamente;
6. feedback vira ajuste numerico no motor.

Entregas prioritarias:

- `playbook.db` ou estrutura equivalente de regras, folgas, proporcoes e compatibilidades;
- endpoint `/molde`;
- logica parametrica para **saia reta** como primeira base;
- separacao entre medida corporal, folga e medida final do molde;
- `dependency_graph` para propagacao de medidas;
- `compatibility_matrix` para impedir componentes impossiveis;
- `PatternValidator` para curvas, intersecoes, encaixes, comprimentos e limites;
- visualizacao SVG estatica gerada sob demanda;
- PDF A4 com tesselation, margens, overlap e marcas de montagem;
- formulario minimo de entrada, sem linguagem natural na V1;
- documentacao tecnica das formulas e testes;
- validacao com 5 a 8 beta users;
- criterio de saida: pelo menos 3 usuarios cortaram e costuraram ou testaram fisicamente uma peca gerada pelo motor.

Ordem de pecas:

1. Saia reta.
2. Blusa basica.
3. Camiseta.
4. Vestido simples.
5. Calca reta.

## 5. O que fica fora do escopo imediato

Nao priorizar antes da validacao do motor:

- interface completa de gestao de colecao;
- dashboard amplo do Fashion OS;
- linguagem natural como input primario;
- preview em tempo real;
- calca como primeira base;
- geracao de imagem com ComfyUI;
- banco de fotos editoriais como produto;
- MRP, estoque e ordem de producao;
- personas digitais;
- marketplace;
- agente autonomo como promessa de produto;
- SaaS amplo para moda antes de provar o patternmaking engine.

Esses componentes podem voltar quando houver evidencia de uso, pagamento e precisao tecnica do motor.

## 6. Relacao com PHYLLOS Wear

PHYLLOS Wear continua sendo laboratorio de marca, produto fisico e linguagem de prova.

Mas a comunicacao publica deve separar:

- PHYLLOS como marca em desenvolvimento;
- Motor de Moldes como produto tecnico em validacao;
- Fashion OS como infraestrutura interna e horizonte de plataforma.

Nao comunicar produto final, material, sustentabilidade, performance ou precisao industrial sem evidencia documentada.

## 7. Prioridades para agentes

1. **Founder Orchestrator:** manter foco, bloquear dispersao, transformar pedidos amplos em entregaveis do Motor de Moldes.
2. **Technology Director / Frontend / Data:** construir Engine, Validator, SVG/PDF, dados, versionamento e testes antes de interface sofisticada.
3. **Product Director / Modelagem / Fit:** transformar conhecimento tacito em Playbook, validar logica geometrica, medidas criticas, folgas, prova fisica e criterios de qualidade.
4. **Curadores de moda:** alimentar Library, bases, componentes, compatibilidades e regras que afetam molde real, nao apenas imagem bonita.
5. **CX / Growth:** recrutar beta users, coletar feedback estruturado e medir disposicao a pagar.
6. **Brand / Communication:** comunicar o motor como acesso a precisao tecnica; evitar hype de IA, CAD completo ou promessa de perfeicao.
7. **CFO / Strategy / Investor Relations:** tratar ARR, valuation e captacao como hipotese dependente de prova tecnica e beta users.

## 8. Regras de decisao

- Se uma tarefa nao ajuda a codificar o Playbook, gerar uma base parametrica, validar geometria ou testar fisicamente o primeiro molde, ela e secundaria.
- Se houver conflito entre interface polida e logica correta, priorizar logica correta.
- Se houver conflito entre imagem bonita e molde cortavel, priorizar molde cortavel.
- Se houver conflito entre plano amplo e usuario real, priorizar usuario real.
- Se houver conflito entre linguagem natural e formulario estruturado, priorizar formulario estruturado ate a engine ser confiavel.
- Se houver conflito entre calca e saia reta como primeira entrega, priorizar saia reta.
- Toda afirmacao tecnica deve registrar premissas, limites e proxima prova necessaria.
- Todo agente deve explicitar quando esta falando de hipotese, prototipo, beta ou produto validado.

## 9. Vulnerabilidades obrigatorias para avaliacao de escopo

Antes de aprovar qualquer sprint, considerar o `Risk & Scope Review` em `docs/planejamento/risk-scope-review-mvp.md`, especialmente:

- auto-intersecoes e splines invalidas;
- componentes incompatíveis;
- medida corporal confundida com medida final do molde;
- tecido, elasticidade e gramatura ausentes;
- consumo de tecido;
- grading chegando cedo;
- falta de versionamento;
- falta de testes geometricos, golden patterns e visual diff;
- risco de construir um mini Audaces em vez do Canva da modelagem.

## 10. Fontes complementares

- `docs/planejamento/risk-scope-review-mvp.md`
- `docs/planejamento/estrategia-motor-moldes-v1.md`
- `docs/brand/voz-motor-moldes.md`
- `docs/patternmaking/catalogo-moldes-base.md`
- `docs/patternmaking/catalogo-saias-externas.md`
- `docs/patternmaking/calca-performance-alfaiataria-molde-v0.md`
- `docs/patternmaking/calca-performance-molde-interativo.html`
- `docs/patternmaking/catalogo-calcas.md`
- `.claude/agents/references/patternmaking-geometric-algorithmic-principles.md`
- `.claude/agents/references/patternmaking-construction-techniques-marlene-mukai.md`
