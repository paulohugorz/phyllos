# PHYLLOS Fashion OS - Especializacao da Plataforma

Este documento orienta todos os agentes da PHYLLOS e do Fashion OS a partir de 2026-06-10. Ele deve ser usado junto com o racional de posicionamento vigente em `positioning-rationale-2026-06.md`.

## 1. Visao

A PHYLLOS e uma marca especializada em roupas femininas de alta versatilidade, unindo:

- elegancia;
- conforto;
- mobilidade;
- tecnologia textil;
- funcionalidade;
- longevidade;
- facilidade de manutencao.

O Fashion OS e o sistema operacional responsavel por transformar a intencao do usuario em:

1. imagem realista da peca;
2. especificacao tecnica;
3. modelagem parametrizada;
4. kit de producao;
5. documentacao completa;
6. molde em tamanho real para reproducao.

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

Objetivo: gerar fotografias que respeitem:

- peso;
- altura;
- proporcoes corporais;
- tecido;
- elasticidade;
- folgas de vestibilidade;
- caimento real.

Decisao vigente: o SVG local do Fashion OS e apenas rascunho tecnico/fallback offline. Imagem realista exige banco de termos de moda + prompt compiler + motor visual dedicado. Seguir `docs/decisoes/adr-001-motor-imagem-realista-fashion-os.md`, `data/fashion-taxonomy/schema.md` e `data/fashion-taxonomy/seed_terms.csv`.

Camadas obrigatorias:

1. Taxonomia de moda: tipos de peca, silhuetas, golas, mangas, bolsos, acabamentos, tecidos, texturas, modelagem e fit.
2. Prompt Compiler Fashion: converte ficha tecnica e termos curados em prompt positivo, prompt tecnico e prompt negativo.
3. Gerador visual: ComfyUI ou equivalente com workflow controlavel para foto/croqui realista.
4. QA de realismo: valida tecido, caimento, construcao, corpo, pose e coerencia PHYLLOS.

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

Transforma medidas + tecido + design + mobilidade em:

- molde parametrizado;
- margem de costura;
- piques;
- linha de fio;
- plano de corte.

## 10. Kit PHYLLOS

Apos aprovacao da imagem, o sistema deve gerar:

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

- Fase 1: imagem + ficha tecnica.
- Fase 2: Pattern Engine.
- Fase 3: PDF A4.
- Fase 4: biblioteca de tecidos.
- Fase 5: biblioteca de bases.
- Fase 6: prototipagem 3D.
- Fase 7: personalizacao completa.
- Fase 8: Atelier Digital Autonomo PHYLLOS.

## Regras de Uso para Agentes

1. Ao criar produto, imagem, ficha, molde, custo, briefing ou plano de producao, usar esta especializacao como fonte de verdade operacional.
2. Diferenciar prioridade de produto de promessa publica: nem todo atributo tecnico pode virar claim sem teste, documento ou evidencia.
3. Toda recomendacao de tecido deve explicar efeito em caimento, mobilidade, manutencao e longevidade.
4. Toda imagem gerada deve respeitar corpo, tecido, folga, elasticidade e caimento plausivel.
5. Toda ficha tecnica deve mirar o Kit PHYLLOS completo, ainda que a fase atual entregue apenas parte dele.
6. Toda decisao de roadmap deve respeitar a sequencia: imagem + ficha tecnica, Pattern Engine, PDF A4, biblioteca de tecidos, biblioteca de bases, prototipagem 3D, personalizacao completa e Atelier Digital Autonomo.
