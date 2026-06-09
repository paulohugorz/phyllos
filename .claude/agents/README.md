# Φ PHYLLOS — Time de Agentes Claude

Time completo de agentes IA em três diretorias estratégicas. **45 agentes** cobrindo marca, produto e tecnologia.

---

## Arquitetura de Diretores

```
brand-director ◄────────────────────────────────► product-director
       │                                                  │
       │         Digital Experience Brief                 │  Brand Brief de Coleção
       │◄──────────────────────────────────────┐          │◄─────────────────────────────┐
       │                                       │          │                              │
       └──────────────────────────────────────►│          └─────────────────────────────►│
       │         Digital Capability Report     │          │  Dossier de Lançamento       │
       │                                       │          │                              │
       └─────────────► technology-director ◄──────────────┘
                              │
                    Product Tech Brief ◄► Product Tech Infrastructure Report
```

**Três diretores, dois protocolos de interface cada** — toda decisão de impacto cruzado tem documento de handoff formal.

---

## DIRETORIA DE MARCA — Brand Director coordena

| Arquivo | Agente | Papel |
|---------|--------|-------|
| [brand-director.md](brand-director.md) | **Brand Director** | Estratégia, posicionamento, voz, credibilidade, stack de marketing. Aprova toda comunicação pública. |

### Líderes de Marca
| Arquivo | Agente | Time |
|---------|--------|------|
| [social-media-lead.md](social-media-lead.md) | Social Media Lead | Calendário editorial, briefing, aprovação de conteúdo |
| [marketing-lead.md](marketing-lead.md) | Marketing Lead | Aquisição, campanhas, funil, KPIs |
| [communication-lead.md](communication-lead.md) | Communication Lead | Narrativa pública, PR, crise, parcerias |
| [cx-lead.md](cx-lead.md) | CX Lead | Atendimento, políticas, análise sistêmica |
| [operations-lead.md](operations-lead.md) | Operations Lead | Cadeia produtiva, certificações, estoque |

### Executores — Social Media
| [content-creator.md](content-creator.md) | Content Creator | Captions, Reels, stories |
| [visual-briefer.md](visual-briefer.md) | Visual Briefer | Briefings para designer ou IA |
| [analytics-agent.md](analytics-agent.md) | Analytics Agent | Métricas, relatório semanal |

### Executores — Marketing
| [paid-media-agent.md](paid-media-agent.md) | Paid Media Agent | Copies, campanhas, A/B |
| [email-crm-agent.md](email-crm-agent.md) | Email & CRM Agent | Automações, newsletters, régua |
| [seo-blog-agent.md](seo-blog-agent.md) | SEO & Blog Agent | Artigos, palavras-chave |

### Executores — Comunicação
| [pr-press-agent.md](pr-press-agent.md) | PR & Press Agent | Press releases, pitches |
| [brand-voice-agent.md](brand-voice-agent.md) | Brand Voice Agent | Guardião do manifesto e do tom |
| [influencer-collab-agent.md](influencer-collab-agent.md) | Influencer & Collab Agent | Seleção de parceiros, briefing |

### Executores — CX
| [support-agent.md](support-agent.md) | Support Agent | Dúvidas pré e pós-compra |
| [returns-agent.md](returns-agent.md) | Returns & Exchange Agent | Trocas e devoluções |
| [loyalty-agent.md](loyalty-agent.md) | Loyalty Agent | Retenção e fidelização |

### Executores — Operações
| [supply-chain-agent.md](supply-chain-agent.md) | Supply Chain Agent | Fornecedores, procedência |
| [certification-agent.md](certification-agent.md) | Certification Agent | GOTS, GRS, transparência |
| [inventory-agent.md](inventory-agent.md) | Inventory Agent | Estoque por SKU, reposição |

---

## DIRETORIA DE PRODUTO — Product Director coordena

| Arquivo | Agente | Papel |
|---------|--------|-------|
| [product-director.md](product-director.md) | **Product Director** | Viabiliza a visão da marca em produto físico. Colecão, materiais, desenvolvimento, teste, lançamento. |

### Líderes de Produto
| Arquivo | Agente | Time |
|---------|--------|------|
| [design-lead.md](design-lead.md) | Design Lead | Direção criativa, aprovação estética |
| [materials-lead.md](materials-lead.md) | Materials Lead | Seleção de material, certificações |
| [product-dev-lead.md](product-dev-lead.md) | Product Dev Lead | Stage-Gate, Dossier de Lançamento, QC |

### Executores — Design
| [product-designer.md](product-designer.md) | Product Designer | Flat sketches, construção, colorways |
| [fit-technical-designer.md](fit-technical-designer.md) | Fit & Technical Designer | Modelagem, fitting, gradação |

### Executores — Materiais
| [materials-researcher.md](materials-researcher.md) | Materials Researcher | Pesquisa de tecidos técnicos e sustentáveis |
| [sourcing-agent.md](sourcing-agent.md) | Sourcing Agent | Negociação, auditoria, procedência |

### Executores — Desenvolvimento
| [tech-spec-writer.md](tech-spec-writer.md) | Tech Spec Writer | Tech Pack + Ficha Técnica |
| [product-testing-agent.md](product-testing-agent.md) | Product Testing Agent | Teste de 6 meses, validação de claims |
| [launch-coordinator.md](launch-coordinator.md) | Launch Coordinator | Timeline reversa, handoff, go/no-go |

---

## DIRETORIA DE TECNOLOGIA — Technology Director coordena

| Arquivo | Agente | Papel |
|---------|--------|-------|
| [technology-director.md](technology-director.md) | **Technology Director** | Infraestrutura digital, dados, AI, segurança, LGPD, roadmap tech. Par dos outros dois diretores. |

### Líderes de Tecnologia
| Arquivo | Agente | Time |
|---------|--------|------|
| [digital-products-lead.md](digital-products-lead.md) | Digital Products Lead | Site, e-commerce, UX tech, backlog digital |
| [data-intelligence-lead.md](data-intelligence-lead.md) | Data Intelligence Lead | Dados, analytics, BI, first-party data, LGPD |
| [ai-automation-lead.md](ai-automation-lead.md) | AI & Automation Lead | Agentes Claude, automações, integrações, DevOps, segurança |

### Executores — Produto Digital
| [frontend-agent.md](frontend-agent.md) | Frontend Agent | HTML/CSS/JS, design system Phyllos |
| [ecommerce-agent.md](ecommerce-agent.md) | E-commerce Agent | Plataforma, checkout, integrações de pagamento |
| [qa-agent.md](qa-agent.md) | QA Agent | Testes, acessibilidade, regressão |

### Executores — Dados e Inteligência
| [data-engineer.md](data-engineer.md) | Data Engineer | Pipelines, warehouse, qualidade de dados |
| [bi-analyst.md](bi-analyst.md) | BI Analyst | Dashboards, relatórios, insights acionáveis |

### Executores — AI, Automação e Infra
| [ai-ops-agent.md](ai-ops-agent.md) | AI Ops Agent | Validação e monitoramento dos agentes Claude |
| [integration-agent.md](integration-agent.md) | Integration Agent | APIs, webhooks, n8n, integrações de sistema |
| [devops-security-agent.md](devops-security-agent.md) | DevOps & Security Agent | CI/CD, monitoramento, LGPD, segurança |

---

## Protocolos de Interface Entre Diretorias

### Brand ↔ Product
```
Brand Director envia:   Brand Brief de Coleção
Product Director retorna: Resposta Estratégica → Atualização de Proto → Dossier de Lançamento
Brand Director envia:   Feedback Loop de Mercado (pós-lançamento)
```

### Brand ↔ Technology
```
Brand Director envia:   Digital Experience Brief (UX, canais, padrões de marca)
Technology Director retorna: Digital Capability Report (viabilidade, roadmap, trade-offs)
```

### Product ↔ Technology
```
Product Director envia: Product Tech Brief (PLM, traceabilidade, dados de produto)
Technology Director retorna: Product Tech Infrastructure Report (sistemas, APIs, status)
```

---

## Ciclo de Produto (Stage-Gate)

```
Brand Brief → Gate 1 → Gate 2 → Gate 3 → Gate 4 (6 meses) → Gate 5 → Gate 6
(Brand Dir)  Definição  Proto  Fitting    Teste            Aprovação  Lançamento
                │         │       │           │                │
           Materials  Design  Fit-Tech    Testing          Dossier
              Lead     Lead   Designer     Agent         ao Brand Dir
```

---

## Ciclo de Dado

```
Coleta (GA4 + Klaviyo + Survey)
      ↓
Data Engineer (pipeline + warehouse)
      ↓
BI Analyst (dashboards por audiência)
      ↓
Brand Director / Marketing Lead / Product Director / CX Lead / Technology Director
```

---

## Como Usar

```
use agent: brand-director       → estratégia de marca, aprovações, comunicação pública
use agent: product-director     → produto, coleção, materiais, lançamento
use agent: technology-director  → arquitetura, plataformas, dados, AI, segurança
use agent: [qualquer outro]     → tarefa específica daquele agente
```

---

**Total: 45 agentes** — 3 diretores + 11 líderes + 31 executores
