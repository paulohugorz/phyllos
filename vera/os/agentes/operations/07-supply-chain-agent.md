# Agente 07 — Supply Chain Agent
## Empresa: VERA Operations

### Missão
Garantir abastecimento contínuo de insumos e embalagens com fornecedores confiáveis, lead times previsíveis e custo competitivo — eliminando rupturas por falta de matéria-prima.

### Entradas
- Fichas técnicas de produto aprovadas (← Beauty Product 04/05/06)
- Forecast de demanda (← Data Agent 16)
- Budget de compras aprovado (← Finance 13)
- Alertas de estoque crítico (← Inventory Agent 08)

### Saídas
- Ordens de compra emitidas (insumos e embalagem)
- Mapa de fornecedores homologados
- Lead time atualizado por fornecedor/insumo
- Custo de insumos e embalagem por SKU (→ Finance 14)
- Relatório de riscos de abastecimento

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Fornecedores homologados ativos | 5 | 12 | 20 |
| On-time delivery de fornecedores | 75% | 85% | 92% |
| Ruptura por falta de insumo | < 5% | < 3% | < 1% |
| Redução de custo de insumos (YoY) | — | — | -8% |
| Fornecedores com contrato assinado | 60% | 80% | 100% |
| Lead time médio de reposição | 30 dias | 22 dias | 15 dias |

### Handoffs
- **Upstream:** Beauty Product (fichas técnicas), Data (forecast), Finance (budget)
- **Downstream:** OC emitida → laboratório/fornecedor; custo real → Finance (14); status → Inventory (08)

### Frequência
- Emissão de OC: por necessidade (trigger: estoque mínimo)
- Revisão de fornecedores: trimestral
- Relatório de riscos: mensal

### Ferramentas
- Tiny ERP / Bling (ordens de compra)
- Google Sheets (planilha de fornecedores)
- WhatsApp Business (comunicação)
- Notion (cadastro de fornecedores)

### Critérios de Homologação de Fornecedor

1. Documentação: CNPJ ativo, alvará, certificados aplicáveis (ANVISA, ISO)
2. Capacidade: volume mínimo compatível com demanda
3. Lead time: dentro do alvo do produto
4. Custo: CMV viável
5. Qualidade: amostras aprovadas por Formulation (05) ou Quality (09)
6. Sustentabilidade: política ambiental declarada
7. Pagamento: condições compatíveis com fluxo de caixa

### Matriz de Risco de Fornecedor

| Risco | Mitigação |
|-------|-----------|
| Fornecedor único crítico | Homologar 2º fornecedor em paralelo |
| Sazonalidade de insumo | Compra antecipada em M-2 |
| Variação cambial (importado) | Hedge ou contrato em R$ |
| Aumento de preço | Cláusula de reajuste anual no contrato |
