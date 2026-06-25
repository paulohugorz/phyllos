# Catálogo de Fatores de Impacto — DPP Studio

**Data:** 2026-06-25
**Status:** aprovado — duas frentes em paralelo
**Responsável:** CTO + CFO + Curador de Materiais

---

## Decisão

Seguir com **duas frentes simultâneas**:

| Frente | O que é | Prazo | Custo |
|---|---|---|---|
| **A — Fatores genéricos** | Usar bancos abertos (Ecoinvent, IPCC, Higg MSI public) para o piloto | Agosto/2026 | Zero |
| **B — Catálogo próprio** | Curar fatores específicos para fibras brasileiras prioritárias | Out/2026–Q1/2027 | 40–80h pesquisa + curadoria |

A Frente A permite entregar DPPs calculados no piloto sem depender de terceiros ou licenças.
A Frente B é um ativo estratégico: o catálogo de fibras BR não existe no mercado — quem o construir define o padrão.

---

## Frente A — Fatores Genéricos (Piloto Agosto)

### Fontes abertas por indicador

| Indicador | Fonte primária | Fonte secundária |
|---|---|---|
| CO₂eq (kg/kg fibra) | Ecoinvent 3.9 (free tier) | IPCC AR6 Annex II |
| Água (L/kg) | Higg MSI 2023 (public summary) | Water Footprint Network |
| Energia (MJ/kg) | ProBAS / INMETRO BR | IEA Textile Sector Report |
| Resíduo pós-corte (%) | Estimativa padrão têxtil: 15–20% | Dado declarado pela marca |

### Declaração obrigatória no DPP (anti-greenwashing)

Todo campo calculado com Frente A deve exibir:

```json
{
  "metodologia": "estimativa_generica",
  "fonte": "ecoinvent_3.9 / higg_msi_2023_public",
  "confianca": "media",
  "nota": "Fator genérico não calibrado para origem brasileira. Substitua por dado verificado do fornecedor para aumentar precisão."
}
```

### Fibras cobertas no piloto (mínimo viável)

| Fibra | CO₂eq kg/kg | Água L/kg | Energia MJ/kg | Fonte |
|---|---|---|---|---|
| Algodão convencional (genérico) | 5,9 | 10.000 | 55 | Higg MSI 2023 |
| Algodão orgânico (GOTS) | 3,8 | 2.100 | 48 | Higg MSI 2023 |
| Poliéster virgem | 9,5 | 71 | 125 | Ecoinvent 3.9 |
| Poliéster reciclado (GRS) | 3,8 | 50 | 77 | Higg MSI 2023 |
| Viscose/Modal (genérico) | 3,7 | 150 | 45 | Higg MSI 2023 |
| Elastano (Spandex) | 26,0 | 300 | 230 | Ecoinvent 3.9 |
| Lã virgem | 28,0 | 170 | 63 | Higg MSI 2023 |
| Linho | 1,7 | 500 | 10 | Water Footprint Network |
| Nylon 6 | 7,9 | 230 | 120 | Ecoinvent 3.9 |
| Nylon 6.6 | 8,1 | 250 | 125 | Ecoinvent 3.9 |

> Arquivo estruturado: `produto/catalogo-impacto/fatores-genericos-v0.json`

---

## Frente B — Catálogo Próprio (Ativo Estratégico)

### Por que isso é um moat

- O **Higg MSI** é o padrão global mas não tem especificidade para fibras brasileiras (algodão BR cerrado, viscose Lenzing de fábrica BR, poliéster reciclado nacional).
- Nenhum player brasileiro publicou isso como dado calibrado.
- Quem construir e publicar o catálogo de fibras BR vira a referência — inclusive para INMETRO e futura regulação brasileira.
- O catálogo alimenta o **PLC** e é protegível como compilação (copyright + trade secret técnico na metodologia).

### Fibras prioritárias para curadoria BR

**Lote 1 — Agosto/2026** (volume de uso nas marcas-alvo do piloto)
- Algodão convencional Cerrado (Mato Grosso — maior produtor BR)
- Algodão orgânico BR (certificado ABR ou GOTS)
- Viscose BR (Lenzing / fábrica de celulose nacional)
- Fio reciclado (PET garrafa BR — dado ABIPET disponível)

**Lote 2 — Out/2026**
- Fibra de coco babaçu (amazônico, crescente)
- Linho BR (Paraná — produção emergente)
- Seda BR (São Paulo — nicho premium)
- Tencel / Lyocell com cadeia nacional
- Malha de algodão pima BR

**Lote 3 — Q1/2027**
- Blends mais comuns: 65/35 poliéster-algodão, 95/5 algodão-elastano
- Tecidos funcionais: dry-fit, anti-UV, repelente
- Fibras inovadoras: Piñatex, QMilk, Econyl

### Metodologia de curadoria

Para cada fibra, coletar e documentar:

```
1. Dados de Life Cycle Assessment (LCA) disponíveis na literatura
2. Contato direto com fornecedor BR para EPD (Environmental Product Declaration)
3. Triangulação: mínimo 2 fontes antes de publicar fator
4. Hash SHA-256 + timestamp de cada versão (proteção de PI)
5. Marcação de confiança: genérico / calibrado-BR / verificado-fornecedor
```

### Parceiros potenciais para co-curadoria

| Parceiro | O que traz | O que a PHYLLOS oferece |
|---|---|---|
| ABIT (Assoc. Brasileira da Indústria Têxtil) | Dados de produção BR | Metodologia + publicação DPP |
| ABVTEX | Cadeia de fornecimento auditada | Integração no passaporte |
| INMETRO | Legitimidade regulatória | Piloto de certificação DPP BR |
| Universidades (USP, UNICAMP, UFSC) | Pesquisa LCA em fibras BR | Co-autoria + dados primários |
| Lenzing / Suzano | EPDs de viscose e eucalipto BR | Selo "Dado verificado pelo fornecedor" |

---

## Custo de construção do catálogo

| Item | Horas | Custo estimado |
|---|---|---|
| Pesquisa bibliográfica + LCA (por fibra) | 4–6h/fibra | R$0 (interno) ou R$800–1.500/fibra (freelance especialista) |
| Contato e coleta EPD com fornecedores | 2h/fornecedor | R$0 |
| Estruturação JSON + validação técnica | 1h/fibra | R$0 (interno) |
| Revisão por especialista em LCA (externo) | 8–16h total | R$2.000–5.000 one-time |
| **Lote 1 (4 fibras) — mínimo viável** | ~24h | **R$0–3.000** |
| **Catálogo completo (30 fibras)** | ~120h | **R$5.000–15.000** |

---

## Estrutura do arquivo de catálogo

Definido em `produto/catalogo-impacto/fatores-genericos-v0.json`.
Schema reutilizado pelo DPP Studio para calcular indicadores automaticamente.

```json
{
  "fibra_id": "algodao_convencional_br",
  "nome_pt": "Algodão Convencional — Brasil",
  "categoria": "natural_vegetal",
  "origem": "brasil",
  "indicadores": {
    "co2eq_kg_por_kg":    { "valor": 5.9,    "unidade": "kgCO2eq/kg", "confianca": "media" },
    "agua_l_por_kg":      { "valor": 10000,  "unidade": "L/kg",       "confianca": "media" },
    "energia_mj_por_kg":  { "valor": 55,     "unidade": "MJ/kg",      "confianca": "media" }
  },
  "fonte": "higg_msi_2023_public",
  "metodologia": "estimativa_generica",
  "versao": "v0.1",
  "data_curadoria": "2026-06-25",
  "hash_sha256": null
}
```

---

## Próximas ações

| Ação | Responsável | Prazo |
|---|---|---|
| Criar `fatores-genericos-v0.json` com 10 fibras do piloto | CTO | Jul/2026 |
| Integrar catálogo na API `/dpp/calcular` do DPP Studio | CTO | Jul/2026 |
| Iniciar coleta de dados EPD com fornecedores Lote 1 | Curador de Materiais | Ago/2026 |
| Contratar especialista LCA para revisão (R$2–5K) | CFO | Q3/2026 |
| Publicar metodologia aberta (sem os dados) como OSS | CMO + CTO | Q3/2026 |
| Versão calibrada-BR das 4 fibras prioritárias | CTO + Curador | Out/2026 |
