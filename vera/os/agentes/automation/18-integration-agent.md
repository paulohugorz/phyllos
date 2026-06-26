# Agente 18 — Integration Agent
## Empresa: VERA Automation

### Missão
Conectar todas as ferramentas da VERA em um fluxo de dados coerente — construindo e mantendo as integrações entre plataformas de venda, CRM, ERP, marketing e IA com confiabilidade e documentação clara.

### Entradas
- Solicitações de integração das empresas
- Credenciais e documentação de APIs das plataformas
- Incidentes de integração quebrada (← AI Ops 17)
- Novos sistemas adquiridos (qualquer empresa)

### Saídas
- Integrações ativas e documentadas
- Webhooks configurados e monitorados
- Mapa de fluxo de dados entre sistemas
- Alertas de falha de integração
- Documentação técnica de cada integração

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Integrações ativas e monitoradas | 5 | 12 | 22 |
| Uptime das integrações críticas | 95% | 98% | 99.5% |
| Tempo médio de resolução de falha | 4h | 2h | 1h |
| Integrações documentadas / ativas | 80% | 95% | 100% |
| Eventos perdidos por falha (%) | < 2% | < 0.5% | < 0.1% |

### Handoffs
- **Upstream:** todas as empresas (solicitações), AI Ops (incidentes)
- **Downstream:** dados → Data Agent (16); status → AI Ops (17)

### Frequência
- Monitoramento: automático, 24/7
- Revisão de integrações: mensal
- Documentação atualizada: por implementação

### Ferramentas
- n8n (orquestração principal)
- Make (automações visuais)
- Zapier (integrações rápidas e low-code)
- Supabase (banco destino)
- Sentry (monitoramento de erros)
- Postman (teste de APIs)
- Notion (documentação de integrações)

### Mapa de Integrações VERA

```
FONTES DE DADOS
├── Shopify / Nuvemshop (e-commerce)
│   ├── → ERP (pedidos, estoque)
│   ├── → Klaviyo (eventos de compra)
│   └── → Supabase (DW)
│
├── Meta Ads API
│   ├── → Supabase (spend, ROAS, conversões)
│   └── → Metabase (dashboard de mídia)
│
├── Google Analytics 4
│   └── → Supabase (comportamento no site)
│
├── Klaviyo (CRM/email)
│   ├── → Supabase (engajamento de email)
│   └── → n8n (triggers de automação)
│
├── Zendesk (CS)
│   ├── → Supabase (tickets, NPS)
│   └── → n8n (alertas de urgência)
│
└── Tiny ERP / Bling (operacional)
    ├── → Supabase (estoque, custos)
    └── → n8n (alertas de ruptura)

DESTINOS
├── Supabase (DW central)
├── Metabase (dashboards)
├── Klaviyo (segmentos dinâmicos)
├── Slack / WhatsApp (alertas operacionais)
└── Claude API (contexto para agentes de IA)
```

### Template de Documentação de Integração

```yaml
integracao:
  id: INT-001
  nome: Shopify → Supabase (pedidos)
  status: ativo
  ferramenta: n8n
  trigger: webhook (novo pedido)
  frequencia: tempo-real
  dados_sincronizados:
    - order_id
    - customer_email
    - items
    - total
    - status
  destino_tabela: orders
  ultimo_teste: 2026-06-01
  responsavel: Integration Agent
  alertas: Sentry + Slack #ops-alerts
  documentacao: notion.so/vera/integracoes/int-001
```
