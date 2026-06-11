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
| use_case | imagem_editorial, croqui_tecnico, ficha_tecnica, modelagem |
| example_text | Exemplo curto |

## Regra de ouro

O banco nao deve guardar apenas palavras. Cada termo precisa ensinar o sistema a reconhecer forma, construcao, caimento e erro comum.
