# Φ PHYLLOS — Time de Agentes Claude

Time completo de agentes IA organizados em duas camadas (líderes e executores) para operar a Phyllos wear. **35 agentes** cobrindo todos os times do negócio.

---

## Arquitetura Geral

```
        brand-director ◄────────────────► product-director
               │                                  │
    ┌──────────┼──────────┐          ┌────────────┼────────────┐
    │          │          │          │            │            │
 social    marketing   comm       design       materials    product
 media      lead       lead        lead          lead        dev-lead
  lead        │          │          │              │            │
    │      ┌──┼──┐    ┌──┼──┐    ┌──┴──┐       ┌──┴──┐    ┌───┼───┐
  [3]     [3]  [3]   [3]      designer fit     researcher sourcing spec  testing launch
                              fit-tech          sourcing   writer  agent  coord
```

**Dois diretores, um protocolo de interface** — Brand Brief vai de Brand Director para Product Director. Dossier de Lançamento vai de Product Director para Brand Director. O produto prova o que a marca promete.

---

## DIRETORIA — Camada Estratégica

| Arquivo | Agente | Papel |
|---------|--------|-------|
| [brand-director.md](brand-director.md) | **Brand Director** | Estratégia de marca, posicionamento, voz, credibilidade, stack de marketing. Aprova toda comunicação pública. Par do Product Director. |
| [product-director.md](product-director.md) | **Product Director** | Viabiliza a visão da marca em produto físico. Gestão de coleção, materiais, desenvolvimento, teste e lançamento. Par do Brand Director. |

### Interface entre os dois diretores

```
BRAND DIRECTOR                              PRODUCT DIRECTOR
      │                                            │
      │── Brand Brief de Coleção ──────────────►  │
      │                                            │── Materials Lead
      │◄── Resposta Estratégica de Produto ────────│── Design Lead
      │                                            │── Product Dev Lead
      │── [feedback de estética] ───────────────►  │
      │◄── Atualização de Proto ────────────────── │
      │                                            │
      │◄── Dossier de Lançamento ───────────────── │  (Gate 5)
      │── Aprovação de Lançamento ──────────────►  │
      │                                            │
      │── Feedback Loop de Mercado ─────────────►  │  (L+30)
      │◄── Resposta ao Feedback Loop ───────────── │
```

---

## TIME DE MARCA — Brand Director coordena

### Líderes
| Arquivo | Agente | Time |
|---------|--------|------|
| [social-media-lead.md](social-media-lead.md) | Social Media Lead | Calendário editorial, briefing, aprovação de conteúdo |
| [marketing-lead.md](marketing-lead.md) | Marketing Lead | Aquisição, campanhas, funil, KPIs |
| [communication-lead.md](communication-lead.md) | Communication Lead | Narrativa pública, PR, crise, parcerias |
| [tech-lead.md](tech-lead.md) | Tech Lead | Arquitetura digital, backlog, qualidade |
| [cx-lead.md](cx-lead.md) | CX Lead | Atendimento, políticas, análise sistêmica |
| [operations-lead.md](operations-lead.md) | Operations Lead | Cadeia produtiva, certificações, estoque |

### Executores — Time Social Media
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [content-creator.md](content-creator.md) | Content Creator | Captions, Reels, stories, threads |
| [visual-briefer.md](visual-briefer.md) | Visual Briefer | Briefings para designer ou IA generativa |
| [analytics-agent.md](analytics-agent.md) | Analytics Agent | Métricas, relatório semanal |

### Executores — Time Marketing
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [paid-media-agent.md](paid-media-agent.md) | Paid Media Agent | Copies de anúncio, campanhas, A/B |
| [email-crm-agent.md](email-crm-agent.md) | Email & CRM Agent | Automações, newsletters, régua |
| [seo-blog-agent.md](seo-blog-agent.md) | SEO & Blog Agent | Artigos, palavras-chave, otimização |

### Executores — Time Comunicação
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [pr-press-agent.md](pr-press-agent.md) | PR & Press Agent | Press releases, pitches, press kit |
| [brand-voice-agent.md](brand-voice-agent.md) | Brand Voice Agent | Revisão de tom, guardião do manifesto |
| [influencer-collab-agent.md](influencer-collab-agent.md) | Influencer & Collab Agent | Seleção de parceiros, propostas, briefing |

### Executores — Time Tech
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [frontend-agent.md](frontend-agent.md) | Frontend Agent | HTML/CSS/JS, design system Phyllos |
| [ecommerce-agent.md](ecommerce-agent.md) | E-commerce Agent | Plataforma, checkout, integrações |
| [qa-agent.md](qa-agent.md) | QA Agent | Testes, acessibilidade, regressão |

### Executores — Time Customer Experience
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [support-agent.md](support-agent.md) | Support Agent | Dúvidas pré e pós-compra |
| [returns-agent.md](returns-agent.md) | Returns & Exchange Agent | Trocas, devoluções, reembolsos |
| [loyalty-agent.md](loyalty-agent.md) | Loyalty Agent | Retenção, fidelização, feedback |

### Executores — Time Operações
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [supply-chain-agent.md](supply-chain-agent.md) | Supply Chain Agent | Fornecedores, procedência, ruptura |
| [certification-agent.md](certification-agent.md) | Certification Agent | GOTS, GRS, relatório de transparência |
| [inventory-agent.md](inventory-agent.md) | Inventory Agent | Estoque por SKU, reposição, demanda |

---

## TIME DE PRODUTO — Product Director coordena

### Líderes
| Arquivo | Agente | Time |
|---------|--------|------|
| [design-lead.md](design-lead.md) | Design Lead | Direção criativa, aprovação de estética, silhueta e detalhes |
| [materials-lead.md](materials-lead.md) | Materials Lead | Seleção de material, critérios sustentáveis, certificações |
| [product-dev-lead.md](product-dev-lead.md) | Product Dev Lead | Stage-Gate, Dossier de Lançamento, QC de produção |

### Executores — Time Design
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [product-designer.md](product-designer.md) | Product Designer | Flat sketches, construção de peça, colorways |
| [fit-technical-designer.md](fit-technical-designer.md) | Fit & Technical Designer | Modelagem, fitting, gradação por tamanho |

### Executores — Time Materiais
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [materials-researcher.md](materials-researcher.md) | Materials Researcher | Pesquisa de tecidos técnicos e sustentáveis |
| [sourcing-agent.md](sourcing-agent.md) | Sourcing Agent | Negociação, auditoria de fornecedor, procedência |

### Executores — Time Desenvolvimento
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [tech-spec-writer.md](tech-spec-writer.md) | Tech Spec Writer | Tech Pack + Ficha Técnica de Produto |
| [product-testing-agent.md](product-testing-agent.md) | Product Testing Agent | Protocolo de teste de 6 meses, validação de claims |
| [launch-coordinator.md](launch-coordinator.md) | Launch Coordinator | Timeline reversa, handoff de lançamento, go/no-go |

---

## Ciclo de produto Phyllos (Stage-Gate)

```
Brand Brief          Gate 1       Gate 2      Gate 3      Gate 4        Gate 5        Gate 6
(Brand Dir) ──────► Definição ──► Proto ────► Fitting ──► Teste ──────► Aprovação ──► Lançamento
                   (90 dias)    (75 dias)   (60 dias)   (6 meses)     (-L90 dias)    (L = dia 0)
                       │            │           │            │              │
                  Materials    Design      Fit-Tech     Testing        Dossier ao
                    Lead        Lead       Designer      Agent        Brand Dir
```

---

## Fluxos principais

**Aprovação de conteúdo de marca:**
```
Executor cria → Líder revisa → Brand Voice revisa → Brand Director aprova → Publicar
```

**Lançamento de produto:**
```
Brand Brief → Product Director → [Design + Materiais + Dev em paralelo] → Dossier → Brand Director aprova → Launch Coordinator → Mercado
```

**Feedback pós-lançamento:**
```
Cliente → CX → Analytics → Brand Director → Feedback Loop → Product Director → Próxima coleção
```

---

## Como usar

```
use agent: brand-director   → objetivos estratégicos, aprovações, múltiplos times
use agent: product-director → desenvolvimento de produto, coleção, materiais, lançamento
use agent: [qualquer outro] → tarefa específica daquele agente
```

**Total: 35 agentes** — 2 diretores + 9 líderes + 24 executores
