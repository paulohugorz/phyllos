# VERA Operations
## Empresa 03 — Supply Chain, Estoque & Qualidade

### Missão
Garantir que o produto certo esteja disponível, no prazo certo, com qualidade certificada e custo operacional otimizado — sem ruptura e sem excesso.

### Escopo
- Gestão de fornecedores de insumos e embalagem
- Planejamento e controle da produção (PCP)
- Gestão de estoque e reposição
- Logística de entrada (inbound) e saída (fulfillment)
- Controle de qualidade e inspeção
- Gestão de devoluções e trocas (reverse logistics)
- Conformidade com ANVISA e boas práticas de fabricação (BPF)

### Entradas
- SKUs aprovados com fichas técnicas (← Beauty Product)
- Previsão de demanda (← Automation / Data)
- Pedidos de reposição (← Inventory Agent)
- Budget de compras (← Finance)

### Saídas
- Ordens de produção emitidas
- Relatório de estoque em tempo real
- Relatório de inspeção de qualidade por lote
- Lead times atualizados por fornecedor
- Custo de produção real por SKU (→ Finance)
- Disponibilidade de produto (→ Customer / CX)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Fill rate (disponibilidade) | 90% | 95% | 98% |
| Lead time médio (produção) | 45 dias | 35 dias | 25 dias |
| Giro de estoque (meses) | 3 | 2.5 | 2 |
| Taxa de devoluções por qualidade | < 3% | < 2% | < 1% |
| Aprovação de lote em 1ª inspeção | 85% | 90% | 95% |
| Custo logístico / receita | 12% | 10% | 8% |

### Agentes Internos
- **07 — Supply Chain Agent** → fornecedores, cotações, PCP, lead time
- **08 — Inventory Agent** → estoque, SKU, reposição, ruptura
- **09 — Quality Agent** → inspeção, testes, BPF, conformidade

### Handoffs
- `Operations → Customer` : disponibilidade de estoque, prazo de entrega
- `Operations → Finance` : custo real de produção, custo logístico
- `Operations → Beauty Product` : feedback de fornecedor, variações de insumo

### Fluxo Operacional

```
[Forecast] → [Ordem de Compra] → [Produção/Manipulação]
    → [Inspeção de Qualidade] → [Armazenagem]
    → [Pedido do Cliente] → [Separação] → [Entrega]
    → [Pós-entrega / Devolução se necessário]
```

### Ferramentas
- Tiny ERP / Bling (ordens e estoque)
- Supabase (dados operacionais)
- Melhor Envio / Jadlog (logística)
- Google Sheets (PCP inicial)
- WhatsApp Business (fornecedores)
