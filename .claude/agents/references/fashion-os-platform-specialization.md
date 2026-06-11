# PHYLLOS Fashion OS - Especializacao da Plataforma

Este documento orienta todos os agentes da PHYLLOS e do Fashion OS a partir de 2026-06-10. Ele deve ser usado junto com o racional de posicionamento vigente em `positioning-rationale-2026-06.md` e com as premissas estrategicas vigentes em `motor-moldes-strategic-premises.md`.

## 0. Premissa vigente - 2026-06-11

O MVP imediato da PHYLLOS e o **Parametric Pattern Engine** da PHYLLOS Create.

O Fashion OS continua sendo a infraestrutura tecnica e operacional mais ampla, mas no curto prazo deve servir a um objetivo estreito: transformar parametros estruturados, medidas corporais, tecido e design em molde 2D parametrizado, validavel e exportavel em SVG/PDF A4.

Tudo que nao ajuda a codificar o playbook, gerar uma base parametrica, validar geometria ou testar fisicamente o primeiro molde fica subordinado: linguagem natural, preview em tempo real, interface completa de gestao de colecao, Motor de Imagens, MRP, marketplace, agentes autonomos, e-commerce e SaaS amplo sao horizontes posteriores, nao escopo de MVP.

## 1. Visao

A PHYLLOS opera em duas camadas:

1. **PHYLLOS Wear:** marca em desenvolvimento, usada como laboratorio de produto, criterio, linguagem e prova real.
2. **Motor de Moldes / Fashion OS:** infraestrutura tecnica para transformar intencao de vestuario em especificacao, modelagem, molde e documentacao.

A camada de produto fisico da PHYLLOS segue priorizando roupas de alta versatilidade, unindo:

- elegancia;
- conforto;
- mobilidade;
- tecnologia textil;
- funcionalidade;
- longevidade;
- facilidade de manutencao.

No horizonte amplo, o Fashion OS e o sistema operacional responsavel por transformar a intencao do usuario em:

1. modelagem parametrizada;
2. molde em tamanho real para reproducao;
3. especificacao tecnica;
4. kit de producao;
5. documentacao completa;
6. imagem realista da peca, quando houver necessidade de comunicacao ou visualizacao.

No MVP atual, a ordem muda: **molde antes de imagem, logica antes de interface, validacao fisica antes de promessa de plataforma.**

## 2. Posicionamento da Marca

A PHYLLOS ocupa o espaco entre:

- alfaiataria tradicional;
- activewear;
- roupas para viagem;
- roupas para trabalho;
- roupas para vida cotidiana.

Principios:

- parecer elegante;
- sentir-se confortavel;
- mover-se livremente;
- vestir-se uma vez para multiplas situacoes.

## 3. Segmento Prioritario

Mulheres entre 25 e 65 anos.

Perfis:

- executivas;
- empreendedoras;
- professoras;
- profissionais liberais;
- viajantes;
- mulheres que buscam conforto sem aparencia esportiva.

Nota de aplicacao: este segmento orienta produto, pesquisa, modelagem, imagem e priorizacao comercial. Em comunicacao publica, continua valendo a regra do posicionamento vigente: reconhecer a origem e prioridade feminina sem transformar genero em limite desnecessario nem recorrer a linguagem elitista.

## 4. Categorias de Produto

### Essentials

- calca performance;
- camisa performance;
- blusa minimalista;
- t-shirt premium;
- saia confortavel;
- vestido versatil.

### Travel

- calcas antiamarrotamento;
- conjuntos compactaveis;
- pecas de secagem rapida.

### Work

- alfaiataria confortavel;
- pecas hibridas;
- conjuntos coordenados.

### Wellness

- roupas para caminhada;
- roupas para alongamento;
- pecas para home office;
- pecas para viagens longas.

## 5. Biblioteca de Tecidos

### Poliamida + Elastano

Objetivo: mobilidade maxima.

Caracteristicas:

- secagem rapida;
- alta elasticidade;
- resistencia;
- leveza.

Aplicacoes:

- calcas;
- blusas;
- travel wear.

### Viscose + Poliamida + Elastano

Objetivo: conforto premium.

Caracteristicas:

- toque macio;
- respirabilidade;
- excelente caimento.

Aplicacoes:

- alfaiataria confortavel;
- vestidos;
- camisas.

### Poliviscose + Elastano

Objetivo: visual de alfaiataria.

Caracteristicas:

- pouca amassabilidade;
- estrutura;
- conforto.

Aplicacoes:

- calcas;
- blazers;
- conjuntos.

### Modal

Objetivo: frescor.

Caracteristicas:

- toque sedoso;
- respirabilidade.

Aplicacoes:

- camisetas;
- blusas.

### Tencel / Lyocell

Objetivo: luxo e sustentabilidade.

Caracteristicas:

- alta respirabilidade;
- excelente caimento.

Aplicacoes:

- vestidos;
- camisas;
- pecas premium.

### La Merino Tecnologica

Objetivo: controle de odor.

Caracteristicas:

- termorregulacao;
- antiodor natural;
- conforto termico.

Aplicacoes:

- travel wear;
- pecas premium.

## 6. Fit Engine

Entradas:

- peso;
- altura;
- busto;
- cintura;
- quadril;
- entreperna;
- comprimento desejado;
- grau de ajuste;
- tecido;
- nivel de mobilidade.

Saidas:

- medidas finais da peca;
- folgas de vestibilidade;
- distribuicao de elasticidade;
- proporcoes adequadas.

## 7. Fabric Engine

Responsavel por calcular:

- elasticidade;
- gramatura;
- fluidez;
- estrutura;
- memoria do tecido;
- respirabilidade;
- secagem;
- tendencia ao amassamento;
- nivel de mobilidade.

Estas propriedades influenciam:

- o molde;
- o caimento;
- a imagem gerada;
- a ficha tecnica;
- a sequencia de costura.

## 8. Motor de Imagens

Status estrategico: componente futuro/subordinado. O Motor de Imagens nao e o MVP imediato. Ele so deve virar prioridade depois que o Motor de Moldes provar precisao tecnica, uso real e valor para beta users.

Objetivo: gerar fotografias que respeitem:

- peso;
- altura;
- proporcoes corporais;
- tecido;
- elasticidade;
- folgas de vestibilidade;
- caimento real.

Decisao vigente: o SVG local do Fashion OS e apenas rascunho tecnico/fallback offline. Imagem realista exige banco de termos de moda + prompt compiler + motor visual dedicado + QA visual em camadas. Seguir `docs/decisoes/adr-001-motor-imagem-realista-fashion-os.md`, `data/fashion-taxonomy/schema.md`, `data/fashion-taxonomy/seed_terms.csv` e [image-quality-verification-layers.md](image-quality-verification-layers.md).

Camadas obrigatorias:

1. Taxonomia de moda: tipos de peca, silhuetas, golas, mangas, bolsos, acabamentos, tecidos, texturas, modelagem e fit.
2. Contrato de alinhamento: define pose, enquadramento, eixo corporal, eixo da peca, partes visiveis, detalhes proibidos e negativos de desalinhamento.
3. Prompt Compiler Fashion: converte ficha tecnica e termos curados em prompt positivo, prompt tecnico, prompt negativo e pacote de QA.
4. Gerador visual: ComfyUI ou equivalente com workflow controlavel para foto/croqui realista.
5. QA de realismo em camadas: valida entrada, composicao, anatomia, alinhamento da roupa, fit/modelagem, tecido, construcao, fidelidade e coerencia PHYLLOS.
6. Ciclo de correcao: imagem reprovada deve gerar ajuste objetivo de prompt, pose, referencia, mascara, seed ou variante tecnica antes de nova tentativa.

Tipos de imagem:

- editorial;
- e-commerce;
- lifestyle;
- viagem;
- trabalho;
- alongamento;
- caminhada;
- academia leve.

## 9. Pattern Engine

Status estrategico: centro do MVP atual. O Pattern Engine e a base tecnica do Motor de Moldes.

Transforma `corpo 3D + tecido + design + mobilidade + construcao` em molde 2D parametrizado, validavel e graduavel.

O Pattern Engine deve seguir a referencia profunda em [patternmaking-geometric-algorithmic-principles.md](patternmaking-geometric-algorithmic-principles.md), alem da sintese construtiva em [patternmaking-construction-techniques-marlene-mukai.md](patternmaking-construction-techniques-marlene-mukai.md).

Tese operacional:

- uma roupa e uma superficie flexivel que sai de um plano, envolve um volume e volta a ser plano quando aberta;
- pences, recortes, costuras, pregas, folgas, vies e elasticidade sao mecanismos para correlacionar volume 3D com molde 2D;
- toda linha de molde deve explicar qual volume, movimento, tecido ou operacao construtiva ela resolve;
- nenhum molde deve ser tratado como desenho solto: ele precisa de medidas finais, linha de fio, paineis, pontos de controle, margens, piques, validacao e regra de graduacao.

Entradas minimas:

- medidas corporais e linhas de referencia;
- tecido, elasticidade, recuperacao, caimento, encolhimento e estabilidade;
- briefing de design, silhueta, grau de ajuste e componentes;
- movimentos obrigatorios;
- maquinario, costuras, margem e tolerancias de producao.

Saidas obrigatorias:

- molde parametrizado;
- base escolhida;
- medidas finais por regiao;
- folgas positivas, folgas negativas ou reducoes elasticas;
- mapa de volume 3D para solucao 2D;
- pences, recortes, pregas, franzidos, elastico, vies ou paineis usados;
- margem de costura;
- piques;
- linha de fio;
- plano de corte;
- sequencia de montagem;
- checklist de prova funcional;
- regra inicial de graduacao.

## 10. Kit PHYLLOS

Apos aprovacao do molde e da logica tecnica, o sistema deve gerar:

- ficha tecnica;
- tabela de medidas;
- lista de materiais;
- consumo de tecido;
- sequencia operacional;
- plano de corte;
- moldes em tamanho real;
- paginacao em A4;
- mapa de montagem;
- instrucoes de costura;
- checklist de qualidade;
- PDF final.

## 11. Primeira Familia de Produtos

- PH001 - Calca Performance Alfaiataria.
- PH002 - Calca Dia a Dia.
- PH003 - Camisa Performance.
- PH004 - Vestido Versatil.
- PH005 - Saia Conforto.

## 12. Roadmap

- Fase 1: Playbook + Engine - saia reta parametrica, SVG estatico, PatternValidator, PDF A4 e validacao fisica.
- Fase 2: blusa basica, tesselation mais robusta, testes geometricos e biblioteca modular.
- Fase 3: calca reta, validadores avancados, grade inicial e feedback de fitting.
- Fase 4: historico, projetos, usuarios e versionamento.
- Fase 5: linguagem natural como camada sobre parametros confiaveis.
- Fase futura: Motor de Imagens, prototipagem 3D, MRP, marketplace, API, biblioteca comercial ampliada e Atelier Digital Autonomo.

## Regras de Uso para Agentes

1. Ao criar produto, imagem, ficha, molde, custo, briefing ou plano de producao, usar esta especializacao junto com `motor-moldes-strategic-premises.md` como fonte de verdade operacional.
2. Diferenciar prioridade de produto de promessa publica: nem todo atributo tecnico pode virar claim sem teste, documento ou evidencia.
3. Toda recomendacao de tecido deve explicar efeito em caimento, mobilidade, manutencao e longevidade.
4. Toda decisao do MVP deve priorizar Playbook, logica parametrica, validação geometrica, SVG estatico, PDF A4 e validacao fisica antes de imagem, dashboard, linguagem natural ou automacao ampla.
5. Toda ficha tecnica deve mirar o Kit PHYLLOS completo, ainda que a fase atual entregue apenas parte dele.
6. Toda decisao de roadmap deve respeitar a sequencia vigente: Playbook/Engine, saia reta, SVG/PDF A4, validadores, blusa/camiseta, calca, historico/usuarios, linguagem natural, depois imagem/3D/MRP/API.
7. Toda tarefa de modelagem deve explicar como o volume 3D foi traduzido para o plano 2D e qual mecanismo resolve cada volume critico: pence, recorte, folga, elastico, vies, prega, franzido, painel ou costura.
8. Nenhuma imagem pode virar referencia de produto sem passar pelas camadas de QA visual em [image-quality-verification-layers.md](image-quality-verification-layers.md). Falha critica de anatomia, alinhamento da roupa, fit/modelagem ou fidelidade reprova a imagem.
