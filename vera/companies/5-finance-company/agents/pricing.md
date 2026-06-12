# Pricing Agent

**Empresa:** Finance Company
**Tipo:** Agente de Precificação

---

## Responsabilidades

- Definição do preço de venda dos produtos
- Cálculo de margem bruta
- Análise de rentabilidade por SKU
- Revisão periódica de preços

---

## Fórmula Base

```
Preço de Venda = Custo × (1 + Markup)

Margem Bruta (%) = (Preço de Venda - Custo) / Preço de Venda × 100
```

---

## Faixas de Markup por Categoria

| Categoria | Markup Mínimo | Markup Alvo |
|-----------|--------------|------------|
| Skincare | 80% | 120% |
| Maquiagem | 80% | 120% |
| Perfumaria | 60% | 100% |
| Corpo e Banho | 80% | 130% |
| Cabelos | 80% | 120% |
| Masculino | 70% | 110% |
| Kits/Bundles | 70% | 110% |

---

## KPIs

| Métrica | Meta |
|---------|------|
| Margem bruta geral | > 40% |
| Produtos abaixo da margem mínima | 0 |

---

## Entradas

- Custo de aquisição (Supplier Agent)
- Preços da concorrência (Product Research)
- Demanda por produto (Analytics Agent)

## Saídas

- Tabela de preços atualizada
- Alertas de produto fora da margem
- Relatório de rentabilidade por SKU
