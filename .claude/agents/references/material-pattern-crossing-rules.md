# Regras de Cruzamento Molde × Material — PHYLLOS

**Versão:** 1.0 · **Data:** 2026-06-26  
**Origem:** Análise cruzada do `seed_modelagens.py` (Mukai 2015), `fatores-genericos-v0.json` e modelos SQLAlchemy do Fashion OS.

---

## 1. Impossibilidades físicas — bloqueiam o produto

### 1.1 Compression sem elastano
`grau_ajuste = "compression"` usa folga de −4 cm no busto (tabela `folgas_vestibilidade`). Isso exige recuperação elástica. Fibras sem componente elástico **não permitem esse grau de ajuste**.

**Incompatíveis com compression:**
- algodao_convencional 100%, algodao_organico 100%
- linho 100%, canamo 100%
- lyocell_tencel 100%, viscose_modal 100%
- la_virgem 100%, la_cashmere 100%
- seda 100%, cupro 100%

**Regra:** compression requer `elastano_spandex ≥ 8%` ou nylon/poliéster em malha de alta elasticidade.  
**Ativewear de compressão típico:** 78% nylon reciclado + 22% elastano.

### 1.2 tipo_tecido = "plano" + elasticidade = "alta"
As tabelas `MEDIDAS_FEM_MALHA_ALTA` (30% de redução) existem apenas para `tipo_tecido = "malha"`. Tecido plano — mesmo com elastano — raramente supera 20% de alongamento. Usar `tipo_tecido = "plano"` com `elasticidade = "alta"` gera molde subdimensionado que não veste.

**Limite realista para tecido plano com elastano:** elasticidade = "baixa" (10%).

### 1.3 linha_fio = "vies" em malha
Viés é técnica exclusiva de tecido plano (corte a 45° da urdidura). Malha não tem urdidura estrutural — o conceito não se aplica.

**Inválido também:** `linha_fio = "trama"` em malha. Malha tem cursos/colunas, não trama/urdidura.

### 1.4 tingimento = "vegetal" com fibras sintéticas
Corantes vegetais precisam de grupos OH ou NH₂ para fixação. Poliéster não tem esses grupos — requer corante disperso em 130°C (autoclave). Incompatíveis:

| Fibra | Incompatibilidade |
|---|---|
| poliester_virgem | Impossível — sem grupos de fixação |
| poliester_reciclado | Impossível — mesma razão |
| nylon_6, nylon_66 | Muito difícil — aceita ácido mas não vegetal |
| pla_biopolimero | Impossível — sem grupos disponíveis |
| elastano_spandex | Não se tinge o elastano puro |

### 1.5 fibra_coco como tecido de vestuário
Coir tem diâmetro de 100–450 μm (algodão = 11–20 μm). É lignificada e rígida — nenhum maquinário de fiação convencional a processa. **Inaplicável para qualquer peça de vestuário.** Uso legítimo: isolamento técnico, solado, enchimento.

---

## 2. Conflitos de construção — produto fica errado

### 2.1 Pences em malha
Pences (base-blusa-basica-pences, base-vestido-tubo-pences, base-camisa-fem-pences) são mecanismo de tecido plano. Em malha, a elasticidade absorve a curvatura tridimensional — pences criam tensão irregular e deformam o caimento.  
**Evitar:** pences + `tipo_tecido = "malha"` de média ou alta elasticidade.

### 2.2 Franzido desaparece em malha de alta elasticidade
`base-manga-bufante`, `base-saia-pregueada`, `base-blusa-cigana` dependem de excesso de tecido comprimido. Em malha de alta elasticidade, a recuperação do tecido absorve o franzido e o volume desaparece ao vestir.  
**Regra:** franzido + `elasticidade = "alta"` = efeito nulo.

### 2.3 base-vestido-drapeado requer fibra fluida obrigatoriamente
A parte "frente com excesso para drapeamento" só funciona se o tecido cede ao peso e forma dobras suaves. Linho, cânhamo, algodão acima de 160 g/m² criam quebras angulares.  
**Mínimo:** 50% de fibra fluida (viscose, seda, lyocell, cupro, chiffon).

### 2.4 base-saia-gode — janela de gramatura estreita para viés
6 cunhas cortadas no viés. Tecidos muito leves (<90 g/m²) torcem durante a costura; tecidos pesados (>200 g/m²) deformam as cunhas pelo próprio peso.  
**Janela:** 120–200 g/m².  
**Incompatíveis:** cashmere pesado, lã tweed ≥ 280 g/m², viscose fina <90 g/m².

### 2.5 base-manga-petala — tecido pesado perde o efeito
Manga pétala/tulipa depende de leveza para ter movimento. Tecidos ≥ 150 g/m² resultam em pétalas estáticas que adicionam volume sem efeito visual.  
**Ideal:** mousseline, chiffon, viscose leve 80–110 g/m².

### 2.6 Blazer/sobretudo — viscose e lyocell não estruturam sem entretela
Fibras fluidas (viscose, lyocell, seda, cupro) não têm memória de forma. Blazer ou sobretudo nessas fibras sem entretela termocolante perde a estrutura de lapelas, frentes e ombros.  
**Obrigatório:** entretela específica por fibra. Viscose requer entretela mais pesada; linho requer entretela própria para linho (evitar amassado).

### 2.7 Sobreposição + tecido transparente sem forro
Moldes base-blusa-transpassada, base-vestido-envelope, base-sobretudo-transpassado têm sobreposição de camadas. Tecidos transparentes/semi-opacos (chiffon, organza, mousseline) revelam o corpo — forro é obrigatório.

### 2.8 base-vestido-tomara / base-calca-pijama — elástico do cós como material separado
A sustentação do "tomara que caia" e o cós da calça pijama dependem de elastano na ribana/elástico, não na fibra do corpo. O corpo pode ser 100% linho, mas o cós precisa ser cadastrado como `PecaMaterial` separado com `funcao = "elastico"`. Omitir isso torna a `composicao_fibras` e o `conteudo_reciclado_pct` do DPP incorretos.

---

## 3. Regras de caimento por fibra

| Fibra | Caimento natural | Incompatível com |
|---|---|---|
| linho | estruturado/médio | caimento fluido |
| canamo | estruturado | caimento fluido |
| pla_biopolimero | médio/rígido | caimento fluido |
| algodao_reciclado | médio (fibra curta) | caimento fluido |
| viscose_modal | fluido | caimento estruturado sem entretela |
| lyocell_tencel | fluido/médio | caimento estruturado sem entretela |
| seda | fluido | caimento estruturado sem forro rígido |
| cupro | fluido | caimento estruturado |
| cashmere (fino) | médio/fluido | compression, activewear |
| la_virgem espessa | estruturado/médio | caimento fluido |

---

## 4. Tabela de gramatura por categoria de peça

| Categoria | g/m² min | g/m² max | Fora da faixa |
|---|---|---|---|
| Blusa/camisa fluida | 60 | 140 | <60 = transparente; >140 = perde caimento |
| Calça plano | 150 | 280 | <150 = transparência ao sentar |
| Saia godê | 120 | 200 | <90 = torce no viés; >200 = deforma cunhas |
| Blazer/casaco | 220 | 420 | <220 = precisa entretela pesada |
| Vestido drapeado | 60 | 130 | >130 = quebra angular, sem drapeado real |
| Manga bufante/pétala | 50 | 100 | >100 = sem movimento |
| Malha fitted (jersey) | 140 | 220 | <130 = transparência; >300 = pesado |
| Legging/compression | 180 | 280 | <160 = sem compressão real |

---

## 5. Regras de blend críticas

### 5.1 Elastano em compression — CO₂ vs. água
Leggings de compressão usam 12–22% de elastano (não 2–8%). Isso inverte o discurso de sustentabilidade:

```
78% poliamida_reciclada + 22% elastano
CO₂ = 0.78 × 7.2 + 0.22 × 26.0 = 11.34 kgCO2e/kg
vs. algodão convencional = 5.9 kgCO2e/kg

MAS: água = 0.78 × 40 + 0.22 × 300 = 97 L/kg
vs. algodão convencional = 10.000 L/kg
```

**Comunicação correta:** o diferencial de activewear reciclado está no consumo hídrico, não no carbono.  
**Flag obrigatório quando:** elastano ≥ 10% no blend.

### 5.2 Algodão reciclado — durabilidade reduzida não declarada
Fibra pós-consumo tem comprimento de 1–2 cm (virgem = 2.5–3.5 cm). Resistência à tração 30–40% menor → pilling acelerado. `durabilidade_ciclos_lavagem` deve ser corrigido:

```
durabilidade_ajustada = durabilidade_base × (1 − 0.007 × %reciclado_algodao)
```

### 5.3 PLA + qualquer fibra — temperatura máxima do blend
PLA degrada ≥ 55°C. A `temperatura_maxima_lavagem` do blend é o mínimo entre todas as fibras:

| Fibra | T máx |
|---|---|
| PLA | 50°C |
| Seda, lã | 30°C |
| Viscose, nylon | 40°C |
| Poliéster | 40–60°C |
| Algodão | 60–95°C |

### 5.4 Algodão + poliéster — fim de vida "reciclável" é incorreto
Separação mecânica de algodão/poliéster existe mas não está disponível em escala no Brasil. Declarar "reciclável" no DPP para esse blend = greenwashing inadvertido. Correto: "Encaminhar para reuso — separação de fibras mistas não disponível em escala BR."

### 5.5 Lã + linho — blend incompatível em calor/vapor
Lã encolhe com calor/vapor; linho não. Blazer ou calça social com esse blend deforma após as primeiras lavagens. O DPP deve exigir lavagem a seco e declarar a incompatibilidade.

---

## 6. Certificações × composição — validações ausentes no modelo

| Certificação | Regra | Violação comum |
|---|---|---|
| GOTS | Máx 30% de fibras não orgânicas (incluindo sintéticos) | Blend com >30% poliéster reciclado + certificação GOTS |
| GRS | Certifica fração reciclada, não a peça inteira | `conteudo_reciclado_pct = 100%` em blend misto |
| OEKO-TEX | Exige teste de substâncias — tingimento não rastreado incompatível | Tingimento convencional sem rastreio de fornecedor |

**Derivação obrigatória:**
```
conteudo_reciclado_pct = Σ (pct_fibra_i) 
  onde fibra_i.categoria ∈ {sintetica_reciclada, natural_reciclada}
```

---

## 7. Refinamentos de indicadores DPP

### 7.1 agua_peca_litros subestimada sem tingimento
Os fatores de `agua_l_por_kg` cobrem apenas produção da fibra. Tingimento adiciona:

| Método | L/kg adicional |
|---|---|
| sem_tingimento | 0 |
| vegetal | 80–180 |
| convencional | 150–350 |

Viscose tingida convencional: 150 (fibra) + 250 (tingimento) = **400 L/kg total** — 167% do declarado hoje.

### 7.2 perda_corte_pct deve variar por tipo de material

| Tipo de material | % perda corte |
|---|---|
| Estruturados (linho, gabardine, lã) | 10–14% |
| Médios (algodão, sarja) | 13–17% |
| Fluidos (viscose, seda, lyocell) | 17–22% |
| Malha sem estabilização | 15–20% |
| Malha com papel estabilizador | 10–14% |

### 7.3 temperatura_maxima_lavagem_c — campo ausente
Campo obrigatório para DPP EU ESPR. Deve ser calculado automaticamente como:
```
temperatura_maxima_lavagem_c = min(T_max_fibra_i) para todas as fibras do blend
```

### 7.4 Hierarquia de confiança dos dados de impacto

| Nível | Descrição | Ação no DPP |
|---|---|---|
| 1 — EPD primária | lyocell_tencel (Lenzing/IBU 2023) | Badge "verificado por EPD" |
| 2 — Calibrado BR | algodão Cerrado, viscose Lenzing BR (meta Frente B) | Badge "dado BR verificado" |
| 3 — Estimativa genérica | Higg MSI / ecoinvent 3.9 | Nota "estimativa" |
| 4 — Literatura sintetizada | cashmere, seda, cânhamo, fibra_coco | **Bloquear publicação pública** — exigir EPD do fornecedor |

### 7.5 Cashmere — confiança "baixa" não captura a severidade
`co2eq = 150 kgCO2e/kg` com amplitude 35–600. Mesmo no limite inferior é a fibra mais impactante do catálogo (107× o lyocell). O DPP não deve ser publicado sem EPD primária do fornecedor.

---

## 8. Lacunas estruturais do modelo

| Gap | Impacto | Solução |
|---|---|---|
| Nenhum `MoldeBase` para activewear/compression | Base_id ausente para legging, top esportivo, body | Criar bases-legging-alta, base-top-esportivo |
| `MEDIDAS_FEM_MALHA_*` só cobre 36–46 | Plus size em malha sem medida de referência | Estender tabela até 62 para malha média e alta |
| `reducao_elastica_pct` sem vínculo à composição | Molde com redução sem fibra elástica passa sem alerta | Validação cruzada FichaTecnica.composicao_fibras |
| `perda_corte_pct` como valor único | Tecidos fluidos subestimam área perdida em ~8pp | Derivar automaticamente por tipo de material |
| `tingimento` não integrado ao cálculo de água | `agua_peca_litros` incompleto | Adicionar fator de água de tingimento no catálogo |
| `temperatura_maxima_lavagem_c` ausente | Durabilidade declarada pode ser irreal | Campo derivado do blend (mínimo T_max das fibras) |
| `requer_forro` não existe no modelo | Sobreposição + transparência sem alerta | Campo booleano derivado de molde + opacidade do material |
