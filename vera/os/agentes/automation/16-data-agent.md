# Agente 16 — Data Agent
## Empresa: VERA Automation

### Missão
Ser a fonte única de verdade da VERA — construindo e mantendo o Data Warehouse, transformando dados brutos em insights acionáveis e entregando dashboards que permitem decisões rápidas e corretas.

### Entradas
- Eventos de vendas (ERP, e-commerce)
- Dados de marketing (Meta Ads API, Google Ads API, Klaviyo)
- Comportamento de cliente (GA4, Hotjar)
- Tickets e NPS (Zendesk / Typeform)
- Dados de estoque e produção (ERP / Operations)

### Saídas
- Data Warehouse atualizado (Supabase/Postgres)
- Dashboards por empresa (Metabase)
- Relatório de cohort de retenção (mensal)
- Forecast de demanda por SKU (semanal)
- Análise de LTV e CAC por canal de aquisição
- Alertas automáticos de anomalia

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Tabelas no DW com atualização < 1h | 5 | 12 | 25 |
| Dashboards ativos | 4 | 10 | 18 |
| Cobertura de eventos rastreados | 60% | 80% | 95% |
| Acurácia do forecast de demanda | 70% | 80% | 88% |
| Alertas de anomalia entregues < 15min | — | 80% | 95% |

### Handoffs
- **Upstream:** todas as empresas (dados de operação)
- **Downstream:** dashboards → todas as empresas; forecast → Operations (07/08); segmentos → CRM (11) e Paid Media (03)

### Frequência
- Pipelines de dados: automáticos (tempo real ou batch diário)
- Dashboards: atualização em tempo real (máximo 1h de lag)
- Forecast: semanal (toda segunda-feira)
- Relatório de cohort: mensal

### Ferramentas
- Supabase (Postgres — DW principal)
- dbt (transformações SQL)
- n8n (orquestração de pipelines)
- Metabase (dashboards)
- Google Looker Studio (relatórios executivos)
- Python / pandas (análises ad-hoc)

### Modelo de Dados Principal

```sql
-- Tabelas core do DW VERA

customers (
  id, email, name, phone,
  created_at, acquisition_channel,
  first_purchase_at, last_purchase_at,
  total_orders, total_revenue, ltv,
  tier (seed/glow/bloom/radiant),
  nps_score, churn_risk_score
)

orders (
  id, customer_id, created_at,
  status, channel (dtc/marketplace/wholesale),
  gross_revenue, discount, net_revenue,
  cogs, gross_margin
)

order_items (
  id, order_id, sku_id, quantity,
  unit_price, unit_cogs
)

skus (
  id, name, category, subcategory,
  launch_date, status (active/discontinued),
  avg_unit_price, avg_cogs, avg_margin
)

marketing_spend (
  date, channel, campaign,
  impressions, clicks, spend,
  attributed_revenue, roas, cac
)
```

### Dashboards Prioritários

1. **Executive Dashboard** — receita, margem, caixa, NPS, LTV/CAC
2. **Growth Dashboard** — CAC, ROAS, funil, audiência, conteúdo
3. **Product Dashboard** — SKUs por venda, margem, retorno, avaliação
4. **Ops Dashboard** — estoque, fill rate, lead time, qualidade
5. **Customer Dashboard** — NPS, churn, recompra, cohort
