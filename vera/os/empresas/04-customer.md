# VERA Customer
## Empresa 04 — CX, CRM & Fidelização

### Missão
Transformar cada interação com a cliente em uma prova de que a VERA se importa — com atendimento humano e ágil, comunicação personalizada e um programa de fidelidade que faz o cliente querer ficar.

### Escopo
- Atendimento ao cliente (omnichannel: WhatsApp, email, DM)
- Gestão de tickets e resolução de problemas
- Pesquisa de satisfação (NPS, CSAT, CES)
- Segmentação de base e automações de CRM
- Programa de fidelidade e comunidade VERA
- Gestão de devoluções e trocas (interface com Operations)
- Pesquisa de ICP e entrevistas de cliente

### Entradas
- Pedidos entregues e status de estoque (← Operations)
- Novos produtos e claims (← Beauty Product)
- Campanhas e promoções ativas (← Growth)
- Dados de comportamento de compra (← Automation)

### Saídas
- NPS e CSAT mensais
- Relatório de dores e feedbacks de produto
- Segmentos de cliente para Growth/CRM
- Taxa de resolução de tickets e SLA
- Relatório de churn e motivos
- Insights de ICP (→ Beauty Product, Growth)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| NPS | 45 | 55 | 70 |
| CSAT | 4.2/5 | 4.5/5 | 4.7/5 |
| Tempo médio de resposta | < 4h | < 2h | < 1h |
| Taxa de resolução no 1º contato | 60% | 75% | 85% |
| Churn mensal | < 10% | < 7% | < 4% |
| Taxa de recompra (M3) | 20% | 35% | 50% |
| Clientes ativos no programa | — | 500 | 3K |

### Agentes Internos
- **10 — CX Agent** → atendimento, tickets, satisfação, devoluções
- **11 — CRM Agent** → segmentação, automações, nutrição, recuperação
- **12 — Loyalty Agent** → programa de pontos, comunidade, retenção, advocacia

### Handoffs
- `Customer → Growth` : segmentos qualificados, personas validadas
- `Customer → Beauty Product` : feedbacks de produto, dores recorrentes
- `Customer → Finance` : dados de LTV, churn e retenção

### Jornada do Cliente VERA

```
[Descoberta] → [Interesse / Lista de Espera]
    → [1ª Compra] → [Onboarding]
    → [Uso do Produto] → [Feedback / NPS]
    → [Recompra] → [Programa Loyalty]
    → [Advocacia / UGC / Indicação]
```

### Ferramentas
- Zendesk / Freshdesk (tickets)
- Klaviyo (CRM e automações)
- Typeform (pesquisas NPS/CSAT)
- WhatsApp Business API
- Supabase (dados de cliente)
- Notion (base de conhecimento CS)
