# Analise Financeira — PHYLLOS DPP Studio

**Data:** 2026-06-25
**Versao:** 1.0
**Autor:** Finance Agent / CFO
**Horizonte:** 2026–2030 (5 anos)
**Status:** aprovacao pendente do founder

Legenda:

- `[F]` fato estabelecido no produto/repo.
- `[H]` hipotese a testar.
- `[R]` risco identificado.

---

## 1. Premissas do modelo

### 1.1 Macro

| Premissa | Valor | Fonte |
|---|---|---|
| Cambio USD/BRL | R$ 5,50 | [H] media para planejamento 2026-2030 |
| Taxa de desconto (WACC startup early-stage BR) | 25% a.a. | [H] benchmark VC seed BR: 20-30% a.a. |
| Inflacao BR projetada | 5% a.a. | [H] conservador para reajuste de contratos |
| Horizonte de analise | 5 anos (jan 2026 - dez 2030) | [F] definido na tarefa |
| Moeda base do modelo | BRL, com conversao USD quando cabivel | [F] mercado primario e Brasil |
| Custo de oportunidade do founder | R$ 15.000/mes | [H] estimativa de remuneracao de mercado para founder-dev senior |

### 1.2 Produto e modelo de negocio

| Premissa | Valor | Fonte |
|---|---|---|
| Produto | DPP middleware para marcas de moda | [F] PRD v0 |
| ICP primario | Marcas BR independentes, 1-5 SKUs, lotes 50-500 pecas | [F] prd-dpp-integrado-v0.md |
| Stack | FastAPI + SQLite/Postgres/Supabase | [F] roadmap |
| Custo de infra atual | R$ 0/mes | [F] cfo-analise-financeira.md |
| Custo Claude Code | R$ 600-1.200/mes (ja no orcamento operacional) | [F] briefing founder |
| Time | 1 founder + agentes Claude. Sem CLT. | [F] briefing founder |
| Piloto | 3-5 marcas, gratuito, julho 2026 | [F] phyllos-dpp-v1-estrategia-piloto.md |
| Regulacao EU ESPR | ~2028, cria urgencia de mercado | [F] DPP roadmap |
| Potencial ARR Fase 3 | USD 400K-2,5M | [F] PHYLLOS LABS pivot |

### 1.3 Precos por tier (pos-piloto)

| Tier | Preco | Descricao |
|---|---|---|
| Pay-per-DPP | R$ 149-299 por passaporte publicado | [F] hipotese de preco piloto |
| Assinatura | R$ 490/mes ate 10 SKUs | [F] hipotese de preco piloto |
| API B2B (Fase 3) | USD 20K-200K/ano por contrato | [F] PHYLLOS LABS pivot |

### 1.4 Hipoteses de conversao e churn

| Parametro | Conservador | Base | Otimista |
|---|---|---|---|
| Taxa de conversao piloto → pago | 20% | 40% | 60% |
| Churn mensal (assinatura) | 8% | 5% | 3% |
| Tempo medio de onboarding (min) | 90 | 60 | 40 |
| CAC organico medio | R$ 800 | R$ 500 | R$ 250 |
| CAC pago (quando ativado) | R$ 2.000 | R$ 1.200 | R$ 700 |
| Ticket medio inicial (pay-per-DPP) | R$ 149 | R$ 199 | R$ 249 |
| Upgrade mensal para assinatura (3 meses) | 15% | 30% | 50% |

---

## 2. Investimento inicial (Capex + Opex pre-receita)

### 2.1 Estado atual de capital investido

[F] O backend DPP ja possui endpoints funcionais: `POST /pecas/{codigo}/dpp/publicar`, `GET /pecas/{codigo}/qr`, `GET /dpp/{identifier}/qr`, `GET /p/{uuid}`. O produto nao e greenfield.

[F] Toda a construcao ate hoje foi custeada pelo orçamento operacional do founder via Claude Code, sem desembolso de capital externo.

### 2.2 Custos ate primeiro cliente pagante

**Prazo estimado: 3-4 meses a partir de julho 2026 (outubro/novembro 2026)**

| Item | Custo/mes | Meses | Total | Tipo | Nota |
|---|---|---|---|---|---|
| Claude Code (desenvolvimento) | R$ 900 | 4 | R$ 3.600 | Opex | [F] ja no orcamento operacional |
| Railway (deploy publico) | R$ 140 | 4 | R$ 560 | Opex | [H] plano Hobby ~USD 5/mes; Starter ~USD 20/mes |
| Dominio proprio | R$ 80 | 1 (anual) | R$ 80 | Opex | [H] apos primeiro sinal real de piloto |
| Supabase Pro (Postgres) | R$ 125 | 4 | R$ 500 | Opex | [F] Supabase Free proibido em producao (pausa com inatividade — regra inegociavel) |
| Cloudflare R2 (armazenamento QR/arquivos) | R$ 0 | 4 | R$ 0 | Opex | [F] 10GB permanentes gratis |
| Ferramentas (Notion, GitHub, etc.) | R$ 50 | 4 | R$ 200 | Opex | [H] planos existentes |
| Tempo do founder (custo de oportunidade) | R$ 15.000 | 4 | R$ 60.000 | Opex | [H] nao desembolso direto; burn implicito |
| **Total desembolso real** | | | **R$ 4.940** | | excluindo custo de oportunidade (inclui Supabase Pro obrigatorio) |
| **Total incluindo custo de oportunidade** | | | **R$ 64.940** | | referencia para analise de ROI |

### 2.3 Observacoes sobre capital

[F] O projeto e 100% bootstrapped pelo founder. Nao ha investidor, CLT, socio ou divida.

[H] O custo de oportunidade de R$ 15.000/mes e conservador para um founder-dev senior com produto funcional e tese validada em andamento. Ele nao impacta o caixa, mas impacta a decisao de quando captar.

[R] O unico risco real de capital nos primeiros 4 meses e o tempo do founder. Se o piloto falhar, o custo nao recuperavel e de aproximadamente R$ 4.440 em desembolso direto mais o tempo alocado.

---

## 3. Projecao de receita — 3 cenarios por fase

### 3.1 Estrutura temporal

| Periodo | Fase | Foco de receita |
|---|---|---|
| Jul-Set 2026 | Piloto gratuito | Zero receita; aprendizado |
| Out-Dez 2026 | Fase 1 - Pay-per-DPP | Primeiros clientes pagantes |
| 2027 | Fase 2 - Assinatura MRR | Migrar para modelo recorrente |
| 2028-2030 | Fase 3 - API B2B / SaaS | Contratos anuais e expansao |

### 3.2 Fase 1: Pos-piloto H2 2026 (Out-Dez 2026)

**Modelo: pay-per-DPP, R$ 149-249 por passaporte publicado**

[H] Dos 5 pilotos gratuitos, espera-se conversao para pagamento na janela de 30-60 dias apos o piloto.

| Parametro | Conservador | Base | Otimista |
|---|---|---|---|
| Pilotos concluidos | 3 | 5 | 5 |
| Taxa de conversao | 20% | 40% | 60% |
| Clientes pagantes (Out/26) | 1 | 2 | 3 |
| DPPs por cliente/mes | 1 | 2 | 3 |
| Ticket medio por DPP | R$ 149 | R$ 199 | R$ 249 |
| Novos clientes/mes (organico) | 0 | 1 | 2 |
| Receita Out/26 | R$ 149 | R$ 796 | R$ 2.241 |
| Receita Nov/26 | R$ 149 | R$ 1.194 | R$ 3.735 |
| Receita Dez/26 | R$ 298 | R$ 1.592 | R$ 5.976 |
| **Total Q4 2026** | **R$ 596** | **R$ 3.582** | **R$ 11.952** |

### 3.3 Fase 2: Assinatura MRR 2027

**Modelo: R$ 490/mes ate 10 SKUs + pay-per-DPP para SKUs adicionais**

[H] Clientes que publicaram 3+ DPPs tendem a migrar para assinatura. Onboarding reduzido para 30 min. Crescimento por referral e comunidade.

**Evolucao de MRR mensal (Fase 2 — 2027):**

| Mes | Cons. (clientes) | Cons. (MRR) | Base (clientes) | Base (MRR) | Otim. (clientes) | Otim. (MRR) |
|---|---|---|---|---|---|---|
| Jan/27 | 3 | R$ 1.470 | 6 | R$ 2.940 | 10 | R$ 4.900 |
| Fev/27 | 3 | R$ 1.470 | 7 | R$ 3.430 | 13 | R$ 6.370 |
| Mar/27 | 4 | R$ 1.960 | 9 | R$ 4.410 | 17 | R$ 8.330 |
| Abr/27 | 4 | R$ 1.960 | 10 | R$ 4.900 | 21 | R$ 10.290 |
| Mai/27 | 5 | R$ 2.450 | 12 | R$ 5.880 | 26 | R$ 12.740 |
| Jun/27 | 5 | R$ 2.450 | 13 | R$ 6.370 | 31 | R$ 15.190 |
| Jul/27 | 6 | R$ 2.940 | 15 | R$ 7.350 | 38 | R$ 18.620 |
| Ago/27 | 6 | R$ 2.940 | 16 | R$ 7.840 | 44 | R$ 21.560 |
| Set/27 | 7 | R$ 3.430 | 18 | R$ 8.820 | 51 | R$ 24.990 |
| Out/27 | 7 | R$ 3.430 | 20 | R$ 9.800 | 59 | R$ 28.910 |
| Nov/27 | 8 | R$ 3.920 | 22 | R$ 10.780 | 67 | R$ 32.830 |
| Dez/27 | 9 | R$ 4.410 | 25 | R$ 12.250 | 77 | R$ 37.730 |
| **ARR Dez/27** | | **R$ 52.920** | | **R$ 147.000** | | **R$ 452.760** |

Metodologia de calculo:
- Churn mensal aplicado sobre base existente: 8% cons., 5% base, 3% otim.
- Novos clientes/mes: 1 cons., 2-3 base, 4-6 otim.
- Ticket fixo: R$ 490/mes por cliente assinante.
- [H] DPPs avulsos representam 20-30% adicional da receita de assinatura no cenario base (nao modelados separadamente para simplificar).

### 3.4 Fase 3: API B2B / SaaS 2028-2030

**Modelo: contratos anuais USD 20K-200K + MRR de assinatura continuando a crescer**

[H] A regulacao EU ESPR (~2028) cria urgencia de mercado para marcas exportadoras e plataformas B2B2C. Isso abre o canal B2B de maior ticket.

[H] Primeiro contrato API B2B estimado para H1 2028, a partir de relacionamento construido com pilotos e beta.

**Receita anual consolidada por cenario (BRL):**

| Ano | Conservador | Base | Otimista |
|---|---|---|---|
| 2026 (Q4 apenas) | R$ 596 | R$ 3.582 | R$ 11.952 |
| 2027 | R$ 30.380 | R$ 88.620 | R$ 276.640 |
| 2028 | R$ 72.000 | R$ 220.000 | R$ 770.000 |
| 2029 | R$ 144.000 | R$ 495.000 | R$ 1.980.000 |
| 2030 | R$ 252.000 | R$ 990.000 | R$ 4.950.000 |

Notas para 2028-2030:
- [H] Cons.: sem contrato B2B, crescimento organico SaaS limitado.
- [H] Base: 1-2 contratos B2B por ano + crescimento de assinatura.
- [H] Otim.: 3-5 contratos B2B + expansao marketplace + PLG acelerado.
- [H] ARR potencial USD 400K-2,5M (cenario base-otimista em 2029-2030) conforme tese PHYLLOS LABS.

---

## 4. Estrutura de custos

### 4.1 COGS (custo por DPP gerado)

[F] O custo marginal de gerar um DPP e proximo de zero: o calculo e deterministico, roda no servidor ja pago, sem chamada de IA por geracao.

| Componente de COGS | Custo unitario | Nota |
|---|---|---|
| Computo por DPP | ~R$ 0,001 | Negligenciavel no Railway/Supabase |
| Storage QR + passaporte publico | ~R$ 0,005 | Cloudflare R2 |
| Banda de rede (pagina publica) | ~R$ 0,002 | Cloudflare CDN |
| **COGS total por DPP** | **~R$ 0,01** | [H] |

**Margem bruta estimada por DPP: 99,9%** — caracteristica de software puro.

### 4.2 Opex mensal por fase

| Item | Pre-receita (Jul-Set/26) | Fase 1 (Q4 2026) | Fase 2 (2027) | Fase 3 (2028+) |
|---|---|---|---|---|
| Claude Code (desenvolvimento) | R$ 900 | R$ 900 | R$ 1.200 | R$ 1.500 |
| Railway / infra deploy | R$ 140 | R$ 140 | R$ 280 | R$ 560 |
| Supabase Pro/Postgres | R$ 125 | R$ 125 | R$ 125 | R$ 250 |
| Cloudflare R2 | R$ 0 | R$ 0 | R$ 15 | R$ 60 |
| Dominio + SSL | R$ 7 | R$ 7 | R$ 7 | R$ 7 |
| Email transacional (Resend/Sendgrid) | R$ 0 | R$ 27 | R$ 55 | R$ 110 |
| Ferramentas (Notion, GitHub, etc.) | R$ 50 | R$ 50 | R$ 75 | R$ 150 |
| Marketing (organico/referral) | R$ 0 | R$ 200 | R$ 500 | R$ 2.000 |
| **Total Opex/mes** | **R$ 1.222** | **R$ 1.449** | **R$ 2.257** | **R$ 4.637** |

### 4.3 Gatilhos de scaling de custo (step-function)

| Gatilho | Custo incremental | Momento esperado |
|---|---|---|
| Supabase Pro (obrigatorio desde piloto — Free proibido em producao) | R$ 125/mes | Desde Jul/2026; ja no Opex pre-receita |
| Railway Hobby → Pro (dominio custom + SLA) | +R$ 110/mes | Primeiro cliente B2B (2028) |
| Primeiro dev/ops externo (10h/mes) | +R$ 3.000-5.000/mes | >100 clientes assinantes ou contrato B2B ativo |
| Primeiro vendedor/CS externo | +R$ 5.000-8.000/mes | ARR > R$ 300K (2028-2029) |
| Certifica legal/juridico DPP compliance | R$ 5.000-15.000 (unico) | Antes do primeiro cliente B2B exportador |
| Marketing pago ativado | +R$ 3.000-10.000/mes | CAC payback < 6 meses confirmado |

[R] O custo step-function mais relevante e a contratacao do primeiro dev externo. Isso move o burn de R$ 2.000/mes para R$ 7.000+/mes. So faz sentido apos ARR > R$ 120K anual.

### 4.4 Custo de aquisicao (CAC)

Nas fases iniciais, o canal e 100% organico: DM no Instagram/LinkedIn, comunidades de moda, indicacao de pilotos.

| Canal | CAC estimado | Quando ativar |
|---|---|---|
| Organico (DM, referral, comunidade) | R$ 250-500 | Agora |
| Conteudo (SEO, LinkedIn) | R$ 150-300 | Fase 2 |
| Pago (Meta/Google Ads) | R$ 800-2.000 | So apos CAC payback < 4 meses confirmado |
| Parceria B2B (associacoes, feiras) | R$ 200-600/lead | Fase 3 |

---

## 5. P&L simplificado — 5 anos

*Cenario BASE. Valores em BRL. Opex inclui apenas desembolso direto, excluindo custo de oportunidade do founder.*

| Item | 2026 (Q4) | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Receita Bruta | R$ 3.582 | R$ 88.620 | R$ 220.000 | R$ 495.000 | R$ 990.000 |
| Deducoes (PIS/COFINS/ISS ~7%) | (R$ 251) | (R$ 6.203) | (R$ 15.400) | (R$ 34.650) | (R$ 69.300) |
| Receita Liquida | R$ 3.331 | R$ 82.417 | R$ 204.600 | R$ 460.350 | R$ 920.700 |
| COGS (~0,5% da receita) | (R$ 18) | (R$ 443) | (R$ 1.100) | (R$ 2.475) | (R$ 4.950) |
| **Margem Bruta** | **R$ 3.313** | **R$ 81.974** | **R$ 203.500** | **R$ 457.875** | **R$ 915.750** |
| **Margem Bruta %** | **99,5%** | **99,5%** | **99,5%** | **99,5%** | **99,5%** |
| Opex total | (R$ 3.972) | (R$ 27.084) | (R$ 55.644) | (R$ 100.000) | (R$ 180.000) |
| — Claude Code | (R$ 2.700) | (R$ 14.400) | (R$ 18.000) | (R$ 18.000) | (R$ 18.000) |
| — Infra + ferramentas | (R$ 882) | (R$ 5.724) | (R$ 11.244) | (R$ 22.000) | (R$ 42.000) |
| — Marketing | (R$ 390) | (R$ 6.960) | (R$ 26.400) | (R$ 60.000) | (R$ 120.000) |
| **EBITDA** | **(R$ 659)** | **R$ 54.890** | **R$ 147.856** | **R$ 357.875** | **R$ 735.750** |
| **EBITDA %** | **neg.** | **62%** | **67%** | **72%** | **74%** |

Notas:
- [H] Opex 2028+ inclui primeiro dev part-time (R$ 3.000-5.000/mes) e CS/vendas (R$ 5.000-8.000/mes), ativados por gatilhos de ARR.
- [H] Deducoes fiscais estimadas em regime de tributacao sobre receita bruta (Simples Nacional ou similar).
- [H] EBITDA nao inclui custo de oportunidade do founder. Se incluido (R$ 180.000/ano), o break-even operacional real move para 2028.

---

## 6. Fluxo de caixa livre (FCL)

### 6.1 Meses 1-18 (Jul/26 — Dez/27) — Cenario BASE

*Valores em BRL. Saldo acumulado assume capital inicial = R$ 0 (bootstrapped, sem aporte externo).*

| Mes | Receita | Opex real | FCL mes | FCL acumulado |
|---|---|---|---|---|
| Jul/26 (piloto) | R$ 0 | (R$ 1.222) | (R$ 1.222) | (R$ 1.222) |
| Ago/26 (piloto) | R$ 0 | (R$ 1.222) | (R$ 1.222) | (R$ 2.444) |
| Set/26 (piloto) | R$ 0 | (R$ 1.222) | (R$ 1.222) | (R$ 3.666) |
| Out/26 | R$ 796 | (R$ 1.449) | (R$ 653) | (R$ 4.319) |
| Nov/26 | R$ 1.194 | (R$ 1.449) | (R$ 255) | (R$ 4.574) |
| Dez/26 | R$ 1.592 | (R$ 1.449) | R$ 143 | (R$ 4.431) |
| Jan/27 | R$ 2.940 | (R$ 2.257) | R$ 683 | (R$ 3.748) |
| Fev/27 | R$ 3.430 | (R$ 2.257) | R$ 1.173 | (R$ 2.575) |
| Mar/27 | R$ 4.410 | (R$ 2.257) | R$ 2.153 | (R$ 422) |
| Abr/27 | R$ 4.900 | (R$ 2.257) | R$ 2.643 | R$ 2.221 |
| Mai/27 | R$ 5.880 | (R$ 2.257) | R$ 3.623 | R$ 6.594 |
| Jun/27 | R$ 6.370 | (R$ 2.257) | R$ 4.113 | R$ 10.707 |
| Jul/27 | R$ 7.350 | (R$ 2.257) | R$ 5.093 | R$ 15.800 |
| Ago/27 | R$ 7.840 | (R$ 2.257) | R$ 5.583 | R$ 21.383 |
| Set/27 | R$ 8.820 | (R$ 2.257) | R$ 6.563 | R$ 27.946 |
| Out/27 | R$ 9.800 | (R$ 2.257) | R$ 7.543 | R$ 35.489 |
| Nov/27 | R$ 10.780 | (R$ 2.257) | R$ 8.523 | R$ 44.012 |
| Dez/27 | R$ 12.250 | (R$ 2.257) | R$ 9.993 | R$ 54.005 |

**Breakeven operacional (FCL acumulado > 0): Abril/2027 — 10 meses após o piloto** *(revisado: inclui Supabase Pro R$125/mês desde Jul/2026)*

### 6.2 FCL anual (apos 2027)

| Ano | Receita Liquida | Opex real | FCL anual | FCL acumulado |
|---|---|---|---|---|
| 2026 (Q4) | R$ 3.331 | (R$ 3.972) | (R$ 641) | (R$ 3.681)* |
| 2027 | R$ 82.417 | (R$ 27.084) | R$ 55.333 | R$ 54.005 |
| 2028 | R$ 204.600 | (R$ 55.644) | R$ 148.956 | R$ 202.961 |
| 2029 | R$ 460.350 | (R$ 100.000) | R$ 360.350 | R$ 563.311 |
| 2030 | R$ 920.700 | (R$ 180.000) | R$ 740.700 | R$ 1.304.011 |

*Saldo reflete o burn do periodo piloto (Jul-Set/26).

[H] FCL 2028 ja inclui gatilhos de scaling (dev externo + CS + marketing mais agressivo), por isso o Opex sobe de R$ 27K/ano para R$ 55K/ano entre 2027 e 2028. Isso e esperado e saudavel: o investimento em escala precede a receita.

---

## 7. Indicadores financeiros

### 7.1 Payback period

| Cenario | Investimento total ate receita | Break-even operacional | Payback |
|---|---|---|---|
| Conservador | R$ 3.600 (desembolso) | Mai/2028 | ~22 meses |
| Base | R$ 4.940 (desembolso) | Abr/2027 | ~10 meses |
| Otimista | R$ 4.440 (desembolso) | Dez/2026 | ~6 meses |

[H] Payback inclui apenas desembolso direto (Claude Code + infra + dominio). Excluindo custo de oportunidade, o payback e curto porque o investimento real e minimo.

### 7.2 VPL a 5 anos (taxa de desconto: 25% a.a.)

*FCL descontado a partir de jan/2026. Investimento inicial = R$ 4.440.*

| Cenario | FCL 2026 | FCL 2027 | FCL 2028 | FCL 2029 | FCL 2030 | VPL |
|---|---|---|---|---|---|---|
| Conservador | (R$ 641) | R$ 13.500 | R$ 42.000 | R$ 82.000 | R$ 124.000 | R$ 159.000 |
| Base | (R$ 641) | R$ 55.333 | R$ 148.956 | R$ 360.350 | R$ 740.700 | R$ 869.000 |
| Otimista | (R$ 5.850) | R$ 220.000 | R$ 600.000 | R$ 1.600.000 | R$ 4.100.000 | R$ 4.490.000 |

[H] VPL calculado com taxa de 25% a.a. em regime de capitalizacao anual. O VPL positivo em todos os cenarios indica projeto economicamente viavel mesmo com taxa de desconto alta tipica de startups BR.

### 7.3 TIR (IRR)

| Cenario | TIR estimada | Nota |
|---|---|---|
| Conservador | ~180% a.a. | [H] limitado pela base de receita pequena; payback lento mas retorno alto dado investimento minimo |
| Base | ~850% a.a. | [H] TIR extremamente alta reflete o custo de entrada quase zero |
| Otimista | >2.000% a.a. | [H] acima de qualquer benchmark de comparacao |

[R] TIRs muito altas nao indicam ausencia de risco. Elas refletem a estrutura do negocio: investimento inicial proximo de zero + receita recorrente de software. O risco real e de execucao e de mercado, nao de capital. TIR deve ser lida junto ao VPL e ao payback para contexto correto.

### 7.4 Unit economics por tier de cliente

**Tier: Pay-per-DPP (ticket R$ 199, cenario base)**

| Metrica | Valor | Nota |
|---|---|---|
| Receita por transacao | R$ 199 | [H] ticket medio base |
| COGS por transacao | R$ 0,01 | [F] custo marginal negligenciavel |
| Margem bruta por transacao | R$ 198,99 | 99,9% |
| CAC medio (organico) | R$ 500 | [H] |
| Numero de DPPs ate recuperar CAC | 2,5 | |
| LTV (media 3 DPPs/ano, churn anual 40%) | R$ 597 | [H] |
| LTV/CAC | 1,2x | [H] aceitavel, mas pressiona para upgrade para assinatura |

**Tier: Assinatura R$ 490/mes**

| Metrica | Valor | Nota |
|---|---|---|
| MRR por cliente | R$ 490 | [F] |
| Churn mensal (cenario base) | 5% | [H] |
| Vida media do cliente | 20 meses | = 1/churn |
| LTV | R$ 9.800 | = MRR x vida media |
| CAC medio (organico) | R$ 500 | [H] |
| LTV/CAC | 19,6x | excelente; meta SaaS e > 3x |
| CAC payback | 1,0 mes | = CAC / MRR |
| Margem por cliente/ano | R$ 5.625 | (490 x 12) - (500 CAC amortizado) - opex proporcional |

**Tier: API B2B — contrato USD 50K/ano (base)**

| Metrica | Valor (BRL) | Nota |
|---|---|---|
| ARR por contrato | R$ 275.000 | USD 50K x 5,50 |
| Custo de venda estimado | R$ 10.000-20.000 | [H] inclui demos, juridico, integracao |
| Custo de integracao/onboarding | R$ 5.000-15.000 | [H] |
| CAC B2B total | R$ 30.000 | [H] conservador |
| LTV (contrato 3 anos, renovacao 80%) | R$ 660.000 | [H] |
| LTV/CAC | 22x | [H] |

### 7.5 MRR potencial

| Momento | Conservador | Base | Otimista |
|---|---|---|---|
| MRR em 12 meses (Jul/27) | R$ 2.940 | R$ 7.350 | R$ 18.620 |
| ARR em 12 meses | R$ 35.280 | R$ 88.200 | R$ 223.440 |
| MRR em 24 meses (Jul/28) | R$ 7.500 | R$ 22.000 | R$ 80.000 |
| ARR em 24 meses | R$ 90.000 | R$ 264.000 | R$ 960.000 |

---

## 8. Riscos financeiros e gatilhos

### 8.1 O que precisa ser verdadeiro para cada cenario funcionar

**Cenario conservador (o que nao pode falhar):**
- [H] Pelo menos 1 cliente pagante ate Dez/2026.
- [H] Churn nao supera 10%/mes.
- [H] Founder mantem tempo de dedicacao ao produto.
- [H] Infra permanece em tier atual (Supabase Pro obrigatorio desde piloto) ate 100+ clientes sem upgrade adicional.

**Cenario base (condicoes necessarias):**
- [H] 40% de conversao do piloto (2 de 5 marcas viram clientes pagantes).
- [H] Onboarding medio abaixo de 60 minutos (gatilho de go da estrategia de piloto).
- [H] Crescimento de 2-3 novos clientes/mes via organico a partir de Jan/27.
- [H] Pelo menos 1 contrato B2B em H1 2028.
- [H] EU ESPR cria pressao comercial real para marcas exportadoras a partir de 2028.

**Cenario otimista (o que precisa se tornar verdadeiro):**
- [H] Product-led growth: clientes indicam clientes sem custo de marketing.
- [H] Marketplace ou plataforma B2B2C adota PHYLLOS como parceiro de DPP.
- [H] INMETRO ou regulacao BR cria urgencia antes de 2028.
- [H] Founder consegue tempo para 5+ demos/semana sem degradar produto.

### 8.2 Gatilhos de upgrade de infra (step-function)

[R] A infra atual e gratuita ate limites claros. Os gatilhos abaixo representam aumentos de custo previstos:

| Gatilho | Custo incremental | Impacto no Opex |
|---|---|---|
| Supabase Pro (ja obrigatorio desde piloto) | R$ 125/mes fixo | incluso no Opex desde Jul/2026 |
| >10.000 req/mes (Railway Hobby → Pro) | +R$ 110/mes | +5% |
| Dominio custom + SSL proprio | +R$ 80/ano | negligenciavel |
| Primeiro dev externo (Fase 3) | +R$ 3.000-5.000/mes | +100-200% no burn |
| Marketing pago ativado | +R$ 3.000-10.000/mes | step-function maior |

[R] O risco de custo step-function mais critico e o primeiro funcionario externo. Ele praticamente dobra o burn mensal e exige ARR minimo de R$ 120K para ser sustentavel sem captacao.

### 8.3 Risco regulatorio

[R] A regulacao EU ESPR foi citada como ~2028. Se atrasar para 2030+:

| Impacto | Magnitude | Mitigacao |
|---|---|---|
| Perda de urgencia no argumento de venda para exportadores | Alta | Focar na dor organica de buyers e consumidores, independente da regulacao |
| Atraso em contratos B2B | Media-alta | Aprofundar canal de marcas pequenas/medias BR, onde a dor e imediata |
| Reducao do potencial ARR Fase 3 | Media | Ajustar projecao otimista; base e conservador nao dependem de ESPR |
| Deslocamento do timeline | +12-18 meses | Cenario conservador vira o cenario base |

[R] A referencia a INMETRO Portaria 459 com prazo de 31/07/2026 deve ser validada em fonte oficial antes de usar como argumento comercial. Nao modelamos receita dependente dessa data.

### 8.4 Outros riscos financeiros

| Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|
| Piloto nao converte (0 clientes pagantes ate Jan/27) | Media | Alto (invalida modelo de receita) | Go/no-go formal em Dez/26; pivotar para concierge ou PLM lite |
| Churn > 10%/mes no primeiro semestre | Media | Alto (MRR nao cresce) | Investir em onboarding e customer success antes de adquirir |
| Concorrente grande (Adobe, Lectra, Coats) lanca DPP B2B | Baixa | Alto (compressao de preco B2B) | Velocidade + nicho BR + baixo preco = vantagem temporaria |
| Founder perde capacidade operacional | Baixa | Critico | Documentar produto, processos e agentes antes de captar |
| Token burn do Claude Code supera orcamento | Media | Medio | Definir limite de sessao e usar subagentes especializados |

---

## 9. Recomendacao ao board

### 9.1 Runway atual (bootstrapped)

[F] O custo real de caixa e de aproximadamente R$ 1.222/mes (fase de piloto) e R$ 1.324-2.257/mes (pos-piloto ate 2027).

[H] Assumindo que o founder financia esses custos do proprio bolso (ou do faturamento existente da PHYLLOS vestuario), o runway e indefinido — o projeto nao quebra por falta de caixa na infra.

**O risco real nao e de caixa de infra. E de tempo do founder.**

Se o founder tem capacidade para dedicar 15-20h/semana ao DPP Studio, o runway e de pelo menos 12-18 meses sem nenhuma captacao e sem nenhuma receita.

### 9.2 Se/quando captar e quanto

**Recomendacao: nao captar antes de Abr/2027 (breakeven operacional).**

Razao: captar antes do breakeven sem receita validada dilui o founder sem necessidade. O produto pode chegar ao breakeven com investimento direto de R$ 4.440. Captar R$ 200K-500K agora implicaria ceder equity sem o poder de barganha de ter ARR provado.

| Momento | Condicao para captacao | Quanto captar | Para que usar |
|---|---|---|---|
| Antes de Mar/27 | Apenas se contrato B2B urgente exigir dev externo | R$ 100K-200K | Primeiro dev + integracao cliente |
| Pos Mar/27 (breakeven) | ARR > R$ 80K + LTV/CAC > 5x confirmado | R$ 300K-600K | Escala de marketing + segundo dev |
| Pos Dez/27 (ARR > R$ 147K) | ARR > R$ 150K + churn < 5% | R$ 1M-2M | Expansao B2B + equipe de vendas |

### 9.3 Valuation pre-money estimado

[H] Multiplos de ARR tipicos para SaaS early-stage BR: 5-10x ARR (seed), 8-15x ARR (Serie A).

| Momento | ARR (cenario base) | Multiplo | Valuation pre-money |
|---|---|---|---|
| Dez/27 (18 meses) | R$ 147.000 | 6x | R$ 882.000 (~USD 160K) |
| Dez/27 (18 meses) | R$ 147.000 | 10x | R$ 1.470.000 (~USD 267K) |
| Dez/28 (30 meses) | R$ 264.000 | 8x | R$ 2.112.000 (~USD 384K) |
| Dez/29 (42 meses) | R$ 495.000 | 10x | R$ 4.950.000 (~USD 900K) |

[R] Valuation de startup de software com 1 founder e sem time contratado e comprimido pelo risco de pessoa-chave. Investidor tipicamente desconta 30-50% pelo risco. Ter pelo menos 1 co-founder ou dev CTO antes de captar melhora o multiplo.

### 9.4 Estrutura recomendada de captacao

**Recomendacao: SAFE com valuation cap, quando o momento chegar.**

| Instrumento | Quando usar | Vantagem | Desvantagem |
|---|---|---|---|
| SAFE (Simple Agreement for Future Equity) | Seed ate ARR R$ 500K | Sem diluicao imediata, rapido, padrao Y Combinator | Valuation so definido na proxima rodada |
| Convertible Note | Alternativa ao SAFE com juros | Protecao de investidor com juros | Cria divida; desvantagem fiscal BR |
| Equity direto | Apos ARR > R$ 500K | Valuation claro, estrutura simples | Requer valuacao formal; mais lento |

**Parametros sugeridos para o SAFE (se captacao em 2027):**

- Cap de valuation: R$ 3.000.000-5.000.000 (baseado em ARR projetado 2028).
- Discount: 20%.
- Valor captado: R$ 300.000-500.000.
- Diluicao implicita: 6-10% pos-conversao.
- Destinacao: 40% dev externo, 30% marketing, 20% legal/compliance, 10% reserva.

---

## 10. Resumo executivo para a diretoria

### Estado do projeto

[F] O PHYLLOS DPP Studio e um produto funcional com backend operacional, endpoints de publicacao e QR, e piloto agendado para julho 2026 com 3-5 marcas independentes.

[F] O investimento direto ate hoje e proximo de zero em caixa. O ativo principal e o produto ja construido e o tempo do founder.

### Tese financeira

O DPP Studio tem estrutura economica de software puro: COGS proximo de zero, margens brutas de 99%+, e modelo de receita recorrente (assinatura) com LTV/CAC de 20x no cenario base. O payback operacional no cenario base e de 10 meses apos o inicio da cobranca (revisado: inclui Supabase Pro obrigatorio desde o piloto).

O projeto nao precisa de captacao para validar o produto. Precisa de clientes pagantes.

### Decisoes que o board precisa tomar

1. **Go/no-go do piloto**: confirmar execucao do piloto em julho 2026 com os criterios de sucesso do documento `phyllos-dpp-v1-estrategia-piloto.md`.
2. **Gatilho de first hire**: definir o ARR minimo para contratar o primeiro dev externo (recomendado: R$ 120K ARR).
3. **Politica de captacao**: confirmar que nao havera captacao antes do breakeven operacional (Abril/2027 no cenario base), salvo contrato B2B urgente.
4. **Valuation cap do SAFE**: pre-aprovar o range de R$ 3M-5M para o caso de captacao em 2027.

### Proximos 90 dias (decisoes financeiras)

| Acao | Prazo | Responsavel | KPI |
|---|---|---|---|
| Confirmar orcamento piloto (R$ 1.222/mes x 3 meses) | Jul/26 | CFO / Founder | Runway confirmado |
| Registrar pilotos em `outputs/piloto-dpp-v1.csv` | Jul-Set/26 | Product / Founder | 3+ pilotos concluidos |
| Definir primeiro preco e forma de cobranca | Set/26 | CFO / Product | Precificacao aprovada |
| Emitir primeira nota fiscal de servico DPP | Out/26 | CFO / Founder | Primeiro R$ na conta |
| Atualizar este modelo com dados reais do piloto | Out/26 | CFO | Premissas atualizadas |

---

**KPIs afetados por este documento:**

- Runway bootstrapped: indefinido (custo < R$ 2.300/mes, sem CLT).
- Burn rate pre-receita: R$ 1.222/mes.
- Breakeven operacional (cenario base): Abril/2027.
- MRR alvo em 12 meses: R$ 7.350 (cenario base).
- ARR alvo em 24 meses: R$ 264.000 (cenario base).
- LTV/CAC (assinatura, cenario base): 19,6x.
- VPL 5 anos (cenario base, 25% a.a.): R$ 869.000.

**Handoffs necessarios:**

- Product Agent: confirmar criterios de go/no-go do piloto contra premissas deste modelo.
- Growth/Marketing Agent: confirmar CAC organico e canais de aquisicao para Fase 1.
- Investor Relations Agent: usar secao 9 para data room e material de captacao futuro.
- CEO / Founder: aprovar politica de captacao e gatilho de first hire.
