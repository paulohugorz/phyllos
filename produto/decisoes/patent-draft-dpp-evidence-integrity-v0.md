# PHYLLOS — Rascunho de Depósito de Patente v0

**Título:** Sistema e Método para Geração de Passaporte Digital de Produto com Integridade de Evidência por Campo e Acesso Público sem Autenticação

**Data do rascunho:** 2026-06-27  
**Status:** rascunho interno — requer revisão de advogado de patentes antes de qualquer depósito  
**Referência competitiva:** BASF WO2025209938A1 (DPP + validação, identificadores descentralizados)  
**Diferencial central:** o P10 da BASF valida completude agregada de dados de fornecedores em rede. Este pedido protege a integridade de evidência por campo individual, o gate de publicação anti-greenwashing e o passaporte público plug-and-play acessível por buyer sem integração técnica.

---

## 1. Campo Técnico

A presente invenção refere-se a sistemas e métodos para geração, validação e publicação de passaportes digitais de produto (DPP) no setor de moda, vestuário e calçados, em particular a um mecanismo de tipagem de evidência por campo de dado, gate de publicação baseado em limiar de integridade de evidência, e interface pública acessível sem autenticação por qualquer parte interessada.

---

## 2. Antecedentes

### 2.1 O problema da assimetria de evidência em passaportes de produto

Regulações emergentes — incluindo a Portaria INMETRO 459/2025 (Brasil, calçados) e o Regulamento UE 2024/1781 (EU ESPR, têxtil) — exigem que marcas de moda publiquem dados técnicos de produto em formato digitalmente acessível. O descumprimento implica multas de até R$1,5M (INMETRO) e vedação à comercialização no mercado europeu (EU ESPR).

O problema central não é ausência de dados — a maioria das marcas possui fichas técnicas, especificações de material e registros de lote. O problema é a **assimetria de evidência**: dados declarados verbalmente pelo fornecedor, dados calculados por fórmula estimada e dados verificados por laudo independente são tratados como equivalentes nos sistemas existentes, criando risco regulatório e comercial.

### 2.2 Limitações das soluções existentes

Soluções existentes de DPP (incluindo WO2025209938A1, US12223513B2, US12482004B2) apresentam as seguintes limitações para o segmento de marcas de médio e pequeno porte:

(a) **Dependência de integração técnica**: exigem que fornecedores integrem APIs ou sistemas ERP para prover dados, inviabilizando adoção por pequenas marcas sem infraestrutura técnica.

(b) **Métrica de completude agregada**: calculam um percentual de campos preenchidos, sem diferenciar o grau de confiança de cada campo individualmente.

(c) **Passaporte restrito**: o acesso ao passaporte exige autenticação ou pertencimento a uma rede fechada, impedindo uso como credencial de negociação por buyers externos.

(d) **Ausência de gate anti-greenwashing por campo**: nenhum sistema existente bloqueia a publicação de um campo específico quando a evidência que o suporta não atinge o limiar mínimo declarado para aquele campo.

### 2.3 Necessidade não atendida

Existe necessidade de um sistema plug-and-play que permita a qualquer marca, sem integração técnica prévia, inserir dados de produto com tipagem de evidência individual por campo, obter validação contra perfis regulatórios específicos, e publicar um passaporte digitalmente acessível por qualquer buyer via URL permanente e código QR, onde cada campo exibe publicamente sua evidência de suporte.

---

## 3. Sumário da Invenção

A presente invenção provê:

**(a)** Um método para geração de passaporte digital de produto com integridade de evidência por campo, compreendendo: recebimento de entradas de dado de produto, cada entrada associada a um tipo de evidência selecionado de uma hierarquia de evidência predefinida; validação de cada entrada contra um perfil de conformidade regulatória que define campos obrigatórios e limiares mínimos de evidência por campo; bloqueio de publicação quando qualquer campo obrigatório não atinge o limiar mínimo; geração de registro de passaporte associando cada valor de dado ao seu tipo de evidência; publicação do registro em URL permanente acessível sem autenticação; e geração de identificador legível por máquina vinculado à URL permanente.

**(b)** Um sistema compreendendo processador, módulo de tipagem de evidência, motor de validação de perfil regulatório, repositório de passaportes imutável, servidor de página pública e gerador de identificador QR.

**(c)** Um meio legível por computador não transitório armazenando instruções executáveis para implementar o método descrito em (a).

O diferencial técnico central reside na combinação de: (i) tipagem de evidência aplicada individualmente por campo (não como métrica agregada); (ii) gate de publicação baseado em limiar de evidência mínima por campo obrigatório; e (iii) exposição pública do tipo de evidência de cada campo no passaporte acessível sem autenticação.

---

## 4. Descrição Detalhada

### 4.1 Hierarquia de evidência

A invenção define uma hierarquia de evidência ordenada com os seguintes níveis, em ordem crescente de confiança:

| Nível | Código | Definição |
|---|---|---|
| 0 | `ausente` | Dado não disponível — campo não publicado |
| 1 | `declarado` | Fornecedor ou marca informou verbalmente ou por documento não verificado |
| 2 | `calculado` | Derivado por fórmula determinística a partir de parâmetros documentados |
| 3 | `documentado` | Existe arquivo de suporte verificável (ficha técnica, nota fiscal, laudo) |
| 4 | `verificado` | Certificação ou laudo emitido por terceiro independente acreditado |

Cada campo de dado no passaporte recebe exatamente um tipo de evidência da hierarquia acima. O tipo de evidência viaja com o campo em todas as representações do passaporte — interna, pública e exportada.

### 4.2 Perfis de conformidade regulatória

O sistema mantém perfis de conformidade regulatória configuráveis. Cada perfil define:

- conjunto de campos obrigatórios para aquele perfil;
- limiar mínimo de evidência para cada campo obrigatório;
- identificador do instrumento regulatório de referência.

Exemplos de perfis implementados na V1:

**Perfil INMETRO-BR-459-2025 (calçados):**

| Campo | Limiar mínimo | Instrumento |
|---|---|---|
| Composição por parte (cabedal, forro, palmilha, solado) | `declarado` | Portaria INMETRO 459/2025 |
| GTIN (GS1) ou código interno | `declarado` | Portaria INMETRO 459/2025 |
| CNPJ do fabricante ou importador | `declarado` | Portaria INMETRO 459/2025 |
| País de fabricação | `declarado` | Portaria INMETRO 459/2025 |

**Perfil EU-ESPR-2024-1781-T1 (têxtil, Tier 1):**

| Campo | Limiar mínimo | Instrumento |
|---|---|---|
| Composição de fibras (% por fibra, soma = 100%) | `declarado` | Reg. UE 2024/1781 |
| País de fabricação | `declarado` | Reg. UE 2024/1781 |
| Instruções de cuidado | `declarado` | Reg. UE 2024/1781 |
| Identificador único de produto | `declarado` | Reg. UE 2024/1781 |

### 4.3 Gate de publicação

Antes de gerar o passaporte público, o sistema executa o seguinte algoritmo:

```
para cada campo_obrigatorio em perfil_selecionado:
    se tipo_evidencia(campo) < limiar_minimo(campo, perfil):
        bloquear_publicacao()
        retornar erro com: campo, tipo_atual, limiar_requerido
retornar autorizado_para_publicacao()
```

O gate é determinístico, auditável e não contornável via interface. Nenhum campo obrigatório pode ser publicado com evidência inferior ao limiar do perfil sem que o publicador seja explicitamente informado e confirme a lacuna como `ausente` (nível 0), resultando em campo não publicado.

### 4.4 Passaporte público plug-and-play

O passaporte publicado é acessível em URL permanente no formato:

```
https://{dominio}/p/{identificador-unico-de-produto}
```

A página pública:

(a) não requer autenticação de nenhuma parte para acesso de leitura;  
(b) exibe cada campo com seu valor e seu tipo de evidência visível;  
(c) exibe alerta visual para campos com evidência `declarado` ou `calculado` distinguindo-os de campos `verificado`;  
(d) não exibe campos com tipo `ausente` como valores numéricos ou textuais;  
(e) não exibe índice agregado, nota verde, score composto ou equivalente.

### 4.5 Identificador legível por máquina (QR)

O sistema gera um código QR seguindo o padrão GS1 Digital Link (ISO/IEC 18004), vinculando o GTIN ou identificador interno do produto à URL permanente do passaporte. O QR é gerado exclusivamente após aprovação do gate de publicação descrito em 4.3.

### 4.6 Plug-and-play para a marca (cliente)

O sistema provê interface de auto-serviço baseada em formulário web que não requer:
- integração de API;
- instalação de software;
- acesso a sistemas ERP, PLM ou CAD existentes da marca.

A marca insere dados manualmente ou por upload de arquivo estruturado (CSV, XLSX). O sistema normaliza os dados para o modelo interno, solicita tipagem de evidência para cada campo e executa o gate de publicação. O tempo estimado de onboarding para um passaporte Tier 1 é inferior a 60 minutos.

### 4.7 Plug-and-play para o buyer (consumidor da credencial)

O buyer acessa o passaporte por URL direta ou leitura de QR em dispositivo móvel. Nenhuma instalação de aplicativo, criação de conta ou autenticação é necessária. O passaporte é uma página web estática cacheada em CDN global com latência alvo inferior a 80ms para acesso de edge.

### 4.8 Repositório imutável e histórico de versões

Cada publicação gera uma versão imutável do passaporte com timestamp. Revisões posteriores criam novas versões sem apagar versões anteriores. O histórico completo de versões é preservado para fins regulatórios e de auditoria.

---

## 5. Reivindicações

### Reivindicação Independente 1 — Método

Um método implementado por computador para geração de passaporte digital de produto com integridade de evidência por campo, compreendendo:

(a) receber, por uma interface de auto-serviço sem exigência de integração de API, uma pluralidade de entradas de dado de produto, cada entrada compreendendo um valor de dado e um tipo de evidência selecionado pelo operador de uma hierarquia de evidência predefinida e ordenada;

(b) associar cada entrada de dado ao seu tipo de evidência em um registro interno;

(c) receber seleção de um perfil de conformidade regulatória, sendo o perfil definido por: conjunto de campos obrigatórios e limiar mínimo de evidência para cada campo obrigatório;

(d) executar, para cada campo obrigatório do perfil selecionado, uma verificação de integridade de evidência comparando o tipo de evidência da entrada com o limiar mínimo do perfil;

(e) bloquear geração do passaporte público quando qualquer campo obrigatório apresentar tipo de evidência inferior ao limiar mínimo correspondente, retornando identificação do campo, tipo atual e limiar requerido;

(f) quando todos os campos obrigatórios atenderem ao limiar mínimo, gerar registro de passaporte público associando cada valor de dado ao seu tipo de evidência;

(g) publicar o registro de passaporte em URL permanente acessível por qualquer agente sem autenticação, exibindo cada campo com seu valor e seu tipo de evidência visível;

(h) gerar identificador legível por máquina segundo padrão GS1 Digital Link vinculado à URL permanente do passaporte.

### Reivindicação Independente 2 — Sistema

Um sistema para geração de passaporte digital de produto com integridade de evidência por campo, compreendendo:

(a) uma interface de auto-serviço configurada para receber entradas de dado de produto com seleção de tipo de evidência por campo, sem exigência de integração de API por parte do operador;

(b) um módulo de tipagem de evidência configurado para associar cada campo de dado a exatamente um tipo de evidência de uma hierarquia predefinida de níveis ordenados;

(c) um motor de validação de perfil regulatório configurado para verificar, campo a campo, se o tipo de evidência atende ao limiar mínimo definido pelo perfil de conformidade selecionado;

(d) um gate de publicação configurado para bloquear geração do passaporte público quando qualquer campo obrigatório não atender ao limiar mínimo de evidência;

(e) um repositório de passaportes configurado para armazenar versões imutáveis de passaportes publicados com timestamp;

(f) um servidor de página pública configurado para servir o passaporte em URL permanente sem autenticação, exibindo cada campo com seu tipo de evidência;

(g) um gerador de identificador QR configurado para produzir código segundo padrão GS1 Digital Link após aprovação do gate de publicação.

### Reivindicação Independente 3 — Meio legível por computador

Um meio não transitório legível por computador armazenando instruções que, quando executadas por um processador, implementam o método da Reivindicação 1.

---

### Reivindicações Dependentes

**4.** O método da Reivindicação 1, em que a hierarquia de evidência compreende, em ordem crescente de confiança: ausente, declarado, calculado, documentado, verificado.

**5.** O método da Reivindicação 1, em que campos com tipo de evidência `ausente` não são exibidos como valores numéricos ou textuais na página pública.

**6.** O método da Reivindicação 1, em que campos com tipo de evidência `calculado` exibem, na página pública, a fórmula ou parâmetros utilizados no cálculo.

**7.** O método da Reivindicação 1, em que o perfil de conformidade regulatória referencia o instrumento normativo específico (número, órgão emissor e data de vigência) para cada campo obrigatório e limiar mínimo.

**8.** O método da Reivindicação 1, em que a página pública é servida por infraestrutura de distribuição de conteúdo (CDN) com latência alvo inferior a 80ms para acesso de borda, independentemente da localização geográfica do agente acessante.

**9.** O método da Reivindicação 1, compreendendo adicionalmente: armazenar cada versão publicada do passaporte em repositório imutável com timestamp, sem exclusão de versões anteriores, para fins de auditoria regulatória.

**10.** O método da Reivindicação 1, em que o identificador legível por máquina compreende código QR conforme ISO/IEC 18004 codificando URI no formato GS1 Digital Link.

**11.** O método da Reivindicação 1, em que a interface de auto-serviço aceita entrada manual por formulário web e/ou upload de arquivo estruturado nos formatos CSV ou XLSX, sem instalação de software adicional pelo operador.

**12.** O sistema da Reivindicação 2, em que o motor de validação suporta múltiplos perfis de conformidade regulatória simultaneamente, permitindo validação cruzada do mesmo passaporte contra diferentes instrumentos normativos.

**13.** O sistema da Reivindicação 2, em que a página pública não exibe índice agregado, pontuação composta, nota verde ou equivalente derivado da combinação de múltiplos campos de evidência.

**14.** O sistema da Reivindicação 2, em que revisões do passaporte geram novas versões imutáveis sem alteração das versões anteriores, sendo cada versão acessível por URL versionada.

---

## 6. Resumo (Abstract)

Sistema e método para geração de passaporte digital de produto com integridade de evidência por campo. Uma interface de auto-serviço recebe entradas de dado de produto, cada entrada associada a um tipo de evidência selecionado de uma hierarquia ordenada (ausente, declarado, calculado, documentado, verificado). Um motor de validação verifica, campo a campo, se o tipo de evidência de cada campo obrigatório atende ao limiar mínimo definido por um perfil de conformidade regulatória selecionado. Um gate de publicação bloqueia a geração do passaporte quando qualquer campo obrigatório não atinge o limiar mínimo. O passaporte aprovado é publicado em URL permanente acessível sem autenticação, com cada campo exibindo seu valor e tipo de evidência, e um código QR GS1 Digital Link é gerado vinculando o produto à URL pública. O sistema não requer integração técnica pelo operador (plug-and-play para marca) nem autenticação pelo acessante (plug-and-play para buyer).

---

## 7. Diferenciação do estado da técnica

| Característica | BASF WO2025209938A1 | IBM US12482004B2 | PHYLLOS (presente pedido) |
|---|---|---|---|
| Fluxo de dados | Pull de nós de fornecedor em rede | Foundation model para Scope 3 | Push por auto-serviço sem integração |
| Granularidade de evidência | Métrica de completude agregada (%) | N/A | Tipagem por campo individual |
| Gate de publicação | Por limiar de completude agregada | N/A | Por limiar de evidência por campo obrigatório |
| Acesso ao passaporte | Rede fechada / autenticado | N/A | URL pública sem autenticação, CDN global |
| Exposição de evidência | N/A | N/A | Tipo de evidência visível por campo na página pública |
| Setor | Baterias / químicos (industrial) | Geral (enterprise) | Moda, calçados, têxtil (SMB) |
| Integração requerida | API de fornecedor | ERP/dados financeiros | Nenhuma (formulário web ou upload CSV) |
| Índice agregado | Presente (completude %) | N/A | Ausente por design (anti-greenwashing) |

---

## 8. Notas para revisão jurídica

1. **Jurisdição prioritária:** Brasil (INPI) + PCT para cobertura EU/US. Prazo INPI para depósito prioritário: 12 meses a partir desta data.
2. **Busca de anterioridade adicional:** verificar WO2025209938A1 (claims completas via INPI/WIPO), US20220036273A1 (Siemens digital thread) e EP4369263A1 (ATS sensores).
3. **Prior art defensivo:** publicar white paper técnico descrevendo o mecanismo de Evidence Ledger antes do depósito para proteger contra reivindicações amplas do P10 BASF.
4. **Reivindicação mais defensável:** Reivindicação 1(d)+(e) — o gate por campo individual com retorno de campo+tipo+limiar é o diferencial mais distinto do estado da técnica.
5. **Reivindicação mais comercialmente relevante:** Reivindicação 1(g) — passaporte público sem autenticação com evidência visível por campo. É o produto que buyers usam em negociação.
6. **Risco:** se BASF P10 for concedido com reivindicação ampla cobrindo qualquer "validação de completude de DPP", a Reivindicação 1(d) pode precisar ser delimitada. A distinção técnica está em "por campo individual" vs "agregado".
