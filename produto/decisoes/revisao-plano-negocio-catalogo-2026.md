# Revisão do Plano de Negócio — Impacto do Catálogo de Fatores

**Data:** 2026-06-25
**Referência:** `analise-financeira-dpp-2026.md` (v1.0) + `tese-produto-dpp-integrado-phyllos.md`
**Gatilho:** Implementação do catálogo de fatores de impacto (`catalogo-fatores-impacto-2026.md`) e endpoints `/catalogo/*`
**Status:** revisão aprovada pelo founder / CEO

---

## O que mudou no produto

Antes do catálogo, o fluxo de onboarding exigia que a marca soubesse — ou pesquisasse — os fatores de impacto do seu material:

```
Fluxo ANTERIOR
Marca informa: composição + gramatura + área + agua_litros_kg + energia_kwh_kg + carbono_kgco2e_kg
Problema: nenhuma marca independente sabe esses valores de cabeça
Resultado: campo "Calculado" ficava vazio → DPP publicado com indicadores "Ausente"
```

Depois do catálogo:

```
Fluxo ATUAL
Marca informa: composição (%) + gramatura (g/m²) + área (m²)
Sistema: POST /catalogo/calcular-peca → fatores automáticos do catálogo → "Calculado"
Resultado: DPP com água, energia e carbono calculados em qualquer piloto
```

**Isso muda a proposta de valor central:** a PHYLLOS passou de "nós calculamos se você nos der os dados" para "traga a composição da etiqueta — nós calculamos o resto".

---

## Premissas revisadas

### 1.4 — Hipóteses de conversão e onboarding

| Parâmetro | Antes | Revisado | Razão |
|---|---|---|---|
| Tempo médio de onboarding — base | 60 min | 40 min | Fatores de impacto são automáticos. Marca não precisa pesquisar Higg MSI |
| Tempo médio de onboarding — conservador | 90 min | 60 min | Mesmo com fricção, o catálogo elimina a etapa mais difícil |
| Tempo médio de onboarding — otimista | 40 min | 25 min | Composição na etiqueta + gramatura do fornecedor → 1 chamada → DPP completo |
| Taxa de conversão piloto → pagante — base | 40% | 50% | Onboarding mais rápido + DPP mais completo = "aha moment" mais provável |
| Taxa de conversão piloto → pagante — conservador | 20% | 25% | Mesmo no pior caso, DPP com "Calculado" é mais convincente que DPP com "Ausente" |
| Taxa de conversão piloto → pagante — otimista | 60% | 70% | Session de 25 min + QR real + indicadores calculados = argumento de venda imediato |
| Upgrade mensal para assinatura (3 meses) — base | 30% | 40% | Se o 1º DPP entregou "Calculado", o 2º e 3º têm valor claro |

**Impacto no critério de go/no-go do piloto:** o gatilho "onboarding abaixo de 60 min" da estratégia de piloto está praticamente garantido por construção. O novo gatilho relevante passa a ser: "marca consegue informar composição + gramatura + área sem assistência do founder?"

---

## Receita revisada — Fase 1

### 3.2 — Q4 2026 com premissas de conversão revisadas

| Parâmetro | Antes (base) | Revisado (base) |
|---|---|---|
| Pilotos concluídos | 5 | 5 |
| Taxa de conversão | 40% (2 clientes) | 50% (2-3 clientes) |
| DPPs por cliente/mês | 2 | 2-3 |
| Ticket médio por DPP | R$199 | R$199 |
| Receita Out/26 | R$796 | R$996 |
| Receita Nov/26 | R$1.194 | R$1.592 |
| Receita Dez/26 | R$1.592 | R$2.189 |
| **Total Q4 2026** | **R$3.582** | **~R$4.777** |

**Novo breakeven operacional estimado:** permanece Marco/2027 no cenário base (aceleração de ~3 semanas). A mudança real é na qualidade do DPP entregue, não no timing de caixa.

---

## Estrutura de custos revisada

### 4.2 — Novo item Opex: construção do catálogo próprio (Frente B)

| Item | Custo | Fase | Nota |
|---|---|---|---|
| Pesquisa e curadoria Lote 1 (4 fibras BR) — interno | R$0 | Q3/2026 | 20-30h do founder + agentes |
| Revisão por especialista LCA externo | R$2.000–5.000 | Q3/2026 | One-time. Viabiliza "dados calibrados-BR" no DPP |
| Curadoria Lote 2 (5 fibras) | R$0–2.000 | Q4/2026–Q1/2027 | Parcialmente via contato com fornecedores |
| Curadoria Lote 3 (blends + funcionais) | R$0–3.000 | Q1–Q2/2027 | |
| **Total Frente B (18 meses)** | **R$2.000–10.000** | | Amortizado no período |

**Impacto no burn:** negligenciável. R$2-5K one-time em Q3/2026 não muda o breakeven.

**Impacto estratégico:** alto. O catálogo de fibras BR calibradas não existe no mercado. Quem construir primeiro define o padrão.

---

## Nova linha de produto: Catalog API

### Produto não modelado na v1.0 da análise financeira

O catálogo de fatores se torna um **produto separável** com demanda própria:

| Comprador potencial | O que quer | Disposição para pagar |
|---|---|---|
| Outros DPP providers em LatAm | Fatores de fibras BR sem precisar construir | USD 1.000–5.000/ano |
| PLM e ERP de moda (TOTVS, etc.) | Módulo de sustentabilidade sem pesquisa própria | USD 2.000–20.000/ano |
| Plataformas de ESG reporting | Fatores BR para cálculo de Scope 3 | USD 500–3.000/ano |
| Consultoras de compliance ambiental | Base de dados auditável | USD 1.000–8.000/ano |
| INMETRO / Sebrae (dados públicos BR) | Referência setorial | Parceria, não receita direta |

**Modelo de monetização sugerido:**
- Catálogo v0 (10 fibras genéricas): OSS / gratuito como posicionamento
- Catálogo v1 (fibras calibradas-BR, 30+ fibras): API paga, USD 99–499/mês
- Catálogo enterprise (EPD de fornecedores específicos, atualizações trimestrais): USD 2.000–10.000/ano

**Projeção conservadora Catalog API (Fase 3, 2028-2029):** 5–15 licenciados × USD 1.500/ano médio = USD 7.500–22.500/ano de receita adicional com COGS próximo de zero.

**Não incluído na projeção base.** Upside real mas dependente de crescimento do catálogo próprio.

---

## Moat revisado

A análise financeira original descrevia o moat como "velocidade e nicho BR". Após o catálogo, o moat tem uma camada adicional:

| Antes | Depois |
|---|---|
| Software com custo baixo de entrada | Software + ativo de dados proprietário |
| "Quem chega primeiro" na regulação | "Quem definiu o padrão de dados BR" |
| Dificuldade de copiar o workflow | Dificuldade de copiar o workflow E o corpus calibrado |

O catálogo de fibras BR calibradas funciona como o corpus PLC funciona para o Fashion OS: é proteção por composição (10.000+ horas de curadoria documentadas), não por patente.

**Implicação para valuation:** o múltiplo de ARR aplicável aumenta de 6–10× para 8–15× quando existe ativo de dados proprietário escalável, conforme precedentes como Retraced (EUR 15M Série A, ~15× ARR) e plataformas de ESG com banco de dados próprio.

---

## Unit economics revisado

### 7.4 — Tier Assinatura R$490/mês

| Métrica | Antes | Revisado | Razão |
|---|---|---|---|
| Churn mensal (base) | 5% | 4% | DPP com "Calculado" tem mais valor percebido que DPP com "Ausente" |
| Vida média do cliente | 20 meses | 25 meses | Churn menor |
| LTV | R$9.800 | R$12.250 | |
| LTV/CAC | 19,6× | 24,5× | |

### 7.4 — Tier Pay-per-DPP

| Métrica | Antes | Revisado |
|---|---|---|
| LTV/CAC | 1,2× | 1,5× |
| Razão | Marca sabe o que o DPP entrega antes de comprar (viu o Calculado no piloto) |

---

## Riscos novos introduzidos pelo catálogo

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Fatores genéricos do catálogo são imprecisos para fibras BR e marca exposta a crítica | Média | Médio | Declarar metodologia e confiança no DPP. "Estimativa genérica" está marcada |
| Concorrente copia o catálogo JSON público | Alta (se publicado sem proteção) | Médio | Canary data + publicar metodologia (OSS) mas não os dados calibrados. Dados ficam em API fechada |
| Especialista LCA discorda da metodologia de blend | Baixa | Médio | Revisão externa Q3/2026. Documentar limitações |
| Marca usa fatores do catálogo para claims de marketing sem declarar "estimativa" | Média | Alto | Aviso obrigatório no DPP e no output da API (`aviso` field já implementado) |

---

## Decisão de produto decorrente

**O DPP Studio canonico precisa incorporar o catalogo sem voltar ao wizard antigo.**

A interface vigente e o bundle registrado em `dpp-studio-versao-canonica-2026-06-25.md`. Qualquer evolucao de materiais deve partir desse bundle ou de uma fonte editavel equivalente aprovada, nao do prototipo anterior.

No fluxo atual, materiais e composicao sao macroetapa central. Com o catalogo, a evolucao correta e:

```
Materiais — Catalogo de fatores
  → usuário informa: composição em % (fibra_id + percentual)
  → sistema chama POST /catalogo/calcular-blend automaticamente
  → campos agua/energia/carbono preenchidos automaticamente com status "Calculado — catálogo v0"
  → usuário pode substituir por dado do fornecedor → status sobe para "Documentado"
```

Isso elimina a principal barreira técnica do onboarding e torna o campo "Calculado" acessível para 100% das marcas com qualquer dado de etiqueta.

**Próxima ação técnica:** integrar `/catalogo/calcular-blend` na macroetapa de materiais do DPP Studio canonico, registrando novo hash se a interface mudar.

---

## Resumo das revisões

| Dimensão | v1.0 | v2.0 (este documento) |
|---|---|---|
| Onboarding base | 60 min | 40 min |
| Conversão piloto→pagante base | 40% | 50% |
| Receita Q4/2026 base | R$3.582 | ~R$4.777 |
| Churn mensal base | 5% | 4% |
| LTV/CAC assinatura base | 19,6× | 24,5× |
| Múltiplo de valuation aplicável | 6–10× ARR | 8–15× ARR |
| Breakeven | Marco/2027 | Marco/2027 (sem alteração) |
| Nova linha de produto | — | Catalog API (Fase 3+) |
| Novo custo Frente B | — | R$2–10K (18 meses) |
| Moat | Velocidade + nicho BR | Velocidade + nicho BR + ativo de dados |
