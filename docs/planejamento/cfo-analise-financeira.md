# Análise Financeira e de Recursos — Fashion OS Fase 2

> **Nota vigente em 2026-06-11:** atualizar qualquer leitura financeira deste documento pela premissa do Motor de Moldes. O risco principal agora e precisao tecnica + validacao de beta users, nao custo de interface web. Receita SaaS ampla so deve ser tratada como hipotese posterior a prova do patternmaking engine.
**PHYLLOS / CFO / Junho 2026**

## Leitura Executiva

A PHYLLOS opera hoje com custo de infraestrutura próxima de zero: Fashion OS v1 roda localmente. O risco imediato não é caixa de infra — é o custo de decisão errada de stack na virada para a Fase 2. Escolher arquitetura cara antes de ter receita é erro clássico. Escolher uma que não escala e precisa ser refeita em 6 meses tem custo ainda maior: tempo de engenharia e perda de aprendizado acumulado no código.

---

## Estimativa de Custos por Decisão de Stack

### Frontend

| Opção | Custo/mês | Observação |
|---|---|---|
| Streamlit (local) | R$ 0 | Acesso só local |
| Streamlit Cloud Free | R$ 0 | 1 app, dorme após inatividade |
| Next.js (local/dev) | R$ 0 | Precisa de Node |
| Next.js + Vercel Hobby | R$ 0 | Funciona para uso interno sem SLA |
| Next.js + Vercel Pro | ~R$ 200/mês | Necessário em uso comercial real |

**Veredicto CFO:** Streamlit resolve a Fase 2 com zero reais. O custo não é financeiro — é de UX e escala. Se a interface for apenas para uso interno, Streamlit é correto *financeiramente*. O CTO tem veto técnico (e recomenda Next.js) — aceitar.

### Banco de Dados

| Opção | Custo/mês | Observação |
|---|---|---|
| SQLite (local) | R$ 0 | Correto para uso solo |
| SQLite + Litestream → R2 | ~R$ 5 | Adiciona resiliência — **recomendado** |
| Supabase Free | R$ 0 | 500MB, pausa após 1 semana inativo |
| Supabase Pro | ~R$ 125/mês | Necessário na Fase 4-5 |

### Armazenamento de Imagens

| Opção | Custo/mês | Limite | Observação |
|---|---|---|---|
| Local (pasta no disco) | R$ 0 | Limite do HD | Sem CDN |
| Cloudflare R2 | R$ 0 | 10 GB permanentes | **Zero egress fee — melhor opção** |
| Cloudinary Free | R$ 0 | 25 GB storage | Otimização de imagem inclusa |
| AWS S3 Free Tier | R$ 0 | 5 GB (expira em 12 meses) | Evitar |

**Veredicto CFO:** Cloudflare R2 é a melhor escolha. Zero egress fee (diferente do S3), compatível com boto3/S3 SDK, 10 GB gratuitos permanentes. Adicionar Cloudinary Free por cima para otimização de thumbnails.

---

## Stack Fase 2 com Custo R$0/mês

| Componente | Solução | Custo |
|---|---|---|
| Frontend | Next.js local (ou Streamlit se CTO decidir) | R$ 0 |
| Banco | SQLite local + backup automático Google Drive | R$ 0 |
| Imagens | Cloudflare R2 (10 GB gratuitos permanentes) | R$ 0 |
| Deploy | Local (máquina do founder) | R$ 0 |
| Autenticação | Sem (uso interno) | R$ 0 |
| LLM/Agentes | Claude Code (já no fluxo operacional) | Variável |
| **Total de infra** | | **R$ 0/mês** |

O único custo monetário da Fase 2 é uso de Claude Code para construir e iterar — já no orçamento operacional atual.

---

## Prioridade por ROI Operacional

| Prioridade | Feature | Impacto | Esforço |
|---|---|---|---|
| 1 | Dashboard de status do Fashion OS | Elimina 30–60 min/semana de navegação em CLI | Baixo |
| 2 | Gerenciamento de imagens de produto | Centraliza referências visuais espalhadas em pastas locais | Médio |
| 3 | Visualização de BOM e CMV por SKU | Elimina planilhas paralelas com risco de erro de versão | Baixo |
| 4 | Interface de agentes (chat ou log de decisões) | Rastreabilidade — mais narrativo que operacional | Médio |
| 5 | Autenticação e controle de acesso | Necessário quando houver colaboradores externos | Baixo |

---

## Gatilhos de Upgrade de Infraestrutura

| Serviço atual | Quando fazer upgrade | Custo do upgrade | Momento esperado |
|---|---|---|---|
| SQLite → PostgreSQL | >2 usuários simultâneos, ou >5.000 SKUs | R$ 125/mês (Supabase Pro) | Fase 4 (MRP e estoque) |
| Next.js local → Vercel Pro | Interface precisa de acesso público a cliente final | R$ 200/mês | Fase 5 (vendas) |
| R2 gratuito → pago | Catálogo de imagens acima de 10 GB (~5.000 fotos em alta resolução) | R$ 0,015/GB | Após primeiro lançamento com catálogo fotográfico completo |
| Deploy local → cloud | Fashion OS precisa rodar 24/7 sem depender da máquina do founder | R$ 25/mês (Railway) | Quando fundador precisar apresentar o sistema remotamente com frequência |

---

## Riscos Financeiros — Custos Surpresa

### Risco 1 — GPU para ComfyUI (Fase 3) — ALTO ⚠️

Este é o item de maior exposição financeira do roadmap inteiro.

| Opção | Custo | Recomendação |
|---|---|---|
| RTX 4090 nova | R$ 12.000–18.000 (capex) | Não comprar agora |
| RTX 3080 usada | R$ 4.000–8.000 (capex) | Não comprar agora |
| RunPod pay-per-use (RTX 4090) | ~R$ 4/hora (~R$ 40–200/mês) | **Recomendado** |
| Modal.com | Similar ao RunPod | Alternativa |

**Break-even:** RTX 3080 usada (R$ 5.000) vs. RunPod (R$ 200/mês) = 25 meses. Em fase pré-receita, o capital é mais valioso que a conveniência.

**Decisão que precisa de aprovação do CEO:** não comprar GPU antes de 3 meses de uso consistente de geração de imagem em produção.

### Risco 2 — Limites de free tier que "dormem"
Supabase Free pausa após 1 semana sem acesso. Streamlit Cloud Free dorme após inatividade. **Mitigação:** script de "wake up" que acessa cada endpoint antes de qualquer apresentação.

### Risco 3 — Custo de tokens Claude Code em iteração de frontend
Uma sessão de desenvolvimento de 2–3 horas pode custar USD 5–20 dependendo do modelo e do contexto carregado. **Mitigação:** usar subagentes especializados com contexto mínimo, separar sessões de planejamento (texto) de sessões de código.

### Risco 4 — Dívida técnica de SQLite na transição para Fase 4
**Mitigação:** implementar Alembic para controle de migrações desde o início da Fase 2. Custo: zero de infra, 2–4 horas de configuração inicial.

---

## Recomendação Consolidada

**Agora (Fase 2):**
1. Manter SQLite + backup automático para Google Drive + Alembic para controle de migrações
2. Cloudflare R2 para imagens — gratuito, permanente, pronto para escala
3. Não migrar para cloud ainda
4. Primeiro real gasto em infra: Litestream para R2 (~R$ 5/mês) — resolve maior risco operacional (perda de dados)

**Fase 3 — GPU:** usar RunPod pay-per-use até exceder 25h/mês de uso consistente.
