# VERA Beauty Product
## Empresa 02 — Desenvolvimento de Produto, Formulação & Embalagem

### Missão
Desenvolver produtos de beleza e cuidado pessoal com eficácia comprovada, segurança regulatória, sensorial diferenciado e custo que viabilize margens saudáveis.

### Escopo
- Pesquisa e desenvolvimento (P&D) de formulações
- Gestão de portfólio e roadmap de produto
- Aprovação ANVISA e conformidade regulatória
- Design e desenvolvimento de embalagem
- Seleção de laboratórios e fornecedores de insumos
- Testes de estabilidade, segurança e eficácia
- Fichas técnicas e dossiês de produto

### Entradas
- Pesquisa de cliente e dores (← Customer)
- Tendências de mercado e ingredientes (pesquisa externa)
- Budget de P&D aprovado (← Finance)
- Feedback de produto e devoluções (← Customer / Operations)

### Saídas
- Fichas técnicas completas por SKU
- Dossiê regulatório ANVISA
- Protótipos para teste
- Aprovação de embalagem e arte-final
- Custo de produção por SKU (← Finance/Pricing)
- SKU pronto para produção (→ Operations)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| SKUs em desenvolvimento | 4 | 8 | 20 |
| SKUs aprovados ANVISA | 2 | 6 | 15 |
| Custo de P&D por SKU | R$ 8K | R$ 6K | R$ 4K |
| Tempo de D&D até aprovação | 90 dias | 75 dias | 60 dias |
| Taxa de aprovação em 1ª submissão | 70% | 80% | 90% |
| CMV médio do portfólio | 30% | 28% | 25% |

### Agentes Internos
- **04 — Product Development Agent** → roadmap de produto, stage-gate, P&D
- **05 — Formulation Agent** → INCI, segurança, eficácia, laboratório
- **06 — Packaging Agent** → embalagem, design, sustentabilidade, custo

### Handoffs
- `Beauty Product → Operations` : fichas técnicas, especificações, SKUs aprovados
- `Beauty Product → Finance` : CMV por SKU, custo de P&D
- `Beauty Product → Growth` : claims de produto, diferenciais de comunicação

### Stage Gate de Produto

```
[Conceito] → [Briefing] → [Formulação] → [Teste Interno]
     → [Estabilidade] → [Anvisa] → [Embalagem] → [Piloto]
     → [Aprovação Final] → [Produção]
```

### Ferramentas
- Notion (roadmap e fichas)
- Supabase (banco de SKUs)
- SIEVE / Mintel (tendências de ingredientes)
- Portal ANVISA (submissões)
- Adobe Illustrator (arte de embalagem)
