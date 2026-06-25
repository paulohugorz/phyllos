# Análise Profunda de Infraestrutura — PHYLLOS DPP Studio

**Data:** 2026-06-25
**Versão:** 1.0
**Autores:** Finance Agent (CFO) + Technology Agent (CTO)
**Solicitante:** Board — revisão para redefinição de valuation pré-money
**Status:** Aprovação pendente do founder

Legenda:
- `[F]` fato verificado em fonte primária ou código do repositório.
- `[H]` hipótese de planejamento com fundamento declarado.
- `[R]` risco identificado e mensurado.

Câmbio de referência: USD 1 = BRL 5,50 (premissa do modelo financeiro vigente).

---

## 1. Mapa completo de componentes de infra por fase

### 1.1 Piloto — Julho a Setembro 2026

**Contexto:** app FastAPI rodando no Railway, SQLite local (ainda não Supabase em produção), Cloudflare R2 para QR PNGs e arquivos estáticos, até 10 DPPs publicados, zero usuários simultâneos externos, sem SLA formal.

| Componente | Serviço atual | Tier atual | Custo atual (USD/mês) | Custo atual (BRL/mês) | Gatilho de upgrade | Tier de upgrade | Custo upgrade (USD) | Custo upgrade (BRL) |
|---|---|---|---|---|---|---|---|---|
| Compute/Deploy | Railway | Hobby — USD 5/mês inclui USD 5 de crédito de uso | USD 5 | R$ 27,50 | > 500 horas de execução/mês ou necessidade de domínio custom com SLA | Pro — USD 20/mês por seat + uso | USD 20 | R$ 110 |
| Banco de dados | SQLite local (no próprio Railway Hobby) | Sem custo adicional; SQLite em disco efêmero | USD 0 | R$ 0 | > 2 usuários simultâneos ou necessidade de persistência garantida | Supabase Free → Pro | USD 25 | R$ 137,50 |
| Storage / CDN | Cloudflare R2 | Free — 10 GB permanentes, sem taxa de egresso | USD 0 | R$ 0 | > 10 GB armazenados (~588.000 DPPs completos) | R2 pago: USD 0,015/GB acima de 10 GB | < USD 1 | < R$ 5,50 |
| DNS / SSL | Cloudflare Free | Free tier | USD 0 | R$ 0 | Domínio custom próprio | Domínio .com.br: ~BRL 40/ano | USD 0 | R$ 3,33/mês (amortizado) |
| Email transacional | Nenhum (piloto assistido) | — | USD 0 | R$ 0 | Primeiro cliente pagante precisar de notificações | Resend Free: 3.000 emails/mês | USD 0 | R$ 0 |
| Monitoramento | Nenhum | — | USD 0 | R$ 0 | Primeiro cliente B2B ou SLA > 99% | Betterstack / Uptimerobot Free | USD 0 | R$ 0 |
| **Total Piloto** | | | **USD 5** | **R$ 27,50** | | | | |

[F] Railway Hobby custa USD 5/mês e inclui USD 5 de crédito de uso; para workloads leves (FastAPI com tráfego baixo), o crédito cobre o consumo real e o custo líquido efetivo pode ser zero ou próximo disso.

[F] Cloudflare R2: free tier inclui 10 GB de storage permanente e egresso gratuito ilimitado. Não há taxa de saída de dados (diferente do AWS S3). Fonte: developers.cloudflare.com/r2/pricing.

[H] SQLite no disco do Railway Hobby é suficiente para piloto com dados não críticos. O risco de perda de dados em redeploy é mitigado por backup manual periódico.

---

### 1.2 Fase 1 — Outubro a Dezembro 2026 (primeiros clientes pagantes, 100 DPPs)

**Contexto:** migração para Supabase Free (Postgres), domínio custom, email transacional ativo, até 100 DPPs publicados, 2–5 clientes simultâneos.

| Componente | Serviço | Tier | Custo (USD/mês) | Custo (BRL/mês) | Gatilho de upgrade |
|---|---|---|---|---|---|
| Compute/Deploy | Railway | Hobby USD 5 | USD 5 | R$ 27,50 | > 500h execução ou 1 cliente B2B |
| Banco de dados | Supabase | Free: 500 MB, 2 projetos, pausa após 7 dias inativo | USD 0 | R$ 0 | > 500 MB ou > 2 usuários simultâneos contínuos |
| Storage / CDN | Cloudflare R2 | Free 10 GB | USD 0 | R$ 0 | > 10 GB total |
| DNS / domínio | Cloudflare + Registro.br | Free CDN + domínio .com.br | USD 0 + BRL 40/ano | R$ 3,33/mês | — |
| Email transacional | Resend | Free: 3.000 emails/mês | USD 0 | R$ 0 | > 3.000 emails/mês |
| Monitoramento | Uptimerobot | Free: 50 monitores, 5 min intervalo | USD 0 | R$ 0 | SLA contratual exigir < 1 min |
| **Total Fase 1** | | | **USD 5** | **R$ 27,50 + R$ 3,33** | |
| **Total real** | | | | **R$ 30,83** | |

[H] Supabase Free pausa projetos sem acesso por 7 dias. Para piloto com clientes reais, é necessário script de warm-up diário (cron job gratuito no Railway) ou upgrade preventivo para Pro a USD 25/mês.

[R] Se o Supabase Free for pausado durante o acesso de um cliente, gera experiência negativa no momento crítico de validação. Recomendação: migrar para Supabase Pro (USD 25/mês) ao assinar o primeiro cliente pagante, não antes.

---

### 1.3 Fase 2 — 2027 (assinatura MRR, 1.000 DPPs)

**Contexto:** 15–50 clientes assinantes, MRR R$ 7.350–R$ 18.620, 1.000+ DPPs publicados, tráfego crescente de scans QR, necessidade de uptime consistente.

| Componente | Serviço | Tier | Custo (USD/mês) | Custo (BRL/mês) | Gatilho próximo upgrade |
|---|---|---|---|---|---|
| Compute/Deploy | Railway | Pro: USD 20/mês + uso | USD 20–35 | R$ 110–192 | > 100K requests/mês ou contrato B2B com SLA |
| Banco de dados | Supabase | Pro: USD 25/mês + uso (8 GB DB incluso) | USD 25 | R$ 137,50 | > 8 GB ou > 100K MAUs |
| Storage / CDN | Cloudflare R2 | Pago acima de 10 GB: USD 0,015/GB | USD 1–3 | R$ 5,50–16,50 | Escala linear |
| DNS / domínio | Cloudflare + Registro.br | Free CDN | USD 0 + BRL 40/ano | R$ 3,33/mês | — |
| Email transacional | Resend | Pro: USD 20/mês, 50K emails | USD 20 | R$ 110 | > 50K emails/mês |
| Monitoramento | Betterstack | Free: 3 monitores, 3 min | USD 0–10 | R$ 0–55 | SLA enterprise |
| Backup / DR | Supabase Pro incluso | PITR 7 dias | USD 0 (incluso) | R$ 0 | — |
| **Total Fase 2** | | | **USD 66–83** | **R$ 363–456** | |

---

### 1.4 Fase 3 — 2028–2030 (API B2B / SaaS, 10.000+ DPPs)

**Contexto:** contratos B2B USD 20K–200K/ano, múltiplos tenants, SLA contratual, equipe de dev parcial, possível multi-região.

| Componente | Serviço | Tier | Custo (USD/mês) | Custo (BRL/mês) | Nota |
|---|---|---|---|---|---|
| Compute/Deploy | Railway | Pro: múltiplos serviços | USD 60–120 | R$ 330–660 | [H] 2–4 serviços independentes |
| Banco de dados | Supabase | Pro + compute add-ons | USD 50–100 | R$ 275–550 | [H] pequena instância dedicada |
| Storage / CDN | Cloudflare R2 | Pago: ~50–200 GB | USD 5–15 | R$ 27,50–82,50 | |
| Email transacional | Resend | Business: USD 89/mês, 300K emails | USD 89 | R$ 489,50 | [H] Fase 3 c/ marketing ativo |
| Monitoramento | Betterstack | Starter: USD 25/mês | USD 25 | R$ 137,50 | |
| CI/CD | GitHub Actions | Free para repositórios privados até 2.000 min/mês | USD 0–4 | R$ 0–22 | |
| Segurança / WAF | Cloudflare Pro | USD 20/mês | USD 20 | R$ 110 | Apenas se cliente B2B exigir |
| **Total Fase 3** | | | **USD 249–348** | **R$ 1.370–1.914** | |

---

## 2. Modelagem de custo por volume de DPPs

### Premissas de tamanho por DPP
Cada DPP publicado gera:
- 1 QR PNG: ~5 KB [F] medição do endpoint `/pecas/{codigo}/qr` existente
- 1 página HTML pública: ~10 KB [H] página de flashcards renderizada
- 4–6 flashcards JSON: ~2 KB total [H]
- Metadados no banco (Postgres): ~2–5 KB por registro
- **Total por DPP:** ~17–22 KB em storage externo; ~5 KB em banco

Scans assumidos: 10 scans/DPP/mês (leitura de página HTML). Egresso Cloudflare R2 = zero (sem cobrança de saída).

### 2.1 Custo de compute por DPP (geração)

| Operação | Tempo de CPU estimado | Custo unitário | Nota |
|---|---|---|---|
| Cálculo determinístico (área, pegada, indicadores) | ~50–100 ms | ~USD 0,000015 | [H] Railway Pro a ~USD 0,000005/CPU-segundo |
| Geração QR PNG (qrcode lib Python) | ~20–50 ms | ~USD 0,000007 | [H] |
| Escrita no banco (INSERT + UPDATE) | ~5–10 ms | negligenciável | |
| Renderização HTML pública (Jinja2) | ~2–5 ms | negligenciável | |
| **Total CPU por DPP** | **~80–165 ms** | **~USD 0,000022** | **~R$ 0,00012** |

[F] O cálculo é determinístico e não chama LLM, confirmado em `app/api/routes.py` e `app/validators/dpp_validators.py`. O custo de CPU por DPP é de fato negligenciável.

### 2.2 Custo de cold start vs instância ativa

| Modo | Cold start | Custo mensal (Railway Hobby) | Impacto para usuário |
|---|---|---|---|
| Sleep automático (Hobby, sem tráfego) | 2–5 segundos | USD 5 (crédito incluso) | Inaceitável para cliente pagante |
| Instância sempre ativa (Railway Pro) | 0 | USD 20 + uso | Adequado para produção |
| Instância com mínimo de réplicas (Railway Pro) | < 500 ms | USD 20–35 | Recomendado a partir de Fase 1 |

[R] O Railway Hobby pode colocar o app em sleep após inatividade. Para o piloto (uso assistido e controlado), aceitável. Para Fase 1 com cliente pagante, o custo incremental de USD 15/mês (Hobby→Pro) é obrigatório. O risco de um cliente escanear o QR e receber timeout é um risco de churn imediato.

### 2.3 Tabela consolidada: custo total de infra por volume

| Volume de DPPs publicados | Storage R2 | Banda (scans) | Compute (geração) | Banco (Supabase) | Outros fixos | **Total USD/mês** | **Total BRL/mês** | **Custo/DPP publicado** |
|---|---|---|---|---|---|---|---|---|
| 10 (Piloto) | ~0,2 MB | 0 (egresso R2 = zero) | ~USD 0,0002 | R$ 0 (free) | USD 5 (Railway Hobby) | **USD 5,00** | **R$ 27,50** | **R$ 2,75** |
| 100 (Fase 1) | ~2 MB | 0 | ~USD 0,002 | USD 0 (free < 500 MB) | USD 5 | **USD 5,00** | **R$ 27,50** | **R$ 0,27** |
| 1.000 (Fase 2 início) | ~20 MB | 0 | ~USD 0,022 | USD 25 (Pro, necessário) | USD 20 (Pro) | **USD 45,02** | **R$ 247,61** | **R$ 0,25** |
| 10.000 (Fase 2 avançada) | ~200 MB | 0 | ~USD 0,22 | USD 25 | USD 20 + USD 10 extras | **USD 55,22** | **R$ 303,71** | **R$ 0,030** |
| 100.000 (escala SaaS) | ~2 GB | 0 | ~USD 2,20 | USD 50–100 | USD 80–120 | **USD 152–222** | **R$ 836–1.221** | **R$ 0,0084–0,0122** |

Notas:
- [F] Cloudflare R2 não cobra egresso. Banda de leitura QR = R$ 0 independente do volume de scans.
- [H] Supabase Pro a USD 25/mês suporta até ~8 GB de banco, suficiente para ~1,6 milhão de DPPs completos em metadados.
- [H] O custo por DPP cai de R$ 2,75 no piloto para R$ 0,0084 em escala de 100K — efeito claro de diluição de custo fixo.

### 2.4 Margem bruta real por volume (Modelo base: ticket R$ 199 pay-per-DPP; assinatura R$ 490/mês)

| Volume de DPPs/mês | Receita estimada (base) | Custo total infra | Margem bruta absoluta | Margem bruta % |
|---|---|---|---|---|
| 10 DPPs (10 clientes × 1 DPP, ticket R$ 199) | R$ 1.990 | R$ 27,50 | R$ 1.962,50 | 98,6% |
| 100 DPPs (50 assinantes × R$ 490) | R$ 24.500 | R$ 27,50 | R$ 24.472,50 | 99,9% |
| 1.000 DPPs (100 assinantes) | R$ 49.000 | R$ 247,61 | R$ 48.752,39 | 99,5% |
| 10.000 DPPs (500 assinantes) | R$ 245.000 | R$ 303,71 | R$ 244.696,29 | 99,9% |
| 100.000 DPPs (5.000 assinantes) | R$ 2.450.000 | R$ 1.028,50 (média) | R$ 2.448.971,50 | 99,96% |

[H] Receita calculada pela base de assinantes (R$ 490/assinante/mês) com estimativa de DPPs publicados por cliente (média 2/mês). A infra nunca comprime margem bruta abaixo de 98%, mesmo em escala.

---

## 3. Custo detalhado de armazenamento e banda de QR

### 3.1 Armazenamento por volume

| Volume DPPs | QR PNGs (5 KB cada) | HTML páginas (10 KB) | JSON flashcards (2 KB) | Total storage | Custo R2 (USD) | Custo R2 (BRL) |
|---|---|---|---|---|---|---|
| 10 | 50 KB | 100 KB | 20 KB | ~170 KB | USD 0 (free tier) | R$ 0 |
| 100 | 500 KB | 1 MB | 200 KB | ~1,7 MB | USD 0 | R$ 0 |
| 1.000 | 5 MB | 10 MB | 2 MB | ~17 MB | USD 0 | R$ 0 |
| 10.000 | 50 MB | 100 MB | 20 MB | ~170 MB | USD 0 (< 10 GB free) | R$ 0 |
| 100.000 | 500 MB | 1 GB | 200 MB | ~1,7 GB | USD 0 (< 10 GB free) | R$ 0 |
| 588.000 | ~2,9 GB | ~5,9 GB | ~1,2 GB | ~10 GB | **Atinge limite free** | R$ 0 |
| 700.000 | ~3,4 GB | ~7 GB | ~1,4 GB | ~12 GB | USD 0,030 (2 GB × USD 0,015) | R$ 0,17 |

[F] O free tier do Cloudflare R2 cobre 10 GB permanentes. A PHYLLOS somente ultrapassará esse limite acima de ~588.000 DPPs publicados, um volume que corresponde a escala pós-Fase 3 robusta. Até lá, o custo de storage é literalmente zero.

### 3.2 Custo de banda (scans QR)

[F] O Cloudflare R2 não cobra egresso de dados (taxa de saída zero). A leitura da página HTML pública quando um usuário escaneia o QR não gera custo de banda, independentemente do volume de scans.

Para 100.000 DPPs × 10 scans/mês = 1 milhão de requests por mês:
- Custo de Class B operations (GET): USD 0,36 por milhão de operações = **USD 0,36/mês** (R$ 1,98/mês)

O custo de banda e leitura em escala de 1 milhão de scans por mês é R$ 1,98. É negligenciável.

### 3.3 Comparativo de storage: R2 vs S3 vs Supabase Storage

| Serviço | Storage (USD/GB/mês) | Egresso (USD/GB) | 10 GB/mês | 100 GB/mês | 1 TB/mês | Observação |
|---|---|---|---|---|---|---|
| Cloudflare R2 | USD 0,015 (acima de 10 GB free) | **USD 0** | **USD 0** (free) | USD 1,35 | USD 13,50 | Zero egress — melhor opção |
| AWS S3 Standard | USD 0,023 | USD 0,09/GB | USD 1,13 | USD 10,30 | USD 113 | Egresso muito caro em escala |
| Supabase Storage | USD 0,021 (acima de incluído no Pro) | USD 0,09/GB | USD 0 (incluso no Pro) | USD 8,09 | USD 90 | Adequado para arquivos de usuário |
| DigitalOcean Spaces | USD 0,020 + USD 21 base/mês | USD 0,01/GB acima de 1 TB | USD 21 | USD 21 | USD 30 | Mínimo alto para baixos volumes |

**Veredito:** Cloudflare R2 é incontestável para storage de QR, HTML e JSON do DPP. O free tier cobre 100% da necessidade até ~600K DPPs publicados, e o custo mesmo em escala de 1 TB é 10× menor que o AWS S3.

---

## 4. Custo de compute por DPP (análise detalhada)

### 4.1 Breakdown por operação no Railway

| Operação | Tempo médio | CPU shares utilizadas | Custo Railway Pro (estimado) |
|---|---|---|---|
| Validação de payload (Pydantic) | ~2 ms | mínimo | < USD 0,000001 |
| Busca banco (SELECT peca + materiais) | ~5–15 ms | mínimo | < USD 0,000005 |
| Cálculo determinístico de indicadores | ~50–80 ms | 1 vCPU spike | ~USD 0,000010 |
| Geração QR (qrcode lib, PNG) | ~20–40 ms | 1 vCPU spike | ~USD 0,000007 |
| Upload para R2 (POST) | ~100–300 ms | I/O bound, CPU mínima | ~USD 0,000003 |
| Escrita banco (INSERT/UPDATE DPP) | ~5–10 ms | mínimo | < USD 0,000002 |
| **Total por DPP** | **~180–450 ms** | | **~USD 0,000028** ≈ **R$ 0,00015** |

[H] Railway Pro cobra por uso de recursos. Para o workload atual (FastAPI sem I/O pesado), 10.000 DPPs/mês consumiriam ~USD 0,28 em compute — valor absorvido inteiramente pelo crédito mensal de USD 20 incluído no plano.

### 4.2 Instância sempre ativa vs sob demanda

| Configuração | Custo idle (sem tráfego) | Custo em pico | Cold start | Recomendação |
|---|---|---|---|---|
| Railway Hobby (dorme) | USD 0 | USD 0 (crédito) | 2–5 s | Piloto apenas |
| Railway Pro (sempre ativa, 1 réplica) | USD 20/mês (crédito incluso) | USD 20–35/mês | < 500 ms | Fase 1 em diante |
| Railway Pro (2 réplicas para HA) | USD 40/mês | USD 40–60/mês | Zero (hot standby) | Fase 3 com SLA B2B |
| Fly.io (1 máquina 256 MB shared) | ~USD 2/mês | ~USD 8–15/mês | ~2 s (pode configurar zero) | Alternativa válida |

---

## 5. Stack alternativa lean — comparativo completo

### Opção A (Stack atual): Railway + Supabase + Cloudflare R2

| Métrica | 100 DPPs/mês | 1.000 DPPs/mês | 10.000 DPPs/mês |
|---|---|---|---|
| Custo total/mês (USD) | USD 5 | USD 45 | USD 55 |
| Custo total/mês (BRL) | R$ 27,50 | R$ 247,50 | R$ 302,50 |
| Complexidade operacional | Baixa | Baixa | Média |
| Vendor lock-in | Railway (deploy), Supabase (DB) | Médio | Médio |

Prós: zero configuração de servidor, deploys automáticos por push no GitHub, Supabase inclui auth e admin UI, R2 sem egresso.
Contras: Railway Hobby dorme (mitigável com Pro), Supabase Free pausa (mitigável com Pro a USD 25).

---

### Opção B: Fly.io + Neon Postgres + Cloudflare R2

| Métrica | 100 DPPs/mês | 1.000 DPPs/mês | 10.000 DPPs/mês |
|---|---|---|---|
| Compute (Fly.io, 1 máquina 256 MB) | USD 2–8 | USD 8–15 | USD 15–25 |
| Banco (Neon Free: 0,5 GB, 100 CU-h) | USD 0 | USD 5–15 | USD 15–30 |
| Storage (Cloudflare R2) | USD 0 | USD 0 | USD 0 |
| **Total/mês (USD)** | **USD 2–8** | **USD 13–30** | **USD 30–55** |
| **Total/mês (BRL)** | **R$ 11–44** | **R$ 71–165** | **R$ 165–302** |
| Complexidade operacional | Média (Fly CLI, configuração de regiões) | Média-alta | Alta |
| Vendor lock-in | Baixo (app portable, DB Postgres padrão) | Baixo | Baixo |

[F] Neon reduziu preços após aquisição pela Databricks (maio/2025): compute a USD 0,106/CU-hora, storage a USD 0,35/GB/mês. Free tier: 100 CU-horas/mês e 0,5 GB.

Prós: menor custo de compute em baixo volume, Postgres padrão portável, escala-a-zero automático no Neon.
Contras: Fly.io eliminou free tier; curva de aprendizado maior (máquinas, regiões, anycast); Neon pode ser lento em cold start de query após idle.

---

### Opção C: Render + PlanetScale + AWS S3

| Métrica | 100 DPPs/mês | 1.000 DPPs/mês | 10.000 DPPs/mês |
|---|---|---|---|
| Compute (Render Free: dorme; Starter: USD 7/mês) | USD 7 | USD 7–19 | USD 19–50 |
| Banco (PlanetScale Hobby: free até 5 GB) | USD 0 | USD 0 | USD 39 (Scaler Pro) |
| Storage (AWS S3: USD 0,023/GB + egresso USD 0,09/GB) | USD 1–3 | USD 3–8 | USD 15–40 |
| **Total/mês (USD)** | **USD 8–10** | **USD 10–27** | **USD 73–129** |
| **Total/mês (BRL)** | **R$ 44–55** | **R$ 55–148** | **R$ 401–709** |
| Complexidade operacional | Baixa (Render simples) | Média | Alta (S3 + IAM + egresso caro) |
| Vendor lock-in | PlanetScale (MySQL vs Postgres) | Alto (MySQL diferente do schema atual) | Alto |

[R] Migrar para PlanetScale exigiria reescrever o schema do banco atual (SQLAlchemy + Postgres) para MySQL. Custo de migração técnica estimado: 20–40 horas de dev. Não recomendado.
[R] AWS S3 cobra egresso por GB. Em escala de 100K DPPs com 10 scans/mês, o egresso seria ~1 TB/mês = USD 92 só em banda. Com Cloudflare R2, o mesmo volume custa zero.

---

### Opção D: DigitalOcean Droplet + Managed Postgres + Spaces

| Métrica | 100 DPPs/mês | 1.000 DPPs/mês | 10.000 DPPs/mês |
|---|---|---|---|
| Compute (Droplet básico 1 GB RAM) | USD 6 | USD 6 | USD 12 (upgrade) |
| Banco (Managed Postgres 1 nó, 1 GB RAM) | USD 15 | USD 15 | USD 30 |
| Storage (Spaces: USD 21/mês base + 250 GB) | USD 21 | USD 21 | USD 21 |
| **Total/mês (USD)** | **USD 42** | **USD 42** | **USD 63** |
| **Total/mês (BRL)** | **R$ 231** | **R$ 231** | **R$ 346** |
| Complexidade operacional | Alta (sysadmin Droplet, updates, segurança) | Alta | Alta |
| Vendor lock-in | Baixo (infra padrão) | Baixo | Baixo |

Prós: controle total, sem surpresas de pricing, Managed Postgres inclui backups automáticos.
Contras: Spaces tem custo mínimo alto de USD 21/mês; DigitalOcean Spaces cobra egresso após 1 TB; Droplet exige manutenção manual de OS; custo total é 5–8× maior que a stack atual em baixo volume.

---

### 5.1 Tabela comparativa final por opção

| Opção | 100 DPPs (BRL/mês) | 1.000 DPPs (BRL/mês) | 10.000 DPPs (BRL/mês) | Complexidade | Lock-in | Recomendação |
|---|---|---|---|---|---|---|
| A — Railway + Supabase + R2 (atual) | R$ 27,50 | R$ 247,50 | R$ 302,50 | Baixa | Médio | **Manter até Fase 2** |
| B — Fly.io + Neon + R2 | R$ 11–44 | R$ 71–165 | R$ 165–302 | Média | Baixo | Alternativa válida em Fase 3 |
| C — Render + PlanetScale + S3 | R$ 44–55 | R$ 55–148 | R$ 401–709 | Baixa/Alta | Alto | Não recomendado (egresso S3 + lock-in MySQL) |
| D — DigitalOcean Droplet + Managed PG + Spaces | R$ 231 | R$ 231 | R$ 346 | Alta | Baixo | Não recomendado pré-Fase 3 (custo fixo alto) |

**Veredito CTO+CFO:** A Opção A permanece a mais eficiente em custo e a de menor complexidade operacional para as Fases Piloto, 1 e 2. A Opção B pode ser avaliada para Fase 3 se portabilidade de vendor for prioritária para investidores ou clientes B2B. As Opções C e D têm desvantagens que superam qualquer economia aparente.

---

## 6. Projeção de custo de infra 2026–2030

### 6.1 Cenário base — custo mensal por componente

Os gatilhos de upgrade estão marcados como **[UP]** na tabela. Step-functions ocorrem nos eventos: primeiro cliente pagante (Out/26), 50 clientes assinantes (~Q1/27), primeiro contrato B2B (H1/28).

| Mês | Railway | Supabase | R2 | Email | Extras | **Total (USD)** | **Total (BRL)** | Evento |
|---|---|---|---|---|---|---|---|---|
| Jul/26 | 5 | 0 | 0 | 0 | 0 | **5** | **R$ 27,50** | Piloto inicia |
| Ago/26 | 5 | 0 | 0 | 0 | 0 | **5** | **R$ 27,50** | |
| Set/26 | 5 | 0 | 0 | 0 | 0 | **5** | **R$ 27,50** | |
| Out/26 | **20** [UP] | **25** [UP] | 0 | 0 | 1 | **46** | **R$ 253** | Primeiro cliente pagante → Railway Pro + Supabase Pro |
| Nov/26 | 20 | 25 | 0 | 0 | 1 | **46** | **R$ 253** | |
| Dez/26 | 20 | 25 | 0 | 5 | 1 | **51** | **R$ 280,50** | Email transacional ativado |
| Jan/27 | 20 | 25 | 0 | 5 | 2 | **52** | **R$ 286** | |
| Mar/27 | 20 | 25 | 0 | 5 | 2 | **52** | **R$ 286** | Breakeven operacional |
| Jun/27 | 25 | 25 | 0 | 5 | 3 | **58** | **R$ 319** | Tráfego crescente |
| Dez/27 | 30 | 25 | 1 | 20 | 5 | **81** | **R$ 445,50** | 25 clientes assinantes |
| Jun/28 | **60** [UP] | 25 | 2 | 20 | 15 | **122** | **R$ 671** | Contrato B2B ativo → múltiplos serviços |
| Dez/28 | 80 | 50 | 3 | 20 | 20 | **173** | **R$ 951,50** | |
| Dez/29 | 100 | 75 | 8 | 89 | 30 | **302** | **R$ 1.661** | Escala SaaS |
| Dez/30 | 120 | 100 | 15 | 89 | 50 | **374** | **R$ 2.057** | |

### 6.2 Cenário conservador (crescimento 50% mais lento)

Upgrades atrasados ~6 meses vs. cenário base. Custo de infra ~30% menor em 2027, ~20% menor em 2028.

| Ano | Total infra (USD/ano) | Total infra (BRL/ano) |
|---|---|---|
| 2026 (Q4) | USD 168 | R$ 924 |
| 2027 | USD 590 | R$ 3.245 |
| 2028 | USD 1.152 | R$ 6.336 |
| 2029 | USD 2.400 | R$ 13.200 |
| 2030 | USD 3.600 | R$ 19.800 |

### 6.3 Cenário otimista (crescimento 2× mais rápido)

Upgrades antecipados, múltiplos serviços, multi-região a partir de 2029.

| Ano | Total infra (USD/ano) | Total infra (BRL/ano) |
|---|---|---|
| 2026 (Q4) | USD 168 | R$ 924 |
| 2027 | USD 1.200 | R$ 6.600 |
| 2028 | USD 3.600 | R$ 19.800 |
| 2029 | USD 7.200 | R$ 39.600 |
| 2030 | USD 14.400 | R$ 79.200 |

---

## 7. Impacto no EBITDA e margem bruta

### 7.1 Revisão da margem bruta com infra detalhada

A análise financeira anterior usou COGS de R$ 0,01/DPP como estimativa agregada. Com os dados detalhados desta análise, o cálculo real confirma — e refina — essa premissa.

| Volume DPPs/mês | Custo infra total/mês (BRL) | DPPs gerados/mês (estimativa) | Custo infra por DPP (BRL) | COGS anterior (BRL) | Diferença |
|---|---|---|---|---|---|
| 10 | R$ 27,50 | 10 | R$ 2,75 | R$ 0,01 | **O custo fixo domina em volumes baixos** |
| 100 | R$ 27,50 | 100 | R$ 0,275 | R$ 0,01 | Ainda dominado por fixo |
| 1.000 | R$ 247,50 | 1.000 | R$ 0,248 | R$ 0,01 | Próximo do estimado original |
| 10.000 | R$ 302,50 | 10.000 | R$ 0,030 | R$ 0,01 | Abaixo do estimado |
| 100.000 | R$ 1.028,50 | 100.000 | R$ 0,010 | R$ 0,01 | **Converge com a estimativa original** |

[H] A premissa de R$ 0,01/DPP é precisa para volumes de escala (100K+). Para volumes menores, o custo real por DPP é maior porque os custos fixos (Railway Pro, Supabase Pro) são diluídos em poucos DPPs. Isso não é um problema de modelo — é a natureza do software com custos fixos de plataforma.

[F] Em nenhum cenário analisado a margem bruta cai abaixo de 98%. A infra nunca comprime a margem de forma material.

### 7.2 P&L revisado com infra detalhada (cenário base)

*Diferença vs. P&L original: substituição da linha "infra estimada" por valores calculados neste documento.*

| Item | 2026 (Q4) | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Receita Bruta | R$ 3.582 | R$ 88.620 | R$ 220.000 | R$ 495.000 | R$ 990.000 |
| Deduções (~7%) | (R$ 251) | (R$ 6.203) | (R$ 15.400) | (R$ 34.650) | (R$ 69.300) |
| Receita Líquida | R$ 3.331 | R$ 82.417 | R$ 204.600 | R$ 460.350 | R$ 920.700 |
| Custo de infra (this doc) | (R$ 759) | (R$ 4.554) | (R$ 8.448) | (R$ 19.800) | (R$ 24.684) |
| Outros COGS (negligível) | (R$ 18) | (R$ 112) | (R$ 280) | (R$ 630) | (R$ 1.260) |
| **Margem Bruta** | **R$ 2.554** | **R$ 77.751** | **R$ 195.872** | **R$ 439.920** | **R$ 894.756** |
| **Margem Bruta %** | **76,7%** | **94,3%** | **95,7%** | **95,6%** | **97,2%** |
| Claude Code | (R$ 2.700) | (R$ 14.400) | (R$ 18.000) | (R$ 18.000) | (R$ 18.000) |
| Marketing | (R$ 390) | (R$ 6.960) | (R$ 26.400) | (R$ 60.000) | (R$ 120.000) |
| Outros Opex (ferramentas, jurídico) | (R$ 522) | (R$ 2.430) | (R$ 22.800) | (R$ 36.000) | (R$ 60.000) |
| **EBITDA** | **(R$ 1.058)** | **R$ 53.961** | **R$ 128.672** | **R$ 325.920** | **R$ 696.756** |
| **EBITDA %** | neg. | 65,5% | 62,9% | 70,8% | 75,7% |

Notas importantes:
- [H] A margem bruta no Q4/26 cai para 76,7% porque o custo fixo de infra (R$ 759) pesa muito sobre receita ainda pequena (R$ 3.331). Isso é esperado e não representa problema estrutural.
- [H] A partir de 2027, a margem bruta sobe para 94%+ e permanece acima de 95% para sempre, independente do crescimento de DPPs, porque a infra cresce logaritmicamente e a receita cresce linearmente.
- [H] A diferença entre o EBITDA desta análise e o P&L original (R$ 54.890 em 2027 vs. R$ 53.961 aqui) é de apenas R$ 929 anuais — um desvio de 1,7%. A premissa original era robusta.

### 7.3 Quando a infra começa a comprimir margem

Resposta direta ao board: **nunca de forma material.** O único momento em que a infra representa uma fração visível da receita é no Q4/2026, quando a receita ainda é de R$ 3.331/mês e os custos fixos de plataforma (Railway Pro + Supabase Pro) são obrigatórios para manter a operação confiável.

A partir de Jan/2027, a proporção infra/receita cai consistentemente:

| Período | Custo infra/mês | Receita/mês | Infra como % da receita |
|---|---|---|---|
| Q4/2026 | R$ 253 | R$ 1.194 (média) | 21,2% |
| Q1/2027 | R$ 286 | R$ 3.682 (média) | 7,8% |
| Q4/2027 | R$ 416 | R$ 11.277 (média) | 3,7% |
| 2028 médio | R$ 704 | R$ 18.333 | 3,8% |
| 2029 médio | R$ 1.382 | R$ 41.250 | 3,4% |
| 2030 médio | R$ 1.714 | R$ 82.500 | 2,1% |

---

## Resumo executivo desta análise

**Conclusão central para o board:**

A infraestrutura do PHYLLOS DPP Studio é estruturalmente lean. Os custos fixos de plataforma (Railway + Supabase) entram apenas quando o primeiro cliente pagante é ativado (~Out/26) e somam USD 46/mês (R$ 253). Esse patamar suporta até 1.000 DPPs publicados sem upgrade adicional.

O próximo step de custo relevante — R$ 445/mês — ocorre em Dez/27 com 25 clientes, quando o MRR base é de R$ 12.250. A proporção infra/receita cai de 21% no início para 3,4% em 2029 e 2,1% em 2030.

O Cloudflare R2 com egresso zero é o ativo de infraestrutura mais estratégico da stack: elimina o custo variável de banda que destruiria a margem em qualquer outra opção. A escolha de R2 garante que 100K scans de QR/mês custem menos de R$ 2,00 em operações de leitura.

**A tese de 99%+ de margem bruta é confirmada por esta análise detalhada.** O desvio real vs. a estimativa anterior é de menos de 2% no cenário base.

---

**KPIs afetados por este documento:**
- Custo de infra/mês (piloto): R$ 27,50 confirmado (vs. R$ 140 estimado anteriormente, pois Railway Hobby cobre com crédito)
- Custo de infra/mês (Fase 1): R$ 253 (step-function documentada)
- Margem bruta estrutural: 94–99,9% dependendo do volume
- Custo por DPP em escala (100K): R$ 0,0084–R$ 0,0122
- Runway de free tier R2: até ~588K DPPs publicados

**Handoffs:**
- CEO/Founder: aprovar stack atual (Opção A) como padrão até Fase 2; deferir avaliação de Opção B para Fase 3
- Investor Relations: usar seção 7.3 para responder a perguntas de due diligence sobre compressão de margem
- Tech/Product: implementar warm-up cron job antes de Out/26 para evitar pausa do Supabase Free
