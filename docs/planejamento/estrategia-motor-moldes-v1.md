# Estrategia PHYLLOS Create / Motor de Moldes — v1

**Versao:** 1.0
**Data:** 2026-06-11
**Responsavel:** Strategy Agent — PHYLLOS
**Status:** Referencia estrategica vigente para MVP, revisada pela auditoria CTO/Product/Engenharia

> Esta estrategia e a fonte de referencia para o pivô do MVP em 2026-06-11. Agentes e documentos operacionais devem usar tambem `.claude/agents/references/motor-moldes-strategic-premises.md` e `docs/planejamento/risk-scope-review-mvp.md`.
>
> Revisao critica da auditoria: V1 nao deve depender de linguagem natural nem comecar por calca. O MVP deve comecar por parametros estruturados, Playbook, Engine, Validator, Library e uma base simples: saia reta. Linguagem natural entra depois, quando a engine geometrica estiver confiavel.

---

## 0. Contexto do pivo

O roadmap anterior do Fashion OS cobria cinco fases paralelas: API, interface visual, geracao de imagem com ComfyUI, MRP e comercial. Era um sistema de gestao de colecao tentando ser muitas coisas ao mesmo tempo.

O pivô reduz escopo a zero e recomeça com uma pergunta cirurgica: existe um problema tecnico, cotidiano e doloroso no vestuario que codigo pode resolver de forma radicalmente mais simples do que o que existe hoje?

A resposta é sim. O problema é modelagem.

---

## 1. Tese do Produto

### O que é o motor de moldes

O motor e um sistema que transforma parametros estruturados, medidas corporais e regras de modelagem em moldes tecnicos 2D prontos para corte, com SVG, PDF A4 e, em fase posterior, exportacao DXF.

Na V1, o usuario escolhe uma base e informa parametros: medidas do corpo, tecido, elasticidade, comprimento, folgas e detalhes essenciais. O motor responde com coordenadas calculadas, curvas parametricas, margens de costura, piques, sequencia operacional e PDF imprimivel. Nenhum software de desenho e obrigatorio.

O prototipo em `/docs/patternmaking/calca-performance-alfaiataria-molde-v0.md` demonstra que a logica parametrica e possivel. Porem, a primeira base operacional deve ser mais simples que uma calca: **saia reta**, por ter menos curvas, menos dependencias e menor risco geometrico.

### Por que isso e uma categoria nova

Nao e CAD: CAD requer que o usuario saiba desenhar, conheca os atalhos do software e tome decisoes geometricas a cada passo. O motor toma as decisoes geometricas por dentro e entrega o resultado.

Nao e PLM: PLM gerencia o ciclo de vida de produtos existentes. O motor cria a geometria do produto antes que ele exista.

Nao e gerador de imagem: geradores de imagem produzem pixels de roupas. O motor produz arquivos cortaveis de moldes reais. A diferenca e a diferenca entre uma foto de bolo e uma receita.

Nao e apenas um calculador de medidas: o motor conhece a logica de volume 3D para solucao 2D — como a diferenca de quadril e cintura se distribui entre lateral, pence e formato de gancho; como o gluteo exige extensao de gancho assimetrica; como tecido elastico reduz a folga necessaria. Essa logica era patrimonio implicito de modelistas experientes. O motor a torna explicita, parametrica e replicavel.

A categoria correta e: **Parametric Pattern Engine**. Um motor especializado em geometria de vestuario, operado primeiro por parametros estruturados e, depois, por linguagem natural.

### O problema que resolve — ICP preciso

O problema existente: transformar uma ideia de roupa em um molde cortavel custa entre R$300 e R$1.200 por peca (modelista por hora, 2 a 6 horas de trabalho) e leva de 2 dias a 3 semanas. Para marcas pequenas, cada iteracao é uma decisao de caixa. Para atelies, é um gargalo na capacidade de atender. Para professores, é uma barreira para que alunos experimentem. Para alfaiates independentes, é o limite entre escalar ou nao.

**ICP primario:** criador de moda independente — fundador de marca pequena, modelista freelance, alfaiate com atelie proprio, professor de modelagem em escola tecnica ou faculdade. Caracteristicas: opera com 1 a 5 pessoas, produz de 20 a 500 pecas por modelo, paga software atualmente entre R$0 (papel milimetrado) e R$300/mes (CLO3D basico), tem acesso a maquina de costura e faccionista, mas nao tem modelista fixo.

**ICP secundario:** marca media (50 a 500 pecas/modelo) que quer paralelizar desenvolvimento de colecao sem contratar mais modelistas. Usaria o motor como camada de rascunho — o modelista so entra para ajuste fino no piloto fisico, nao para construir do zero.

**ICP terciario (fase 3+):** plataformas de moda sob demanda, faccionistas digitais, academias de costura, desenvolvedores de apps de customizacao.

---

## 2. TAM / SAM / SOM

### Premissas de mercado

O mercado global de software de design e producao de moda foi estimado entre USD 2,7 bilhoes e USD 3,4 bilhoes em 2025, com CAGR de 11% projetado ate 2030 (Business Research Company, Research and Markets, 2026). A amplitude das estimativas reflete definicoes diferentes de escopo — os numeros maiores incluem PLM, ERP textil e gerenciamento de supply chain.

O segmento especifico de patternmaking e modelagem — excluindo PLM e ERP — representa aproximadamente 15% a 20% desse mercado, chegando a USD 400–600 milhoes globalmente em 2025.

Existem aproximadamente 200.000 designers de moda profissionais no mundo, com mais de 32.000 negocios de design registrados apenas nos EUA (FashionABC, 2026). Somando alfaiates independentes, professores, criadores de pattern para costura artesanal e micro-marcas, o universo de usuarios potenciais de uma ferramenta de modelagem acessivel alcanca de 2 a 5 milhoes de pessoas globalmente.

### TAM — Total Addressable Market

Mercado global de software especializado em patternmaking e gradacao de moldes: **USD 500 milhoes/ano** (estimativa conservadora, 2025).

Considerando a expansao por democratizacao — usuarios que hoje nao pagam nenhum software e usariam uma solucao acessivel — o TAM expansivel chega a **USD 1,2 bilhao**, incorporando professores, estudantes, alfaiates artesanais e criadores de conteudo de costura.

### SAM — Serviceable Addressable Market

Foco nos proximos 3 anos: criadores independentes e marcas pequenas em mercados com acesso digital, disposicao para pagar por SaaS e barreira de entrada ao CAD tradicional (custo ou curva de aprendizado).

Estimativa de universo: 500.000 a 800.000 usuarios potenciais na America Latina, Europa e Americas do Norte combinadas, dispostos a pagar entre USD 20 e USD 80/mes por uma solucao de patternmaking acessivel.

SAM estimado: **USD 120–180 milhoes/ano** (capturando 25% do universo com ticket medio de USD 35/mes).

### SOM — Serviceable Obtainable Market (18 meses)

Premissa: o motor entra no mercado no Q3 2026 com MVP, atinge 300 usuarios pagantes ate dezembro de 2026 e 1.500 ate junho de 2027.

| Cenario | Usuarios pagantes (mes 18) | ARPU/mes | ARR projetado |
|---|---:|---:|---:|
| Conservador | 800 | USD 25 | USD 240.000 |
| Base | 1.500 | USD 35 | USD 630.000 |
| Otimista | 3.000 | USD 45 | USD 1.620.000 |

SOM conservador para o periodo de 18 meses: **USD 240–630 mil ARR**.

Esse numero e pequeno em valor absoluto e correto como premissa de pre-seed. A tese nao e o ARR de 18 meses — e a prova de que o problema existe, que usuarios pagam e que o motor escala sem custo marginal relevante por usuario adicional.

---

## 3. Proposta de Valor Central

### Tagline

**"Da descricao ao molde. Sem software de CAD."**

### Narrativa de pitch em 3 frases

Criar uma roupa exige um molde. Fazer um molde exige um modelista — ou anos aprendendo software especializado. O motor de moldes PHYLLOS resolve isso por etapas: voce escolhe uma base, informa medidas e parametros, e recebe coordenadas, curvas, PDF e instrucoes prontas para validar no corte.

### Diferenciacao vs. concorrentes diretos

| Solucao | Posicionamento atual | Limitacao principal | Diferencial do motor PHYLLOS |
|---|---|---|---|
| CLO3D | Visualizacao 3D, simulacao de drapeado | USD 50/mes; exige modelagem 2D previa; curva de aprendizado alta | Motor gera o 2D; o 3D e opcional, nao o ponto de entrada |
| Optitex | CAD/CAM industrial, gradacao, encaixe | USD 1.200–1.500/ano; foco em grandes fabricantes; nao serve o indie | Acessivel por design; ICP primario e quem o Optitex ignora |
| Lectra | Suite PLM + corte automatizado | USD 8.000+/ano; enterprise; fora de alcance para o ICP alvo | Nao compete — serve um mercado diferente |
| Valentina | Open source, modelagem geometrica | Interface tecnica; requer conhecimento de modelagem; sem linguagem natural | Valentina e uma mesa de desenho digital; o motor e um coautor |
| Grafis | CAD europeu tradicional | Assinatura; interface anos 90; sem API; nao e SaaS | Motor e API-first, integravel, moderno por arquitetura |

O espaco vazio e este: uma ferramenta acessivel, parametrica e orientada por conhecimento de modelagem, capaz de devolver moldes cortaveis sem exigir que o usuario opere CAD industrial. Linguagem natural pode virar diferencial depois, mas nao e o fundamento da V1.

---

## 4. Roadmap Revisado (18 meses)

### Fase 1 — MVP do Motor (0–3 meses: julho a setembro de 2026)

Objetivo: provar que Playbook + Engine + Validator geram uma peca simples, com usuario real, produzindo arquivo imprimivel e validavel fisicamente.

Entregas:
- API FastAPI com endpoint `/molde` aceitando JSON estruturado de medidas e parametros de design
- `playbook.db` ou estrutura equivalente com regras, folgas, proporcoes e compatibilidades
- `dependency_graph` para propagacao de medidas
- Logica de calculo parametrico para saia reta
- `PatternValidator` inicial para limites, comprimentos e auto-intersecoes obvias
- Exportacao em SVG com coordenadas, curvas e piques marcados
- PDF A4 com tesselation, margens, overlap e marcas de montagem
- Interface minima de entrada: formulario web estruturado
- Validacao com 5 a 10 usuarios reais fazendo o ciclo completo: input → molde → corte → prova

Criterio de saida da fase: ao menos 3 usuarios terem cortado e costurado uma peca usando molde gerado pelo motor, com feedback documentado.

Tecnologia existente: FastAPI ja configurado, SQLite, Pydantic, Jinja2. O catalogo de moldes e as referencias de modelagem fornecem base para iniciar pela saia reta e evoluir para blusa/camiseta antes da calca.

### Fase 2 — Gradacao, Multiplas Pecas e Feedback de Fitting (3–9 meses: outubro 2026 a marco de 2027)

Objetivo: tornar o motor util para um wardrobe completo e para iteracao rapida.

Entregas:
- Gradacao automatica por grade de tamanhos (P, M, G, GG) preparada na arquitetura e exposta quando houver confiabilidade
- Pecas novas: blusa basica, camiseta, vestido simples e, depois, calca reta — cada uma com sua logica de calculo
- Mecanismo de feedback de fitting: usuario registra o que nao funcionou na prova (repuxo no gancho, folga no ombro, barra assimetrica) e o motor propoe ajuste numerico
- Historico de versoes por peca — molde v0, v1, v2 com diff de parametros
- Exportacao DXF consolidada

Criterio de saida da fase: 100 usuarios pagantes ativos, NPS acima de 40, pelo menos 3 depoimentos publicos de producao real.

### Fase 3 — Marketplace, Colaboracao e API para Marcas (9–18 meses: abril a dezembro de 2027)

Objetivo: transformar o motor em plataforma de valor acumulado, com rede e receita diversificada.

Entregas:
- Marketplace de moldes: usuarios publicam suas pecas geradas, outros compram e adaptam
- Colaboracao em tempo real: dois usuarios editando o mesmo molde
- API licenciada para marcas: uma marca integra o motor ao seu proprio sistema de desenvolvimento de produto
- Personalizacao por corpo: usuario cadastra suas medidas e recebe moldes adaptados automaticamente
- Integracao com Valentina para edicao tecnica avancada pos-geracao

Criterio de saida da fase: ARR de USD 400.000 base, 3 marcas usando a API B2B, data room pronto para Serie A.

---

## 5. Valuation e Captacao

### Unit Economics — Premissas

**Modelo de preco — tres camadas:**

- **Individual:** USD 29/mes — modelista freelance, alfaiate, professor. Acesso completo ao motor, exportacao ilimitada, historico de versoes.
- **Profissional:** USD 79/mes — marca pequena, atelie com equipe. Colaboracao, gradacao automatica, multiplos usuarios.
- **Licenca B2B (API):** USD 500 a USD 2.000/mes por marca — integracao direta ao sistema de desenvolvimento da marca, volume de chamadas escalonado.

**ARPU blended projetado:** USD 35/mes no cenario base (mix de 70% individual, 25% profissional, 5% B2B).

**CAC estimado:** USD 80 a USD 120 no digital (conteudo organico + comunidade de costura). Motor de patternmaking tem palavra-chave de alta intencao e comunidade ativa no YouTube, Instagram e Patreon. CAC tende a cair com boca a boca tecnico.

**LTV estimado:** 24 meses de retencao media (produto de workflow, nao de entretenimento) × USD 35 = USD 840.

**LTV/CAC:** 7x a 10x — saudavel para SaaS.

**Margem bruta:** acima de 80%. O custo marginal de gerar um molde adicional e computacional, nao humano.

### Cenarios de ARR (mes 18)

| Cenario | Usuarios pagantes | ARPU/mes | ARR |
|---|---:|---:|---:|
| Conservador | 800 | USD 25 | USD 240.000 |
| Base | 1.500 | USD 35 | USD 630.000 |
| Otimista | 3.000 | USD 45 | USD 1.620.000 |

### Tese para captacao — Pre-Seed

**Ticket alvo:** USD 300.000 a USD 500.000
**Dilution target:** 8% a 12%
**Instrumento:** SAFE com valuation cap de USD 3,5 a USD 5 milhoes
**Uso dos recursos:**
- 50%: desenvolvimento tecnico do motor (engenharia de software + logica de patternmaking)
- 30%: aquisicao dos primeiros 200 usuarios pagantes (conteudo, comunidade, parcerias com escolas)
- 20%: operacao, infraestrutura e juridico (IP, termos de servico)

**Por que agora:** o motor de moldes parametrico se tornou mais viavel pela combinacao de software acessivel, SVG/PDF no browser, LLMs como camada posterior de traducao e demanda crescente de criadores independentes por autonomia tecnica. A janela de criacao de categoria e agora, mas a defesa nasce da engine e do playbook, nao de uma interface conversacional isolada.

### Comparaveis de referencia

| Empresa | Foco | Round relevante | Valor |
|---|---|---|---|
| CLO Virtual Fashion | Simulacao 3D de vestuario | Serie B (2021) | USD 75 milhoes |
| Fit Collective | Sizing AI em producao | Pre-Seed (2025) | EUR 3,4 milhoes |
| True Fit | Recomendacao de tamanho no varejo | Serie C | USD 55 milhoes |
| Sizely | Medidas corporais por foto | Seed | USD 3,5 milhoes |

A PHYLLOS nao compete com nenhum deles diretamente. O espaco vazio — motor parametrico de moldes, acessivel, SaaS, API-first e sustentado por playbook de modelagem — nao tem ocupante claro. Esse e o argumento de categoria.

**Risco de timing:** o risco principal nao e competicao direta hoje. E que uma das grandes (Lectra, Optitex, CLO) lanca um produto similar com distribuicao ja estabelecida. A defesa e velocidade de adocao, profundidade tecnica da logica de vestuario e comunidade de usuarios que geram moldes proprios — uma rede que um incumbent nao copia facilmente.

---

## 6. O que SAIR do escopo imediato

Esta secao existe para ser comunicada claramente a co-fundadores, time e investidores. Desprioritizar nao e falhar — e foco.

| Componente desprioritizado | Por que saiu | Quando pode voltar |
|---|---|---|
| Geracao de imagem com ComfyUI | Resolve um problema de marketing/visualizacao, nao de producao. Nao e o que o ICP primario paga para ter. Requer GPU e infra cara. | Fase 3, como feature de apresentacao de colecao pos-geracao de molde |
| Banco de fotos editoriais (72 fotos curadas) | Ativos validos para brand PHYLLOS, nao para o produto SaaS. Podem viver em outro contexto. | Nao ha previsao para o SaaS; pode ser usado para marketing da marca PHYLLOS |
| Taxonomia visual (77 termos) | Trabalho relevante de arquitetura de produto, mas serve PLM e catalogo — nao o motor de moldes. | Relevante quando houver marketplace de moldes com busca semantica (Fase 3) |
| Personas e modelos digitais (Ollama local) | Depende de infra pesada e resolve visualizacao, nao producao. | Pode ser explorado como demo tecnico apos produto principal estar validado |
| MRP, ordem de producao, estoque | Gestao de producao e um problema diferente, com ICP diferente. Misturar aumenta complexidade sem aumentar valor para o ICP primario atual. | Produto separado, nao extensao do motor de moldes |
| Interface visual completa (Next.js/Streamlit) | Interface minima e suficiente para validar o motor. Investir em UI antes de provar a logica e gastar dinheiro no lugar errado. | Fase 2, quando usuarios pagantes pedirem experiencia mais polida |
| Agentes Claude especializados (22 agentes do Fashion OS original) | Arquitetura interessante mas prematura. Um motor bem construido nao precisa de 22 agentes para funcionar — precisa de logica solida e uma API clara. | Refatorar em Fase 2 se a complexidade do motor justificar orquestracao |
| Linguagem natural como input primario | Pode interpretar errado alteracoes geometricas ambiguas. | Depois da Engine, Validator e Playbook estarem confiaveis |
| Preview em tempo real | Alto custo de engenharia antes de provar a logica. | Depois do SVG estatico e PDF A4 funcionarem |
| Calca como primeira base | Gancho, quadril, joelho e equilibrio frente/costas tornam a peca complexa demais para V1. | Depois de saia reta, blusa/camiseta e vestido simples |

**Mensagem para investidores sobre o pivô:** o escopo anterior demonstrou capacidade tecnica e visao de plataforma. O pivô nao descarta esse trabalho — ele usa a camada tecnica existente (FastAPI, SQLite, Pydantic, prototipo de molde) e elimina tudo que nao serve ao problema central. Isso e disciplina, nao reversao.

---

## 7. Proximos 30 dias — 5 acoes concretas e priorizadas

### Acao 1 — Transformar a primeira base simples em API funcional (semanas 1 e 2)

A primeira entrega deve ser saia reta. A acao e transformar regras de medida, folga, tecido e comprimento em um endpoint `/molde` que aceita JSON estruturado e devolve parametros calculados + SVG gerado.

Criterio de conclusao: endpoint respondendo corretamente para tres variantes de medidas, com golden patterns e validacao geometrica basica.

Responsavel sugerido: engenharia (pode ser o founder se full-stack).

### Acao 2 — Recrutar 5 a 8 beta users do ICP primario (semanas 1 a 3, paralela)

Identificar modelistas freelances, professores de modelagem e fundadores de micro-marcas no Brasil e convidá-los para testar o motor em troca de feedback estruturado. Fontes: grupos de costura no Instagram, comunidades de moda no LinkedIn, escolas tecnicas de moda (Senac, SPFW network, atelies independentes em SP e RJ).

Criterio de conclusao: 5 usuarios comprometidos com o ciclo completo — receber o molde, cortar, costurar (ou testar em papel), enviar foto e preencher formulario de feedback.

### Acao 3 — Definir a versao minima do formulario de entrada (semana 2)

Mapear quais campos sao obrigatorios para gerar um molde valido vs. quais podem ter defaults inteligentes. O objetivo e reduzir o formulario ao minimo sem comprometer a precisao geometrica. Para a primeira base, separar medida corporal, folga e medida final do molde. Para saia reta, as medidas essenciais sao cintura, quadril, altura do quadril e comprimento. Tipo de tecido, elasticidade e gramatura entram como parametros criticos para folga e caimento.

Criterio de conclusao: formulario de entrada definido, documentado e validado com ao menos um modelista real antes de codar a interface.

### Acao 4 — Documentar a logica de calculo como especificacao tecnica (semanas 2 e 3)

O prototipo v0 usa formulas implicitas. Para o motor escalar para novas pecas, a logica precisa estar explicitada como especificacao — formulas, condicoes, casos de borda, referencias a normas de modelagem quando existirem.

Criterio de conclusao: documento de especificacao tecnica do motor para saia reta, revisado por pelo menos um modelista.

### Acao 5 — Definir o arco de captacao dos proximos 90 dias (semana 3)

Com o MVP em andamento, preparar o one-pager de investidor com: problema, solucao, tese de mercado, prototipo funcional (link ao endpoint), time e ask. Nao esperar o produto perfeito. Um endpoint funcionando com usuarios reais que imprimiram, cortaram ou validaram fisicamente uma base simples ja e demo suficiente para conversa de pre-seed.

Criterio de conclusao: one-pager revisado pelo founder, lista de 10 investidores-alvo mapeada (angels em fashion tech, fundos de pre-seed focados em ferramentas criativas ou manufatura).

---

## Apendice — Riscos estrategicos identificados

| Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|
| Logica geometrica do motor nao gera moldes precisos o suficiente para producao real | Media | Alto | Validar com modelistas antes de lancar publicamente; ser transparente que v0 e rascunho parametrico, nao substituto de prova fisica |
| ICP nao paga porque esta acostumado a receber moldes de modelista (custo percebido zero) | Media | Medio | O problema nao e preco — e velocidade e autonomia. Narrativa de pitch precisa enfatizar iteracao rapida, nao economia de dinheiro |
| Concorrente lanca feature similar antes da PHYLLOS ter traction | Baixa no curto prazo | Alto no longo prazo | Velocidade de adocao e comunidade sao a defesa; publicar conteudo tecnico ativamente para construir autoridade de categoria |
| Founder sozinho nao tem capacidade tecnica para entregar o motor no prazo | Depende do time | Critico | Mapear co-fundador tecnico ou freelancer especializado em geometria computacional / Python nas proximas 4 semanas |
| Exportacao DXF nao e compativel com o software do faccionista | Media | Medio | Testar com ao menos 3 faccionistas reais nas primeiras 8 semanas; ter SVG como fallback |

---

*Este documento e o artefato estrategico de referencia para o pivô do Motor de Moldes PHYLLOS. Deve ser revisado pelo founder antes de qualquer comunicacao externa com investidores ou parceiros.*
