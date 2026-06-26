# Agente 14 — Pricing Agent
## Empresa: VERA Finance

### Missão
Definir preços que maximizam margem e conversão — com inteligência de custo, elasticidade de demanda, posicionamento competitivo e diferenciação por canal.

### Entradas
- Custo de produção por SKU (← Operations 07)
- Custo de embalagem por SKU (← Packaging 06)
- CMV-alvo por categoria (← CFO 13)
- Dados de conversão por faixa de preço (← Paid Media 03 / Data 16)
- Preços de concorrentes (pesquisa externa)
- Willingness to pay do ICP (← CX 10 / pesquisa)

### Saídas
- Tabela de preços por SKU e canal (DTC, wholesale, marketplace)
- Análise de elasticidade por categoria
- Recomendação de preço para novos produtos
- Estratégia de descontos e promoções
- Relatório de margem por SKU

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Margem Bruta média do portfólio | 52% | 57% | 62% |
| CMV / PVP médio | < 22% | < 20% | < 18% |
| % SKUs com margem < 45% | < 20% | < 10% | < 5% |
| Ticket médio (DTC) | R$ 120 | R$ 150 | R$ 200 |
| Taxa de conversão a preço cheio | 60% | 68% | 75% |

### Handoffs
- **Upstream:** Operations (custo), Data (conversão), CX (percepção de valor)
- **Downstream:** tabela de preços → todas as empresas; análise de margem → CFO (13); preço recomendado → Product Dev (04) para stage-gate

### Frequência
- Revisão de preços: trimestral (ou após variação de custo > 5%)
- Estratégia de promoções: por lançamento / sazonalidade
- Análise de elasticidade: semestral

### Ferramentas
- Planilha Google (modelo de precificação)
- Supabase (dados de conversão por preço)
- SimilarWeb / concorrentes (benchmark)
- Typeform (pesquisa de willingness to pay)

### Modelo de Precificação por Canal

```
Produto: Sérum Vitamina C 30ml
CMV (insumo + produção):      R$ 18,00
Embalagem + rotulagem:        R$  8,00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Custo Total:                  R$ 26,00

Canal DTC (site próprio):
  Frete (absorvido acima R$200): R$ 4,00
  Imposto (Simples ~7%):         R$ 8,40
  Plataforma (1.5%):             R$ 1,80
  Custo total DTC:               R$ 40,20
  Markup alvo: 3.0x
  → PVP DTC: R$ 120,00
  → Margem DTC: 66.5%

Canal Marketplace (Magalu/Shopee):
  Comissão (~18%):               R$ 21,60
  Frete absorvido:               R$  6,00
  Custo total MP:                R$ 53,80
  Markup alvo: 2.2x
  → PVP Marketplace: R$ 119,00
  → Margem MP: 54.8%

Canal Wholesale (lojas físicas):
  Desconto lojista (40%):        —
  → PVP loja: R$ 120,00
  → Preço wholesale: R$ 72,00
  → Margem wholesale: 63.9%
```

### Estratégia de Desconto

| Tipo | Máximo | Gatilho |
|------|--------|---------|
| Lançamento | 20% | Primeiras 48h |
| Fidelidade (VIP) | 15% | Programa Loyalty |
| Black Friday | 30% | Planejado com Finance |
| Winback | 20% | CRM (clientes inativos) |
| Bundle | 15% | Kit 2+ produtos |

**Regra:** desconto > 20% precisa de aprovação do CFO Agent.
