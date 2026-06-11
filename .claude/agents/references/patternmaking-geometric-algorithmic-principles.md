# Patternmaking geometrico e algoritmico - referencia operacional

Esta referencia orienta os agentes PHYLLOS Fashion OS quando a tarefa envolver modelagem, fit, ficha tecnica, prototipagem, plano de corte, graduacao ou Pattern Engine.

Objetivo: transformar a criacao de moldes em um raciocinio reprodutivel. O molde nao deve nascer de intuicao solta. Ele deve ser uma traducao controlada de `corpo 3D + tecido + intencao de design + mobilidade + construcao` para pecas 2D que possam ser cortadas, costuradas, provadas e graduadas.

Limite importante: esta referencia nao substitui modelista, prova fisica, piloto ou validacao em corpo real. Ela define a logica para construir a primeira versao correta, reduzir tentativa e erro e documentar por que cada linha do molde existe.

## Tese central

Roupa e uma superficie flexivel que negocia quatro sistemas:

- Corpo: volume irregular, articulado, assimetrico e em movimento.
- Tecido: superficie plana com fio, trama, vies, elasticidade, caimento e memoria.
- Molde: representacao 2D de partes dessa superficie, com recortes, pences, folgas e margens.
- Montagem: sequencia de costura que fecha o plano em volume novamente.

Um molde correto e um algoritmo espacial. Ele escolhe onde o plano sera cortado, onde o excesso sera retirado, onde o volume sera liberado, onde o tecido pode deformar e onde a costura vai reconstruir a forma 3D.

## Principios geometricos

### 1. O corpo nao e planificavel como uma folha unica

O corpo tem dupla curvatura em busto, ombro, escapula, abdomen, quadril, gluteo, gancho e joelho. Uma superficie plana nao cobre dupla curvatura sem uma destas solucoes:

- dividir em paineis;
- inserir pences;
- transferir pences para recortes;
- abrir pregas, franzidos ou drapeados;
- usar elasticidade;
- cortar em vies;
- permitir folga;
- aceitar uma deformacao controlada do tecido.

Regra para agentes: sempre que houver volume 3D importante, perguntar qual mecanismo vai resolver esse volume no plano. Se nenhum mecanismo aparecer, o molde esta incompleto.

### 2. Pences sao cunhas de volume

Uma pence remove ou controla uma cunha no plano para criar volume quando fechada. Ela tem:

- ponto de foco: regiao volumetrica que a pence respeita, como busto, cintura ou escapula;
- intake: quantidade de tecido absorvida;
- direcao: caminho visual e construtivo ate uma costura ou borda;
- equivalentes: recorte princesa, prega, franzido, drapeado ou deslocamento de costura.

Formula de raciocinio:

```text
intake_total_da_regiao =
  medida_final_da_regiao_maior
  - medida_final_da_regiao_menor
  - diferenca_que_sera_absorvida_por_laterais
```

Exemplo: em uma peca superior ajustada, a diferenca entre busto final e cintura final precisa ser distribuida entre laterais, pences, recortes ou folga aparente. Em uma saia/calca, a diferenca entre quadril final e cintura final precisa virar lateral, pence, cos anatomico, elastico ou prega.

### 3. Folga e dado de projeto, nao sobra

Folga de vestibilidade e o espaco entre corpo e roupa. Ela depende de:

- categoria da peca;
- tecido;
- grau de ajuste;
- funcao;
- movimento;
- conforto termico;
- aparencia desejada.

Formula base:

```text
medida_final_da_peca =
  medida_corporal
  + folga_de_vestibilidade
  + folga_de_movimento
  - reducao_elastica_ou_compressao
```

Para tecido plano sem elasticidade, a folga tende a ser positiva. Para malha ou tecido tecnico elastico, pode existir folga zero ou negativa, desde que recuperacao, conforto e transparencia sejam validados.

### 4. O fio do tecido e um eixo de engenharia

Linha de fio nao e marcacao burocratica. Ela define estabilidade, queda, torcao e deformacao.

- Fio reto: mais estabilidade vertical, melhor para estrutura e alinhamento.
- Trama: estabilidade horizontal, geralmente menos usada como eixo principal.
- Vies: mais deformacao e caimento, bom para fluidez, perigoso para distorcao.
- Maior elasticidade: deve ser orientada conforme a demanda de movimento.

Regra para agentes: toda peca de molde deve declarar linha de fio, direcao de maior extensibilidade e justificativa.

### 5. Costuras sao cortes de planificacao

Costura nao e apenas uniao. Ela e onde o sistema decidiu quebrar a superficie 3D para transforma-la em 2D.

Uma boa costura deve:

- reduzir distorcao;
- respeitar movimento;
- permitir montagem limpa;
- servir ao design;
- ficar em area toleravel para conforto;
- preservar simetria quando necessario;
- facilitar graduacao e producao.

## Modelo de entradas do Pattern Engine

Todo estudo de molde deve comecar com estes grupos de dados.

### Corpo

- altura;
- busto/torax;
- cintura;
- quadril;
- ombro;
- largura de costas;
- cava;
- braco;
- punho;
- gancho;
- coxa;
- joelho;
- panturrilha;
- tornozelo;
- entreperna;
- comprimentos desejados;
- postura e assimetrias relevantes.

### Design

- tipo de peca;
- silhueta;
- grau de ajuste;
- linhas de estilo;
- recortes;
- bolsos;
- golas;
- mangas;
- fechamentos;
- forro/revel/entretela;
- comprimento;
- efeito visual desejado.

### Tecido

- composicao;
- gramatura;
- espessura;
- elasticidade no fio, na trama e no vies;
- recuperacao elastica;
- encolhimento;
- transparencia sob tensao;
- caimento;
- estabilidade;
- necessidade de descanso antes do corte;
- comportamento de costura.

### Mobilidade

- sentar;
- caminhar;
- agachar;
- levantar bracos;
- dirigir;
- carregar objetos;
- alongar;
- treino leve ou intenso;
- tempo de uso continuo.

### Construcao

- maquinario disponivel;
- tipos de costura;
- margem padrao por operacao;
- tolerancias;
- sequencia de montagem;
- controle de qualidade;
- custo e tempo de producao.

## Receita de bolo para construir qualquer molde

### Etapa 1 - Classificar a familia da peca

Definir se a peca e:

- inferior: saia, calca, short, bermuda;
- superior: blusa, camisa, top, jaqueta, blazer;
- inteira: vestido, macacao, chemisier;
- componente: manga, gola, cos, bolso, carcela, punho, revel;
- hibrida: peca com funcao tecnica, compressao, alfaiataria confortavel ou performance.

Saida: familia, base inicial e componentes obrigatorios.

### Etapa 2 - Mapear o corpo em planos de referencia

Transformar medidas em linhas horizontais e verticais:

- centro frente;
- centro costas;
- linha de busto/torax;
- linha de cintura;
- linha de quadril;
- linha de gancho;
- linha de joelho;
- linha de barra;
- linha de ombro;
- linha de cava;
- eixo da manga;
- eixo da perna.

Saida: grade corporal 2D inicial.

### Etapa 3 - Definir medida final por regiao

Para cada regiao, calcular:

```text
medida_final = corpo + folga + movimento - reducao_elastica
```

Exigir tabela com:

- medida corporal;
- folga positiva ou negativa;
- justificativa;
- medida final da peca;
- tolerancia.

Saida: matriz de medidas finais.

### Etapa 4 - Escolher a base

Selecionar a base mais proxima:

- saia reta, lapis, evase ou gode;
- calca base, pantalona, alfaiataria, jogger ou legging;
- blusa basica, camisa, regata, corpete ou jaqueta;
- vestido tubo, evase, envelope, chemisier ou frente unica;
- manga reta, longa, bufante, alfaiataria, raglan, japonesa;
- gola simples, colarinho com pe, xale, esporte, chinesa.

Saida: base escolhida e motivo.

### Etapa 5 - Calcular excesso, falta e volume

Comparar regioes maiores e menores:

```text
diferenca_cintura_quadril = quadril_final - cintura_final
diferenca_busto_cintura = busto_final - cintura_final
diferenca_coxa_barra = coxa_final - barra_final
diferenca_braco_punho = braco_final - punho_final
```

Decidir para onde vai a diferenca:

- lateral;
- pence;
- recorte;
- prega;
- elastico;
- franzido;
- drapeado;
- abertura;
- volume solto.

Saida: mapa de distribuicao de volume.

### Etapa 6 - Definir costuras e paineis

Escolher onde a superficie sera quebrada:

- lateral;
- ombro;
- entreperna;
- gancho;
- pala;
- recorte princesa;
- centro frente/costas;
- ilharga;
- recorte de joelho;
- recorte de manga;
- pala traseira;
- costura de cos.

Cada painel precisa ter:

- funcao;
- par de costura correspondente;
- comprimento compatibilizado;
- linha de fio;
- tolerancia de encaixe;
- piques.

Saida: arquitetura de paineis.

### Etapa 7 - Desenhar o esqueleto coordenado

Criar um sistema de coordenadas por peca de molde:

```text
origem = ponto superior esquerdo ou centro frente/costas
x = largura horizontal
y = comprimento vertical
pontos_de_controle = curvas de cava, gancho, decote, quadril, barra
```

Cada curva deve nascer de pontos mensuraveis, nao de gesto solto:

- cava liga ombro, profundidade de cava e lateral;
- gancho liga cintura, profundidade, extensao e entreperna;
- quadril liga cintura, ponto alto do quadril e maior quadril;
- manga liga cabeca, biceps, cotovelo e punho;
- decote liga centro, ombro e abertura.

Saida: molde base sem margem.

### Etapa 8 - Aplicar transformacoes de design

Adicionar:

- recortes;
- aberturas;
- transpasses;
- bolsos;
- golas;
- punhos;
- carcelas;
- ziperes;
- elastico;
- forro;
- revel;
- entretela;
- bainha.

Regra: cada transformacao deve declarar o impacto no molde, na costura e no fit.

Saida: molde transformado sem margem.

### Etapa 9 - Adicionar construcao

Somente depois da forma aprovada, adicionar:

- margem de costura por operacao;
- margem de bainha;
- piques;
- furos;
- marcacoes de pence;
- linha de fio;
- indicacao de dobra;
- identificacao de peca;
- quantidade a cortar;
- tecido/forro/entretela;
- sentido do pelo/estampa quando houver.

Saida: molde de corte.

### Etapa 10 - Validar numericamente antes do piloto

Checar:

- pares de costura com mesmo comprimento ou easing previsto;
- cintura, quadril, busto, coxa, manga e barra batem com medidas finais;
- pences fecham sem degrau;
- curvas tem continuidade;
- linha de fio esta coerente;
- margem nao foi esquecida;
- componentes encaixam;
- plano de corte respeita largura do tecido;
- consumo esta plausivel;
- pontos criticos de mobilidade foram previstos.

Saida: checklist de liberacao para piloto.

### Etapa 11 - Provar, corrigir e registrar aprendizado

Prova obrigatoria:

- em pe;
- sentada;
- caminhando;
- agachando quando aplicavel;
- bracos levantados quando aplicavel;
- movimento real do job-to-be-done.

Cada correcao deve virar dado:

```text
problema observado -> causa provavel -> ajuste no molde -> medida alterada -> resultado esperado
```

Saida: molde revisado e historico de decisao.

### Etapa 12 - Graduar

Graduacao nao e escala uniforme. Cada ponto tem deslocamento proprio:

- larguras crescem mais que comprimentos;
- cintura, busto e quadril crescem em proporcoes diferentes;
- cava, gancho e ombro exigem regras especificas;
- detalhes precisam preservar posicao visual e funcional;
- costuras devem continuar casando apos cada tamanho.

Saida: tabela de grade points, regra por tamanho e QA da grade.

## Regras por familia

### Calcas

Pontos criticos:

- cintura;
- quadril;
- gancho frente;
- gancho costas;
- entreperna;
- coxa;
- joelho;
- barra;
- altura de cos;
- bolso;
- fechamento.

Algoritmo minimo:

```text
1. calcular cintura_final, quadril_final, coxa_final e barra_final
2. definir profundidade e extensao de gancho
3. separar frente e costas com mais volume nas costas quando necessario
4. distribuir diferenca cintura/quadril entre laterais, pences, cos ou elastico
5. validar sentado e agachando
6. posicionar bolso sem abrir, marcar ou criar volume indevido
```

Risco classico: corrigir gancho apenas alargando lateral. Isso pode piorar dobra, repuxo e volume. O ajuste deve considerar profundidade, extensao, inclinacao e curva.

### Saias

Pontos criticos:

- cintura;
- quadril;
- comprimento;
- abertura de passo;
- volume de barra;
- fechamento;
- cos/revel.

Algoritmo minimo:

```text
1. calcular cintura_final e quadril_final
2. decidir silhueta: reta, lapis, evase, gode ou envelope
3. distribuir diferenca cintura/quadril em pences, laterais, elastico ou pregas
4. validar abertura de passo e sentar
5. definir cos, revel ou acabamento interno
```

### Blusas e camisas

Pontos criticos:

- busto/torax;
- cintura;
- ombro;
- costas;
- cava;
- decote;
- abertura frontal;
- pala;
- manga;
- gola;
- punho.

Algoritmo minimo:

```text
1. calcular busto_final, cintura_final e largura de costas
2. construir eixo centro frente/costas, ombro, cava e lateral
3. distribuir volume de busto/cintura em pence, recorte ou folga
4. compatibilizar cava com cabeca de manga
5. definir gola, vista, carcela e punho como componentes conectados
6. validar bracos levantados, alcance frontal e postura sentada
```

### Vestidos e pecas inteiras

Pontos criticos:

- conexao corpo superior + saia;
- linha de cintura real ou deslocada;
- quadril;
- abertura de passo;
- fechamento;
- equilibrio frente/costas.

Algoritmo minimo:

```text
1. escolher se a base nasce de blusa + saia ou corpo unico
2. calcular busto, cintura, quadril e comprimento total
3. decidir como o volume sera resolvido no busto e no quadril
4. prever abertura de movimento
5. validar sentar, caminhar e levantar bracos
```

### Mangas

Pontos criticos:

- comprimento;
- biceps;
- cotovelo;
- punho;
- cabeca da manga;
- encaixe na cava;
- rotacao do braco.

Algoritmo minimo:

```text
1. medir cava da frente e das costas
2. definir altura de cabeca conforme estilo e mobilidade
3. calcular largura de biceps e punho
4. distribuir easing da cabeca de manga se houver
5. validar braco levantado, alcance frontal e conforto no cotovelo
```

## Pseudocodigo do Pattern Engine

```text
function construir_molde(brief, corpo, tecido, mobilidade, construcao):
  familia = classificar_peca(brief)
  base = selecionar_base(familia, brief.silhueta)
  grade_corporal = mapear_linhas_do_corpo(corpo, familia)
  medidas_finais = {}

  for regiao in regioes_relevantes(familia):
    folga = decidir_folga(regiao, brief.fit, tecido, mobilidade)
    reducao = decidir_reducao_elastica(regiao, tecido, brief.compressao)
    medidas_finais[regiao] = corpo[regiao] + folga - reducao

  mapa_volume = distribuir_diferencas(medidas_finais, brief.linhas_de_estilo)
  paineis = definir_paineis(base, mapa_volume, brief, construcao)
  pecas_sem_margem = desenhar_pecas(paineis, grade_corporal, medidas_finais)
  pecas_transformadas = aplicar_design(pecas_sem_margem, brief.componentes)
  pecas_de_corte = adicionar_margens_marcas(pecas_transformadas, construcao)
  qa = validar_molde(pecas_de_corte, medidas_finais, tecido, mobilidade)

  if qa.reprovado:
    revisar_parametros(qa)

  return kit_molde(pecas_de_corte, medidas_finais, mapa_volume, qa)
```

## Saida obrigatoria dos agentes

Quando um agente produzir estudo de molde, deve entregar:

- objetivo da peca;
- corpo-alvo e medidas usadas;
- medidas ausentes;
- tecido e comportamento esperado;
- base escolhida;
- familia e componentes;
- medida final por regiao;
- folga/reducao por regiao;
- mapa de volume 3D para solucao 2D;
- pences, recortes, pregas, elastico ou folga usados;
- arquitetura de paineis;
- partes do molde;
- linha de fio;
- margens;
- piques e marcas;
- ordem de montagem;
- testes de mobilidade;
- riscos de piloto;
- regra inicial de graduacao;
- proximos dados a coletar.

## Agenda de estudo para os agentes do segmento

### Modelagem

- Transformar qualquer briefing em receita de molde.
- Manter biblioteca de bases e transformacoes.
- Explicar sempre o mecanismo 3D para 2D.

### Fit Technical Designer

- Validar folgas, reducoes elasticas e mobilidade.
- Converter problemas de prova em ajustes mensuraveis.
- Garantir que graduacao preserve proporcao e conforto.

### Curador de Modelagem e Fit

- Curar vocabulario tecnico de fit, volume, folga e movimento.
- Converter termos visuais em impacto real no molde.
- Criar regras reutilizaveis para Fit Engine e Pattern Engine.

### Tech Spec Writer

- Traduzir a receita do molde para tech pack.
- Documentar medidas finais, tolerancias, costuras, margens, piques e ordem de montagem.

### Product Director e Product Development Lead

- Exigir que todo gate de produto tenha decisao de modelagem rastreavel.
- Bloquear avanco quando o molde nao explicar volume, tecido, fit, construcao e validacao.

### Technology Director e AI Automation Lead

- Transformar esta logica em modelos de dados, schemas e validadores.
- Evitar automacao que gere curvas sem medidas, sem QA ou sem rastreabilidade.

## Leituras tecnicas para o Pattern Engine

Estas fontes foram usadas como referencia de pesquisa para a camada computacional do raciocinio:

- Nico Pietroni et al., "Computational Pattern Making from 3D Garment Models", arXiv:2202.10272. Relevante para segmentacao de uma roupa 3D em patches 2D, alinhamento de fio, simetria de costura, pences e distorcao anisotropica do tecido. https://arxiv.org/abs/2202.10272
- Anran Qi e Takeo Igarashi, "PerfectTailor: Scale-Preserving 2D Pattern Adjustment Driven by 3D Garment Editing", arXiv:2312.08386. Relevante para ajuste de molde 2D a partir de edicoes 3D sem ignorar escala local e convencoes industriais. https://arxiv.org/abs/2312.08386
- Sauradip Nag et al., "PersonalTailor: Personalizing 2D Pattern Design from 3D Garment Point Clouds", arXiv:2303.09695. Relevante para personalizacao de paineis 2D a partir de nuvem de pontos 3D e restricoes do usuario. https://arxiv.org/abs/2303.09695
- Kiyohiro Nakayama et al., "Garment Particles: A 2D--3D Symmetric Garment Representation for Generation and Editing", arXiv:2605.26391. Relevante para representacao conjunta 2D/3D de roupas e edicao integrada entre padroes e geometria. https://arxiv.org/abs/2605.26391
