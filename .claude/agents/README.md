# Φ PHYLLOS — Time de Agentes Claude

Time completo de agentes IA organizados em duas camadas (líderes e executores) para operar a Phyllos wear.

## Arquitetura

```
                    brand-director
                         │
     ┌───────────────────┼─────────────────────┐
     │           │       │        │             │
social-media  marketing  comm   tech-lead    operations
  -lead        -lead    -lead               -lead
     │           │       │        │             │
  ┌──┴──┐    ┌───┼──┐  ┌─┼──┐  ┌──┼──┐   ┌───┼───┐
content  visual  paid  email  seo  pr brand  inf  front  ecomm  qa  supply  cert  inv
creator  brief  media   crm  blog press voice  col  end    erc       chain        ory
                agent  agent  agent   agent agent  agent agent  agent agent  agent
```

## Time Completo

### Camada 0 — Orquestrador
| Arquivo | Agente | Papel |
|---------|--------|-------|
| [brand-director.md](brand-director.md) | Brand Director | Orquestrador. Distribui objetivos, valida coerência de marca, aprova comunicação pública |

### Camada 1 — Líderes
| Arquivo | Agente | Time |
|---------|--------|------|
| [social-media-lead.md](social-media-lead.md) | Social Media Lead | Calendário editorial, briefing de posts, aprovação de conteúdo |
| [marketing-lead.md](marketing-lead.md) | Marketing Lead | Estratégia de aquisição, campanhas, funil, KPIs |
| [communication-lead.md](communication-lead.md) | Communication Lead | Narrativa pública, PR, crise, parcerias |
| [tech-lead.md](tech-lead.md) | Tech Lead | Arquitetura digital, backlog, qualidade técnica |
| [cx-lead.md](cx-lead.md) | CX Lead | Padrão de atendimento, políticas, análise sistêmica |
| [operations-lead.md](operations-lead.md) | Operations Lead | Cadeia produtiva, certificações, estoque |

### Camada 2 — Executores

**Time Social Media**
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [content-creator.md](content-creator.md) | Content Creator | Captions, roteiros de Reels, stories, threads |
| [visual-briefer.md](visual-briefer.md) | Visual Briefer | Briefings técnicos para designer ou IA generativa |
| [analytics-agent.md](analytics-agent.md) | Analytics Agent | Métricas de performance, relatório semanal |

**Time Marketing**
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [paid-media-agent.md](paid-media-agent.md) | Paid Media Agent | Copies de anúncio, estrutura de campanha, A/B |
| [email-crm-agent.md](email-crm-agent.md) | Email & CRM Agent | Fluxos de automação, newsletters, régua de comunicação |
| [seo-blog-agent.md](seo-blog-agent.md) | SEO & Blog Agent | Artigos, otimização de páginas, palavras-chave |

**Time Comunicação**
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [pr-press-agent.md](pr-press-agent.md) | PR & Press Agent | Press releases, pitches, press kit |
| [brand-voice-agent.md](brand-voice-agent.md) | Brand Voice Agent | Revisão de tom, checklist contra manifesto |
| [influencer-collab-agent.md](influencer-collab-agent.md) | Influencer & Collab Agent | Seleção de parceiros, propostas, briefing de collab |

**Time Tech**
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [frontend-agent.md](frontend-agent.md) | Frontend Agent | HTML/CSS/JS do site Phyllos, design system |
| [ecommerce-agent.md](ecommerce-agent.md) | E-commerce Agent | Plataforma de loja, checkout, integrações de pagamento |
| [qa-agent.md](qa-agent.md) | QA Agent | Testes de feature, acessibilidade, regressão |

**Time Customer Experience**
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [support-agent.md](support-agent.md) | Support Agent | Dúvidas pré e pós-compra, tamanhos, prazos |
| [returns-agent.md](returns-agent.md) | Returns & Exchange Agent | Trocas, devoluções, reembolsos |
| [loyalty-agent.md](loyalty-agent.md) | Loyalty Agent | Retenção, fidelização, coleta de feedback |

**Time Operações**
| Arquivo | Agente | Responsabilidade |
|---------|--------|-----------------|
| [supply-chain-agent.md](supply-chain-agent.md) | Supply Chain Agent | Fornecedores, procedência, riscos de ruptura |
| [certification-agent.md](certification-agent.md) | Certification Agent | Certificações (GOTS, GRS), relatório de transparência |
| [inventory-agent.md](inventory-agent.md) | Inventory Agent | Estoque por SKU, reposição, projeção de demanda |

## Como usar

No Claude Code, chame qualquer agente via:
```
use agent: [nome-do-agente]
```

Ou deixe o Brand Director orquestrar a tarefa:
```
use agent: brand-director
[descreva o objetivo]
```

## Fluxo de aprovação de conteúdo

```
Executor cria → Líder revisa → Brand Voice revisa → Brand Director aprova → Publicar
```
