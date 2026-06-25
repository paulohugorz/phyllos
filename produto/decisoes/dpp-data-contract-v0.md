# PHYLLOS DPP Integrado - Contrato de Dados v0

**Data:** 2026-06-25  
**Status:** fonte operacional para schema, validacoes e prototipo  
**Relacionado:** [prd-dpp-integrado-v0.md](prd-dpp-integrado-v0.md)

---

## 1. Formula base

```text
area_total_requerida = area_peca / (1 - perda_pct)
area_perdida = area_total_requerida - area_peca
peso_peca = area_total_requerida * gramatura_kg_m2
agua_peca = peso_peca * agua_litros_kg
energia_peca = peso_peca * energia_kwh_kg
carbono_peca = peso_peca * carbono_kgco2e_kg
```

Regras:

- `perda_pct` deve ser armazenado em decimal no calculo: 20% = `0.20`.
- `gramatura_g_m2` deve virar `gramatura_kg_m2`: 200 g/m2 = `0.200 kg/m2`.
- Valores negativos sao invalidos.
- `perda_pct >= 1` e invalido.
- Fatores editados pelo usuario devem mudar status para `declarado`, salvo upload de documento.
- Todo fator de agua, energia e carbono precisa de uma fonte textual cadastrada antes da publicacao. Proxy de demonstracao nao e fonte publicavel.

## 2. Entidades conceituais

```text
Produto
├── Material
├── ArquivoTecnico
├── Lote
├── Indicador
├── Evidencia
├── DPP
└── Flashcard
```

## 3. Campos obrigatorios para publicacao

### Identificacao do produto

| Campo | Tipo | Obrigatorio | Observacao |
|---|---|---:|---|
| `gtin` | string | sim | GTIN real ou codigo interno gerado no MVP |
| `sku_interno` | string | sim | Codigo da marca |
| `nome_produto` | string | sim | Nome comercial |
| `categoria` | enum/string | sim | Ex: calca, camisa, vestido, blazer |
| `pais_fabricacao` | string | sim | Declarado |
| `lote_quantidade` | integer | sim | Necessario para contexto de producao |
| `dpp_uuid` | uuid | automatico | Identificador interno |

### Material e composicao

| Campo | Tipo | Obrigatorio | Observacao |
|---|---|---:|---|
| `composicao_fibras` | json array | sim | Soma dos percentuais deve ser 100 |
| `gramatura_g_m2` | float | sim | Base do calculo de peso |
| `area_peca_m2` | float | sim | Declarada/documentada/extraida futuramente |
| `perda_corte_pct` | float | sim | Default sugerido: 15% |
| `fornecedor_nome` | string | recomendado | |
| `fornecedor_pais` | string | recomendado | |
| `fornecedor_gln` | string | opcional | Rastreabilidade avancada |

### Indicadores calculados

| Campo | Tipo | Origem |
|---|---|---|
| `area_total_requerida_m2` | float | calculado |
| `area_perdida_m2` | float | calculado |
| `peso_peca_kg` | float | calculado |
| `agua_peca_litros` | float | calculado |
| `energia_peca_kwh` | float | calculado |
| `carbono_peca_kgco2e` | float | calculado |
| `fonte_agua_litros_kg` | text | fonte obrigatoria do fator de agua |
| `fonte_energia_kwh_kg` | text | fonte obrigatoria do fator de energia |
| `fonte_carbono_kgco2e_kg` | text | fonte obrigatoria do fator de carbono |
| `metodologia_fatores_impacto` | text | limitacao/metodologia comum aos fatores |

### Certificacoes e durabilidade

| Campo | Tipo | Obrigatorio |
|---|---|---:|
| `certificacoes` | json array | opcional |
| `conteudo_reciclado_pct` | float | opcional |
| `durabilidade_ciclos_lavagem` | integer | opcional |
| `instrucoes_cuidado` | string | recomendado |
| `instrucoes_reparo` | string | opcional |
| `instrucoes_fim_de_vida` | string | recomendado |

### Cadeia produtiva

| Campo | Tipo | Obrigatorio |
|---|---|---:|
| `etapas_producao` | array | opcional no MVP |
| `instalacao_nome` | string por etapa | opcional |
| `instalacao_pais` | string por etapa | opcional |

### Metadados do DPP

| Campo | Tipo | Origem |
|---|---|---|
| `dpp_status` | enum | automatico: rascunho/publicado/revogado |
| `data_publicacao` | datetime | automatico |
| `data_atualizacao` | datetime | automatico |
| `versao_dpp` | string | automatico |

## 4. Status de evidencia

| Status | Codigo | Significado | Uso publico |
|---|---:|---|---|
| `ausente` | 0 | Campo nao informado | nao publica como numero; exibe lacuna |
| `declarado` | 1 | Usuario informou sem documento | publica com aviso "declarado pela marca" |
| `calculado` | 2 | Formula deterministica com dados declarados | publica como estimativa calculada |
| `documentado` | 3 | Documento anexado | publica como documentado |
| `verificado` | 4 | Terceiro confirmou | publica como verificado |
| `publicavel` | composto | obrigatorios completos | habilita publicacao |

Transicoes:

```text
ausente -> declarado
ausente -> calculado
declarado -> documentado
documentado -> verificado
```

Regras:

- UI nao deve permitir regressao simples de `documentado` para `declarado`.
- Revogar DPP nao altera evidencia de campo; altera apenas `dpp_status`.
- Todo indicador publico precisa de badge de evidencia.

## 5. Labels publicos por origem

| Campo | Status | Label |
|---|---|---|
| `composicao_fibras` | declarado | Composicao declarada pela marca |
| `composicao_fibras` | documentado | Composicao com documento do fornecedor |
| `carbono_peca_kgco2e` | calculado | Estimativa com fator medio de referencia setorial |
| `carbono_peca_kgco2e` | declarado | Estimativa com fator declarado pela marca, nao auditado |
| `carbono_peca_kgco2e` | documentado | Baseado em documento ou ACV parcial anexado |
| `certificacoes` | declarado | Certificacao declarada |
| `certificacoes` | documentado | Certificado documentado, com numero e validade |
| `pais_fabricacao` | declarado | Informado pela marca |
| `etapas_producao` | declarado | Cadeia declarada pela marca |
| `etapas_producao` | documentado | Cadeia com documento de rastreio |

## 6. Validacoes obrigatorias

- `composicao_fibras` deve somar 100.
- `area_peca_m2 > 0`.
- `gramatura_g_m2 > 0`.
- `0 <= perda_corte_pct < 100`.
- Certificacao expirada nao pode aparecer como valida.
- QR publico exige campos obrigatorios pelo menos `declarado`.
- Campo calculado sem label publico deve falhar.
- Fator fora de limite de referencia deve exigir documento antes de `documentado` ou `verificado`.
- Fator calculado sem fonte textual deve falhar.
- Fonte contendo proxy interno, demonstracao, demo ou "nao usar em piloto" deve falhar.

## 7. Payload de exemplo para prototipo

```json
{
  "sku_interno": "PH-CC-2601",
  "nome_produto": "Calca conforto de rotina",
  "categoria": "calca",
  "pais_fabricacao": "BR",
  "lote_quantidade": 80,
  "composicao_fibras": [
    {"fibra": "poliester_reciclado", "pct": 78},
    {"fibra": "elastano", "pct": 22}
  ],
  "gramatura_g_m2": 220,
  "area_peca_m2": 1.42,
  "perda_corte_pct": 14,
  "fatores": {
    "agua_litros_kg": 320,
    "energia_kwh_kg": 12,
    "carbono_kgco2e_kg": 4.8,
    "fonte_agua_litros_kg": "Fonte documentada do fornecedor ou base setorial textil indicada no piloto",
    "fonte_energia_kwh_kg": "Fonte documentada do fornecedor ou base setorial textil indicada no piloto",
    "fonte_carbono_kgco2e_kg": "Fonte documentada do fornecedor, Higg MSI, ecoinvent, IPCC ou GHG Protocol conforme material/processo",
    "metodologia_fatores_impacto": "Estimativa calculada por peso da peca; nao substitui ACV oficial ou auditoria ambiental"
  }
}
```
