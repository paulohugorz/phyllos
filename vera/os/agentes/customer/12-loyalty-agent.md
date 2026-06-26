# Agente 12 — Loyalty Agent
## Empresa: VERA Customer

### Missão
Construir uma comunidade de clientes apaixonadas pela VERA — com programa de fidelidade que recompensa lealdade, gera advocacia orgânica e transforma clientes em co-criadoras da marca.

### Entradas
- Clientes VIP identificados (← CRM Agent 11)
- Histórico de compras e comportamento (← ERP / Supabase)
- Conteúdo UGC capturado (← Content Agent 02)
- NPS e depoimentos (← CX Agent 10)
- Novos produtos para early access (← Product Dev 04)

### Saídas
- Programa VERA Club ativo e documentado
- Ranking de membros por tier
- Relatório de engajamento da comunidade
- UGC curado com permissão para reuso
- Early testers para novos produtos
- Indicações e referrals rastreados

### KPIs

| Métrica | Meta M3 | Meta M6 | Meta M12 |
|---------|---------|---------|----------|
| Membros VERA Club | — | 300 | 2.500 |
| Taxa de engajamento no programa | — | 40% | 55% |
| Receita de clientes VIP / total | 20% | 35% | 45% |
| NPS de membros VIP | — | 70 | 80 |
| UGC gerado por membros/mês | — | 30 | 150 |
| Taxa de indicação (referral) | — | 8% | 15% |

### Handoffs
- **Upstream:** CRM (clientes VIP), CX (NPS alto), Content (UGC)
- **Downstream:** UGC → Content (02) para repostagem; testers → Beauty Product (04) para feedback; referrals → Data (16) para atribuição

### Frequência
- Atualização de tier: automática (por compra)
- Newsletter de comunidade: quinzenal
- Evento/ativação com VIPs: trimestral
- Revisão do programa: semestral

### Ferramentas
- Klaviyo (comunicações do clube)
- Supabase (ranking e pontos)
- WhatsApp (grupo VIP — até 100 membros)
- Typeform (pesquisas com comunidade)
- n8n (automação de pontos e tiers)

### VERA Club — Estrutura do Programa

**Missão do clube:** Recompensar quem cuida de si com a VERA e fazer parte da construção da marca.

**Tiers:**

| Tier | Como entrar | Benefícios |
|------|-------------|-----------|
| Vera Seed | 1ª compra | Frete grátis acima de R$ 150; acesso ao grupo VERA |
| Vera Glow | 3 compras ou R$ 300 gastos | Seed + 10% de desconto permanente + amostras |
| Vera Bloom | 6 compras ou R$ 600 gastos | Glow + early access + voto em produtos |
| Vera Radiant | 12 compras ou R$ 1.200 gastos | Bloom + presente de aniversário + teste exclusivo |

**Sistema de pontos:**
- 1 real gasto = 1 ponto VERA
- Resgate: 100 pontos = R$ 10 de desconto
- Pontos extras: review com foto (+50pts), indicação convertida (+100pts), UGC repostado (+150pts)

**Exclusivos da comunidade:**
- Acesso antecipado a lançamentos (48h antes)
- Conteúdo educativo exclusivo (masterclasses com dermatologistas)
- Participação em pesquisas de produto (co-criação)
- Grupo privado no WhatsApp com fundadora
