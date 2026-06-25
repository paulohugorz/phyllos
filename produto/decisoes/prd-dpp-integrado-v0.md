# PHYLLOS DPP Integrado - PRD v0

**Data:** 2026-06-25  
**Status:** rascunho executivo para execucao no Codex  
**Produto:** V1 - DPP middleware para moda  
**Fonte:** briefing consolidado no Claude em 2026-06-25, convertido em artefato operacional no repo

---

## 1. Problema

Marcas de moda produzem fichas tecnicas, especificacoes de material e dados de cadeia produtiva em silos separados. Falta uma camada acessivel que una esses arquivos, calcule indicadores por peca e publique um passaporte digital verificavel que o consumidor consiga ler.

A pressao regulatoria e comercial esta crescendo, mas marcas pequenas, medias e atelies nao tem estrutura para contratar consultorias caras ou operar ferramentas enterprise. O risco para a PHYLLOS e cair em dois extremos ruins: prometer sustentabilidade sem prova ou tentar construir um CAD/PLM completo antes de validar a dor.

## 2. Proposta de valor

PHYLLOS DPP Integrado transforma arquivos tecnicos de moda e especificacoes de produto em passaportes digitais verificaveis para pecas acabadas.

Entrada:

- ficha tecnica;
- especificacao de material;
- dados de lote;
- area tecnica por peca;
- perda de corte;
- fatores de impacto.

Saida:

- DPP interno;
- QR code por peca/lote;
- pagina publica com flashcards;
- status de evidencia visivel por campo;
- lacunas que impedem claim indevido.

## 3. Posicionamento

| Dimensao | Posicao |
|---|---|
| Categoria | DPP middleware para moda |
| Nao e | CAD, PLM, ERP, motor de moldes, ACV oficial, ferramenta de auditoria |
| Usuario primario | Gestor de produto ou founder de marca pequena-media |
| Caso de uso central | Publicar passaporte de uma peca com QR antes de colocar na etiqueta |
| Promessa controlada | Transparencia honesta sobre dados declarados, calculados, documentados e verificados |

## 4. Escopo da V1

Entra:

- input de arquivo tecnico via upload ou formulario manual;
- cadastro de produto: SKU, nome, categoria, lote, GTIN/codigo interno;
- cadastro de material: composicao, gramatura, fornecedor e certificacoes;
- area tecnica por peca;
- percentual de perda de corte;
- calculo deterministico por peca: peso, agua, energia e carbono;
- status de evidencia por campo;
- QR para pagina publica;
- flashcards para consumidor;
- dashboard interno simples de completude do DPP.

Nao entra:

- edicao de molde;
- ajuste de desenho;
- encaixe automatico;
- substituicao de Audaces, Lectra, Gerber, CLO, CAD, PLM ou ERP;
- ACV oficial ISO 14040/14044;
- auditoria ambiental;
- compliance juridico garantido;
- integracao automatica com sistemas externos;
- IA gerando claims de sustentabilidade.

## 5. ICP

### ICP primario

Marca de moda independente no Brasil, com lotes de 50 a 500 pecas por referencia.

Sinais:

- 1 a 5 pessoas no time;
- vende via Instagram, ecommerce proprio, marketplace ou loja pequena;
- ja recebe perguntas sobre origem, tecido e impacto;
- tem ficha tecnica parcial ou informacoes de fornecedor;
- quer diferenciar produto sem montar um PLM;
- aceita pagar por assinatura leve ou por passaporte publicado.

Job principal:

> Gerar um QR na etiqueta que prove o que a marca sabe sobre a peca, sem contratar uma consultoria de sustentabilidade.

### ICP secundario

Atelie ou estilista com producao terceirizada, lotes de 10 a 50 unidades e dados incompletos.

Job principal:

> Ter um documento honesto e publicavel mesmo quando parte dos dados ainda e declarada ou estimada.

### ICP futuro

Marketplace, plataforma B2B2C ou operador de moda que precisa padronizar DPPs de multiplos fornecedores via API.

## 6. Jornada do usuario

Fluxo linear do DPP Studio:

```text
1. Arquivo tecnico / especificacao
2. Cadastro do produto
3. Cadastro do material
4. Calculo de indicadores
5. Gestao de evidencias
6. Geracao do QR
7. Flashcards publicos
```

### Etapa 1 - Arquivo tecnico

O usuario faz upload de ficha tecnica, imagem, PDF, CSV ou preenche os campos basicos manualmente.

O sistema aceita ou registra:

- codigo da peca;
- nome;
- categoria;
- lote;
- area da peca em m2;
- percentual de perda de corte.

Regra: o sistema nao interpreta geometria de molde nem edita o arquivo. Area entra como dado declarado, documentado ou futuro parser.

### Etapa 2 - Produto

Campos:

- SKU/codigo interno;
- nome comercial;
- categoria;
- lote/quantidade;
- GTIN ou codigo interno gerado;
- pais de fabricacao declarado.

Regra: sem area da peca e sem quantidade do lote, o calculo nao avanca.

### Etapa 3 - Material

Campos:

- composicao de fibras com soma igual a 100%;
- gramatura em g/m2;
- fornecedor;
- pais do fornecedor;
- GLN quando houver;
- certificacoes;
- fatores de agua, energia e carbono.

Regra: se o usuario editar fator de impacto, o status do fator vira `declarado`. Se houver laudo ou documento, vira `documentado`.

### Etapa 4 - Calculo

Indicadores:

- area total requerida;
- area perdida no corte;
- peso da peca;
- agua estimada;
- energia estimada;
- carbono estimado.

Restricao: nao existe nota verde, score composto ou indice de sustentabilidade publico na V1.

### Etapa 5 - Evidencias

Estados possiveis:

- `ausente`;
- `declarado`;
- `calculado`;
- `documentado`;
- `verificado`.

Regra: o botao de publicar so habilita quando todos os campos obrigatorios estao pelo menos como `declarado`.

### Etapa 6 - QR

O sistema:

- confirma ou gera identificador publico;
- gera URL publica do DPP;
- gera QR em PNG/SVG;
- muda `dpp_status` para `publicado` apos confirmacao.

Regra: QR publico so deve ser impresso depois de dominio/rota publica testados.

### Etapa 7 - Flashcards publicos

A pagina publica mostra dados estruturados, cada um com badge de evidencia. Nao ha campo livre de marketing e nenhum indicador aparece sem contexto de origem.

## 7. Criterios de aceite do MVP

Funcionais:

- criar peca com area, lote e perda de corte;
- cadastrar material com composicao somando 100%;
- calcular indicadores com formula deterministica;
- persistir status de evidencia e impedir regressao indevida via UI;
- gerar QR somente com campos obrigatorios completos;
- carregar pagina publica sem login;
- revogar DPP sem apagar historico;
- exibir badge de evidencia em todo indicador publico.

Anti-greenwashing:

- indicador ausente nao aparece como numero;
- indicador calculado exibe nota de estimativa;
- score composto ou nota verde nao existe na V1 publica;
- usuario nao publica claim livre como "produto sustentavel";
- fator declarado pela marca exibe aviso de nao auditoria;
- certificacao expirada nao aparece como valida.

Performance:

- pagina publica em menos de 2s em rede lenta simulada;
- QR gerado em menos de 1s;
- calculo em menos de 200ms;
- cobertura minima de testes de 80% no modulo de calculo.

Validacao com dado real:

- ao menos 3 pecas reais passam pelo fluxo completo;
- ao menos 1 piloto confirma viabilidade de QR na etiqueta;
- nenhum piloto entende dado estimado como dado verificado.

## 8. Pilotos alvo

1. Marca slow fashion feminina em SP, com 2 fundadoras, lotes de 80 a 150 pecas e tecidos nacionais certificados.
2. Estilista independente com producao em faccao, lotes de 20 a 40 pecas e dados minimos.
3. Marca de athleisure/moda ativa no RJ, lotes de 200 a 500 pecas e composicao sintetica.
4. Cooperativa de costura com marca propria no Nordeste, lotes pequenos e cadeia social relevante.
5. Marca infantil premium em MG, lotes de 100 a 300 pecas, OEKO-TEX e interesse em exportacao.

## 9. Perguntas para entrevista

Contexto de dados:

- Quais documentos chegam junto com o tecido?
- Voce sabe a composicao exata das fibras?
- Voce tem a area de corte por peca?
- A perda de tecido e medida ou estimada?

Motivacao:

- Cliente ja perguntou origem, material ou impacto?
- Voce colocaria QR na etiqueta? O que impediria?
- Ja tentou calcular carbono ou agua por peca?

Fluxo:

- Em qual das 7 etapas voce travaria?
- Um badge "estimativa com fator padrao" seria aceitavel?
- O que a pagina publica precisa mostrar para representar sua marca?

Viabilidade:

- Quantas referencias novas voce lanca por colecao?
- Quem montaria o DPP?
- Quanto tempo por peca seria aceitavel?
- Qual preco faria sentido por mes ou por passaporte?

## 10. Observacoes regulatorio-juridicas

Este PRD usa regulacao como sinal de urgencia, nao como promessa de conformidade. Datas, interpretacoes e obrigacoes legais devem ser validadas com fonte oficial e/ou assessoria juridica antes de virar copy publica, contrato comercial ou requisito de compliance.

Na V1, a linguagem correta e:

> "Preparado para organizar dados de DPP e rastreabilidade."

Evitar:

> "Conforme a legislacao X" ou "DPP regulatorio garantido".
