# Plano Estratégico de Produto — Fashion OS Web
**PHYLLOS | CEO | Junho 2026**

> **⚠️ ARQUIVO HISTÓRICO — supersedido em 2026-06-27.**
> Este documento descreve a hipótese de Fashion OS Fase 2 (Next.js, interface interna, pipeline criativo). Essa direção foi abandonada.
> **O plano estratégico vigente é o DPP Studio SaaS B2B.** Fontes canônicas: `produto/decisoes/prd-dpp-integrado-v0.md`, `produto/decisoes/tese-produto-dpp-integrado-phyllos.md` e `.claude/agents/references/dpp-integrado-strategic-premises.md`.
> Manter este arquivo apenas como registro de decisão de pivô.

> **Nota anterior (2026-06-11):** este plano registra a hipotese anterior de interface web do Fashion OS. A prioridade executiva atual e o **Parametric Pattern Engine**: Playbook, endpoint de molde, saia reta parametrica, SVG estatico, PDF A4, PatternValidator, validacao fisica e beta users. A interface completa e a linguagem natural passam a ser fases posteriores, nao MVP imediato.

## 1. Tese de produto

**Por que construir agora:** A Fase 1 entregou um sistema funcional de pipeline criativo. O problema é que só funciona para quem opera via terminal. A Fase 2 converte potencial interno em capacidade operacional real. Sem ela, o Fashion OS é uma prova de conceito, não uma plataforma de negócio.

**Para quem:** usuário primário é o próprio time da PHYLLOS (1–3 pessoas). Não é produto para cliente final. Não é SaaS de moda ainda. É uma ferramenta de operação interna para que o ciclo criar-documentar-produzir-lançar deixe de depender de linha de comando.

**Por que importa para a tese:** A PHYLLOS compete com velocidade de aprendizado validado. Uma interface que permita ciclos de feedback mais rápidos entre ideia, ficha técnica e amostra reduz diretamente o tempo entre decisão criativa e prova de mercado.

---

## 2. Prioridades da Fase 2

### Decisão de stack — antes de qualquer coisa

- **Streamlit:** deploy em 2–3 dias, sem frontend dedicado, mas teto de UX baixo. Não escala para Fase 4-5. Não suporta WebSocket para ComfyUI na Fase 3.
- **Next.js:** 1–2 semanas para primeiro deploy funcional, mas sustenta todas as fases seguintes sem reescrita.

**Recomendação:** Next.js. O custo adicional de 10–15 dias agora evita uma reescrita completa em 6 meses. Se o CTO não tiver bandwidth nas próximas 2 semanas, Streamlit como ponte aceitável, com acordo explícito de descarte na Fase 3.

### Deve ter (MVP real)

- Cadastro de coleção (nome, temporada, conceito, status)
- Cadastro de peça com upload de imagem de referência
- Galeria de imagens por peça
- Exportação PDF de ficha técnica (substituível ao template atual)
- Autenticação básica (email/senha) — sem OAuth nesta fase

### Nice-to-have (não agora)

- Histórico de versões de ficha técnica
- Comentários e anotações por peça
- Filtros avançados na galeria
- Dashboard de status da coleção
- Busca full-text

### Explicitamente fora desta fase

- Geração de imagem (ComfyUI, Stable Diffusion) → Fase 3
- Personas digitais → Fase 3
- MRP, ordem de produção, estoque → Fase 4
- Integração com fornecedor, plataforma de venda ou ERP → Fase 5
- Modo público ou acesso para cliente final

---

## 3. Critérios de sucesso da Fase 2

**Critério 1 — Operacional:** qualquer membro do time cria coleção + peça + exporta PDF sem abrir terminal. Tempo máximo: 15 minutos para quem usa pela primeira vez.

**Critério 2 — Cobertura de dados:** as peças da coleção ativa estão todas cadastradas na plataforma antes do fim da Fase 2.

**Critério 3 — PDF utilizável:** o PDF exportado é aceito pelo fornecedor sem reformatação.

---

## 4. Dependências críticas

**CTO precisa resolver antes:**
1. Decisão de stack documentada
2. Banco acessível por mais de uma pessoa (SQLite local vs. Supabase)
3. URL de deploy definida

**CPO precisa resolver antes:**
1. Mapeamento de campos da ficha técnica (obrigatório vs. opcional vs. aparece no PDF)
2. PDF de referência: uma ficha existente anotada como especificação de output

---

## 5. Riscos estratégicos

1. **Scope creep técnico** — a interface da Fase 2 não precisa chamar agentes Claude. Precisa cadastrar e exportar. Integração com agentes é Fase 3.
2. **Nenhum usuário real testando durante o build** — alguém do time precisa usar toda semana durante o desenvolvimento.
3. **PDF inferior ao template atual** — se o PDF exportado for pior que o template Markdown, o time vai ignorar a plataforma.
4. **Fase 3 começando antes da Fase 2 terminar** — a regra é: critérios de sucesso verificados antes de qualquer linha de Fase 3.

---

## 6. Próximas 72 horas — as 3 decisões

| Decisão | Owner | Prazo | Formato |
|---|---|---|---|
| Stack: Next.js vs. Streamlit | CEO + CTO | 24h | Decisão documentada em 1 parágrafo |
| Campos do MVP (obrigatório/opcional/PDF) | CPO | 48h | Planilha simples |
| PDF de referência (ficha anotada) | CPO | 72h | 1 ficha existente marcada |

**KPIs afetados:** velocidade de aprendizado validado, percentual de iniciativas com owner claro, redução de dispersão estratégica.
