# VERA Finance
## Empresa 05 — Finanças, Precificação & Captação

### Missão
Garantir a saúde financeira da VERA, modelar cenários para decisões de produto e canal, precificar com inteligência e construir o case de captação para escala.

### Escopo
- Fluxo de caixa e gestão de tesouraria
- DRE mensal e análise de margens
- Precificação por SKU (CMV, markup, canal)
- Modelagem de cenários (conservador / base / otimista)
- Planejamento orçamentário por empresa
- Gestão de captação (investidores, BNDES, grants)
- Pitch deck, one pager e data room
- Unit economics (CAC, LTV, payback)

### Entradas
- Custo de produção por SKU (← Operations)
- CAC e ROAS por canal (← Growth)
- LTV, churn e retenção (← Customer)
- Forecast de vendas (← Automation / Data)
- Custo de P&D (← Beauty Product)

### Saídas
- DRE mensal por empresa
- Dashboard financeiro (receita, margem, caixa)
- Tabela de preços aprovada por canal
- Budget aprovado por empresa
- Relatório de unit economics
- Pitch deck e data room atualizados

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Receita Bruta Mensal | R$ 15K | R$ 50K | R$ 250K |
| Margem Bruta | 52% | 57% | 62% |
| Margem EBITDA | -30% | -10% | +15% |
| MRR (assinaturas) | R$ 2K | R$ 8K | R$ 40K |
| Runway (meses caixa) | 6 | 8 | 12 |
| CAC payback | 8 meses | 6 meses | 4 meses |
| LTV/CAC | 3.2x | 6x | 12x |

### Agentes Internos
- **13 — CFO Agent** → fluxo de caixa, DRE, cenários, orçamento
- **14 — Pricing Agent** → precificação, markup, CMV, elasticidade
- **15 — Investor Relations Agent** → pitch, captação, data room, SAFE

### Handoffs
- `Finance → Growth` : budget de marketing aprovado, CAC-alvo
- `Finance → Operations` : budget de compras, metas de CMV
- `Finance → Beauty Product` : budget de P&D, CMV-alvo por SKU

### Modelo de Precificação

```
CMV (custo de produção)
  + Embalagem & Logística
  + Impostos (Simples / Lucro Presumido)
  + Taxa de plataforma (e-commerce)
  ─────────────────────────────────────
  = Custo Total por Unidade
  × Markup (2.8x DTC | 2.0x wholesale | 1.6x B2B)
  ─────────────────────────────────────
  = Preço de Venda Final
```

### Ferramentas
- Planilha Google (modelo financeiro)
- Conta Azul / Omie (ERP financeiro)
- Supabase (dados de receita)
- Notion (data room)
- Canva (pitch deck)
