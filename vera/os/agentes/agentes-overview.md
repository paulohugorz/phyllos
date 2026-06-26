# VERA OS — 18 Agentes
## Visão Geral

Cada agente é uma unidade funcional do VERA OS com missão clara, entradas e saídas definidas, KPIs mensuráveis e handoffs explícitos com outras empresas.

---

## Mapa dos Agentes por Empresa

### VERA Growth
| # | Agente | Arquivo |
|---|--------|---------|
| 01 | Brand Agent | `growth/01-brand-agent.md` |
| 02 | Content Agent | `growth/02-content-agent.md` |
| 03 | Paid Media Agent | `growth/03-paid-media-agent.md` |

### VERA Beauty Product
| # | Agente | Arquivo |
|---|--------|---------|
| 04 | Product Development Agent | `beauty-product/04-product-development-agent.md` |
| 05 | Formulation Agent | `beauty-product/05-formulation-agent.md` |
| 06 | Packaging Agent | `beauty-product/06-packaging-agent.md` |

### VERA Operations
| # | Agente | Arquivo |
|---|--------|---------|
| 07 | Supply Chain Agent | `operations/07-supply-chain-agent.md` |
| 08 | Inventory Agent | `operations/08-inventory-agent.md` |
| 09 | Quality Agent | `operations/09-quality-agent.md` |

### VERA Customer
| # | Agente | Arquivo |
|---|--------|---------|
| 10 | CX Agent | `customer/10-cx-agent.md` |
| 11 | CRM Agent | `customer/11-crm-agent.md` |
| 12 | Loyalty Agent | `customer/12-loyalty-agent.md` |

### VERA Finance
| # | Agente | Arquivo |
|---|--------|---------|
| 13 | CFO Agent | `finance/13-cfo-agent.md` |
| 14 | Pricing Agent | `finance/14-pricing-agent.md` |
| 15 | Investor Relations Agent | `finance/15-investor-relations-agent.md` |

### VERA Automation
| # | Agente | Arquivo |
|---|--------|---------|
| 16 | Data Agent | `automation/16-data-agent.md` |
| 17 | AI Ops Agent | `automation/17-ai-ops-agent.md` |
| 18 | Integration Agent | `automation/18-integration-agent.md` |

---

## Estrutura Padrão de Agente

```yaml
id: XX
nome: [Nome do Agente]
empresa: [VERA Growth | Beauty Product | Operations | Customer | Finance | Automation]
missao: [Uma frase clara do que o agente faz e por quê]
entradas:
  - [fonte]: [dado ou artefato recebido]
saidas:
  - [artefato produzido] → [destino]
kpis:
  - [métrica]: [meta M3 / M6 / M12]
handoffs:
  upstream: [o que recebe e de quem]
  downstream: [o que entrega e para quem]
ferramentas:
  - [lista de ferramentas usadas]
frequencia: [diária / semanal / por evento / mensal]
```

---

## Princípios dos Agentes

1. **Missão única** — cada agente faz uma coisa bem, não tudo mal
2. **Entradas explícitas** — nenhum agente opera no escuro; toda informação tem fonte
3. **Saídas verificáveis** — outputs são artefatos concretos, não "análises"
4. **KPIs por agente** — cada um sabe o que é sucesso para ele
5. **Handoffs limpos** — o downstream sabe exatamente o que vai receber
