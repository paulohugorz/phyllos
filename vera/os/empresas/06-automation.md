# VERA Automation
## Empresa 06 — Dados, IA & Integrações

### Missão
Ser o sistema nervoso da VERA — conectar todas as empresas por meio de dados em tempo real, automatizar processos repetíveis e garantir que os agentes de IA operem com informação precisa e handoffs limpos.

### Escopo
- Data Warehouse e modelagem de dados (Supabase/Postgres)
- Pipelines de dados (vendas, CS, marketing, ops)
- Dashboards e BI por empresa
- Automações de processos (n8n, Make, Zapier)
- Gestão operacional dos 18 agentes de IA
- Integrações entre plataformas (ERP, CRM, e-commerce, ads)
- Segurança de dados e conformidade LGPD
- Monitoramento de KPIs em tempo real

### Entradas
- Eventos de todas as empresas (vendas, tickets, cliques, produção)
- Configurações de agentes (missão, entradas, saídas, KPIs)
- Solicitações de automação das empresas
- Dados externos (Meta API, Google Analytics, plataformas de e-commerce)

### Saídas
- Dashboards operacionais por empresa
- Briefing diário automatizado para founder
- Alertas de anomalia (ruptura, churn, ROAS abaixo da meta)
- Relatórios de performance dos agentes
- Integrações funcionando com SLA definido
- Banco de dados de clientes unificado (CDP)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Uptime dos pipelines | 95% | 98% | 99.5% |
| Latência média do dashboard | < 5min | < 2min | < 30s |
| Integrações ativas | 5 | 12 | 20 |
| Automações ativas | 8 | 20 | 40 |
| Cobertura de KPIs monitorados | 60% | 85% | 100% |
| Alertas de anomalia com < 15min | — | 80% | 95% |

### Agentes Internos
- **16 — Data Agent** → warehouse, dashboards, BI, cohort, previsão
- **17 — AI Ops Agent** → operação dos 18 agentes, KPIs, handoffs, qualidade
- **18 — Integration Agent** → APIs, conectores, automações, webhooks

### Handoffs
- `Automation → todas as empresas` : dados, dashboards, alertas
- `Automation → Finance` : forecast de receita, dados para DRE
- `Automation → Growth` : dados de conversão, ROAS, cohort

### Stack Técnico

```
Camada de Dados:
  Supabase (Postgres) — Data Warehouse
  dbt — transformações
  n8n — orquestração de pipelines

Camada de Automação:
  n8n / Make — automações de processo
  Zapier — integrações rápidas

Camada de BI:
  Metabase — dashboards internos
  Google Looker Studio — relatórios executivos

Camada de IA:
  Claude API (Anthropic) — agentes de decisão
  Supabase Vector — memória e RAG dos agentes
  LangChain — orquestração de agentes

Camada de Integração:
  REST APIs (Meta, Google, Shopify, Klaviyo)
  Webhooks (ERP, CS, pagamentos)
```

### Ferramentas
- Supabase (banco + auth + storage)
- n8n (self-hosted ou cloud)
- Metabase (BI)
- Claude API (agentes)
- Sentry (monitoramento de erros)
- Notion (documentação de arquitetura)
