# PHYLLOS Fashion OS - Especializacao da Plataforma

Este documento orienta todos os agentes da PHYLLOS e do Fashion OS. Ele deve ser usado junto com o racional de posicionamento vigente em `positioning-rationale-2026-06.md` e com as premissas estrategicas vigentes em `dpp-integrado-strategic-premises.md`.

## 0. Premissa vigente - 2026-06-23

O MVP imediato da PHYLLOS agora e o **DPP Integrado** descrito em `dpp-integrado-strategic-premises.md`.

O Fashion OS continua sendo a infraestrutura tecnica e operacional mais ampla, mas no curto prazo deve servir a um objetivo estreito: transformar arquivos tecnicos de moda, especificacoes de produto, dados de materia-prima, area, perda e fatores de impacto em um DPP publicavel com QR e flashcards para consumidor.

O Parametric Pattern Engine deixa de ser o primeiro produto da V1. Ele permanece como horizonte tecnico futuro ou camada de integracao, mas nao deve bloquear o MVP. A V1 nao edita molde, nao ajusta desenho e nao substitui ferramentas como Audaces, Lectra, Gerber, CLO, Valentina, CAD, PLM ou ERP.

Tudo que nao ajuda a importar/registrar dados tecnicos, calcular indicadores por peca, classificar evidencia e publicar flashcards fica subordinado: edicao de molde, criacao parametrica de desenho, preview de modelagem, MRP amplo, marketplace, agentes autonomos e SaaS completo sao horizontes posteriores, nao escopo de MVP.

## 1. Visao

A PHYLLOS opera em duas camadas:

1. **PHYLLOS Wear:** marca em desenvolvimento, usada como laboratorio de produto, criterio, linguagem e prova real.
2. **Fashion OS / DPP Studio:** infraestrutura tecnica para transformar especificacoes, arquivos tecnicos, materiais, lotes e evidencias em DPP interno, QR e flashcards publicos.

A camada de produto fisico da PHYLLOS segue priorizando roupas de alta versatilidade, unindo:

- elegancia;
- conforto;
- mobilidade;
- tecnologia textil;
- funcionalidade;
- longevidade;
- facilidade de manutencao.

No horizonte amplo, o Fashion OS e o sistema operacional responsavel por transformar dados tecnicos de produto em:

1. cadastro de produto, material, fornecedor, lote e evidencia;
2. ingestao de ficha tecnica, planilha, PDF, imagem ou arquivo de modelagem existente;
3. calculo de area, consumo, perda, peso e indicadores;
4. estados de evidencia por campo;
5. DPP interno, QR e pagina publica;
6. flashcards claros para consumidor;
7. integracoes futuras com CAD, PLM, ERP, imagem, modelagem e API.

No MVP atual, a ordem muda: **dados tecnicos antes de desenho, calculo deterministico antes de IA, evidencia antes de claim e QR/flashcards antes de plataforma ampla.**

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

Status estrategico: conhecimento de produto e modulo futuro/subordinado para a V1. O Fit Engine pode orientar leitura tecnica, criterios de produto e integracoes futuras, mas nao deve recolocar criacao ou ajuste de molde como escopo imediato.

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

Status estrategico: componente central para o DPP quando traduzido em propriedades mensuraveis, fatores de impacto, composicao, gramatura, origem, durabilidade e evidencia. Na V1, deve alimentar calculos e flashcards, nao um motor autonomo de modelagem.

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

- consumo, peso e perda por peca;
- indicadores de agua, energia e carbono;
- estados de evidencia;
- flashcards publicos;
- ficha tecnica, cuidados, durabilidade e, futuramente, molde, imagem e sequencia de costura.

## 8. Motor de Imagens

Status estrategico: componente futuro/subordinado. O Motor de Imagens nao e o MVP imediato. Ele so deve virar prioridade depois que o DPP Integrado provar uso real, valor para marcas/atelies e clareza para consumidores.

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

Status estrategico: horizonte futuro/integracao. O Pattern Engine nao e o MVP da V1 e nao deve bloquear DPP Studio, calculos, evidencia, QR ou flashcards.

Quando voltar ao roadmap, transforma `corpo 3D + tecido + design + mobilidade + construcao` em molde 2D parametrizado, validavel e graduavel. Na V1, o papel pratico deste conhecimento e ajudar agentes a entenderem arquivos de modelagem recebidos, limites de area/perda, termos tecnicos e riscos de interpretacao.

O Pattern Engine deve seguir a referencia profunda em [patternmaking-geometric-algorithmic-principles.md](patternmaking-geometric-algorithmic-principles.md), alem da sintese construtiva em [patternmaking-construction-techniques-marlene-mukai.md](patternmaking-construction-techniques-marlene-mukai.md).

Tese operacional futura:

- uma roupa e uma superficie flexivel que sai de um plano, envolve um volume e volta a ser plano quando aberta;
- pences, recortes, costuras, pregas, folgas, vies e elasticidade sao mecanismos para correlacionar volume 3D com molde 2D;
- toda linha de molde deve explicar qual volume, movimento, tecido ou operacao construtiva ela resolve;
- nenhum molde deve ser tratado como desenho solto: ele precisa de medidas finais, linha de fio, paineis, pontos de controle, margens, piques, validacao e regra de graduacao.

Entradas minimas para um modulo futuro de modelagem:

- medidas corporais e linhas de referencia;
- tecido, elasticidade, recuperacao, caimento, encolhimento e estabilidade;
- briefing de design, silhueta, grau de ajuste e componentes;
- movimentos obrigatorios;
- maquinario, costuras, margem e tolerancias de producao.

Saidas obrigatorias para um modulo futuro de modelagem:

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

No DPP Integrado, o Kit PHYLLOS deve ser reinterpretado como pacote de dados publicaveis e auditaveis. Apos cadastro do produto, ingestao tecnica e calculo, o sistema deve gerar:

- ficha tecnica ou resumo tecnico normalizado;
- lista de materiais, composicao, fornecedor e lote;
- area tecnica, consumo, perda e quantidade;
- indicadores por peca com status de evidencia;
- lacunas de dados;
- DPP interno;
- QR de etiqueta;
- flashcards publicos;
- exportacao JSON/CSV futura;
- anexos tecnicos preservados como evidencia.

## 11. Primeira Familia de Produtos

- PH001 - Calca Performance Alfaiataria.
- PH002 - Calca Dia a Dia.
- PH003 - Camisa Performance.
- PH004 - Vestido Versatil.
- PH005 - Saia Conforto.

## 12. Roadmap

- Fase 0: alinhamento da tese DPP, PRD, criterios de aceite e usuarios/piloto.
- Fase 1: DPP Studio navegavel canonico, schema conceitual, formulas, evidencia por campo e flashcards.
- Fase 2: backend interno com produto, material, arquivo tecnico, lote, indicador, DPP, flashcard e testes unitarios.
- Fase 3: studio interno com QR funcional, preview publico, lacunas e exportacao simples.
- Fase 4: piloto com 3 a 5 produtos reais, matriz de materiais, arquivos reais e relatorio de lacunas.
- Fase 5: beta privado com login, organizacao, historico, storage, logs e deploy controlado.
- Fase futura: parsers CSV/XLSX/PDF/DXF, integracoes CAD/PLM/ERP, Pattern Engine, Motor de Imagens, 3D, MRP, marketplace e API ampliada.

## Regras de Uso para Agentes

1. Ao criar produto, DPP, ficha, material, custo, briefing, plano de producao, conteudo, interface ou roadmap, usar esta especializacao junto com `dpp-integrado-strategic-premises.md` e `produto/decisoes/dpp-studio-versao-canonica-2026-06-25.md` como fonte de verdade operacional.
2. Diferenciar prioridade de produto de promessa publica: nem todo atributo tecnico pode virar claim sem teste, documento ou evidencia.
3. Toda recomendacao de tecido deve explicar efeito em caimento, mobilidade, manutencao e longevidade.
4. Toda decisao do MVP deve priorizar upload/input tecnico, cadastro de produto/material, calculos deterministicos, evidencia, QR e flashcards antes de imagem, dashboard amplo, linguagem natural, modelagem ou automacao extensa.
5. Toda ficha tecnica deve mirar o Kit PHYLLOS DPP completo, ainda que a fase atual entregue apenas parte dele.
6. Toda decisao de roadmap deve respeitar a sequencia vigente: alinhamento, prototipo canonico, backend MVP, studio interno, piloto, beta privado, depois parsers/integracoes.
7. Toda tarefa de modelagem deve ficar clara como suporte tecnico ou modulo futuro. Se envolver area/perda extraida de arquivo existente, declarar origem, premissa, unidade, lacuna e status de evidencia.
8. Nenhuma imagem pode virar referencia de produto sem passar pelas camadas de QA visual em [image-quality-verification-layers.md](image-quality-verification-layers.md). Falha critica de anatomia, alinhamento da roupa, fit/modelagem ou fidelidade reprova a imagem.
9. Nenhum indicador ambiental, social, tecnico ou de durabilidade deve ser publicado sem status: declarado, calculado, documentado, verificado ou indisponivel.
10. Nenhuma entrega deve trocar o bundle canonico `phyllos/dpp-studio.html` por uma versao anterior ou reconstruida sem nova decisao, novo hash e status de deploy.
