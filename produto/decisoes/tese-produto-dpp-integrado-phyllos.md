# Tese de Produto - PHYLLOS DPP Integrado

**Data:** 2026-06-23
**Status:** tese de produto v0.3 - refinada apos adoção do bundle canonico do DPP Studio
**Owner:** Founder / Product
**Escopo:** PHYLLOS, Fashion OS, DPP, integracao com modelagem, indicadores de produto e experiencia de QR para consumidor

---

## 1. Tese refinada

A PHYLLOS deve ser um **software de DPP integrado ao workflow tecnico da moda**, nao uma ferramenta de modelagem propria na V1.

O produto se integra a ferramentas e arquivos ja usados por modelistas, marcas, atelies e faccoes para gerar um passaporte digital da peca acabada. Ele combina:

1. especificacoes do produto cadastrado;
2. dados vindos de arquivos de modelagem, encaixe, ficha tecnica ou planilhas;
3. calculos de area, consumo de materia-prima e perda;
4. indicadores de agua, energia, carbono, durabilidade e cobertura de dados;
5. flashcards publicos exibidos ao consumidor quando o QR da etiqueta e escaneado.

A decisao critica da V1:

> PHYLLOS nao vai ajustar o desenho, editar molde ou substituir softwares de modelagem. Vai receber arquivos e especificacoes como entrada para calcular e publicar o DPP da peca.

Isso reduz risco tecnico, deixa o produto mais crivel e posiciona a PHYLLOS onde a dor de rastreabilidade aparece com mais clareza: a transformacao de dados tecnicos dispersos em informacao publicavel, auditavel e compreensivel.

---

## 2. Novo enquadramento

### 2.1 Antes

PHYLLOS como atelie virtual que ajuda a criar a peca, passar por modelagem, ficha tecnica, material e etiqueta.

### 2.2 Agora

PHYLLOS como camada de DPP que entra **depois ou ao lado da modelagem**, recebendo os outputs tecnicos existentes e convertendo isso em:

- consumo material por peca;
- perda estimada ou medida;
- indicadores ambientais;
- dados de composicao, origem e durabilidade;
- flashcards de transparencia para o consumidor;
- registro interno com status de evidencia.

### 2.3 Frase de produto

> PHYLLOS transforma arquivos tecnicos de moda e especificacoes de produto em passaportes digitais verificaveis para pecas acabadas.

### 2.4 Categoria proposta

**DPP middleware para moda.**

Mais especificamente:

> Uma camada de traducao entre modelagem, ficha tecnica, materia-prima e consumidor.

---

## 3. Problema

### 3.1 Problema real

A cadeia de moda ja produz muitos dados tecnicos, mas eles ficam presos em formatos que nao conversam:

- arquivo de molde;
- arquivo de encaixe;
- ficha tecnica em PDF;
- planilha de consumo;
- cadastro de produto;
- certificado de material;
- nota/lote;
- etiqueta final;
- pagina de produto;
- relatorio de sustentabilidade.

O consumidor final ve quase nada disso. A marca ou atelie tambem tem dificuldade de reaproveitar os dados sem retrabalho.

### 3.2 Hipotese central

> A rastreabilidade nao falha apenas por falta de dado. Ela falha porque os dados tecnicos existentes nao sao normalizados, calculados e traduzidos em uma experiencia publica simples.

### 3.3 Dor para o usuario pagante

O usuario nao quer "mais uma ferramenta de desenho". Ele quer:

- importar ou informar dados que ja existem;
- calcular consumo e perda por peca;
- transformar especificacoes em indicadores;
- saber o que esta documentado, declarado ou ausente;
- publicar um QR confiavel na etiqueta;
- mostrar ao consumidor informacoes em linguagem clara;
- evitar greenwashing por excesso de promessa.

---

## 4. Usuario e ICP

### 4.1 ICP primario

**Pequena marca, atelie estruturado, faccao qualificada ou modelista tecnico que ja possui algum processo de modelagem/ficha tecnica.**

Sinais:

- ja usa Audaces, Lectra, Gerber, CLO, Valentina, PDF, DXF, planilha ou ficha tecnica;
- ja compra materia-prima com alguma especificacao;
- tem necessidade de comunicar composicao, origem, cuidado, durabilidade ou impacto;
- nao tem PLM enterprise;
- precisa gerar QR/passaporte por peca, modelo ou lote.

### 4.2 ICP secundario

**Fornecedor de materia-prima ou consultoria de produto que quer entregar dados prontos para DPP.**

### 4.3 ICP que sai da V1

Costureira iniciante que precisa criar molde do zero. Ela pode ser usuaria futura, mas a V1 nao deve depender dela porque o produto agora pressupoe algum arquivo tecnico ou especificacao de entrada.

---

## 5. Jobs to be Done

### JTBD principal

Quando tenho uma peca pronta para produzir ou vender, quero importar os arquivos/especificacoes tecnicas e gerar um QR com flashcards claros para o consumidor, para transformar dados internos em rastreabilidade publicavel sem montar um PLM.

### JTBDs secundarios

- Quando recebo um arquivo de modelagem/encaixe, quero extrair ou informar area, consumo e perda para calcular indicadores por peca.
- Quando cadastro um produto, quero puxar composicao, lote, fornecedor, cuidados e durabilidade para nao redigitar.
- Quando um dado e estimado, quero marcar como estimado para nao publicar como verificacao.
- Quando o consumidor escaneia o QR, quero que ele veja informacoes simples, nao um JSON tecnico.

---

## 6. Decisao de escopo da V1

### 6.1 Dentro

- Upload ou input manual de arquivo tecnico.
- Cadastro de produto e materia-prima.
- Area de molde ou area cortada por peca.
- Perda percentual ou perda calculada por encaixe.
- Consumo de materia-prima por peca.
- Indicadores derivados por kg/m2/unidade.
- Estados de evidencia por campo.
- Geracao de QR/passaporte em rascunho.
- Flashcards para consumidor.

### 6.2 Fora

- Editar molde.
- Ajustar desenho.
- Criar molde parametrico.
- Resolver encaixe automaticamente.
- Validar geometria de modelagem.
- Substituir CAD, PLM ou ERP.
- Declarar conformidade regulatoria sem validacao juridica.

### 6.3 Por que abrir mao da edicao de desenho

Essa decisao e boa porque:

- reduz risco tecnico da V1;
- evita competir com ferramentas maduras;
- permite vender valor usando arquivos que o usuario ja tem;
- coloca a PHYLLOS no ponto de maior dor: transformar dados dispersos em DPP;
- separa "calcular e comunicar" de "desenhar e modelar";
- torna o produto mais viavel para piloto rapido.

---

## 7. Modelo conceitual

```text
Arquivo tecnico / ficha / planilha
  -> normalizador de entradas
  -> produto cadastrado
  -> materia-prima e lote
  -> area + consumo + perda
  -> indicadores calculados
  -> estados de evidencia
  -> DPP interno
  -> QR
  -> flashcards publicos
```

### 7.1 Entradas aceitas na V1

| Entrada | Como entra | Uso |
|---|---|---|
| PDF de ficha tecnica | upload + campos manuais | identificar produto, materiais, cuidados |
| DXF/AAMA/ASTM | upload ou futuro parser | obter area de moldes quando disponivel |
| CSV/XLSX de encaixe | upload ou colagem | area, rendimento, perda, quantidade |
| Imagem/PDF de molde | upload + input manual | evidenciar arquivo tecnico, sem parser automatico |
| Cadastro de produto | formulario | composicao, lote, fornecedor, durabilidade |
| Cadastro de materia-prima | formulario | indicadores por kg/m2, agua, energia, carbono |

### 7.2 Saidas

| Saida | Usuario |
|---|---|
| DPP interno completo | marca/atelie |
| Flashcards publicos | consumidor |
| QR de etiqueta | consumidor e varejo |
| Relatorio de lacunas | time tecnico |
| JSON/CSV futuro | integracoes |

---

## 8. Calculo de indicadores

### 8.1 Nucleo do calculo

Cada peca tem:

- area tecnica da peca ou do encaixe;
- materia-prima selecionada;
- gramatura ou peso por metro;
- perda estimada ou medida;
- quantidade produzida;
- indicadores unitarios do material.

Com isso, a PHYLLOS calcula:

```text
area_total_requerida = area_peca / (1 - perda_pct)
area_perdida = area_total_requerida - area_peca
peso_peca = area_total_requerida * gramatura_kg_m2
agua_peca = peso_peca * agua_litros_kg
energia_peca = peso_peca * energia_kwh_kg
carbono_peca = peso_peca * carbono_kgco2e_kg
```

### 8.2 Indicadores iniciais

- Agua estimada por peca.
- Energia estimada por peca.
- Pegada de carbono estimada por peca.
- Peso de materia-prima por peca.
- Perda de corte por peca.
- Durabilidade declarada ou testada.
- Cobertura de dados.

### 8.3 Estados de confianca

| Estado | Significado |
|---|---|
| Ausente | dado nao informado |
| Declarado | informado por usuario/fornecedor |
| Calculado | derivado por formula documentada |
| Documentado | possui arquivo, nota, certificado ou laudo |
| Verificado | validado por regra, fonte externa ou auditoria |
| Publicavel | aprovado para aparecer no QR |

---

## 9. Flashcards do consumidor

O QR da etiqueta nao deve abrir uma ficha tecnica fria. Deve abrir um conjunto de flashcards claros:

1. **Do que esta peca e feita** - composicao e material principal.
2. **Quanto material ela usou** - area, peso ou consumo em linguagem simples.
3. **Perda de corte** - percentual e o que a marca faz com sobra, se houver dado.
4. **Indicadores estimados** - agua, energia e carbono com status "estimado" ou "verificado".
5. **Durabilidade e cuidado** - ciclos, lavagem, reparo.
6. **Origem e producao** - fornecedor, lote, etapa ou local quando publicavel.
7. **Nivel de transparencia** - o que esta documentado e o que ainda falta.

Principio:

> O consumidor deve entender a informacao em 30 segundos, sem precisar saber o que e DPP.

---

## 10. Decisoes e por ques

| ID | Decisao | Por que | Trade-off | Guardrail |
|---|---|---|---|---|
| D01 | PHYLLOS sera camada de DPP integrada a ferramentas existentes | O mercado ja tem modelagem; falta traducao para DPP | Menos controle sobre origem do arquivo | Normalizar entradas e exigir fonte por campo |
| D02 | V1 nao edita molde/desenho | Reduz risco e acelera piloto | Produto parece menos "criador" | Valor precisa aparecer no DPP e nos calculos |
| D03 | Upload/input tecnico substitui motor parametrico na V1 | Usa dados reais do usuario | Parsers podem ser limitados | Permitir input manual quando parser falhar |
| D04 | Area e perda viram campos centrais | Sao ponte entre modelagem e indicadores | Dependem de qualidade do encaixe | Mostrar se dado e declarado, calculado ou medido |
| D05 | Indicadores sao derivados do material + consumo | Evita impacto generico por SKU | Requer banco de fatores por material | Comecar com fatores declarados e metodologia visivel |
| D06 | Flashcards sao a experiencia publica | Consumidor nao quer ficha tecnica bruta | Pode simplificar demais | Cada card deve manter status de evidencia |
| D07 | DPP interno e mais completo que QR publico | Nem todo dado deve ser publicado | Exige camada de permissao | Campo publicavel deve ser separado do campo interno |
| D08 | "Sustentabilidade" nao sera claim automatico | Dado preenchido nao e prova | Marketing fica mais cuidadoso | Usar transparencia, cobertura e evidencia |
| D09 | Integracoes futuras, importacao manual agora | Garante MVP sem depender de APIs fechadas | Mais trabalho manual inicial | Medir quais arquivos mais aparecem nos pilotos |
| D10 | O produto calcula por peca, lote e material | DPP precisa ser especifico | Mais complexidade de granularidade | V1 pode usar modelo/lote; unidade vem depois |

---

## 11. MVP proposto

### 11.1 Fatia vertical

**Um produto cadastrado + um arquivo tecnico enviado + uma materia-prima com indicadores + calculo por peca + QR com flashcards.**

### 11.2 Fluxo V1

1. Criar produto.
2. Enviar arquivo tecnico ou preencher dados do arquivo.
3. Informar area da peca/encaixe.
4. Selecionar materia-prima cadastrada.
5. Informar perda e quantidade.
6. Calcular indicadores.
7. Revisar estados de evidencia.
8. Publicar QR de rascunho.
9. Ver flashcards do consumidor.

### 11.3 Criterio de sucesso

O MVP e promissor se 5 marcas/atelies conseguirem, com seus proprios dados:

- gerar um DPP em menos de 30 minutos;
- entender o que e calculado, declarado e ausente;
- usar os flashcards como pagina real de QR;
- identificar campos que hoje ficam perdidos entre modelagem e ficha tecnica;
- aceitar pagar para repetir o processo em mais pecas.

---

## 12. Prototipo

Prototipo canonico atual:

`phyllos/dpp-studio.html`

Decisao de versao:

- fonte de decisao: `produto/decisoes/dpp-studio-versao-canonica-2026-06-25.md`;
- arquivo de origem adotado: `/Users/paulonascimento/Downloads/dpp-studio.html`;
- hash SHA-256: `560add24d6e31860fee858805644270b31e030b0a5d0d5ab273d21d52194b8c2`;
- commit de adoção: `6559b48`.

O prototipo atual mostra:

- intencao da peca;
- tipo de peca;
- materiais e composicao;
- especificacoes dimensionais;
- area, massa e indicadores;
- dossie lateral;
- QR/passaporte em prototipo.

O contrato de produto segue mirando a V1 completa de DPP middleware: arquivo tecnico, produto, material, lote, evidencia, QR publico e flashcards. O bundle atual e a interface de trabalho mais recente, nao a implementacao final de backend.

Nao deve mostrar:

- edicao de molde;
- geracao de molde;
- CAD interno;
- conformidade regulatoria garantida.

---

## 13. Roadmap

### Fase 0 - Prototipo navegavel

- bundle canonico preservado;
- dados mockados/demonstrativos;
- calculos visiveis;
- dossie e QR/passaporte em prototipo;
- teste de entendimento;
- Netlify somente apos permissao e validacao da URL final.

### Fase 1 - MVP manual assistido

- upload de arquivos;
- input manual de area/perda;
- cadastro de materiais;
- fatores de impacto por material;
- QR publico;
- exportacao simples.

### Fase 2 - Parsers e integracoes

- leitura estruturada de CSV/XLSX;
- leitura parcial de DXF/AAMA/ASTM quando possivel;
- conectores para ferramentas ou exports recorrentes;
- versoes de DPP por lote.

### Fase 3 - Passport-ready

- identificadores formais;
- JSON-LD;
- permissao de publicacao por campo;
- assinatura/verificacao;
- adequacao juridica por mercado.

---

## 14. Implicacao estrategica

Essa mudanca melhora a tese porque a PHYLLOS deixa de tentar resolver modelagem e rastreabilidade ao mesmo tempo.

O foco passa a ser:

> Capturar o dado tecnico onde ele ja nasce, calcular o que ainda nao esta claro e traduzir tudo em uma experiencia de transparencia para quem compra a peca.

Essa e uma tese mais enxuta, mais vendavel e mais facil de validar.
