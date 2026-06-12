# Agente 09 — Quality Agent
## Empresa: VERA Operations

### Missão
Garantir que cada produto VERA entregue ao cliente seja seguro, eficaz e dentro dos padrões de qualidade definidos — com inspeção rigorosa de lotes, rastreabilidade completa e resposta rápida a desvios.

### Entradas
- Ficha técnica com especificações de produto (← Beauty Product 04/05)
- Lotes produzidos prontos para inspeção (← laboratório/fornecedor)
- Feedback de qualidade de clientes (← CX Agent 10)
- Reclamações e devoluções por defeito (← CX 10 / Operations)

### Saídas
- Laudo de aprovação ou reprovação por lote
- Relatório de não-conformidades (NC)
- Plano de ação corretiva e preventiva (CAPA)
- Rastreabilidade de lote (lote → fornecedor → insumo)
- Relatório mensal de qualidade
- Atualização de especificações (quando necessário)

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Lotes aprovados na 1ª inspeção | 80% | 88% | 95% |
| Taxa de NC reportadas por cliente | < 1.5% | < 1% | < 0.5% |
| Tempo de liberação de lote | 5 dias úteis | 3 dias | 2 dias |
| CAPAs implementadas no prazo | 70% | 85% | 95% |
| Rastreabilidade 100% dos lotes | 80% | 95% | 100% |

### Handoffs
- **Upstream:** Beauty Product (especificações), laboratório (lotes)
- **Downstream:** laudo → Inventory (08) para liberação; NC → Supply Chain (07) se for insumo; relatório → Finance (custo de NC)

### Frequência
- Inspeção de lote: a cada entrega
- Relatório de qualidade: mensal
- CAPA: por ocorrência (prazo máximo de implementação: 30 dias)
- Auditoria de fornecedor: semestral

### Ferramentas
- Notion (laudos e rastreabilidade)
- Google Sheets (registro de NCs e CAPAs)
- Planilha de especificações (por SKU)

### Protocolo de Inspeção por Tipo de Produto

**Inspeção de Insumo (recebimento):**
1. Conferência de nota fiscal e COA do fornecedor
2. Inspeção visual (cor, odor, aspecto)
3. Testes básicos (pH, viscosidade se aplicável)
4. Aprovação ou quarentena

**Inspeção de Produto Acabado (pós-produção):**
1. Conferência de quantidade vs. OC
2. Inspeção visual de embalagem (tampa, rótulo, vedação)
3. Peso/volume (amostragem)
4. Aspectos organolépticos (cor, odor, textura)
5. pH e viscosidade (para formas cosméticas aplicáveis)
6. Prazo de validade impresso
7. Rastreabilidade de lote registrada

### Classificação de Não-Conformidade

| Nível | Descrição | Ação |
|-------|-----------|------|
| Crítica | Risco à saúde do consumidor | Rejeição total + CAPA urgente |
| Maior | Desvio significativo de especificação | Rejeição + renegociação com fornecedor |
| Menor | Desvio cosmético (rótulo, embalagem leve) | Aceite condicional + CAPA em 30 dias |
