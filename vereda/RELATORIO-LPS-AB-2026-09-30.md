# Relatório de entrega — LPs segmentadas Vereda A/B

**Data:** 30/09/2026  
**Execution Brief:** `VEREDA-LP-AB-2026-09-30`  
**Ambiente:** `https://vereda-dpp.netlify.app`  
**Deploy publicado:** `6abd2acd35adc21db6d36547`

## Resultado

Foram construídas e publicadas dez landing pages, duas para cada segmento comercial do formulário público:

| Segmento | Variante A — risco/readiness | Variante B — acesso a mercado | Distribuição 50/50 |
|---|---|---|---|
| Moda, têxteis e confecção | `/lp/textil-confeccao/a/` | `/lp/textil-confeccao/b/` | `/lp/textil-confeccao/` |
| Calçados e couro | `/lp/calcados-couro/a/` | `/lp/calcados-couro/b/` | `/lp/calcados-couro/` |
| Agro | `/lp/agro/a/` | `/lp/agro/b/` | `/lp/agro/` |
| Manufatura | `/lp/manufatura/a/` | `/lp/manufatura/b/` | `/lp/manufatura/` |
| Cooperativas | `/lp/cooperativas/a/` | `/lp/cooperativas/b/` | `/lp/cooperativas/` |

A rota sem a letra da variante distribui 50/50, grava a escolha no navegador e preserva UTMs. `?variant=a` e `?variant=b` permitem QA e campanhas com bucket forçado.

## Mensuração

O formulário `diagnostico-vereda-lp` foi reconhecido pelo Netlify Forms com os campos:

- `segment`, `variant` e `landing_page`;
- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` e `utm_term`;
- `name`, `company`, `email`, `target_market` e `sku_volume`;
- honeypot ativo.

Os eventos `vereda_landing_view`, `vereda_cta_click`, `vereda_form_start`, `vereda_lead_submitted` e `vereda_form_error` são registrados em `window.dataLayer`. Nenhuma ferramenta externa de analytics foi conectada nesta entrega.

## QA e evidência

- 10 páginas × 3 viewports = 30 verificações em localhost.
- 30 verificações no deploy de preview da Netlify.
- 30 verificações na URL final de produção.
- 5 testes das rotas 50/50 em cada ambiente.
- Sem rolagem horizontal, recursos quebrados ou erros de console.
- Um H1 por LP, foco visível, labels, mensagens de erro e bloqueio de envio na prévia local.
- Formulário reconhecido na produção sem envio de lead fictício.
- Três regras de headers processadas pela Netlify sem erro.

Evidências locais: `previews/lp-qa-results.json` e capturas `previews/lp-*.png`.

## Claims e limites

- Exemplos são identificados como fictícios e ilustrativos.
- As páginas não apresentam clientes, certificações, conformidade ou resultados inventados.
- A conversa inicial não é apresentada como parecer jurídico, diagnóstico completo ou garantia de acesso a mercado.
- A variante B usa canonical da variante A e `noindex, follow` para evitar competição/duplicidade em busca.

## Status por evidência

- **Local:** concluído.
- **Integrado:** formulário, roteamento A/B e atribuição integrados.
- **Testado:** concluído localmente, em preview e em produção.
- **Documentado:** concluído.
- **Publicado:** concluído na Netlify.
- **Verificado ao vivo:** concluído.
- **Mídia/analytics/CRM:** não ativados; fora do escopo.

## Próxima decisão do founder

Definir canal, orçamento, janela e amostra mínima do experimento. A variante vencedora deve ser decidida pela conversão em leads qualificados por sessão e pela qualidade comercial, não por cliques isolados.
