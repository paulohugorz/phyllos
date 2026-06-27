---
name: product-blocks-allocation
description: Blocos evolutivos de produto PHYLLOS — valor entregue por fase e alocação balanceada de agentes. Fonte canônica para sequenciamento de trabalho por agente.
metadata:
  type: project
---

# PHYLLOS — Blocos Evolutivos de Produto e Alocação de Agentes

**Data:** 2026-06-27  
**Status:** fonte canônica para alocação por fase  
**Princípio:** cada bloco entrega valor real antes de abrir o próximo. Agentes só são ativados quando o bloco exige sua contribuição.

---

## Visão geral dos blocos

| Bloco | Período | Valor entregue | Receita |
|---|---|---|---|
| **B0 — Fundação** | Jun–Jul/2026 | Saber exatamente o que construir | R$0 |
| **B1 — Passaporte Mínimo** | Ago/2026 | Marca publica. Buyer lê. QR funciona. | R$0 (piloto) |
| **B2 — Auto-serviço** | Out/2026 | Marca cadastra sozinha e paga por DPP | R$149–299/DPP |
| **B3 — Retenção** | Jan–Jun/2027 | Marca assina. Buyer volta. Histórico protege. | R$490/mês |
| **B4 — Plataforma** | 2028+ | API B2B. Parceiros. Marketplace de buyers. | USD 20–200K/contrato |

---

## B0 — Fundação (Jun–Jul/2026)

**Objetivo:** travar o que construir antes de construir.  
**Gate de saída:** 5 marcas piloto confirmadas + mapa de campos INMETRO + infra de produção no ar.

### Valor entregue
- Clareza sobre ICP real (quem são as 5 marcas do piloto)
- Mapa completo de campos obrigatórios INMETRO Portaria 459/2025
- Infra de produção configurada (Supabase Pro + Railway + Cloudflare)
- Schema de dados DPP v0 aprovado
- Critérios de aceite Tier 1 documentados

### Agentes ativos

| Agente | Entregável no B0 |
|---|---|
| **founder-orchestrator** | go/no-go do escopo do piloto; aprovação do schema v0 |
| **product-director** | critérios de aceite Tier 1; jornada de onboarding assistido |
| **certification-agent** | mapa de campos INMETRO obrigatórios por parte do calçado |
| **cx-lead** | 5 marcas piloto identificadas e confirmadas com data |
| **technology-director** | schema DPP v0; decisão de stack finalizada |
| **devops-security-agent** | Supabase Pro + Railway + Cloudflare configurados e testados |
| **data-intelligence-lead** | dicionário de dados v0; eventos de tracking definidos |
| **cfo** | orçamento do piloto aprovado; runway recalculado com infra Pro |

### Agentes em standby no B0
Todos os demais — marketing, vendas, conteúdo, growth, CRM, BI — aguardam B1.

---

## B1 — Passaporte Mínimo (Ago/2026)

**Objetivo:** 1 marca consegue publicar 1 DPP com QR que funciona; buyer acessa sem login.  
**Gate de saída:** 3 DPPs publicados + QR testado em negociação real + 0 campos publicados sem status de evidência.

### Valor entregue
- Studio assistido (onboarding com suporte direto da equipe)
- Passaporte público por SKU com URL permanente
- QR GS1 Digital Link funcional para etiqueta física
- Status de evidência visível em cada campo (declarado/calculado/documentado/verificado/ausente)
- Validação Tier 1 INMETRO: composição por parte, GTIN, CNPJ, país de fabricação
- Página pública legível por buyer sem login

### Agentes ativos

| Agente | Entregável no B1 |
|---|---|
| **technology-director** | backend FastAPI: CRUD produto/material/DPP, endpoint QR, rota pública |
| **frontend-agent** | DPP Studio HTML funcional (entrada de dados → passaporte publicado) |
| **product-director** | roteiro de onboarding assistido 60 min; critérios de aceite por campo |
| **certification-agent** | validação INMETRO Tier 1 implementada; alertas por campo faltante |
| **qa-agent** | suite de testes dos cálculos; checklist anti-greenwashing; testes de QR |
| **data-intelligence-lead** | schema de produção Supabase; pipeline de eventos básico |
| **devops-security-agent** | deploy Railway + Netlify; Cloudflare na frente de todas as URLs públicas |
| **cx-lead** | condução do onboarding assistido com as 5 marcas; registro de lacunas |
| **founder-orchestrator** | go/no-go de publicação do primeiro passaporte real |

### Agentes em standby no B1
Marketing, vendas, growth, CRM, BI, conteúdo — entram apenas após gate de B1.

---

## B2 — Auto-serviço (Out/2026)

**Objetivo:** marca cadastra sem assistência e paga por DPP publicado.  
**Gate de saída:** 10 DPPs pagos + CAC < R$300 + onboarding < 60 min sem suporte.

### Valor entregue
- Studio self-service: onboarding sem suporte humano
- Checkout e cobrança por DPP (R$149–299)
- Multi-SKU: marca cadastra mais de 1 peça
- Confirmação e recibo automático por e-mail
- Primeira receita real

### Agentes ativos

| Agente | Entregável no B2 |
|---|---|
| **product-director** | UX de auto-serviço; redução de fricção no onboarding |
| **digital-products-lead** | Studio self-service completo; fluxo de publicação sem suporte |
| **frontend-agent** | UI de cadastro multi-SKU; estados de erro e progresso |
| **technology-director** | auth básico (Supabase Auth); multiempresa simples; pagamento |
| **ecommerce-agent** | integração de pagamento (Mercado Pago ou Stripe); recibo automático |
| **email-crm-agent** | sequência de ativação: boas-vindas → onboarding → primeiro DPP publicado |
| **marketing-lead** | primeiros canais de aquisição: TexBrasil, LinkedIn, e-mail frio exportadores |
| **vendas** | abordagem direta às 5 marcas piloto para conversão paga; registro de objeções |
| **cx-lead** | suporte ao onboarding dos primeiros pagantes; mapa de fricção |
| **analytics-agent** | funil de conversão cadastro → pagamento; CAC por canal |
| **qa-agent** | testes de regressão; testes de pagamento; testes de multi-SKU |
| **devops-security-agent** | monitoramento 24/7; alertas de erro em produção; SLA Railway Pro |
| **cfo** | primeira nota fiscal; reconhecimento de receita; atualização do fluxo de caixa |

### Agentes em standby no B2
BI (sem dados suficientes), loyalty (sem base), PR/press (sem tração provada), parceiros.

---

## B3 — Retenção (Jan–Jun/2027)

**Objetivo:** marca assina mensalmente; buyer tem portal próprio; histórico de versões protege a marca.  
**Gate de saída:** 30 marcas ativas em assinatura + churn < 5%/mês + breakeven Mar/2027.

### Valor entregue
- Assinatura mensal por marca (R$490/mês)
- Histórico de versões do DPP (imutabilidade regulatória)
- Buyer portal: buyers acessam DPPs de múltiplas marcas com login
- Templates EU ESPR (vestuário exportador)
- Dashboard de compliance por marca
- Relatório de lacunas e alertas de vencimento

### Agentes ativos

| Agente | Entregável no B3 |
|---|---|
| **product-director** | escopo do buyer portal; templates ESPR; dashboard de compliance |
| **technology-director** | histórico de versões imutável; buyer portal; multiempresa robusto |
| **certification-agent** | mapeamento EU ESPR Tier 2–3; alertas de vencimento por campo |
| **data-intelligence-lead** | warehouse de métricas por marca; cohort de retenção; LTV |
| **bi-analyst** | dashboard executivo: MRR, churn, NPS, cobertura de campos por tier |
| **email-crm-agent** | ciclo de vida: ativação → engajamento → renovação; alertas de compliance |
| **loyalty-agent** | programa de benefícios para marcas com múltiplos DPPs publicados |
| **marketing-lead** | conteúdo ESPR; cases de buyers que fecharam com marcas PHYLLOS |
| **communication-lead** | PR: "marca X fechou com buyer europeu usando DPP PHYLLOS" |
| **vendas** | expansão: upsell de marcas piloto para assinatura; novos exportadores |
| **innovation-director** | análise de expansão: têxtil geral, outros segmentos, LatAm |
| **cfo** | modelo de assinatura; MRR; gatilhos de captação; projeção Série A |
| **devops-security-agent** | data residency EU planejada; PITR auditado; SLA reforçado |

---

## B4 — Plataforma (2028+)

**Objetivo:** API B2B, parceiros que integram DPP, marketplace onde buyers encontram marcas.

### Valor entregue
- API pública para criar e consultar DPPs (USD 20–200K/contrato)
- Integrações nativas com ERPs e plataformas de moda
- Marketplace: buyer busca marcas com DPP por categoria/compliance tier
- JSON-LD completo (EU ESPR nativo)
- Modelo de parceria com certificadoras (GOTS, OEKO-TEX)

### Agentes ativos

| Agente | Entregável no B4 |
|---|---|
| **technology-director** | API pública versionada; parsers CSV/XLSX/PDF; conectores |
| **integration-agent** | conectores ERP, PLM, Nuvemshop, plataformas de exportação |
| **innovation-director** | modelo de marketplace; parcerias estratégicas; expansão LatAm |
| **pr-press-agent** | narrativa de Série A; data room; relacionamento com investidores |
| **vendas** | contratos B2B diretos; pipeline enterprise |
| **product-director** | marketplace UX; API developer experience |
| **certification-agent** | parceria com certificadoras; integração de laudos externos |

---

## Resumo de alocação por bloco

| Agente | B0 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|
| founder-orchestrator | ● | ● | ○ | ○ | ○ |
| product-director | ● | ● | ● | ● | ● |
| technology-director | ● | ● | ● | ● | ● |
| certification-agent | ● | ● | ○ | ● | ● |
| cx-lead | ● | ● | ● | ○ | — |
| devops-security-agent | ● | ● | ● | ● | ○ |
| data-intelligence-lead | ● | ● | ○ | ● | ○ |
| qa-agent | — | ● | ● | ● | ○ |
| frontend-agent | — | ● | ● | ○ | — |
| digital-products-lead | — | ○ | ● | ● | ○ |
| ecommerce-agent | — | — | ● | ○ | — |
| email-crm-agent | — | — | ● | ● | — |
| marketing-lead | — | — | ● | ● | ○ |
| vendas | — | — | ● | ● | ● |
| analytics-agent | — | — | ● | ● | ○ |
| bi-analyst | — | — | — | ● | ● |
| loyalty-agent | — | — | — | ● | ○ |
| communication-lead | — | — | ○ | ● | ● |
| innovation-director | — | — | — | ● | ● |
| cfo | ● | ○ | ● | ● | ● |
| integration-agent | — | — | — | — | ● |
| pr-press-agent | — | — | — | ○ | ● |

**Legenda:** ● ativo com entregável claro · ○ suporte/revisão · — em standby

---

## Gates de decisão (go/no-go por bloco)

| Gate | Critério obrigatório | Responsável |
|---|---|---|
| B0 → B1 | 5 marcas confirmadas + schema aprovado + infra no ar | founder-orchestrator |
| B1 → B2 | 3 DPPs publicados + QR usado em negociação real | product-director + cx-lead |
| B2 → B3 | 10 DPPs pagos + CAC < R$300 + onboarding < 60 min sem suporte | cfo + analytics-agent |
| B3 → B4 | 30 marcas ativas + breakeven atingido + churn < 5%/mês | cfo + founder-orchestrator |
