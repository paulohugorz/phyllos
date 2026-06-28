# Tese de Produto - PHYLLOS DPP Integrado

**Data:** 2026-06-27 (revisada)
**Status:** tese de produto v0.4 - atualizada com novo posicionamento SaaS B2B, terminologia passaporte publico e blocos B0-B4
**Owner:** Founder / Product
**Escopo:** PHYLLOS DPP Studio — plataforma SaaS B2B de governança de dados ambientais para marcas de moda; compliance INMETRO/EU ESPR; acesso a buyers internacionais

---

## 1. Tese refinada

A PHYLLOS deve ser uma **camada de governança de dados ambientais para marcas de moda** — não uma ferramenta de modelagem, não uma calculadora, não um PLM.

> Posicionamento central: **de calcular para governar dados.**

O produto recebe dados técnicos que a marca já tem e os converte em passaporte digital verificável por SKU. Ele combina:

1. especificacoes do produto cadastrado;
2. dados vindos de arquivos de modelagem, encaixe, ficha tecnica ou planilhas;
3. calculos de area, consumo de materia-prima e perda — deterministicos e auditaveis;
4. indicadores de agua, energia, carbono com status de evidencia e rastreabilidade de fonte (unit_source);
5. passaporte publico por SKU com URL permanente acessado pelo buyer sem login.

A decisao critica da V1:

> PHYLLOS nao vai ajustar o desenho, editar molde ou substituir softwares de modelagem. Vai receber arquivos e especificacoes como entrada para calcular e publicar o DPP da peca.

Isso reduz risco tecnico, deixa o produto mais crivel e posiciona a PHYLLOS onde a dor de rastreabilidade aparece com mais clareza: a transformacao de dados tecnicos dispersos em informacao publicavel, auditavel e compreensivel.

---

## 2. Novo enquadramento

### 2.1 Antes

PHYLLOS como atelie virtual que ajuda a criar a peca, passar por modelagem, ficha tecnica, material e etiqueta.

### 2.2 Agora

PHYLLOS como **camada de governança de dados** que entra depois ou ao lado da modelagem, recebendo outputs tecnicos existentes e convertendo em:

- consumo material por peca;
- perda estimada ou medida;
- indicadores ambientais com unidade de fonte registrada (unit_source) e cadeia de evidencia auditavel;
- dados de composicao, origem e durabilidade;
- passaporte publico por SKU acessado pelo buyer;
- registro interno com status de evidencia por campo (ausente/declarado/calculado/documentado/verificado).

### 2.3 Frase de produto

> PHYLLOS transforma os dados tecnicos que a marca ja tem no passaporte digital que regulacao exige e buyers aceitam.

### 2.4 Categoria proposta

**Infraestrutura de compliance para moda.**

Mais especificamente:

> Uma camada de governança de dados ambientais — de calcular para governar.

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

**Marca de moda independente no Brasil que precisa publicar DPP por pressao regulatoria (INMETRO 31/07/2026) ou por exigencia de buyer internacional.**

Sinais:

- ja usa Audaces, Lectra, Gerber, CLO, Valentina, PDF, DXF, planilha ou ficha tecnica;
- exporta ou quer exportar para Europa/EUA; ou produz calcados e precisa cumprir INMETRO Portaria 459/2025;
- ja recebe perguntas de buyers sobre composicao, rastreabilidade e compliance;
- nao tem PLM enterprise;
- quer usar o DPP como credencial de negociacao, nao so como obrigacao legal;
- aceita pagar por passaporte publicado (R$149-299/DPP) ou assinatura (R$490/mes).

### 4.2 ICP secundario

**Fornecedor de materia-prima ou consultoria de produto que quer entregar dados prontos para DPP.**

### 4.3 ICP que sai da V1

Costureira iniciante que precisa criar molde do zero. Ela pode ser usuaria futura, mas a V1 nao deve depender dela porque o produto agora pressupoe algum arquivo tecnico ou especificacao de entrada.

---

## 5. Jobs to be Done

### JTBD principal

Quando tenho uma peca pronta para produzir ou vender, quero importar os arquivos/especificacoes tecnicas e publicar um passaporte digital com QR para o buyer, para transformar dados internos em credencial de compliance e negociacao sem montar um PLM.

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
- Indicadores derivados por kg/m2/unidade com unidade de fonte (unit_source) obrigatoria.
- Estados de evidencia por campo (ausente/declarado/calculado/documentado/verificado).
- Geracao de QR/passaporte em rascunho.
- Passaporte publico por SKU com URL permanente acessado pelo buyer sem login.
- Validacao INMETRO Tier 1: composicao, GTIN/codigo, CNPJ, pais de fabricacao.

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
  -> passaporte publico por SKU
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
| Passaporte publico por SKU (URL permanente) | buyer sem login |
| QR GS1 Digital Link por etiqueta | buyer e varejo |
| Status de evidencia por campo | buyer e marca |
| Relatorio de lacunas de compliance (INMETRO/EU ESPR) | marca |
| JSON/CSV e API (B3/B4) | integracoes e plataformas B2B |

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

## 9. Passaporte publico

O QR da etiqueta abre o passaporte publico da peca — a credencial que o buyer acessa durante negociacao, sem login.

O passaporte exibe dados estruturados, cada um com badge de evidencia visivel. Nenhum indicador aparece sem contexto de origem.

Campos obrigatorios visiveis:

1. **Composicao** — fibras com percentual, status declarado/documentado.
2. **Consumo de material** — area e peso por peca.
3. **Indicadores ambientais** — agua, energia, carbono com status (estimado/documentado/verificado) e fonte.
4. **Durabilidade e cuidado** — ciclos, lavagem, reparo.
5. **Origem e producao** — pais de fabricacao, fornecedor, lote quando publicavel.
6. **Nivel de transparencia** — o que esta documentado e o que ainda e declarado ou ausente.

Principio anti-greenwashing:

> Campo estimado exibe badge "estimativa calculada". Campo ausente nao aparece como numero. Score composto nao existe no passaporte.

**Feature B3 — "Como ler este passaporte":**

Accordion guiado com 7 perguntas que orientam o buyer antes de confiar em um numero: o que foi medido, qual metodologia, dado medido ou declarado, fonte e ano, contexto de lugar, comparabilidade e o que ficou de fora. As respostas vêm dos proprios campos — o accordion direciona o olhar, nao inventa dados.

---

## 10. Decisoes e por ques

| ID | Decisao | Por que | Trade-off | Guardrail |
|---|---|---|---|---|
| D01 | PHYLLOS sera camada de DPP integrada a ferramentas existentes | O mercado ja tem modelagem; falta traducao para DPP | Menos controle sobre origem do arquivo | Normalizar entradas e exigir fonte por campo |
| D02 | V1 nao edita molde/desenho | Reduz risco e acelera piloto | Produto parece menos "criador" | Valor precisa aparecer no DPP e nos calculos |
| D03 | Upload/input tecnico substitui motor parametrico na V1 | Usa dados reais do usuario | Parsers podem ser limitados | Permitir input manual quando parser falhar |
| D04 | Area e perda viram campos centrais | Sao ponte entre modelagem e indicadores | Dependem de qualidade do encaixe | Mostrar se dado e declarado, calculado ou medido |
| D05 | Indicadores sao derivados do material + consumo | Evita impacto generico por SKU | Requer banco de fatores por material | Comecar com fatores declarados e metodologia visivel |
| D06 | Passaporte publico e a experiencia do buyer | Buyer nao quer ficha tecnica bruta | Pode simplificar demais | Cada campo deve manter badge de evidencia visivel |
| D07 | DPP interno e mais completo que QR publico | Nem todo dado deve ser publicado | Exige camada de permissao | Campo publicavel deve ser separado do campo interno |
| D08 | "Sustentabilidade" nao sera claim automatico | Dado preenchido nao e prova | Marketing fica mais cuidadoso | Usar transparencia, cobertura e evidencia |
| D09 | Integracoes futuras, importacao manual agora | Garante MVP sem depender de APIs fechadas | Mais trabalho manual inicial | Medir quais arquivos mais aparecem nos pilotos |
| D10 | O produto calcula por peca, lote e material | DPP precisa ser especifico | Mais complexidade de granularidade | V1 pode usar modelo/lote; unidade vem depois |

---

## 11. MVP proposto

### 11.1 Fatia vertical

**Um produto cadastrado + um arquivo tecnico enviado + uma materia-prima com indicadores + calculo por peca + passaporte publico acessavel pelo buyer via QR.**

### 11.2 Fluxo V1

1. Criar produto.
2. Enviar arquivo tecnico ou preencher dados do arquivo.
3. Informar area da peca/encaixe.
4. Selecionar materia-prima cadastrada (com unit_source obrigatorio para cada fator).
5. Informar perda e quantidade.
6. Calcular indicadores deterministicos.
7. Revisar estados de evidencia — gate anti-greenwashing bloqueia publicacao se faltar campo obrigatorio.
8. Publicar QR GS1 Digital Link.
9. Acessar passaporte publico por URL permanente (sem login).

### 11.3 Criterio de sucesso

O MVP e promissor se 5 marcas/atelies conseguirem, com seus proprios dados:

- gerar um DPP em menos de 30 minutos;
- entender o que e calculado, declarado e ausente;
- usar o passaporte publico como pagina real de QR para negociacao com buyer;
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

O contrato de produto segue mirando a V1 completa de DPP middleware: arquivo tecnico, produto, material, lote, evidencia, QR publico e passaporte por SKU. O bundle atual e a interface de trabalho mais recente, nao a implementacao final de backend.

Nao deve mostrar:

- edicao de molde;
- geracao de molde;
- CAD interno;
- conformidade regulatoria garantida.

---

## 13. Roadmap — Blocos evolutivos

Referencia completa: `.claude/agents/references/product-blocks-allocation.md`

### B0 — Fundacao (Jun–Jul 2026)

- Backend FastAPI funcional: CRUD produto/material/DPP.
- Calculo deterministico com unit_source obrigatorio.
- Gate anti-greenwashing antes de publicar.
- Deploy Railway + Cloudflare na frente de URLs publicas.
- Supabase Pro (Free proibido em producao).

### B1 — Passaporte Minimo (Jul–Ago 2026)

- Passaporte publico por SKU com URL permanente (sem login para buyer).
- QR GS1 Digital Link funcional.
- Status de evidencia visivel em cada campo.
- Validacao INMETRO Tier 1: composicao, GTIN, CNPJ, pais de fabricacao.
- Piloto com 3–5 marcas, gratuito.

### B2 — Auto-servico (Set–Out 2026)

- Onboarding da marca sem assistencia do founder.
- Upload de ficha tecnica / CSV / planilha.
- Cobranca ativada: pay-per-DPP R$149–299.

### B3 — Retencao (2027)

- Assinatura R$490/mes.
- Faixa de incerteza por campo (uncertainty_range) visivel no passaporte.
- "Como ler este passaporte" — accordion guiado para buyer.
- Historico de versoes do DPP por lote.
- IBICT/ANA como fontes canonicas brasileiras sugeridas no onboarding.

### B4 — Plataforma (2028+)

- API B2B (USD 20K–200K/contrato).
- JSON-LD e GS1 Digital Link formal.
- Adequacao EU ESPR (~2028).
- Multitenancy para plataformas e associacoes de exportadores.

---

## 14. Implicacao estrategica

A PHYLLOS nao e uma calculadora de impacto. E uma camada de governança de dados ambientais.

A diferenca nao e semantica: calculadoras produzem numeros. Governança de dados produz rastreabilidade — de onde o numero veio, qual unidade a fonte usava, qual cadeia de evidencia sustenta a afirmacao, o que esta documentado e o que ainda e declarado.

Essa e a posicao defensavel a longo prazo porque:

- regulacao (INMETRO, EU ESPR) exige cadeia de evidencia, nao score;
- buyers sofisticados rejeitam numero sem origem;
- patente (claims 15-16) cobre uncertainty_range por campo e unit_source como atributo de primeiro nivel — prior art nao chega nessa granularidade;
- fontes canonicas brasileiras (IBICT, ANA) diferenciam do Higg MSI global sem substituir — complemento, nao concorrencia.

> Posicionamento: **de calcular para governar dados.**

Tese mais enxuta, mais vendavel, mais facil de validar e mais defensavel contra concorrentes de maior porte.
