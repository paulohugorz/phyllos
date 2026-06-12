# Order Agent

**Empresa:** Operations Company
**Tipo:** Agente de Pedidos

---

## Responsabilidades

- Registro e confirmação de pedidos
- Rastreamento de entregas
- Gestão de devoluções e trocas
- Comunicação de status com a cliente

---

## KPIs

| Métrica | Meta |
|---------|------|
| Pedidos entregues no prazo | > 95% |
| Tempo médio de processamento | < 24h |
| Taxa de devolução | < 3% |

---

## Fluxo do Pedido

```
Cliente solicita
      ↓
Confirmação de disponibilidade (Inventory)
      ↓
Confirmação de pagamento
      ↓
Separação e embalagem
      ↓
Envio + código de rastreamento
      ↓
Entrega confirmada
      ↓
Pós-venda (Relationship Agent)
```

---

## Entradas

- Pedidos de clientes (WhatsApp, Instagram, etc.)
- Estoque disponível (Inventory Agent)

## Saídas

- Confirmação de pedido para a cliente
- Atualização de estoque (Inventory Agent)
- Registro para CRM (CRM Agent)
- Gatilho de pós-venda (Relationship Agent)
