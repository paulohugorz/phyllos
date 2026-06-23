# Fashion Taxonomy - Esquema do Banco de Referencias

Objetivo: criar um banco de dados de termos tecnicos de moda para orientar imagem realista, ficha tecnica, modelagem, producao e comunicacao da PHYLLOS.

## Entidade principal: fashion_terms

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador estavel. Ex: `pants.fit.wide_leg` |
| termo_pt | texto | Termo principal em portugues usado por moda/producao |
| termo_en | texto | Termo em ingles para prompts e pesquisa visual |
| categoria | enum | peca, silhueta, fit, cintura, gola, manga, fechamento, bolso, acabamento, tecido, textura, costura, modelagem |
| subcategoria | texto | Agrupamento especifico. Ex: calcas, camisas, golas, barras |
| definicao | texto | Definicao objetiva do termo |
| atributos_visuais | lista | O que precisa aparecer na imagem |
| atributos_tecnicos | lista | Informacoes de construcao ou modelagem |
| requisitos_alinhamento | lista | Eixos, simetrias, proporcoes e partes que precisam ficar alinhadas ou visiveis na imagem |
| falhas_visuais_criticas | lista | Erros que reprovam imagem: desalinhamento, anatomia ruim, costura quebrada, detalhe inventado ou caimento impossivel |
| prompt_tokens | lista | Termos que entram no prompt de imagem |
| prompt_negativo | lista | Erros comuns a evitar |
| compatibilidades | lista | Termos compativeis |
| incompatibilidades | lista | Termos que conflitam |
| aplicacao_phyllos | texto | Quando usar na PHYLLOS |
| fonte_status | enum | curado, pendente, validado_com_amostra |
| curador | texto | Agente responsavel pela curadoria |
| ultima_revisao | data | Data da ultima validacao |

## Tabelas auxiliares

### term_sources

Registra fonte de referencia, sem copiar imagens proprietarias para dentro do repo.

| Campo | Descricao |
|---|---|
| term_id | Relacao com `fashion_terms.id` |
| source_type | livro, ficha tecnica, fornecedor, aula, editorial, e-commerce, amostra propria |
| source_label | Nome legivel da fonte |
| source_url | URL quando existir |
| rights_note | Observacao de uso e direitos |

### term_examples

Guarda exemplos de uso em prompt e ficha tecnica.

| Campo | Descricao |
|---|---|
| term_id | Relacao com `fashion_terms.id` |
| use_case | imagem_editorial, imagem_tecnica_qa, croqui_tecnico, ficha_tecnica, modelagem |
| example_text | Exemplo curto |

## Extensao semantica para linguagem natural

Esta extensao preserva a fala popular e cria a ponte entre pedido de cliente, conceito tecnico, intencao e parametro de modelagem. Ela nao substitui `fashion_terms`; ela alimenta e complementa a taxonomia tecnica.

### vocabulary_term

Guarda termos populares, tecnicos, comerciais, historicos e regionais.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador estavel. Ex: `vocab.popular.blusa_soltinha` |
| termo | texto | Forma original ou principal do termo |
| termo_normalizado | texto | Forma normalizada para busca e deduplicacao |
| tipo_termo | enum | popular, tecnico, comercial, historico, regional, hibrido |
| linguagem | texto | pt-BR, en, regionalismo ou origem linguistica |
| categoria_moda | texto | caimento, conforto, tecido, modelagem, ajuste etc. |
| descricao | texto | Explicacao simples |
| exemplo_uso | texto | Frase real ou plausivel de uso |
| origem_fonte | texto | Entrevista, apostila, ficha, catalogo, fornecedor, curadoria |

### technical_concept

Guarda conceitos tecnicos acionaveis.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador estavel. Ex: `concept.fit.wearing_ease` |
| nome_tecnico | texto | Nome tecnico canonico |
| categoria | texto | modelagem, tecido, caimento, acabamento, construcao |
| descricao_simples | texto | Explicacao legivel para nao tecnicos |
| descricao_tecnica | texto | Explicacao para modelagem, ficha tecnica ou engenharia |
| efeito_visual | texto | Efeito esperado na imagem ou silhueta |
| efeito_no_caimento | texto | Efeito esperado no corpo e no tecido |
| dificuldade | texto | baixa, media, alta ou criterio equivalente |
| observacoes | texto | Alertas, limites e dependencias |

### term_concept_map

Relaciona termo popular ou tecnico com conceitos tecnicos.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador do relacionamento |
| term_id | texto | FK para `vocabulary_term.id` |
| concept_id | texto | FK para `technical_concept.id` |
| confianca | real | 0.0 a 1.0 |
| observacao | texto | Motivo do mapeamento e riscos |

### user_intent

Guarda intencoes da usuaria, como `disfarcar_abdomen`, `aumentar_conforto_braco`, `alongar_silhueta`, `parecer_elegante`, `facilitar_costura`, `economizar_tecido`, `valorizar_cintura`, `aumentar_mobilidade`, `evitar_transparencia` e `roupa_fresca`.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador estavel da intencao |
| nome | texto | Nome curto legivel |
| descricao | texto | O que a pessoa quer resolver |
| categoria | texto | conforto, efeito_visual, producao, custo, mobilidade, tecido |
| exemplos_fala | texto | Frases reais associadas |
| observacoes | texto | Limites, ambiguidades e cuidado de linguagem |

### intent_concept_map

Relaciona intencao com conceitos tecnicos.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador do relacionamento |
| intent_id | texto | FK para `user_intent.id` |
| concept_id | texto | FK para `technical_concept.id` |
| prioridade | inteiro | Prioridade relativa do conceito para a intencao |
| justificativa | texto | Por que o conceito atende a intencao |

### fabric

Guarda comportamento dos tecidos.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador estavel do tecido |
| nome | texto | Nome comercial ou tecnico |
| familia | texto | plano, malha, alfaiataria, fluido, estruturado etc. |
| composicao | texto | Composicao conhecida ou estimada |
| elasticidade | texto | sem, baixa, media, alta; direcao quando houver |
| gramatura | texto | Leve, media, pesada ou valor g/m2 quando conhecido |
| caimento | texto | Fluido, estruturado, armado, aderente etc. |
| respirabilidade | texto | baixa, media, alta ou observacao |
| transparencia | texto | opaco, semi-transparente, transparente |
| toque | texto | seco, macio, frio, sedoso, encorpado etc. |
| dificuldade_costura | texto | baixa, media, alta |
| indicado_para | texto | Pecas, bases e contextos recomendados |
| evitar_quando | texto | Contextos em que o tecido cria risco |
| observacoes_modelagem | texto | Folga, forro, entretela, agulha, margem ou prova |

### style_reference

Guarda referencias historicas e culturais.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador estavel da referencia |
| nome | texto | Nome da referencia |
| periodo | texto | Periodo historico ou recorte temporal |
| origem | texto | Origem cultural, geografica ou de mercado |
| caracteristicas | texto | Atributos observaveis |
| silhuetas_associadas | texto | Silhuetas relacionadas |
| componentes_associados | texto | Golas, mangas, bolsos, fechamentos, recortes etc. |
| designers_referencia | texto | Designers ou fontes quando verificaveis |
| aplicacao_contemporanea | texto | Como usar hoje sem virar caricatura |

### semantic_review

Registra a revisao antes de um termo entrar como curado.

| Campo | Tipo | Descricao |
|---|---|---|
| id | texto | Identificador da revisao |
| entidade_tipo | texto | vocabulary_term, technical_concept, user_intent, fabric, style_reference |
| entidade_id | texto | ID revisado |
| parecer | enum | aprovado, revisar, fundir, separar, rejeitar |
| confianca | real | 0.0 a 1.0 |
| revisor | texto | Agente responsavel |
| observacao | texto | Justificativa curta |

## Regra de ouro

O banco nao deve guardar apenas palavras. Cada termo precisa ensinar o sistema a reconhecer forma, construcao, caimento e erro comum.

## Regra de QA visual

Todo termo usado para imagem deve alimentar [../../.claude/agents/references/image-quality-verification-layers.md](../../.claude/agents/references/image-quality-verification-layers.md). Para cada termo importante, declarar:

- o que precisa ficar alinhado;
- o que precisa estar visivel;
- que detalhe nao pode ser inventado;
- que erro reprova a imagem;
- que negativo deve entrar no prompt quando o termo for usado.
