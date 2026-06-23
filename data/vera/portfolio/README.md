# Vera - banco de dados do portfólio

Este diretório inicia a organização do portfólio da Vera como banco de dados. A regra é simples: nenhum produto deve ficar apenas em texto corrido. Cada informação precisa entrar no lugar certo para poder ser consultada, atualizada e reutilizada por agentes de atendimento, conteúdo, vendas e compliance.

## Arquivos

- `schema.sql`: estrutura relacional em SQLite.
- `seed_natura_2026-06-18.sql`: primeiro snapshot com os cinco produtos Natura estudados em 2026-06-18.

## Como as informações foram quebradas

| Área | Tabela | O que guarda |
|---|---|---|
| Fonte | `sources` | Origem dos dados, data de coleta e observações. |
| Produto | `products` | SKU, nome, marca, linha, categoria, volume, público e URL oficial. |
| Oferta | `offers` | Preço, estoque, nota e quantidade de avaliações por data de coleta. |
| Produto detalhado | `product_facts` | Notas olfativas, benefícios, claims, reviews, uso, embalagem e lacunas. |
| Venda | `sales_profiles` | Cliente ideal, posicionamento, gancho, uso recomendado e objeção central. |
| Atendimento | `diagnostic_questions` | Perguntas consultivas globais ou por produto. |
| Objeções | `objections` | Objeção do cliente, resposta sugerida e risco de compliance. |
| Campanha | `campaign_ideas` | Tema, canal, formato, gancho, ângulo de conteúdo, CTA e status. |
| Combos | `combos` e `combo_items` | Kits comerciais e produtos que compõem cada combo. |
| Compliance | `compliance_rules` | Regras de linguagem, claims, preço, reviews e proteção solar. |
| Verificação | `verification_tasks` | Lacunas que precisam ser confirmadas antes de publicar ou vender. |
| Agentes | `agent_workstreams` | Escopo e entregáveis de cada agente operacional. |

## Fluxo para novos produtos

1. Criar ou atualizar o produto em `products`.
2. Registrar preço, estoque e avaliações em `offers` com a data da coleta.
3. Quebrar benefícios, notas, modo de uso, claims e reviews em `product_facts`.
4. Marcar cada fato com `evidence_level`:
   - `official_page`: veio da página oficial;
   - `official_page_title`: veio do título/schema;
   - `review_excerpt`: veio de avaliação de cliente;
   - `agent_analysis`: inferência ou organização do agente.
5. Se houver dúvida, usar `needs_verification = 1` e criar uma linha em `verification_tasks`.
6. Criar perfil comercial em `sales_profiles`.
7. Criar perguntas e objeções em `diagnostic_questions` e `objections`.
8. Criar campanha em `campaign_ideas` sempre com `compliance_status = 'needs_review'` ou `blocked_until_verified`.
9. Rodar o agente de compliance antes de transformar qualquer campanha em post, story, reel ou mensagem de WhatsApp.

## Como gerar um SQLite local

```bash
sqlite3 /private/tmp/vera_portfolio.db < data/vera/portfolio/schema.sql
sqlite3 /private/tmp/vera_portfolio.db < data/vera/portfolio/seed_natura_2026-06-18.sql
```

Consultas úteis:

```sql
-- Produtos e ultimo preço coletado
SELECT p.sku, p.product_name, o.price_cents / 100.0 AS price_brl, o.rating_value, o.review_count
FROM products p
JOIN offers o ON o.sku = p.sku
ORDER BY p.business_category, p.brand;

-- Campanhas bloqueadas por verificação
SELECT campaign_id, theme, hook, compliance_status
FROM campaign_ideas
WHERE compliance_status != 'needs_review';

-- Lacunas abertas por agente
SELECT owner_agent, sku, priority, question
FROM verification_tasks
WHERE status = 'open'
ORDER BY owner_agent, priority DESC;
```

## Regra operacional

O portfólio pode ter texto bonito, mas a fonte de verdade deve ser o banco: produto, oferta, fato, venda, campanha, combo e compliance separados. Assim a Vera consegue atualizar preço sem reescrever campanha, criar combo sem duplicar produto e bloquear claims antes que virem promessa pública.
