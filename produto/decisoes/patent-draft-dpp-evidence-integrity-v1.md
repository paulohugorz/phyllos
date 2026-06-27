# PHYLLOS — Pedido de Patente: Rascunho v1

**Título:** Sistema e Método para Geração de Passaporte Digital de Produto com Tipagem de Evidência por Campo, Gate de Publicação por Integridade de Evidência e Acesso Público sem Autenticação

**Data:** 2026-06-27  
**Versão:** v1 — inclui revisão do estado da técnica e argumento de caráter inventivo  
**Status:** rascunho interno — requer revisão de advogado de patentes antes de qualquer depósito  
**Jurisdição pretendida:** Brasil (INPI, prioridade) + PCT (cobertura EU/US/CN)

---

## 1. Campo Técnico

A presente invenção refere-se a sistemas e métodos implementados por computador para geração, validação e publicação de passaportes digitais de produto (DPP) aplicados ao setor de moda, vestuário e calçados. Em particular, a invenção protege: (i) um mecanismo de tipagem de evidência aplicado individualmente a cada campo de dado do passaporte, representando o grau de confiança da informação; (ii) um gate de publicação que bloqueia a geração do passaporte público quando qualquer campo obrigatório não atinge o limiar mínimo de evidência definido pelo perfil regulatório aplicável; e (iii) uma interface pública acessível sem autenticação na qual cada campo exibe, juntamente com seu valor, o tipo de evidência que o suporta. A invenção é aplicável a qualquer regime regulatório que exija publicação de dados técnicos de produto com rastreabilidade de origem e grau de confiança, incluindo mas não se limitando à Portaria INMETRO 459/2025 (Brasil) e ao Regulamento UE 2024/1781 (EU ESPR).

---

## 2. Antecedentes e Revisão do Estado da Técnica

### 2.1 Contexto regulatório

A proliferação de regulações de transparência de produto criou demanda por sistemas que permitam marcas publicar dados técnicos de produto em formato digitalmente acessível e rastreável. A Portaria INMETRO 459/2025 (Brasil) exige, para calçados, a publicação de composição por parte (cabedal, forro, palmilha, solado), GTIN, CNPJ e país de fabricação em formato acessível por código QR, com prazo de 31 de julho de 2026 para fabricantes e importadores e penalidade de até R$1,5M por não conformidade. O Regulamento UE 2024/1781 (EU ESPR) estende exigência equivalente ao setor têxtil para o mercado europeu, com entrada em vigor prevista para 2028. A Diretiva EU 2024/825 (Green Claims Directive) proíbe explicitamente alegações ambientais não substantiadas por evidência verificável.

O crescimento da literatura científica sobre passaportes digitais de produto confirma a aceleração do campo: de 1 publicação em 2019 para 210 em 2025, representando crescimento de 20.900% em seis anos (OpenAlex, 2026-06-27).

### 2.2 Análise do estado da técnica

A seguir apresenta-se a revisão crítica dos documentos mais relevantes do estado da técnica, com análise das limitações técnicas de cada um em relação ao problema resolvido pela presente invenção.

---

#### 2.2.1 WO2025209938A1 — BASF SE (2024)

**Campo:** Sistema para geração de passaporte de produto com validação por regras em rede descentralizada de fornecedores.

**Arquitetura:** O sistema coleta dados de produção de nós de rede de fornecedores (modelo pull) usando identificadores digitais de produto como chaves de busca. Um motor de validação por regras verifica se os dados coletados correspondem a um modelo semântico de dados predefinido. O sistema calcula uma "métrica de completude de dados" que indica o percentual de campos do modelo semântico preenchidos com dados validados.

**Mecanismo de validação:** O motor aplica regras derivadas do modelo semântico. A validação é binária: cada campo passa ou falha a regra. Não há mecanismo de graduação da qualidade ou confiança do dado dentro de um campo que passou a validação. A especificação confirma explicitamente: *"No explicit confidence scoring, probability distributions, or Bayesian uncertainty quantification mechanisms are described. The approach relies on binary validation (pass/fail) against rules rather than graduated confidence assessment."*

**Completude:** Calculada como percentual agregado de campos preenchidos. Um campo preenchido com dado declarado verbalmente pelo fornecedor e um campo preenchido com dado certificado por terceiro independente contribuem de forma idêntica para a métrica de completude. O sistema não distingue entre esses casos.

**Acesso ao passaporte:** O sistema opera em rede fechada de fornecedores integrados. Não há descrição de URL pública acessível sem autenticação por partes externas (buyers, reguladores, consumidores).

**Integração requerida:** Fornecedores precisam integrar o sistema via identificadores de rede e prover dados no formato do modelo semântico. Não existe modalidade de auto-serviço por formulário web sem integração técnica.

**Setor de aplicação primário:** Baterias e químicos industriais. A aplicação prática descrita no documento é a cadeia de fornecimento de baterias.

**Limitações relevantes para o problema aqui resolvido:**
- Não diferencia a qualidade de evidência de campos individuais
- Não bloqueia publicação de campo específico com base no grau de confiança
- Não expõe o tipo de evidência de cada campo para partes externas
- Exige integração técnica de todos os participantes da cadeia
- Não provê acesso público sem autenticação

---

#### 2.2.2 US12223513B2 — BASF SE (2020)

**Campo:** Método para determinação de pegada de carbono de produto em processos de produção interconectados.

**Arquitetura:** Integração com ERP para coleta de dados de processo em tempo real. Propagação de PCF por grafo de processos: matérias-primas → passos de processo → intermediários → produto. Alocação proporcional de emissões entre coprodutos com base em razões de uso.

**Mecanismo de confiança:** O sistema opera sobre dados medidos em planta industrial via sensores e ERP. A confiança dos dados é implícita à integração — dados vêm de sistemas automatizados com medição direta, não de declarações humanas. Não existe mecanismo para lidar com dados de diferentes qualidades de origem dentro do mesmo cálculo.

**Limitações relevantes:** Voltado exclusivamente a plantas industriais com ERP integrado. Não aplicável a pequenas e médias marcas de moda sem infraestrutura de medição. Não resolve o problema de dados de cadeia de fornecimento com qualidade heterogênea (fornecedor A tem laudo, fornecedor B declarou verbalmente).

---

#### 2.2.3 US12482004B2 — IBM Corporation (2023)

**Campo:** Estimação de emissões Scope 3 por modelo de linguagem de grande escala (foundation model).

**Arquitetura:** Geração de embeddings multidimensionais (financeiro, setorial, geográfico, temporal) a partir de dados de transações financeiras e metadados empresariais. Treinamento de modelo NLP especializado com função de perda ponderada por intensidade de carbono por setor.

**Mecanismo de confiança:** O sistema trata incerteza como problema de inferência estatística — reduz incerteza pela qualidade dos embeddings de treinamento e pela ponderação da função de perda. A "confiança" é um produto emergente do modelo, não um atributo explícito associado a campos de dado individuais providos pelo usuário.

**Limitações relevantes:** Não resolve o problema de transparência de evidência de dados de produto para partes externas. O sistema estima emissões automaticamente, enquanto a presente invenção registra e expõe o grau de confiança de dados declarados pelo próprio operador. São problemas fundamentalmente diferentes: estimação vs. integridade de proveniência declarada.

---

#### 2.2.4 EP4369263A1 — ATS Automation Tooling Systems Inc. (2022)

**Campo:** Monitoramento de PCF por unidade de produto em sistemas de automação de montagem.

**Arquitetura:** Sensores de contagem de produto e de consumo de energia em linhas de montagem. Cálculo de PCF por unidade = emissões totais / unidades montadas. Incorporação de pegada de carbono de componentes.

**Mecanismo de confiança:** Os dados são medidos por sensores físicos em tempo real. Não há mecanismo de tipagem de qualidade de dado — a confiança é intrínseca à medição automatizada.

**Limitações relevantes:** Aplicável exclusivamente a processos industriais automatizados com sensores físicos. Não resolve o problema de dados de produto provenientes de múltiplas fontes com qualidades heterogêneas, que é o caso central de marcas de moda com fornecedores sem infraestrutura de medição.

---

#### 2.2.5 WO2012154267A1 — Enviance Inc. (2011)

**Campo:** Avaliação de impacto ambiental integrada com análise de custo financeiro (IHLCA + EVE).

**Arquitetura:** Conversão de fluxos LCA em valores monetários por três dimensões de custo (societal, interno atual, interno futuro). Biblioteca dinâmica de mitigação alimentada por dados reais de múltiplas organizações.

**Mecanismo de validação de dados:** O sistema valida que os dados de operação medidos correspondem às reduções esperadas. A validação é retrospectiva (confirma que a mitigação ocorreu) e não prospectiva (não impede publicação de dados não substantiados).

**Limitações relevantes:** Não existe mecanismo de passaporte público por produto. O sistema produz relatórios organizacionais de impacto, não passaportes digitais individuais por SKU com acesso por QR.

---

#### 2.2.6 US20220036273A1 — Siemens AG + University of Kentucky (2019, abandonado)

**Campo:** Digital thread conectando repositórios de produto ao longo de múltiplos ciclos de vida.

**Limitações relevantes:** Abandonado. Voltado a produtos complexos de engenharia (não moda). Não resolve o problema de acesso público sem autenticação nem tipagem de evidência por campo.

---

### 2.3 Problema técnico não resolvido pelo estado da técnica

A análise dos documentos acima revela uma lacuna técnica comum a todos: **nenhum sistema existente diferencia, em nível de campo individual, o grau de confiança da informação que suporta aquele campo, nem usa essa diferenciação como condição de bloqueio de publicação ou como atributo exibido publicamente ao receptor da credencial.**

O problema técnico central é o seguinte:

Nos sistemas do estado da técnica, um campo de dado em um passaporte de produto é tratado como preenchido ou não preenchido (validação binária). Uma composição de fibra declarada verbalmente pelo fornecedor sem documento de suporte e uma composição certificada por laudo acreditado independente recebem tratamento idêntico no modelo de dados: ambas contribuem igualmente para a métrica de completude; ambas habilitam a publicação do campo; ambas aparecem com igual peso visual para o receptor da credencial.

Este tratamento cria os seguintes efeitos técnicos indesejados:

**(a) Impossibilidade de validação regulatória por grau de confiança:** Regulações como EU ESPR e INMETRO não apenas exigem que o campo exista, mas que a informação seja rastreável e verificável. Um sistema que trata dados declarados e verificados como equivalentes não pode suportar validação de conformidade regulatória real.

**(b) Propagação de greenwashing estrutural:** Marcas podem publicar passaportes com alegações ambientais baseadas em dados apenas declarados, sem qualquer indicação ao receptor de que a informação não foi verificada. A Diretiva EU 2024/825 (Green Claims) proíbe explicitamente essa prática, mas os sistemas existentes não a impedem estruturalmente.

**(c) Ausência de mecanismo plug-and-play para marcas sem integração técnica:** Todos os sistemas identificados exigem integração de API, ERP ou sensores físicos. Marcas de pequeno e médio porte no setor de moda não possuem infraestrutura técnica para essas integrações, excluindo-as do acesso a DPP mesmo quando possuem os dados necessários.

**(d) Passaporte inacessível ao receptor da credencial sem autenticação:** Buyers internacionais que recebem um produto com QR precisam acessar o passaporte em qualquer dispositivo, sem criar conta ou instalar aplicativo. Nenhum sistema existente provê esse acesso com exposição simultânea do tipo de evidência por campo.

---

## 3. Descrição da Invenção

### 3.1 Sumário

A presente invenção resolve o problema técnico descrito na seção 2.3 por meio de três componentes técnicos que, em combinação, produzem efeito técnico novo não sugerido pelo estado da técnica:

**Componente 1 — Tipagem de evidência por campo:** Cada campo de dado do passaporte recebe, no momento da entrada pelo operador, um tipo de evidência extraído de uma hierarquia predefinida e ordenada. O tipo de evidência é um atributo de primeira classe do campo — não é inferido, calculado ou agregado. É declarado explicitamente para cada campo individualmente.

**Componente 2 — Gate de publicação por integridade de evidência:** Antes de gerar o passaporte público, o sistema executa, para cada campo obrigatório definido pelo perfil regulatório selecionado, uma verificação de limiar mínimo de evidência. O passaporte é bloqueado se qualquer campo obrigatório apresentar tipo de evidência inferior ao limiar. O desbloqueio exige que o operador ou eleve o tipo de evidência (fornecendo suporte documental) ou declare explicitamente o campo como `ausente`, resultando em não publicação daquele campo específico.

**Componente 3 — Passaporte público com evidência visível e acesso sem autenticação:** O passaporte publicado é servido em URL permanente acessível por qualquer agente sem autenticação. Cada campo exibe seu valor e seu tipo de evidência de forma visível. Campos `ausente` não aparecem como valores numéricos ou textuais. Campos `calculado` exibem a fórmula ou parâmetros que os geraram. Campos `declarado` exibem alerta diferenciando-os de `verificado`.

O efeito técnico da combinação é: **prevenção estrutural de greenwashing no nível do modelo de dados** — não no nível da apresentação visual ou da política de uso. Um campo não pode ser publicado com grau de confiança superior ao que sua evidência suporta, independentemente da intenção do operador.

### 3.2 Hierarquia de evidência

A hierarquia de evidência compreende os seguintes níveis, em ordem estritamente crescente de confiança:

| Nível | Código | Definição técnica |
|---|---|---|
| 0 | `ausente` | Dado não disponível. Campo não publicado no passaporte público. |
| 1 | `declarado` | Fornecedor ou marca informou o valor sem documento de suporte verificável. |
| 2 | `calculado` | Valor derivado por fórmula determinística a partir de parâmetros com evidência ≥ 1. A fórmula e os parâmetros são armazenados e exibidos. |
| 3 | `documentado` | Existe arquivo de suporte verificável associado ao campo (ficha técnica, nota fiscal, laudo interno, certificado de fornecedor não acreditado). |
| 4 | `verificado` | Certificação ou laudo emitido por organismo de avaliação da conformidade acreditado por organismo nacional de acreditação reconhecido. |

A hierarquia é estritamente ordinal: `ausente` < `declarado` < `calculado` < `documentado` < `verificado`. Operações de comparação entre tipos de evidência usam essa ordem.

**Propriedades da hierarquia:**
- Cada campo recebe exatamente um tipo de evidência
- O tipo de evidência não pode ser promovido sem ação explícita do operador (fornecimento de documento ou certificado)
- O sistema não infere, estima ou agrega tipos de evidência

### 3.3 Perfis de conformidade regulatória

Um perfil de conformidade regulatória é uma estrutura de dados que define:

```
perfil = {
  id: string,                          // identificador único do perfil
  instrumento: {                       // referência regulatória
    nome: string,
    orgao_emissor: string,
    numero: string,
    data_vigencia: date
  },
  campos_obrigatorios: [
    {
      campo_id: string,
      limiar_minimo_evidencia: integer  // valor da hierarquia (0–4)
    }
  ]
}
```

O sistema mantém um repositório de perfis configuráveis. Perfis predefinidos incluem:

**INMETRO-BR-459-2025** (calçados, fabricantes/importadores, prazo 31/07/2026):

| campo_id | limiar_minimo_evidencia | código |
|---|---|---|
| composicao_cabedal | 1 | declarado |
| composicao_forro | 1 | declarado |
| composicao_palmilha | 1 | declarado |
| composicao_solado | 1 | declarado |
| gtin_ou_codigo_interno | 1 | declarado |
| cnpj_fabricante_importador | 1 | declarado |
| pais_fabricacao | 1 | declarado |

**EU-ESPR-2024-1781-TEXTIL-T1** (vestuário, exportadores, preparo para 2028):

| campo_id | limiar_minimo_evidencia | código |
|---|---|---|
| composicao_fibras | 1 | declarado |
| soma_composicao_igual_100pct | 2 | calculado |
| pais_fabricacao | 1 | declarado |
| instrucoes_cuidado | 1 | declarado |
| identificador_unico_produto | 1 | declarado |

Perfis adicionais podem ser criados pelo operador do sistema ou por autoridades regulatórias que integrem a plataforma via API de perfis.

### 3.4 Gate de publicação — especificação algorítmica

```
função gate_publicacao(passaporte, perfil):
  erros = []
  
  para cada campo_req em perfil.campos_obrigatorios:
    campo = passaporte.obter_campo(campo_req.campo_id)
    
    se campo é nulo:
      erros.adicionar({
        campo: campo_req.campo_id,
        tipo_atual: "ausente",
        limiar_requerido: campo_req.limiar_minimo_evidencia,
        acao_requerida: "inserir dado ou confirmar ausência explícita"
      })
    senão se campo.tipo_evidencia < campo_req.limiar_minimo_evidencia:
      erros.adicionar({
        campo: campo_req.campo_id,
        tipo_atual: campo.tipo_evidencia,
        limiar_requerido: campo_req.limiar_minimo_evidencia,
        acao_requerida: "elevar evidência ou confirmar ausência explícita"
      })
  
  se erros não está vazio:
    retornar { autorizado: falso, erros: erros }
  
  retornar { autorizado: verdadeiro }
```

O gate é:
- **Determinístico:** para o mesmo conjunto de dados e perfil, sempre produz o mesmo resultado
- **Auditável:** todos os resultados do gate são armazenados com timestamp no audit log imutável
- **Não contornável:** a interface de publicação não expõe mecanismo de bypass do gate
- **Granular:** identifica especificamente qual campo falhou, com qual tipo de evidência e qual limiar é requerido

### 3.5 Modelo de dados do passaporte

```
passaporte = {
  id: uuid,
  versao: integer,
  timestamp_publicacao: datetime,
  perfis_validados: [perfil_id],
  campos: [
    {
      campo_id: string,
      valor: any,
      tipo_evidencia: integer (0–4),
      metadata_evidencia: {
        documento_id: string | null,    // referência ao arquivo de suporte
        formula: string | null,         // para tipo calculado
        certificado_id: string | null,  // para tipo verificado
        declarado_por: string | null    // para tipo declarado
      }
    }
  ],
  gate_resultado: {
    autorizado: boolean,
    timestamp: datetime,
    perfil_id: string
  },
  qr: {
    uri_gs1_digital_link: string,
    formato: "ISO/IEC 18004",
    imagem_png_base64: string
  }
}
```

### 3.6 Interface de auto-serviço (plug-and-play para marca)

A interface de auto-serviço é uma aplicação web que aceita entrada de dados de produto sem exigir do operador:
- Instalação de software no dispositivo do operador
- Integração de API com sistemas existentes da marca
- Acesso a ERP, PLM, CAD ou qualquer outro sistema empresarial
- Conhecimento técnico além de operação de formulário web

O operador insere dados por formulário web ou por upload de arquivo estruturado (CSV ou XLSX). Para cada campo, o sistema solicita explicitamente que o operador selecione o tipo de evidência correspondente, apresentando a definição de cada nível em linguagem não técnica.

O tempo de onboarding para um passaporte Tier 1 (perfil INMETRO-BR-459-2025) é estimado em menos de 60 minutos por SKU para um operador sem experiência prévia com o sistema.

### 3.7 Passaporte público (plug-and-play para buyer)

O passaporte publicado é acessível em:

```
https://{domínio}/p/{identificador-único-de-produto}
```

Propriedades técnicas da página pública:
- **Sem autenticação:** qualquer agente com a URL ou QR acessa a página sem criar conta
- **Evidência visível:** cada campo exibe seu valor e seu tipo de evidência em representação visual diferenciada
- **Campos ausentes não publicados:** campos com tipo `ausente` não aparecem na página pública como valores ou indicadores
- **Calculados com fórmula:** campos com tipo `calculado` exibem a expressão e os parâmetros utilizados
- **Sem score agregado:** a página não exibe índice composto, nota ambiental, score verde ou equivalente
- **CDN global:** a página é cacheada em infraestrutura de distribuição de conteúdo com latência alvo < 80ms para acesso de edge em qualquer localização geográfica
- **URL permanente:** a URL permanece válida independentemente de alterações subsequentes ao passaporte, que geram novas versões acessíveis por URLs versionadas

### 3.8 Repositório imutável e histórico de versões

Cada publicação de passaporte gera uma versão imutável com timestamp. Versões anteriores são preservadas integralmente. O histórico completo é acessível para fins de auditoria regulatória e de due diligence comercial. Nenhuma versão pode ser alterada após publicação — apenas novas versões podem ser criadas.

---

## 4. Argumento de Caráter Inventivo

### 4.1 Identificação da combinação inventiva

O caráter inventivo da presente invenção reside na combinação dos três componentes descritos na seção 3.1. Cada componente individualmente poderia ser considerado óbvio por um técnico no assunto. A combinação, porém, produz efeito técnico que não é sugerido nem tornada óbvia por qualquer documento do estado da técnica ou por qualquer combinação de documentos do estado da técnica.

### 4.2 Diferença técnica em relação ao documento mais próximo (WO2025209938A1)

O documento mais próximo do estado da técnica é WO2025209938A1 (BASF, 2024), que também se refere à geração de passaportes de produto com validação de dados.

**Diferenças técnicas específicas:**

| Característica | WO2025209938A1 | Presente invenção |
|---|---|---|
| Tipo de validação | Binária (pass/fail por regra) | Ordinal (tipo de evidência 0–4 por campo) |
| Granularidade de qualidade | Completude agregada (%) | Tipo de evidência individual por campo |
| Gate de publicação | Por limiar de completude agregada | Por limiar de evidência de cada campo obrigatório individualmente |
| Tratamento de dado declarado vs. verificado | Idêntico (ambos contam como preenchidos) | Diferenciado (limiar mínimo pode exigir documentado ou verificado para campos específicos) |
| Exposição da qualidade do dado | Não descrita | Tipo de evidência visível por campo na página pública |
| Acesso ao passaporte | Rede fechada de fornecedores integrados | URL pública sem autenticação, CDN global |
| Exigência de integração | API de fornecedor na rede | Nenhuma (formulário web ou upload CSV) |
| Score agregado | Completude % como output | Ausente por design |

### 4.3 Efeito técnico da diferença

A diferença técnica entre validação binária com completude agregada (P10) e tipagem ordinal de evidência por campo (presente invenção) produz o seguinte efeito técnico específico:

**Prevenção estrutural de greenwashing em nível de modelo de dados.** No sistema P10, um campo preenchido com dado `declarado` e um campo preenchido com dado `verificado` são indistinguíveis na saída do sistema (ambos contribuem para completude = 100% para aquele campo). Na presente invenção, esses dois casos produzem saídas diferentes: o campo `declarado` recebe tipo de evidência 1, exibe alerta visual na página pública e pode ser bloqueado pelo gate se o perfil regulatório exigir `documentado` (nível 3) para aquele campo específico.

O efeito técnico é verificável e mensurável: dado o mesmo conjunto de dados de entrada onde metade dos campos tem suporte documental e metade é apenas declarado, os dois sistemas produzem saídas diferentes. O sistema P10 pode gerar um passaporte completo (completude = 100%). O sistema da presente invenção bloqueia a publicação dos campos `declarado` que não atingem o limiar mínimo, ou os publica com indicação explícita de tipo de evidência inferior.

### 4.4 Não-obviedade da combinação

Um técnico no assunto, conhecendo o estado da técnica representado pelos documentos analisados, não chegaria à combinação da presente invenção pelas seguintes razões:

**(a) Tipagem de evidência como atributo de primeira classe:** O estado da técnica trata dados de produto como valores (corretos ou ausentes). A ideia de que um dado correto pode ter diferentes graus de confiança, e que esse grau deve ser um atributo explícito do campo no modelo de dados — não inferido, não calculado, não agregado — não é sugerida por nenhum documento do estado da técnica. IBM P9 trata incerteza como problema de inferência estatística em modelos de ML, não como atributo de proveniência declarado por operador humano. BASF P5 opera sobre dados medidos por sensores, onde a confiança é implícita à medição. Nenhum documento ensina a tratar evidência como tipo de dado explícito de campo de produto.

**(b) Gate de publicação por campo individual:** Mesmo que um técnico chegasse à ideia de tipagem de evidência, a extensão dessa ideia para um gate que bloqueia publicação campo a campo (não em nível de passaporte completo) não é sugerida pelo estado da técnica. P10 usa limiar de completude agregada — o passaporte pode ser gerado com percentual de completude abaixo de 100%. A presente invenção usa limiar por campo obrigatório — um único campo abaixo do limiar bloqueia todo o passaporte ou resulta em `ausente` para aquele campo. Essa granularidade de gate não é sugerida.

**(c) Exposição pública da evidência ao receptor final:** O estado da técnica não descreve sistemas onde o receptor da credencial (buyer, regulador, consumidor) visualiza o tipo de evidência de cada campo. Em todos os documentos, a qualidade do dado é um atributo interno do sistema, não um elemento da interface pública. A presente invenção inverte essa arquitetura: a evidência por campo é a informação primária para o receptor, não um metadado interno. Essa inversão não é óbvia a partir do estado da técnica.

**(d) Ausência de integração como requisito de design:** Todos os sistemas do estado da técnica assumem integração técnica como premissa (ERP, API, sensores, rede de nós). A decisão de design de eliminar a integração como requisito — aceitando entrada manual por formulário como modalidade primária — não é sugerida por nenhum documento. Em particular, a combinação de auto-serviço sem integração com tipagem de evidência explícita por campo não é ensinada pelo estado da técnica.

### 4.5 Aplicação industrial

A invenção é industrialmente aplicável: resolve problema técnico concreto (prevenção de greenwashing estrutural em passaportes de produto) com mecanismo implementável em software convencional (modelo de dados relacional, aplicação web, CDN), produz efeito técnico verificável (bloqueia publicação de campo com evidência insuficiente) e tem aplicação comercial imediata no contexto das regulações INMETRO 459/2025 e EU ESPR 2024/1781.

---

## 5. Reivindicações

### Reivindicação Independente 1 — Método

Um método implementado por computador para geração de passaporte digital de produto com integridade de evidência por campo, compreendendo:

(a) receber, por interface de auto-serviço que não exige integração de API, sistema ERP, PLM, CAD ou sensor físico pelo operador, uma pluralidade de entradas de dado de produto, cada entrada de dado compreendendo um valor de dado e um tipo de evidência selecionado pelo operador de uma hierarquia de evidência predefinida e estritamente ordenada que compreende pelo menos os níveis: ausente, declarado, calculado, documentado e verificado;

(b) armazenar cada entrada de dado associada ao seu tipo de evidência como atributos co-iguais de um campo de dado em um registro de passaporte interno, de modo que o tipo de evidência seja atributo de primeira classe do campo e não seja inferido, calculado a partir de outros campos, ou substituído automaticamente pelo sistema;

(c) receber seleção de ao menos um perfil de conformidade regulatória, sendo o perfil definido por uma estrutura de dados que compreende: identificador do instrumento regulatório de referência; e, para cada campo obrigatório do perfil, um limiar mínimo de evidência expresso como nível da hierarquia de evidência;

(d) executar, para cada campo obrigatório do perfil selecionado, uma verificação de integridade de evidência que compara o tipo de evidência armazenado para aquele campo com o limiar mínimo de evidência definido para aquele campo no perfil, gerando para cada campo com tipo de evidência inferior ao limiar um registro de falha que identifica o campo, o tipo atual de evidência e o limiar requerido;

(e) bloquear a execução da etapa (f) quando qualquer registro de falha for gerado na etapa (d), retornando ao operador o conjunto de registros de falha sem gerar o passaporte público;

(f) quando nenhum registro de falha for gerado na etapa (d), gerar um registro de passaporte público que associa cada campo de dado ao seu valor e ao seu tipo de evidência, sem incluir índice agregado, pontuação composta, nota ambiental ou qualquer métrica derivada da combinação de múltiplos campos;

(g) publicar o registro de passaporte público em uma URL permanente acessível por qualquer agente sem autenticação, sendo cada campo exibido com seu valor e seu tipo de evidência em representação visual diferenciada por nível da hierarquia, e sendo campos com tipo de evidência `ausente` não exibidos como valores numéricos ou textuais;

(h) gerar um identificador legível por máquina segundo o padrão GS1 Digital Link (ISO/IEC 18004) vinculando o identificador único do produto à URL permanente gerada na etapa (g), sendo o identificador gerado somente após a aprovação da verificação descrita na etapa (d).

### Reivindicação Independente 2 — Sistema

Um sistema para geração de passaporte digital de produto com integridade de evidência por campo, compreendendo:

(a) uma interface de auto-serviço configurada para receber entradas de dado de produto com seleção explícita de tipo de evidência por campo pelo operador, sendo a interface configurada para operar sem exigência de integração de API, sistema ERP, PLM, CAD ou sensor físico;

(b) um módulo de tipagem de evidência configurado para armazenar, para cada campo de dado, o valor do campo e o tipo de evidência como atributos co-iguais de primeira classe, sendo o tipo de evidência selecionado de uma hierarquia predefinida e estritamente ordenada;

(c) um repositório de perfis de conformidade regulatória, sendo cada perfil definido por: identificador do instrumento normativo de referência; e limiar mínimo de evidência por campo obrigatório;

(d) um motor de verificação de integridade de evidência configurado para executar, campo a campo, a comparação entre o tipo de evidência armazenado e o limiar mínimo do perfil selecionado, gerando registros de falha específicos por campo;

(e) um gate de publicação configurado para bloquear a geração do passaporte público quando qualquer registro de falha for produzido pelo motor da alínea (d), retornando os registros de falha ao operador;

(f) um servidor de passaporte público configurado para servir o passaporte em URL permanente sem exigência de autenticação, exibindo cada campo com seu valor e seu tipo de evidência em representação visual diferenciada por nível da hierarquia, sendo campos `ausente` não exibidos como valores;

(g) um repositório imutável de versões de passaporte configurado para armazenar cada passaporte publicado com timestamp e preservar versões anteriores sem possibilidade de alteração retroativa;

(h) um gerador de identificador QR configurado para produzir código segundo o padrão GS1 Digital Link após aprovação do gate da alínea (e).

### Reivindicação Independente 3 — Meio legível por computador

Um meio não transitório legível por computador armazenando instruções que, quando executadas por ao menos um processador, implementam o método da Reivindicação 1.

---

### Reivindicações Dependentes

**4.** O método da Reivindicação 1, em que a hierarquia de evidência compreende os níveis: (0) ausente — dado indisponível; (1) declarado — informado sem documento de suporte; (2) calculado — derivado por fórmula determinística a partir de parâmetros com evidência ≥ 1, com armazenamento da fórmula e parâmetros; (3) documentado — existe arquivo de suporte verificável; (4) verificado — certificado por organismo de avaliação da conformidade acreditado; sendo a relação de ordem estritamente ausente < declarado < calculado < documentado < verificado.

**5.** O método da Reivindicação 1, em que campos com tipo de evidência `calculado` armazenam e exibem na página pública a expressão algébrica e os parâmetros utilizados no cálculo, de modo que o receptor possa reproduzir o resultado.

**6.** O método da Reivindicação 1, em que o perfil de conformidade regulatória referencia o instrumento normativo específico por número, órgão emissor e data de vigência, vinculando cada campo obrigatório ao dispositivo específico do instrumento que o fundamenta.

**7.** O método da Reivindicação 1, em que a URL permanente é servida por infraestrutura de distribuição de conteúdo (CDN) com latência alvo inferior a 80ms para acesso de edge, independentemente da localização geográfica do agente acessante, de modo que o passaporte funcione como credencial em negociações internacionais sem degradação de desempenho por distância geográfica.

**8.** O método da Reivindicação 1, compreendendo adicionalmente armazenar, em repositório imutável com timestamp, cada versão publicada do passaporte, sem possibilidade de alteração retroativa, sendo cada versão individualmente acessível por URL versionada para fins de auditoria regulatória.

**9.** O método da Reivindicação 1, em que o sistema suporta validação simultânea do mesmo passaporte contra múltiplos perfis de conformidade regulatória, produzindo para cada perfil um resultado independente de aprovação ou falha com identificação dos campos que não atingem o limiar mínimo de cada perfil.

**10.** O método da Reivindicação 1, em que o bloqueio da etapa (e) não impede que o operador salve o passaporte em estado de rascunho não publicado, de modo que o rascunho possa ser completado em sessões subsequentes.

**11.** O método da Reivindicação 1, em que a interface de auto-serviço aceita, como modalidade alternativa ao formulário web, upload de arquivo estruturado nos formatos CSV ou XLSX para importação em lote de campos de dado, sendo exigida seleção explícita de tipo de evidência para cada campo importado antes da execução da verificação da etapa (d).

**12.** O sistema da Reivindicação 2, em que o motor de verificação da alínea (d) armazena, para cada execução, um registro de auditoria imutável contendo: identificador do passaporte, perfil selecionado, resultado (aprovado/bloqueado), campos que falharam com tipo de evidência e limiar requerido, e timestamp, sendo o registro de auditoria acessível para fins de due diligence regulatória e comercial.

**13.** O sistema da Reivindicação 2, em que o servidor da alínea (f) não exibe, em nenhuma representação pública do passaporte, índice agregado, pontuação ambiental composta, nota verde, certificação derivada por cálculo interno do sistema ou qualquer representação que implique nível de conformidade superior ao que os tipos de evidência dos campos individuais suportam.

**14.** O sistema da Reivindicação 2, em que o repositório de perfis da alínea (c) é extensível por operadores autorizados e por autoridades regulatórias via interface de configuração, permitindo adição de novos instrumentos normativos sem alteração do código-fonte do sistema.

---

## 6. Resumo (Abstract)

Sistema e método implementados por computador para geração de passaporte digital de produto com integridade de evidência por campo. Uma interface de auto-serviço sem exigência de integração técnica recebe, para cada campo de dado de produto, um valor e um tipo de evidência selecionado de uma hierarquia predefinida e ordenada compreendendo os níveis ausente, declarado, calculado, documentado e verificado. Um motor de verificação compara, campo a campo, o tipo de evidência armazenado com o limiar mínimo definido por um perfil de conformidade regulatória selecionado. Um gate de publicação bloqueia a geração do passaporte público quando qualquer campo obrigatório apresenta tipo de evidência inferior ao limiar, retornando ao operador identificação específica de cada falha. O passaporte aprovado é publicado em URL permanente acessível sem autenticação, onde cada campo exibe seu valor e seu tipo de evidência em representação visual diferenciada, campos ausentes não são exibidos como valores, e nenhum índice agregado ou pontuação composta é gerado. Um código QR segundo o padrão GS1 Digital Link é gerado vinculando o produto à URL pública. O sistema previne estruturalmente a publicação de alegações com evidência insuficiente (greenwashing) e opera sem integração técnica pelo operador (plug-and-play para marca) e sem autenticação pelo receptor (plug-and-play para buyer).

---

## 7. Tabela comparativa com o estado da técnica

| Característica | WO2025209938A1 (BASF) | US12223513B2 (BASF) | US12482004B2 (IBM) | EP4369263A1 (ATS) | Presente invenção |
|---|---|---|---|---|---|
| Tipagem de evidência por campo individual | Não | Não | Não | Não | **Sim** |
| Gate de publicação por campo | Não (completude agregada) | Não | Não | Não | **Sim (por campo)** |
| Evidência visível ao receptor externo | Não | Não | Não | Não | **Sim** |
| Acesso público sem autenticação | Não descrito | Não | Não | Não | **Sim** |
| Sem exigência de integração | Não (API de fornecedor) | Não (ERP/sensor) | Não (dados financeiros) | Não (sensor físico) | **Sim (formulário web)** |
| Score/índice agregado ausente por design | Não | N/A | N/A | Não | **Sim** |
| Setor têxtil/calçados | Não (baterias/químicos) | Não (indústria) | Não (enterprise) | Não (automação) | **Sim** |
| Perfil regulatório configurável | Não | Não | Não | Não | **Sim** |

---

## 8. Notas para revisão jurídica

1. **Jurisdição e prazo:** Brasil (INPI) como jurisdição de depósito prioritário. Prazo de 12 meses para extensão PCT a partir do depósito brasileiro. Deadline INMETRO (31/07/2026) cria urgência: depósito antes de agosto/2026 estabelece anterioridade antes do pico de adoção do mercado.

2. **Prior art defensivo:** Publicar white paper técnico descrevendo o mecanismo de tipagem de evidência por campo antes do depósito. Serve para: (a) estabelecer prior art que limita escopo de P10 BASF se concedido com reivindicação ampla; (b) demonstrar que a invenção foi praticada antes de qualquer depósito posterior por terceiros.

3. **Risco P10:** A distinção crítica entre P10 e a presente invenção está em "completude agregada" (P10) vs "tipagem ordinal por campo" (presente invenção). Se P10 for concedido com reivindicação cobrindo qualquer forma de "validação de campo em DPP", a Reivindicação 1(d) precisará ser especificamente delimitada pela referência à comparação ordinal campo-a-campo com geração de registro de falha por campo individual.

4. **Reivindicação mais forte:** Reivindicação 1(a)+(b)+(d)+(e) em combinação — a tipagem de evidência como atributo de primeira classe armazenado co-igualmente ao valor (não inferido), combinada com gate por campo com retorno de falha específica por campo, é o núcleo técnico mais distinto do estado da técnica.

5. **Patenteabilidade de software no Brasil:** O INPI admite patentes de invenções implementadas por computador quando a invenção produz efeito técnico além da operação normal do computador. O efeito técnico aqui é claro: prevenção estrutural de publicação de dado com evidência insuficiente. Recomendar ao advogado enquadrar as reivindicações como "método implementado por computador" com ênfase no efeito técnico, não no software em si.

6. **Classes de patente sugeridas:** CPC G06Q 10/06 (gestão de recursos, planejamento), G06Q 50/04 (têxtil), G06F 16/215 (qualidade de dados), G16Y 40/35 (IoT + produto passport).
