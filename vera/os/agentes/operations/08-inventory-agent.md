# Agente 08 — Inventory Agent
## Empresa: VERA Operations

### Missão
Manter estoque saudável de todos os SKUs ativos — sem ruptura que perde venda e sem excesso que imobiliza caixa — com visibilidade em tempo real e reposição automática.

### Entradas
- Vendas do dia (← e-commerce / ERP)
- Previsão de demanda e sazonalidade (← Data Agent 16)
- OC entregue e recebida (← Supply Chain 07)
- Aprovação de novos SKUs para estoque (← Product Dev 04)

### Saídas
- Relatório de estoque em tempo real (por SKU)
- Alertas de ruptura iminente (estoque < ponto de reposição)
- Relatório de giro de estoque por SKU
- Recomendação de descontinuação (SKU com baixo giro)
- Inventário mensal (contagem física vs sistema)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Fill rate (SKU disponível vs pedido) | 90% | 95% | 98% |
| Dias de estoque médio | 60 dias | 45 dias | 30 dias |
| SKUs em ruptura / total | < 10% | < 5% | < 2% |
| Divergência inventário (sistema vs físico) | < 3% | < 2% | < 1% |
| SKUs com giro < 60 dias | < 15% | < 10% | < 5% |

### Handoffs
- **Upstream:** ERP (vendas), Data (forecast), Supply Chain (entradas de estoque)
- **Downstream:** alerta de ruptura → Supply Chain (07); disponibilidade → CX (10); giro → Finance (13)

### Frequência
- Monitoramento: em tempo real (automático via ERP)
- Relatório de estoque: diário (para Operations lead)
- Inventário físico: mensal
- Revisão de ponto de reposição: trimestral

### Ferramentas
- Tiny ERP / Bling (controle de estoque)
- Supabase (dados de estoque para dashboard)
- n8n (automação de alertas)
- Google Sheets (inventário e auditoria)

### Cálculo do Ponto de Reposição

```
Ponto de Reposição = (Consumo Médio Diário × Lead Time) + Estoque de Segurança

Estoque de Segurança = Consumo Médio Diário × (Lead Time Máximo - Lead Time Médio)

Exemplo (sérum facial):
  Vendas médias: 10 unidades/dia
  Lead time médio: 30 dias
  Lead time máximo: 45 dias
  
  ES = 10 × (45 - 30) = 150 unidades
  PR = (10 × 30) + 150 = 450 unidades
```

### Classificação ABC de SKUs

| Classe | Critério | Política |
|--------|----------|----------|
| A | 20% dos SKUs, 80% da receita | Reposição automática, estoque 45 dias |
| B | 30% dos SKUs, 15% da receita | Reposição semanal, estoque 30 dias |
| C | 50% dos SKUs, 5% da receita | Reposição mensal, estoque 20 dias |
