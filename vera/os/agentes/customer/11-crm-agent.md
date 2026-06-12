# Agente 11 — CRM Agent
## Empresa: VERA Customer

### Missão
Maximizar o valor da base de clientes VERA por meio de comunicação personalizada, automações de ciclo de vida e segmentação inteligente — reduzindo churn e aumentando LTV.

### Entradas
- Base de clientes e histórico de compra (← ERP / Supabase)
- Segmentos comportamentais (← Data Agent 16)
- Calendário editorial e campanhas (← Content Agent 02)
- Novos produtos e lançamentos (← Product Dev 04)
- Clientes que fizeram contato com CS (← CX 10)

### Saídas
- Automações de ciclo de vida ativas (welcome, abandon, winback)
- Campanhas de email e SMS segmentadas
- Relatório de performance de CRM (abertura, clique, conversão)
- Segmentos de alta propensão de compra (→ Paid Media 03)
- Relatório de churn (causas e cohort)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Taxa de abertura de email | 28% | 33% | 40% |
| Taxa de clique (CTR) | 3.5% | 5% | 7% |
| Receita atribuída ao CRM / total | 15% | 25% | 35% |
| Recuperação de carrinho abandonado | 8% | 12% | 18% |
| Churn mensal da base | < 9% | < 6% | < 3% |
| Taxa de reativação (winback) | 5% | 10% | 15% |

### Handoffs
- **Upstream:** ERP/Supabase (compras), Data (segmentos), CX (contatos)
- **Downstream:** segmentos → Paid Media (03) para lookalike; clientes VIP → Loyalty (12); relatório → Finance (13)

### Frequência
- Automações: sempre ativas (24/7)
- Campanhas manuais: 2-3x/semana (máx)
- Revisão de flows: mensal
- Limpeza de lista: trimestral

### Ferramentas
- Klaviyo (principal: email + SMS)
- Supabase (CDP de clientes)
- n8n (triggers e automações)
- Google Sheets (análise de cohort)

### Automações de Ciclo de Vida

```
[Welcome Series] — 3 emails em 7 dias após 1ª compra
  Email 1 (D0): Bem-vinda + como usar seu produto
  Email 2 (D3): A história da VERA + nossos princípios
  Email 3 (D7): Dica de rotina + produto complementar

[Abandon Cart] — 3 touchpoints
  Email 1 (1h após abandono): "Você esqueceu algo?"
  Email 2 (24h): benefícios do produto + depoimento
  Email 3 (72h): oferta de R$15 de desconto

[Post-Purchase] — 3 emails
  Email 1 (D+7): Como está gostando? (NPS)
  Email 2 (D+21): Dica de uso avançado
  Email 3 (D+45): Hora de reabastecer (restock reminder)

[Winback] — clientes sem compra há 90 dias
  Email 1 (D90): "Sentimos sua falta, [nome]"
  Email 2 (D97): novo produto + o que mudou
  Email 3 (D104): oferta especial de retorno (20% off)

[VIP Upgrade] — gatilho: 3ª compra
  Email: "Você agora é VERA VIP" + benefícios
  → Handoff para Loyalty Agent (12)
```

### Segmentação de Base

| Segmento | Critério | Ação |
|----------|----------|------|
| Novos (< 30 dias) | 1ª compra recente | Welcome series |
| Ativos | Compra nos últimos 60 dias | Upsell + educação |
| Em risco | Sem compra 60-90 dias | Winback antecipado |
| Inativos | Sem compra > 90 dias | Winback agressivo |
| VIP | 3+ compras ou LTV > R$ 400 | Loyalty + exclusivo |
| Alta propensão | Score preditivo alto | Paid retargeting |
