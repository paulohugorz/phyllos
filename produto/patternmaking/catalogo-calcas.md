# Catalogo de Calcas PHYLLOS — 50 Bases Parametrizadas

Versao: 1.0
Data: 2026-06-11
Responsavel: Motor de Moldes PHYLLOS
Referencia de formato: `docs/patternmaking/calca-performance-alfaiataria-molde-v0.md`
Referencia de modelagem: `references/patternmaking-construction-techniques-marlene-mukai.md`

---

## Como usar este catalogo

Cada entrada e uma arquitetura parametrizada, nao um molde pronto. O motor usa esses modelos como ponto de partida quando o usuario descreve uma peca em linguagem natural.

Formula de medida final valida para todas as bases:

```
medida_final = corpo + folga_vestibilidade + folga_movimento - reducao_elastica
```

Tolerancia padrao: +/- 0,7 cm em curvas; +/- 0,5 cm em retas.
Corpo-base: tamanho M, altura 168 cm (feminino) / 175 cm (masculino).

---

## GRUPO 1 — Calcas de Alfaiataria e Social

---

### CALC-001 — Calca Reta Classica de Alfaiataria

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** reta social
**Silhueta e fit:** regular — folga equilibrada em todos os segmentos; perna cai em linha reta do quadril a barra

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta | 72 cm | +4 cm | +2 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +4 cm |
| Coxa alta | 58 cm | +7 cm | +4 cm | +6 cm |
| Joelho | 39 cm | +9 cm | +6 cm | +8 cm |
| Barra | 24 cm | +9 cm | +6 cm | +8 cm |
| Profundidade gancho | 27 cm | +1,5 cm | +0,5 cm | +1 cm |
| Entreperna | 76 cm | 0 | 0 | 0 |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Altura de cintura | `media / alta / muito alta` | move linha de cintura -2 / 0 / +4 cm da cintura natural |
| Abertura de barra | `tubo 48 cm / reta 50 cm / levemente alargada 54 cm` | redimensiona pontos de barra e joelho |
| Fechamento | `braguilha frente / ziper lateral / elastico embutido costas` | altera gancho frente e cos |
| Pence frente | `sem pence / uma pence / duas pregas` | adiciona volume controlado na frente |
| Bolso | `faca / americana / sem bolso` | adiciona paineis de bolso e recorte |
| Cos | `liso plano / anatomico levemente curvado / embutido` | muda forma e altura do cos |

#### Transformacoes de design

1. Adicionar yoke de recorte horizontal nas costas a 8 cm abaixo da cintura, separando painel superior do painel de perna — cria linha visual de alfaiataria italiana.
2. Incluir pregas abertas na frente (2 pregas de 2 cm cada) para versao masculina com volume classico no cós.

#### Observacao tecnica

Perna reta exige alinhamento preciso da linha de fio vertical com o eixo da perna; qualquer desvio de mais de 1,5 cm causa torcao visivel apos lavagem. O cos anatomico levemente curvado absorve a diferenca cintura-quadril sem necessidade de pence profunda.

---

### CALC-002 — Calca Slim de Alfaiataria

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** slim social
**Silhueta e fit:** slim — coxa ajustada com folga reduzida; barra estreita sem comprimir; aparencia de corte preciso

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta | 72 cm | +3 cm | +1,5 cm | +2 cm |
| Quadril | 100 cm | +4 cm | +2 cm | +3 cm |
| Coxa alta | 58 cm | +4 cm | +2 cm | +3 cm |
| Joelho | 39 cm | +6 cm | +4 cm | +5 cm |
| Barra | 24 cm | +5 cm | +3 cm | +4 cm |
| Profundidade gancho | 27 cm | +1,5 cm | +0,5 cm | +1 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Grau de slim | `slim moderado / slim preciso / semi-skinny` | varia folga de coxa de +4 cm a +1,5 cm |
| Barra | `barra reta 34 cm / barra afunilada 30 cm / barra cortada` | redimensiona ponto de barra |
| Tecido | `plano com elastano / linho estruturado / gabardine` | ajusta folga e orientacao de fio |
| Fechamento | `braguilha discreta / ziper lateral / elastico parcial costas` | altera gancho frente |

#### Transformacoes de design

1. Transformar em slim cropped com barra de tornozelo visivel (comprimento lateral 96 cm) — efeito de alfaiataria contemporanea.
2. Inserir recorte vertical de painel na lateral da perna com tecido contrastante, correndo do joelho a barra — detalhe de design sem alterar silhueta.

#### Observacao tecnica

Em tecido plano sem elastano, folga minima de coxa de +6 cm e obrigatoria para sentar sem tensao. Com elastano 5-8%, aceita ate +3 cm. O gancho precisa ser validado sentado antes do corte final.

---

### CALC-003 — Calca Wide Leg de Alfaiataria

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** wide leg formal
**Silhueta e fit:** relaxed — coxa e perna com volume generoso; queda reta a partir do quadril; efeito clean e alongado

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta | 72 cm | +4 cm | +2 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +5 cm |
| Coxa alta | 58 cm | +14 cm | +10 cm | +12 cm |
| Joelho | 39 cm | +19 cm | +16 cm | +17 cm |
| Barra | 24 cm | +26 cm | +22 cm | +24 cm |
| Profundidade gancho | 27 cm | +2 cm | +1 cm | +1,5 cm |

Barra pronta referencia: 50-56 cm (total por perna, somando frente e costas).

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Abertura de barra | `wide 50 cm / extra wide 56 cm / palazzo 64 cm` | expande barra e joelho proporcionalmente |
| Altura de cintura | `media / alta` | reposiciona origem do molde |
| Volume de queda | `leve / acentuado` | controla folga entre quadril e joelho |
| Pregas frente | `sem prega / 1 prega aberta / 2 pregas` | distribui o volume na cintura |

#### Transformacoes de design

1. Adicionar 2 pregas abertas na frente (1,5 cm cada) que partem do cos e se abrem ao longo da perna — transforma em wide leg com volume classico masculino.
2. Encurtar para comprimento cropped (comprimento lateral 92 cm, barra visivel sobre o calcado) — detalhe de alfaiataria contemporanea.

#### Observacao tecnica

Com barra acima de 52 cm, a linha de fio precisa ser perfeitamente vertical — qualquer torcao e amplificada pelo volume. Tecidos com caimento (crepe, viscose, gabardine leve) funcionam melhor que tecidos encorpados sem elasticidade. Bainha invisivel ou virada simples de 3 cm.

---

### CALC-004 — Palazzo

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** palazzo fluido
**Silhueta e fit:** oversized — perna muito ampla com queda vertical fluida; silhueta que ignora o contorno da perna

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura | 72 cm | +4 cm | +2 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +5 cm |
| Coxa alta | 58 cm | +22 cm | +18 cm | +20 cm |
| Barra | 24 cm | +36 cm | +32 cm | +34 cm |

Barra pronta referencia: 60-70 cm por perna, visualmente similar a saia dividida.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Abertura de barra | `palazzo 60 cm / palazzo maxi 70 cm` | expande barra uniformemente |
| Cintura | `elastico total / cos liso / cos franzido` | altera painel de cos e abertura |
| Comprimento | `midi (102 cm) / maxi (112 cm)` | estende comprimento lateral |
| Fechamento | `lateral invisivel / elastico embutido / amarracao` | define posicao do fechamento |

#### Transformacoes de design

1. Inserir recorte horizontal na altura do joelho criando dois paineis — efeito de calca wide leg com yoke de perna.
2. Transformar em palazzo de cintura franzida com elastico total e fio de amarracao — versao beach/resort.

#### Observacao tecnica

Palazzo de tecido plano exige entretela no cos para evitar franzido de cintura. Tecidos recomendados: chiffon pesado, crepe de viscose, charmeuse, crepe georgette. Evitar tecidos que avolumam (jersey encorpado, moletom) — perdem o caimento fluido.

---

### CALC-005 — Cigarrete

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** cigarrete classica
**Silhueta e fit:** slim-regular — ajustada na coxa, reta e estreita; barra no tornozelo; visual de alfaiataria anos 50-60

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura | 72 cm | +3 cm | +1,5 cm | +2,5 cm |
| Quadril | 100 cm | +4 cm | +2 cm | +3 cm |
| Coxa alta | 58 cm | +5 cm | +3 cm | +4 cm |
| Joelho | 39 cm | +5 cm | +3 cm | +4 cm |
| Barra | 24 cm | +5 cm | +3 cm | +4 cm |
| Comprimento lateral | 96 cm | — | — | — |

Barra pronta referencia: 29-32 cm por perna — cano estreito e uniforme.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `na canela 90 cm / tornozelo 96 cm / ligeiramente acima 92 cm` | muda comprimento lateral |
| Fenda lateral na barra | `sem fenda / fenda 6 cm / fenda 10 cm` | adiciona abertura na lateral da barra |
| Fechamento | `ziper lateral / braguilha / elastico costas` | altera gancho frente |
| Bolso | `sem bolso / faca discreta / americana` | adiciona painel de bolso |

#### Transformacoes de design

1. Adicionar fenda costas de 8 cm na barra para mobilidade sem alterar silhueta — essencial em tecido sem elastano.
2. Transformar em cigarrete com cinto integrado — cos com passante e cinto do mesmo tecido para efeito de look completo.

#### Observacao tecnica

Barra estreita sem elastano precisa de fenda obrigatoria para mobilidade de subida de escadas. Sem fenda, o usuario e limitado a passos curtos. Fenda lateral e mais discreta; fenda costas e mais funcional.

---

### CALC-006 — Calca Cropped de Alfaiataria

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** cropped social
**Silhueta e fit:** regular — perna reta com comprimento encurtado intencional (tornozelo a meio canela); visual contemporaneo

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta | 72 cm | +4 cm | +2 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +4 cm |
| Coxa alta | 58 cm | +7 cm | +4 cm | +6 cm |
| Joelho | 39 cm | +9 cm | +6 cm | +8 cm |
| Barra | 24 cm | +9 cm | +6 cm | +8 cm |
| Comprimento lateral | 90-98 cm | — | — | — |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `acima do tornozelo 90 cm / tornozelo alto 94 cm / 3/4 80 cm` | ajusta comprimento lateral |
| Acabamento de barra | `bainha virada 3 cm / barra cortada vivo / dobrada e pesponto` | define acabamento inferior |
| Perna | `reta / levemente afunilada` | redimensiona barra em relacao ao joelho |

#### Transformacoes de design

1. Transformar em cropped com barra virada para fora (dobra de 5 cm visivel) — efeito de alfaiataria casual.
2. Adicionar abertura lateral de 4 cm na barra com caseado e botao de pressao — detalhe funcional e visual.

#### Observacao tecnica

O comprimento cropped expoe o tornozelo; a barra precisa ser perfeitamente paralela ao chao. Diferenca de mais de 3 mm entre os lados e visivelmente perceptivel. Bainha final sempre apos o piloto com calcado definitivo.

---

### CALC-007 — Bootcut de Alfaiataria

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** bootcut social
**Silhueta e fit:** regular — ajustada na coxa e joelho; abertura leve na barra a partir do joelho; equilibra volume de bota

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta | 72 cm | +4 cm | +2 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +4 cm |
| Coxa alta | 58 cm | +6 cm | +3 cm | +5 cm |
| Joelho | 39 cm | +7 cm | +5 cm | +6 cm |
| Barra | 24 cm | +14 cm | +10 cm | +12 cm |

Barra pronta referencia: 38-42 cm por perna — abertura comeca 12-15 cm acima da barra.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Grau de abertura | `leve 38 cm / moderado 42 cm / bootcut generoso 46 cm` | expande barra mantendo joelho fixo |
| Inicio da abertura | `12 cm acima da barra / 15 cm / 20 cm` | determina ponto no molde onde a perna começa a alargar |
| Comprimento | `padrao 106 cm / longo 110 cm` | ajusta para cobertura total do calcado |

#### Transformacoes de design

1. Transformar em bootcut com painel de vivo de 1 cm na costura lateral da perna — detalhe que define e acentua a abertura.
2. Adicionar entretela na barra para sustentacao do caimento sobre o calcado sem franzir.

#### Observacao tecnica

A abertura da barra deve comecar exatamente na linha do joelho ou abaixo — acima do joelho transforma em flare. A proporcao da abertura deve ser simetrica entre frente e costas (mesmo aumento em ambos os lados).

---

### CALC-008 — Flare de Alfaiataria

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** flare social
**Silhueta e fit:** regular-relaxed — ajustada ate o joelho; a partir do joelho a perna se abre em forma de sino; amplitude maior que bootcut

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta | 72 cm | +4 cm | +2 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +4 cm |
| Coxa alta | 58 cm | +6 cm | +3 cm | +5 cm |
| Joelho | 39 cm | +8 cm | +5 cm | +7 cm |
| Barra | 24 cm | +24 cm | +20 cm | +22 cm |

Barra pronta referencia: 48-54 cm — abertura em sino a partir do joelho.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Amplitude da barra | `moderado 48 cm / flare 54 cm / maxi flare 60 cm` | expande barra com ponto de joelho fixo |
| Inicio da abertura | `no joelho / 5 cm acima do joelho` | define onde a curva de abertura comeca |
| Comprimento | `padrao 106 cm / longo com volume no chao 112 cm` | barra longa acentua o efeito sino |

#### Transformacoes de design

1. Transformar em flare com corte em vies na barra — a diagonal cria movimento natural no caimento e dispensa bainha reta.
2. Inserir painel de contraste (renda, jacquard, couro vegetal) nos ultimos 20 cm da perna — efeito de statement na barra.

#### Observacao tecnica

Flare exige tecido com caimento — gabardine fluida, crepe pesado, viscose estruturada. Tecidos rigidos criam volume de balao, nao de sino. Bainha em vies precisa de pelo menos 24h de repouso suspenso antes do corte final para acomodar o caimento.

---

### CALC-009 — Paperbag (Cintura com Franzido)

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** paperbag com amarracao
**Silhueta e fit:** relaxed na cintura; regular a slim na perna; cintura franzida acima da natural com cinto ou amarracao

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura franzida (amassada) | 72 cm | +14 cm | +10 cm | +12 cm |
| Quadril | 100 cm | +6 cm | +3 cm | +5 cm |
| Coxa alta | 58 cm | +6 cm | +4 cm | +5 cm |
| Joelho | 39 cm | +8 cm | +5 cm | +7 cm |
| Barra | 24 cm | +8 cm | +5 cm | +7 cm |
| Cos franzido altura | +8 cm acima da cintura natural | — | — | — |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Altura do franzido | `6 cm / 8 cm / 10 cm acima da natural` | altera a altura do cos franzido |
| Cinto | `elastico embutido + cinto do tecido / elastico puro / passantes` | define painel de cos |
| Perna | `reta / afunilada / cigarrete` | redimensiona barra e joelho |
| Bolso | `sem bolso / faca / embutido na costura lateral` | adiciona painel de bolso |

#### Transformacoes de design

1. Transformar em paperbag cropped com perna afunilada — silhueta de alfaiataria moderna e descontraida.
2. Adicionar bolsos laterais de ressalto no franzido da cintura — detalhe funcional que amplifica o volume do franzido.

#### Observacao tecnica

O cos franzido exige tecido leve com caimento — tecidos rigidos criam volume excessivo na cintura. O cinto deve ser cortado na mesma peca de tecido ou em contraste; largura de 3-4 cm com bordas acabadas. Elastico de 2,5 cm no canal embutido do cos.

---

### CALC-010 — Calca de Pregas (Pleated Trouser)

**Familia:** inferior / calca / alfaiataria
**Subfamilia:** social com pregas
**Silhueta e fit:** relaxed — volume generoso na cintura via pregas; perna reta que estreita levemente na barra; classico masculino e alfaiataria italiana

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura alta (antes de pregas) | 72 cm | +4 cm | +2 cm | +3 cm |
| Volume de pregas total | +8 a +12 cm | — | — | — |
| Quadril | 100 cm | +8 cm | +5 cm | +7 cm |
| Coxa alta | 58 cm | +10 cm | +6 cm | +8 cm |
| Joelho | 39 cm | +9 cm | +6 cm | +8 cm |
| Barra | 24 cm | +9 cm | +6 cm | +8 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Numero de pregas | `1 prega por lado / 2 pregas por lado` | adiciona 3-4 cm por prega ao cos |
| Direcao de preca | `preguicosa para dentro / preguicosa para fora` | define direcao de dobragem no molde |
| Profundidade de preca | `1 cm / 1,5 cm / 2 cm de dobra` | define o volume a partir do cos |
| Perna | `reta / levemente afunilada para barra` | redimensiona barra |

#### Transformacoes de design

1. Transformar em calca de pregas com cinto passado em argolas metalicas — detalhe de alfaiataria masculina contemporanea.
2. Adicionar painel de forro total em bemberg — necessario quando o tecido e muito rigido para o conforto.

#### Observacao tecnica

Pregas devem ser presas no cos e libertas logo abaixo (3-4 cm) para criarem volume natural. Pregas costuradas ate o joelho viram pince e mudam o efeito visual. A largura da entreperna deve acompanhar o volume das pregas para nao perder o caimento.

---

## GRUPO 2 — Calcas de Performance e Esporte

---

### CALC-011 — Jogger Refinada

**Familia:** inferior / calca / performance
**Subfamilia:** jogger social-esportivo
**Silhueta e fit:** relaxed na coxa; afunilado no tornozelo; puno elastico; visual entre academia e rua

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga malha | Folga tecnico 4 vias | Reducao elastica |
|---|---:|---:|---:|---:|
| Cintura (cos elastico) | 74 cm | +2 cm | 0 | -8 a -10 cm |
| Quadril | 100 cm | +6 cm | +3 cm | 0 |
| Coxa alta | 58 cm | +6 cm | +3 cm | 0 |
| Joelho | 39 cm | +7 cm | +4 cm | 0 |
| Tornozelo (acima puno) | 26 cm | +3 cm | +2 cm | 0 |
| Puno barra | 24 cm | +1 cm | 0 | -5 a -7 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Largura da perna | `slim jogger / regular / relaxed` | folga de coxa de +4 a +8 cm |
| Altura de cos | `6 cm / 8 cm / 10 cm` | muda altura do painel de cos |
| Cord | `sem cord / cord de ajuste frente` | adiciona casa de cord no cos |
| Bolso | `sem bolso / lateral oculto / ziper lateral` | adiciona painel e recorte |
| Puno | `puno 8 cm / puno 10 cm / sem puno barra reta` | altera painel de barra |

#### Transformacoes de design

1. Inserir painel lateral de tecido plano contrastante de 8 cm de largura, correndo da cintura ao puno — efeito track pant premium.
2. Adicionar gusset triangular de 4 vias na entreperna para mobilidade maxima em agachamento.

#### Observacao tecnica

O puno elastico precisa ter comprimento de molde igual ao tornozelo do corpo mais 1 cm — a reducao elastica garante ajuste. Puno de malha de ribana de 2x2 e mais duravel que tubular. O gusset de entreperna alonga em 1 cm a profundidade de gancho, o que precisa ser compensado no molde.

---

### CALC-012 — Legging Lisa

**Familia:** inferior / calca / performance
**Subfamilia:** legging compressao leve
**Silhueta e fit:** fitted — segue o contorno do corpo com folga minima ou negativa; define musculatura; comprimento ate o tornozelo

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga malha 2 vias | Folga tecnico 4 vias | Reducao elastica |
|---|---:|---:|---:|---:|
| Cintura (cos dobrado) | 74 cm | -2 cm | -4 cm | — |
| Quadril | 100 cm | -2 cm | -4 cm | — |
| Coxa alta | 58 cm | -2 cm | -4 cm | — |
| Joelho | 39 cm | -1 cm | -3 cm | — |
| Tornozelo | 24 cm | 0 | -1 cm | — |

Regra: legging de tecnico 4 vias com compressao leve usa reducao direta na medida do molde. Barra acabada em bico ou virada simples de 1 cm.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Nivel de compressao | `compressao leve / compressao moderada / compressao forte` | varia reducao de -2 cm a -6 cm no quadril e coxa |
| Cos | `cos dobrado 3 cm / cos embutido 5 cm / cos alto 8 cm` | altera altura do painel de cos |
| Acabamento de barra | `barra reta / barra em bico / barra aberta` | define contorno inferior |
| Textura | `liso / com recorte de costura decorativa / com painel de mesh` | adiciona paineis de detalhe |

#### Transformacoes de design

1. Adicionar painel de mesh perfurado na lateral da coxa (8 cm de largura) para ventilacao e efeito visual.
2. Inserir recorte de painel em contraste com costura de topstitch na entreperna e gluteo — detalhe de linha atlética.

#### Observacao tecnica

Legging sem costura lateral (circular knit) elimina o risco de torcao mas exige maquinario especifico. Legging com costura lateral precisa de margem de 0,8 cm e costura de overlock com elasticidade. A linha de fio deve ser vertical no centro da perna — desvio causa torcao visivel ao vestir.

---

### CALC-013 — Legging com Bolso

**Familia:** inferior / calca / performance
**Subfamilia:** legging funcional
**Silhueta e fit:** fitted — identica a legging lisa com adicao de bolso funcional sem deformar silhueta

#### Medidas-chave e folgas por tipo de tecido

Identicas a CALC-012 (Legging Lisa). O bolso e adicionado sem alterar as medidas principais.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Posicao do bolso | `quadril lateral / coxa lateral / costas cintura` | define regiao de insercao do painel de bolso |
| Tamanho do bolso | `celular (18x10 cm) / mini (10x8 cm) / ziper costas (20x5 cm)` | define dimensoes do painel |
| Numero de bolsos | `1 bolso / 2 bolsos laterais / bolso + ziper costas` | adiciona paineis independentes |
| Fechamento do bolso | `elastico de abertura / ziper oculto / abertura livre` | define acabamento da boca do bolso |

#### Transformacoes de design

1. Adicionar bolso de telefone na lateral direita da coxa com aba de fecho por velcro — bolso de corrida funcional.
2. Inserir bolso de ziper embutido no cos costas (5 cm x 10 cm) — para chave e cartao, invisivel de frente.

#### Observacao tecnica

O bolso lateral nao pode ficar na costura lateral pois a margem de costura comprometeria o acabamento. O painel de bolso deve ser cortado em tecido mais firme que o corpo da legging para manter a boca aberta sem franzir.

---

### CALC-014 — Legging de Compressao

**Familia:** inferior / calca / performance
**Subfamilia:** legging compressao forte
**Silhueta e fit:** compressao — reducao ativa de circunferencia para suporte muscular; uso em corrida, ciclismo, musculacao

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecnico 4 vias compressao |
|---|---:|---:|
| Cintura (cos largo) | 74 cm | -5 cm |
| Quadril | 100 cm | -5 cm |
| Coxa alta | 58 cm | -5 cm |
| Joelho | 39 cm | -4 cm |
| Tornozelo | 24 cm | -2 cm |

Reducao gradual do tornozelo para cima — compressao progressiva do tornozelo ao quadril.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Nivel de compressao | `leve 15-20 mmHg / moderado 20-30 mmHg / forte 30-40 mmHg` | define percentual de reducao por regiao |
| Cos | `cos largo de compressao 10 cm / cos alto 14 cm` | painel de cos com entretela elastica |
| Painel de compressao | `uniforme / gradual progressivo` | varia reducao por zona no molde |
| Acabamento de barra | `barra fechada / barra com ponteira de polegar` | adiciona alcas se necessario |

#### Transformacoes de design

1. Inserir painel de compressao diferenciada no gluteo e posterior da coxa para efeito de suporte postural.
2. Adicionar painel reflexivo (tecido reflexivo) na lateral da perna para uso noturno e corrida urbana.

#### Observacao tecnica

Tecido de compressao exige conhecimento da curva tensao-alongamento antes de definir o molde. A reducao de -5 cm em quadril de 100 cm assume elasticidade de 60-70% no eixo de trama. Prova fisica obrigatoria antes de produzir grade.

---

### CALC-015 — Calca 3/4 de Performance

**Familia:** inferior / calca / performance
**Subfamilia:** capri / 3/4 esportivo
**Silhueta e fit:** fitted a regular — comprimento abaixo do joelho; aberto ou com puno; para treino e atividade ao ar livre

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga malha | Folga tecnico 4 vias |
|---|---:|---:|---:|
| Cintura (elastico) | 74 cm | +2 cm | 0 |
| Quadril | 100 cm | +4 cm | +2 cm |
| Coxa alta | 58 cm | +4 cm | +2 cm |
| Joelho | 39 cm | +5 cm | +3 cm |
| Barra 3/4 (abaixo do joelho) | — | +4 cm | +2 cm |
| Comprimento lateral | 68-75 cm | — | — |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `3/4 classico 70 cm / capri 65 cm / joelho+ 60 cm` | muda comprimento lateral |
| Acabamento de barra | `barra aberta / puno elastico 6 cm / barra em bico` | define painel de barra |
| Bolso | `sem bolso / lateral de celular / ziper costas` | adiciona painel |
| Cos | `cos de 6 cm / cos alto de 10 cm` | altera altura do painel de cos |

#### Transformacoes de design

1. Transformar em 3/4 com painel de mesh lateral da coxa ao joelho — ventilacao para treino de verão.
2. Adicionar corda de amarracao na abertura da barra para regulagem de largura — efeito jogger 3/4.

#### Observacao tecnica

O ponto de barra do 3/4 no molde deve ser validado com o usuario de pe e em movimento — o comprimento aparente varia conforme altura e proporcao de canela. Comprimento de 70 cm lateral e referencia para altura 168 cm.

---

### CALC-016 — Cargo Tecnica de Performance

**Familia:** inferior / calca / performance
**Subfamilia:** cargo funcional tecnico
**Silhueta e fit:** regular — perna reta com folga de movimento; multiplos bolsos funcionais; construcao para atividade outdoor e urbana

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecnico plano DWR | Folga tecnico 4 vias |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | +2 cm |
| Quadril | 100 cm | +8 cm | +5 cm |
| Coxa alta | 58 cm | +8 cm | +5 cm |
| Joelho | 39 cm | +10 cm | +7 cm |
| Barra | 24 cm | +8 cm | +5 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Numero de bolsos | `4 bolsos / 6 bolsos / 8 bolsos` | adiciona paineis por regiao |
| Tipo de bolso | `cargo lateral / ziper / faca / ressalto` | define construcao de cada bolso |
| Ajuste de barra | `sem ajuste / velcro / cord de ajuste` | adiciona regulagem no painel de barra |
| Joelheira | `sem joelheira / painel de joelheira com bolso interno` | adiciona painel estruturado no joelho |

#### Transformacoes de design

1. Adicionar painel de reforco em ripstop na zona de joelho e entreperna — durabilidade para trilha e escalada urbana.
2. Inserir ziper lateral de ventilacao da coxa ao joelho (ziper de 30 cm) — transformacao para short quando necessario.

#### Observacao tecnica

Bolsos de cargo lateral (ressalto) adicionam 3-5 cm de largura visual na coxa. O painel de bolso deve ser preso no cos e na costura lateral — solto na parte inferior para o bolso abrir. Reforco com entretela de gramatura 80-100 g/m2 nas zonas de alta tensao.

---

### CALC-017 — Calca Windbreaker

**Familia:** inferior / calca / performance
**Subfamilia:** windbreaker / corta-vento inferior
**Silhueta e fit:** regular a relaxed — tecido plano leve com tratamento DWR ou membrana; forro leve opcional; visual athleisure funcional

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecnico plano | Reducao elastica (cos e barra) |
|---|---:|---:|---:|
| Cintura (cos elastico) | 74 cm | +2 cm | -8 cm |
| Quadril | 100 cm | +6 cm | 0 |
| Coxa alta | 58 cm | +6 cm | 0 |
| Joelho | 39 cm | +8 cm | 0 |
| Barra (puno elastico) | 24 cm | +2 cm | -5 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Perno | `puno na barra / barra reta / barra com velcro` | altera painel de barra |
| Forro | `sem forro / forro de malha seca / forro de polar leve` | adiciona painel de forro independente |
| Ziper lateral | `sem ziper / ziper parcial 30 cm / ziper total` | adiciona abertura lateral completa |
| Bolso | `bolso ziper lateral / bolso embutido / sem bolso` | adiciona painel e recorte |

#### Transformacoes de design

1. Adicionar ziper lateral total de cintura a barra em ambas as pernas — transformacao em calca tracksuit com abertura lateral.
2. Inserir forro de polar removivel por ziper embutido — versao 3 em 1 (windbreaker + polar + ambos).

#### Observacao tecnica

Tecido windbreaker (nylon plano, tafeta) nao tem elasticidade — folgas devem ser mais generosas. Cos e barra com elastico sao obrigatorios para funcionalidade. Costura externa (flat-felled seam) recomendada para impermeabilidade e durabilidade.

---

### CALC-018 — Calca de Trail Running

**Familia:** inferior / calca / performance
**Subfamilia:** trail / corrida off-road
**Silhueta e fit:** regular-fitted — articulada em joelho e gancho; leve e resistente; minimos bolsos funcionais; mobilidade maxima

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecnico 4 vias | Observacao |
|---|---:|---:|---|
| Cintura (cos largo) | 74 cm | 0 | cos de 8 cm com cord |
| Quadril | 100 cm | +3 cm | gusset de quadril opcional |
| Coxa alta | 58 cm | +3 cm | |
| Joelho | 39 cm | +5 cm | painel articulado |
| Barra | 24 cm | +3 cm | puno ou velcro |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Gusset de quadril | `sem gusset / gusset triangular / gusset losango` | insere painel de 4 vias entre coxa e gancho |
| Painel articulado de joelho | `sem painel / painel de mobilidade` | insere recorte pre-curvado no joelho |
| Acabamento de barra | `velcro ajustavel / puno slim / barra aberta` | define painel de barra |

#### Transformacoes de design

1. Adicionar painel ventilado de mesh nas costas da coxa do joelho ao gancho — area de maior calor em corrida.
2. Inserir refletivo integrado no painel lateral (tecido reflexivo nos ultimos 20 cm da barra) para seguranca noturna.

#### Observacao tecnica

O painel articulado de joelho e cortado com pre-curva (molde com curvatura de 10 graus no eixo do joelho) para que a calca ja tenha a forma do joelho em movimento. Sem pre-curva, a calca puxa para tras ao correr.

---

### CALC-019 — Calca de Ciclismo (Bib Opcional)

**Familia:** inferior / calca / performance
**Subfamilia:** ciclismo / bike
**Silhueta e fit:** compressao — ajustada ao corpo em posicao de pedal; forro de chamois no assento; comprimento tornozelo ou 3/4

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecnico 4 vias compressao |
|---|---:|---:|
| Cintura (cos largo) | 74 cm | -3 cm |
| Quadril | 100 cm | -3 cm |
| Coxa alta | 58 cm | -3 cm |
| Joelho | 39 cm | -2 cm |
| Tornozelo | 24 cm | -1 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Chamois | `sem chamois / chamois embutido / chamois removivel` | adiciona painel de assento acolchoado |
| Bib (suspensorio) | `sem bib / bib integrado` | adiciona painel de suspensorio que sobe ao ombro |
| Comprimento | `tornozelo / 3/4 / short de ciclismo` | altera comprimento lateral |
| Silicone anti-escorregamento | `sem silicone / faixa de silicone na barra` | adiciona acabamento na barra |

#### Transformacoes de design

1. Transformar em short de ciclismo com chamois e bib — versao masculina classica de competicao.
2. Adicionar painel de aerogrid perfurado na parte superior da coxa anterior — ventilacao sem comprometer compressao.

#### Observacao tecnica

O chamois de assento precisa ser posicionado no molde considerando a postura de pedal (quadril flexionado), nao a postura de pe. O painel de assento deve ter mais comprimento entre as pernas quando o usuario esta curvado na bicicleta.

---

### CALC-020 — Calca de Ginastica / Academia

**Familia:** inferior / calca / performance
**Subfamilia:** ginastica funcional
**Silhueta e fit:** fitted a regular — confortavel para multiatividade (funcional, yoga, pilates, musculacao); cobertura total sem restringir

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga malha leve | Folga tecnico 4 vias |
|---|---:|---:|---:|
| Cintura (cos alto) | 74 cm | +1 cm | -1 cm |
| Quadril | 100 cm | +2 cm | 0 |
| Coxa alta | 58 cm | +3 cm | +1 cm |
| Joelho | 39 cm | +4 cm | +2 cm |
| Tornozelo | 24 cm | +2 cm | +1 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Altura de cos | `cos medio 6 cm / cos alto 8 cm / cos muito alto 12 cm` | muda painel de cos |
| Textura | `liso / com costura decorativa / painel recortado` | adiciona detalhes visuais sem alterar forma |
| Gusset | `sem gusset / gusset de mobilidade 4 vias` | insere painel triangular no entreperna |
| Acabamento | `barra reta / barra em bico / puno fino` | define acabamento inferior |

#### Transformacoes de design

1. Adicionar recorte de painel em contraste formando recorte de seta no gluteo — detalhe visual popular em legging de academia.
2. Transformar em calca de yoga com barra alargada (boot-yoga) — barra de 40 cm para movimento fluido.

---

## GRUPO 3 — Calcas Casuais e Streetwear

---

### CALC-021 — Baggy

**Familia:** inferior / calca / casual
**Subfamilia:** baggy streetwear
**Silhueta e fit:** oversized — muito volume na coxa e perna; cintura baixa ou media; volume cai reto sem afunilar

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga tecnico |
|---|---:|---:|---:|
| Cintura (media/baixa) | 74 cm | +4 cm | +3 cm |
| Quadril | 100 cm | +12 cm | +10 cm |
| Coxa alta | 58 cm | +18 cm | +15 cm |
| Joelho | 39 cm | +18 cm | +15 cm |
| Barra | 24 cm | +16 cm | +13 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Altura de cintura | `baixa (sobre o osso do quadril) / media` | move a linha de cintura para baixo |
| Volume de perna | `baggy moderado / baggy maximo` | folga de coxa de +16 a +20 cm |
| Barra | `barra reta / virada para cima / puno largo` | define acabamento inferior |
| Bolso | `faca / cargo lateral / sem bolso` | adiciona painel de bolso |

#### Transformacoes de design

1. Transformar em baggy com yoke de recorte nas costas (5 cm abaixo da cintura) e bolso de cargo lateral — efeito skateboard classico.
2. Adicionar barra com puno de jersey de 5 cm em contraste — hibrido baggy-jogger.

#### Observacao tecnica

A diferenca de volume entre cintura e quadril em baggy e extrema. O molde precisa de pences ou pregas no cos para absorver esta diferenca sem franze nao intencional. Alternativa: elastico parcial no cos costas para ajuste.

---

### CALC-022 — Cargo Multi-Bolso

**Familia:** inferior / calca / casual
**Subfamilia:** cargo urbano
**Silhueta e fit:** regular a relaxed — perna reta com volume generoso; 4 a 8 bolsos funcionais; construcao robusta

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano/canvas | Folga tecnico |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | +3 cm |
| Quadril | 100 cm | +8 cm | +6 cm |
| Coxa alta | 58 cm | +8 cm | +6 cm |
| Joelho | 39 cm | +10 cm | +8 cm |
| Barra | 24 cm | +8 cm | +6 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Numero de bolsos | `4 / 6 / 8 bolsos` | adiciona paineis por zona |
| Tipo de fechamento de bolso | `botao de pressao / velcro / ziper / aberto` | define acabamento de cada bolso |
| Material de reforco | `reforcado com ripstop / canvas standard / sem reforco` | define camadas no joelho e assento |
| Ajuste de barra | `barra reta / dobrada / velcro de ajuste` | adiciona regulagem |

#### Transformacoes de design

1. Adicionar D-ring metalico em multiplos pontos da calca — versao tactical/workwear com pontos de fixacao.
2. Transformar em cargo com abertura ziper total na lateral direita — perna pode ser removida para virar short.

#### Observacao tecnica

Bolso de cargo lateral em ressalto: o painel do bolso deve ser 1 cm mais largo que o corpo da calca por baixo para que o bolso caia naturalmente quando cheio, sem puxar a lateral para fora.

---

### CALC-023 — Biker / Moto

**Familia:** inferior / calca / casual
**Subfamilia:** biker urbano
**Silhueta e fit:** slim a fitted — muito ajustada na coxa; detalhe de ziper nos tornozelos; estilo moto-inspirado; visual de couro ou tecido estruturado

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano estruturado | Folga malha pesada |
|---|---:|---:|---:|
| Cintura media | 74 cm | +2 cm | +1 cm |
| Quadril | 100 cm | +3 cm | +2 cm |
| Coxa alta | 58 cm | +3 cm | +2 cm |
| Joelho | 39 cm | +4 cm | +3 cm |
| Tornozelo | 24 cm | +1 cm | 0 |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Ziper de tornozelo | `sem ziper / ziper lateral 8 cm / ziper angular 12 cm` | adiciona abertura no painel de barra |
| Detalhe de painel | `perna lisa / recorte de quilting / recorte moto lateral` | adiciona paineis decorativos |
| Material | `couro vegetal / denim / canvas encorpado / malha pesada` | ajusta folgas conforme rigidez |
| Fechamento | `ziper frente total / ziper lateral / braguilha` | altera painel de gancho frente |

#### Transformacoes de design

1. Adicionar recorte de quilting em losango no joelho e coxa lateral — textura moto-sport.
2. Transformar em biker com cinto de metal D-ring integrado no cos — detalhe de moto-fashion.

#### Observacao tecnica

Couro vegetal (PU) e couro real nao tem elasticidade — folgas devem ser maiores (+4 a +5 cm no quadril) e o gancho deve ser 1 cm mais profundo que o padrao para conforto sentado. Costura de overlock e dispensada; costura simples com linha grossa dupla.

---

### CALC-024 — Patchwork

**Familia:** inferior / calca / casual
**Subfamilia:** patchwork artesanal-fashion
**Silhueta e fit:** regular a relaxed — silhueta pode variar (reta, wide, baggy); o que define e a construcao em blocos de tecidos distintos

#### Medidas-chave e folgas por tipo de tecido

Identicas ao tipo de silhueta base escolhida (reta, wide ou baggy). O patchwork e construcao de painel, nao de silhueta.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Padrao de divisao | `horizontal / vertical / diagonal / geometrico` | define as linhas de corte entre blocos |
| Numero de blocos | `4 / 6 / 8+ blocos por perna` | multiplica paineis frente e costas |
| Silhueta base | `reta / wide / baggy` | define molde base sobre o qual o patchwork e aplicado |
| Tecidos | `mesmo tecido cores distintas / tecidos distintos` | define corte de materiais |

#### Transformacoes de design

1. Aplicar patchwork em degradê de tons da mesma familia de cor — efeito sofisticado sem excentricidade excessiva.
2. Inserir blocos de jacquard e tecido liso alternados em calca wide leg — mistura de alfaiataria e patchwork urbano.

#### Observacao tecnica

Cada bloco deve ter a linha de fio alinhada ao fio do molde base para nao distorcer a silhueta. Tecidos diferentes com gramaturas distintas exigem entretela de igualacao nos blocos mais leves. Margens de costura entre blocos: 1 cm com acabamento de overlock duplo.

---

### CALC-025 — Barrel Leg (Tonelinha)

**Familia:** inferior / calca / casual
**Subfamilia:** barrel leg / tonelinha
**Silhueta e fit:** relaxed — coxa e quadril com volume; afunila levemente na barra; perna em forma de barril; comprimento medio ou cropped

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha |
|---|---:|---:|---:|
| Cintura alta | 72 cm | +4 cm | +2 cm |
| Quadril | 100 cm | +10 cm | +7 cm |
| Coxa alta (maximo volume) | 58 cm | +14 cm | +10 cm |
| Joelho | 39 cm | +12 cm | +8 cm |
| Barra (afunilada) | 24 cm | +6 cm | +4 cm |

A curva do barril e definida pelo ponto de maximo volume (coxa) sendo maior que o joelho e a barra.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Intensidade do barril | `leve / moderado / pronunciado` | varia a diferenca entre coxa maxima e barra |
| Comprimento | `cropped 88 cm / tornozelo 96 cm` | muda comprimento lateral |
| Cintura | `alta com pregas / alta elastico total / media` | altera painel de cos e abertura |
| Bolso | `faca / sem bolso / embutido lateral` | adiciona painel de bolso |

#### Transformacoes de design

1. Barrel leg com bolso vertical de ressalto na lateral da coxa — detalhe que acentua o volume intencional.
2. Transformar em barrel com pance franzida na lateral para amplificar volume — efeito deconstructed fashion.

#### Observacao tecnica

A curva do barril no molde nao e obtida apenas mudando as medidas — a linha de costura lateral precisa ser desenhada com curva convexa entre o quadril e o joelho, e concava entre o joelho e a barra. Sem esta curva, a perna fica com angulo mas nao com a forma de barril.

---

### CALC-026 — Parachute Pant

**Familia:** inferior / calca / casual
**Subfamilia:** parachute / paraquedas
**Silhueta e fit:** relaxed a oversized — muito volume no gancho e coxa; perna afunila abruptamente para puno estreito; gancho intencionalmente baixo

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecnico leve | Folga plano nylon |
|---|---:|---:|---:|
| Cintura (elastico + cord) | 74 cm | +2 cm | +3 cm |
| Quadril + gancho baixo | 100 cm | +20 cm | +22 cm |
| Coxa (ponto de maximo) | 58 cm | +22 cm | +24 cm |
| Joelho | 39 cm | +14 cm | +16 cm |
| Tornozelo (puno estreito) | 24 cm | +2 cm | +3 cm |
| Profundidade de gancho | 27 cm | +8 a +12 cm | +10 a +14 cm |

Gancho proposital baixo: profundidade de 35-40 cm total (vs. 28 cm em calca regular).

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Profundidade de gancho | `baixo moderado +6 cm / baggy +10 cm / drop maximo +14 cm` | muda profundidade do molde de gancho |
| Puno | `puno elastico slim / puno largo / velcro ajustavel` | altera painel de barra |
| Bolso | `cargo lateral / ziper embutido / sem bolso` | adiciona paineis |
| Cord | `cord unico / duplo cord / sem cord (elastico puro)` | define painel de cos |

#### Transformacoes de design

1. Adicionar multiplas tiras de tecido na lateral da perna (efeito paraquedas literal) — detalhe tecnico-decorativo.
2. Transformar em parachute cropped com puno de 15 cm largo — efeito mais oversized e moderno.

#### Observacao tecnica

O gancho baixo extremo cria tensao horizontal na virilha ao caminhar se a perna nao tiver folga suficiente. A profundidade de gancho de +10 cm ou mais exige que a coxa tambem tenha folga generosa. Tecido ideal: nylon plano leve, tafeta, ripstop leve.

---

### CALC-027 — Carpenter (Carpinteiro)

**Familia:** inferior / calca / casual
**Subfamilia:** carpenter workwear casual
**Silhueta e fit:** regular — perna reta; passante de martelo na lateral esquerda; detalhe de regua lateral; visual workwear-fashion

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga denim / canvas | Folga tecnico |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | +3 cm |
| Quadril | 100 cm | +6 cm | +5 cm |
| Coxa alta | 58 cm | +8 cm | +6 cm |
| Joelho | 39 cm | +10 cm | +8 cm |
| Barra | 24 cm | +10 cm | +8 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Passante de martelo | `simples 5 cm / duplo 8 cm / sem passante` | adiciona painel aplicado na lateral esquerda |
| Regua lateral | `regua de 30 cm / sem regua` | adiciona painel de regua na lateral direita |
| Bolso costas | `dois bolsos costas / um bolso / sem bolso` | adiciona paineis aplicados nas costas |
| Tecido | `denim / canvas / duck cotton / tecnico canvas` | ajusta folgas e construcao |

#### Transformacoes de design

1. Transformar em carpenter com acabamento de borda viva e cor de linha contrastante — versao fashion-workwear.
2. Adicionar aba dobravel no cos frente que cobre parcialmente a braguilha — estilo classico de carpenter americano.

#### Observacao tecnica

O passante de martelo e um painel de tira cortado a 45 graus de comprimento de 25 cm e largura de 3 cm, com bordas dobradas e pespontadas. Deve ser aplicado na lateral esquerda a 15 cm do cos. O ponto de fixacao superior suporta o peso de ferramentas.

---

### CALC-028 — Skater

**Familia:** inferior / calca / casual
**Subfamilia:** skater streetwear
**Silhueta e fit:** regular a relaxed — perna reta com folga moderada; comprimento exato no tornozelo; sem excessos; visual de skate classico

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga denim / canvas | Folga tecnico |
|---|---:|---:|---:|
| Cintura media | 74 cm | +4 cm | +3 cm |
| Quadril | 100 cm | +7 cm | +5 cm |
| Coxa alta | 58 cm | +8 cm | +6 cm |
| Joelho | 39 cm | +10 cm | +8 cm |
| Barra | 24 cm | +10 cm | +8 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `no tornozelo 104 cm / ligeiramente acima 100 cm / break no calcado 108 cm` | muda comprimento lateral |
| Cintura | `media 0 cm / ligeiramente baixa -2 cm` | move linha de cintura para baixo |
| Reforco de joelho | `sem reforco / patch interno / patch externo` | adiciona painel de reforco |
| Bolso | `5 bolsos classico / 6 bolsos` | define numero de bolsos no estilo jeans |

#### Transformacoes de design

1. Transformar em skater com joelho pre-lavado com efeito de desgaste — tratamento de superfcie no painel de joelho.
2. Adicionar patch bordado aplicado no joelho esquerdo — identidade de skate fashion.

#### Observacao tecnica

A barra de skater deve cair com break leve sobre o tenis — muito curta e muito longa comprometem o visual. O comprimento ideal varia conforme a altura do calcado escolhido. Prova com calcado definitivo e obrigatoria.

---

### CALC-029 — Relaxed (Chino Relaxado)

**Familia:** inferior / calca / casual
**Subfamilia:** relaxed fit casual
**Silhueta e fit:** relaxed — folga moderada em todo o corpo; nem justa nem baggy; perna levemente afunilada; visual despojado

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga tecnico |
|---|---:|---:|---:|
| Cintura media | 74 cm | +5 cm | +3 cm |
| Quadril | 100 cm | +8 cm | +6 cm |
| Coxa alta | 58 cm | +9 cm | +7 cm |
| Joelho | 39 cm | +9 cm | +7 cm |
| Barra | 24 cm | +7 cm | +5 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Grau de relaxe | `relaxed moderado / relaxed generoso` | varia folga de coxa de +7 a +11 cm |
| Comprimento | `cropped 95 cm / tornozelo 104 cm` | muda comprimento lateral |
| Cintura | `media / elastico costas / elastico total` | altera painel de cos |
| Bolso | `faca / americana / cargo discreto` | adiciona painel de bolso |

#### Transformacoes de design

1. Relaxed com barra dobrada para cima (virada de 4 cm visivel) — versao verão casual com calcado clean.
2. Transformar em relaxed com cintura de paperbag (franzido com cinto) — versao feminina com personalidade.

---

### CALC-030 — Chino

**Familia:** inferior / calca / casual
**Subfamilia:** chino classico
**Silhueta e fit:** regular — perna reta levemente afunilada; tecido de algodao ou algodao-elastano; versao casual de alfaiataria sem ser social

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano algodao | Folga tecnico algodao-elastano |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | +2,5 cm |
| Quadril | 100 cm | +5 cm | +3 cm |
| Coxa alta | 58 cm | +7 cm | +5 cm |
| Joelho | 39 cm | +8 cm | +6 cm |
| Barra | 24 cm | +7 cm | +5 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Acabamento | `bainha dobrada / barra cortada / virada visivel` | define acabamento inferior |
| Fechamento | `braguilha / ziper lateral / elastico costas` | altera gancho frente |
| Bolso | `5 bolsos classico / faca + americana` | define posicao de bolsos |

#### Transformacoes de design

1. Chino com 2 pregas frente — versao vintage-militar para uso mais formal.
2. Transformar em chino de perna reta larga — versao contemporanea do chino classico com mais volume.

---

## GRUPO 4 — Calcas de Trabalho e Uniforme

---

### CALC-031 — Calca Operacional com Reforco

**Familia:** inferior / calca / uniforme
**Subfamilia:** operacional de campo
**Silhueta e fit:** regular — duravel; reforcos em zonas de desgaste; construcao para uso intenso

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga canvas/brim | Observacao |
|---|---:|---:|---|
| Cintura | 74 cm | +5 cm | elastico parcial costas opcional |
| Quadril | 100 cm | +8 cm | folga para agachamento |
| Coxa alta | 58 cm | +10 cm | |
| Joelho | 39 cm | +12 cm | espaco para joelheira |
| Barra | 24 cm | +10 cm | ajuste por velcro opcional |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Reforco de joelho | `sem reforco / reforco interno / painel externo duplo` | adiciona painel de reforco no joelho |
| Reforco de assento | `sem reforco / reforco externo / reforco interno com cordura` | adiciona painel de assento |
| Elastico | `sem elastico / elastico parcial costas / elastico total` | altera painel de cos |
| Joelheira | `sem bolso de joelheira / bolso para joelheira EVA` | adiciona bolso de joelheira no painel do joelho |

#### Transformacoes de design

1. Adicionar painel de cordura dupla no joelho e entreperna — versao para trabalho em campo pedregoso.
2. Inserir costura flat-felled em todas as costuras principais — durabilidade triplicada em uso de trabalho intenso.

#### Observacao tecnica

Reforco de joelho externo: painel de 20x25 cm em tecido de maior resistencia a abrasao, aplicado sobre o joelho com costura perimetral de 2 linhas. Bolso de joelheira interno: bolso de 20x22 cm acessivel por abertura na lateral do joelho.

---

### CALC-032 — Cargo Operacional

**Familia:** inferior / calca / uniforme
**Subfamilia:** cargo de campo funcional
**Silhueta e fit:** regular — perna reta ampla; multiplos bolsos para ferramentas; construcao para trabalho externo

#### Medidas-chave e folgas por tipo de tecido

Identicas a CALC-022 (Cargo Multi-Bolso), com adicional de reforcos de CALC-031.

#### Parâmetros variaveis

Identicos a CALC-022, com adicao de:

| Parametro adicional | Valores possiveis | Impacto no molde |
|---|---|---|
| Reforco de desgaste | `joelho / assento / joelho e assento` | adiciona paineis duplos nas zonas de uso |
| Velcro de ajuste de barra | `sem velcro / velcro 5 cm` | adiciona regulagem no painel de barra |

#### Transformacoes de design

1. Adicionar passantes laterais para cinto de seguranca — adaptacao para trabalho em altura.
2. Inserir fita refletiva no painel lateral e barra para uso noturno — seguranca em campo.

#### Observacao tecnica

Em cargo operacional, o bolso de cargo deve ter fundo duplo costurado — o peso de ferramentas rasga o fundo simples em uso continuo. Bolso com fundo de 2 camadas de brim ou canvas com margem de costura de 1,5 cm.

---

### CALC-033 — Gardine Reta (Uniforme Classico)

**Familia:** inferior / calca / uniforme
**Subfamilia:** uniforme classico
**Silhueta e fit:** regular — perna reta simples; tecido gardine ou microfibra; para uso em escritorio, seguranca, servico de limpeza

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga gardine plano | Folga gardine elastano |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | +2 cm |
| Quadril | 100 cm | +6 cm | +4 cm |
| Coxa alta | 58 cm | +7 cm | +5 cm |
| Joelho | 39 cm | +9 cm | +7 cm |
| Barra | 24 cm | +9 cm | +7 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Fechamento | `braguilha / elastico total / elastico costas` | altera painel de gancho frente |
| Cos | `cos liso / cos com passantes` | adiciona passantes se necessario |
| Bolso | `bolso faca / bolso americana / sem bolso` | adiciona painel de bolso |

#### Transformacoes de design

1. Adicionar faixa de cor no cos — identidade visual de uniforme por funcao.
2. Transformar em calca com pences frente para versao de uniforme com aparencia mais social.

---

### CALC-034 — Calca com Elastico Total

**Familia:** inferior / calca / uniforme
**Subfamilia:** uniforme confortavel
**Silhueta e fit:** regular — sem braguilha; cos de elastico total com dobra dupla; para uso em servicos de alimentacao, saude, logistica

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha | Reducao elastica |
|---|---:|---:|---:|---:|
| Cintura (cos elastico) | 74 cm | +2 cm | +1 cm | -8 cm |
| Quadril | 100 cm | +6 cm | +3 cm | 0 |
| Coxa alta | 58 cm | +6 cm | +3 cm | 0 |
| Joelho | 39 cm | +9 cm | +6 cm | 0 |
| Barra | 24 cm | +9 cm | +6 cm | 0 |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Largura de elastico | `elastico 3 cm / elastico 4 cm / elastico 5 cm` | muda altura do cos |
| Cor do cos | `mesmo tecido / cor contrastante` | define corte do painel de cos |
| Bolso | `dois bolsos faca / bolso americana / sem bolso` | adiciona paineis de bolso |

#### Transformacoes de design

1. Adicionar cos duplo com elastico de 4 cm por dentro e faixa de cor por fora — identidade visual de funcao ou empresa.
2. Transformar em calca de elastico com bolso de celular lateral — praticidade em servico.

#### Observacao tecnica

O cos de elastico total com dobra dupla e formado por um painel de 10-12 cm de largura dobrado ao meio sobre o elastico. O elastico deve ser tracionado 15-20% ao costurar para criar o franzido uniforme. Travamento do elastico nas costuras laterais e obrigatorio.

---

### CALC-035 — Calca com Joelheira Integrada

**Familia:** inferior / calca / uniforme
**Subfamilia:** operacional com protecao
**Silhueta e fit:** regular — construcao para trabalho ajoelhado (jardinagem, piso, eletrica, construcao)

#### Medidas-chave e folgas por tipo de tecido

Identicas a CALC-031 (Operacional com Reforco), com adicao de:

| Parametro especifico | Especificacao |
|---|---|
| Bolso de joelheira | painel interno de 20x22 cm com abertura pela lateral do joelho |
| Profundidade de bolso | suficiente para joelheira EVA de 1,5 cm de espessura |
| Posicao | centro do painel de joelho, 2 cm acima e abaixo da linha de joelho |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Joelheira | `EVA 1 cm / EVA 1,5 cm / gel (espessura custom)` | define dimensoes do bolso interno |
| Fechamento do bolso | `aberto / velcro / botao de pressao` | define acabamento da abertura do bolso |
| Reforco adicional | `ripstop / cordura / denim duplo` | adiciona camada de reforco externa |

#### Transformacoes de design

1. Painel externo de joelheira removivel por velcro — protetor externo visivel em construcao.
2. Adicionar bolso de joelheira em calca de pesca com reforco de fundo — uso nautical e outdoor.

---

### CALC-036 — Calca de Corte e Costura (Uso Profissional)

**Familia:** inferior / calca / uniforme
**Subfamilia:** atelie e confeccao
**Silhueta e fit:** regular — perna reta com folga confortavel; elastico total; sem bolsos de ressalto que acumulem fio; tecido que nao acumula peca eletrostatica

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano anti-estatico | Folga malha |
|---|---:|---:|---:|
| Cintura (elastico total) | 74 cm | +2 cm | +1 cm |
| Quadril | 100 cm | +6 cm | +4 cm |
| Coxa alta | 58 cm | +7 cm | +5 cm |
| Joelho | 39 cm | +9 cm | +7 cm |
| Barra | 24 cm | +9 cm | +7 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Bolso | `faca interna / sem bolso externo / bolso de regua` | bolso de regua: painel estreito na lateral da coxa |
| Tecido | `brim anti-estatico / microfibra / algodao liso` | ajusta folga conforme rigidez do material |

#### Transformacoes de design

1. Adicionar painel de portafita (porta-fita de alfaiate) no quadril esquerdo — funcional para atelie.
2. Inserir bolso de caneta no cos — praticidade em linha de producao.

---

### CALC-037 — Calca de Brigada

**Familia:** inferior / calca / uniforme
**Subfamilia:** brigada e seguranca
**Silhueta e fit:** regular — construcao para mobilidade em emergencia; refletivo e resistencia a chama opcionais; bolsos funcionais acessiveis em pe

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecido tecnico FR | Observacao |
|---|---:|---:|---|
| Cintura | 74 cm | +5 cm | elastico parcial costas |
| Quadril | 100 cm | +8 cm | mobilidade de corrida |
| Coxa alta | 58 cm | +10 cm | |
| Joelho | 39 cm | +12 cm | espaco para joelheira |
| Barra | 24 cm | +10 cm | velcro de ajuste |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Refletivo | `sem refletivo / fita refletiva lateral / painel refletivo total` | adiciona fita ou painel na lateral e barra |
| Resistencia a chama | `tecido padrao / tecido FR / tecido Nomex` | especificacao de material sem alterar molde |
| Bolso de utensilio | `bolso de radio / bolso de lanterna / sem bolso especial` | adiciona painel de bolso tubular |

#### Transformacoes de design

1. Adicionar refletivo na altura da canela (15 cm de largura, circundando a perna) — visibilidade em ocorrencia noturna.
2. Transformar em versao com braguilha de botao de pressao — acesso rapido em emergencia.

---

### CALC-038 — Calca de Cozinha

**Familia:** inferior / calca / uniforme
**Subfamilia:** gastronomia e servico de alimentacao
**Silhueta e fit:** regular — facil de vestir e remover; resiste a manchas; elastico total; construcao higiênica sem bolsos externos desnecessarios

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano resistente a mancha |
|---|---:|---:|
| Cintura (elastico total) | 74 cm | +3 cm |
| Quadril | 100 cm | +7 cm |
| Coxa alta | 58 cm | +8 cm |
| Joelho | 39 cm | +10 cm |
| Barra | 24 cm | +10 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Padrao visual | `xadrez classico de cozinha / liso branco / liso preto / listrado` | define corte do painel de tecido |
| Bolso | `dois bolsos faca / sem bolso / bolso de caneta` | adiciona painel de bolso |
| Barra | `barra dobrada / barra com velcro ajustavel` | define acabamento inferior |

#### Transformacoes de design

1. Adicionar abertura lateral de 8 cm na barra com botao de pressao — facilita calcar sobre sapatos de cozinha sem amarrar.
2. Transformar em calca de cozinha com cinto de fita (drawstring) visivel — versao chef executivo com mais personalidade.

---

## GRUPO 5 — Calcas de Praia e Lazer

---

### CALC-039 — Beach Pant (Calca de Praia)

**Familia:** inferior / calca / praia e lazer
**Subfamilia:** beach resort
**Silhueta e fit:** relaxed a oversized — tecido leve e fluido; seca rapido; usada sobre biquini ou sunga

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecido fluido secagem rapida |
|---|---:|---:|
| Cintura (elastico total) | 74 cm | +4 cm |
| Quadril | 100 cm | +12 cm |
| Coxa alta | 58 cm | +14 cm |
| Barra | 24 cm | +16 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `3/4 70 cm / tornozelo 100 cm / maxi 112 cm` | muda comprimento lateral |
| Cintura | `elastico total / cord de ajuste / elasto + cord` | define painel de cos |
| Perna | `reta fluida / wide fluida / saruel leve` | redimensiona molde de perna |
| Abertura de perna | `fechada / com fenda lateral 20 cm` | adiciona fenda |

#### Transformacoes de design

1. Transformar em beach pant com fenda lateral de 25 cm e borda com franzido — efeito resort de luxo.
2. Adicionar painel estampado de bloco na barra (ultimos 20 cm) — detalhe visual em tecido de praia.

---

### CALC-040 — Calca de Linho Reta

**Familia:** inferior / calca / praia e lazer
**Subfamilia:** linho verao
**Silhueta e fit:** regular — perna reta classica em linho puro ou misto; casual e fresco

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga linho puro | Folga linho-algodao |
|---|---:|---:|---:|
| Cintura | 74 cm | +5 cm | +4 cm |
| Quadril | 100 cm | +7 cm | +6 cm |
| Coxa alta | 58 cm | +8 cm | +7 cm |
| Joelho | 39 cm | +10 cm | +9 cm |
| Barra | 24 cm | +10 cm | +9 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Fechamento | `braguilha / elastico embutido costas / elastico total` | altera gancho frente |
| Cos | `cos liso / sem cos virada dupla / elastico embutido` | muda painel de cos |
| Bolso | `faca / americana / sem bolso` | adiciona painel |
| Barra | `bainha dobrada 3 cm / barra cortada vivo / virada visivel` | define acabamento |

#### Transformacoes de design

1. Linho reta com cos alto franzido e cinto de amarracao — versao feminina elegante de praia.
2. Transformar em linho de perna reta com recorte de painel lateral de cor contrastante — mescla de cores em linho.

#### Observacao tecnica

Linho puro encolhe ate 8% em lavagem. O molde deve ser produzido com adicional de encolhimento confirmado pelo fornecedor. Lavar o tecido antes do corte e obrigatorio. Bainha de 4 cm para linho pesado.

---

### CALC-041 — Calca de Linho Wide Leg

**Familia:** inferior / calca / praia e lazer
**Subfamilia:** linho wide verao
**Silhueta e fit:** relaxed a oversized — perna muito ampla em linho fluido; visual de resort; combine com camisa ou cropped

#### Medidas-chave e folgas por tipo de tecido

Identicas a CALC-003 (Wide Leg de Alfaiataria) com ajuste de adicional de encolhimento de linho (+8% em comprimento e largura).

#### Parâmetros variaveis

Identicos a CALC-003, com adicao de:

| Parametro adicional | Valores possiveis | Impacto no molde |
|---|---|---|
| Adicional de encolhimento | `8% linho puro / 4% linho-algodao / 2% linho-viscose` | aumenta molde antes do corte |
| Cos | `elastico total / cos liso com ziper / paperbag franzido` | define painel de cos |

#### Transformacoes de design

1. Transformar em linho wide leg de cintura franzida com cinto de corda — versao boho-chic de praia.
2. Adicionar barra com recorte diagonal de 10 cm de desnivel — efeito assimetrico em linho.

---

### CALC-042 — Saruel

**Familia:** inferior / calca / praia e lazer
**Subfamilia:** saruel / harem leve
**Silhueta e fit:** oversized — gancho muito baixo; coxa e quadril com volume extremo; perna afunila para tornozelo; origem em tecidos orientais fluidos

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecido fluido |
|---|---:|---:|
| Cintura (elastico) | 74 cm | +4 cm |
| Quadril + gancho baixo | 100 cm | +20 cm |
| Coxa (ponto de volume) | 58 cm | +24 cm |
| Joelho | 39 cm | +10 cm |
| Tornozelo | 24 cm | +4 cm |
| Profundidade de gancho | 27 cm | +14 a +18 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Profundidade de gancho | `saruel medio +10 cm / saruel fundo +16 cm / saruel maximo +20 cm` | define o quanto o gancho cai |
| Tornozelo | `puno estreito / barra aberta / cano largo` | altera painel de barra |
| Cintura | `elastico simples / elastico + cord / cos franzido` | define painel de cos |
| Comprimento | `tornozelo 98 cm / midi 80 cm` | muda comprimento lateral |

#### Transformacoes de design

1. Saruel com cos franzido e amarracao no tornozelo — versao yoga/meditacao fluida.
2. Transformar em saruel de um tecido cortado em vies — queda diferente com mais movimento.

#### Observacao tecnica

O gancho muito baixo cria uma peca com aparencia de "saco" quando em repouso, que se transforma com o uso. O molde de saruel usa um painel de gancho expandido que desce muito mais que o padrao — essencialmente, o tecido entre as pernas forma uma bolsa. A perna afunila a partir de 20 cm acima da barra.

---

### CALC-043 — Calca Pescador

**Familia:** inferior / calca / praia e lazer
**Subfamilia:** pescador classico
**Silhueta e fit:** relaxed — cintura com amarracao lateral; comprimento 3/4 ou tornozelo; visual de atividade nautica e praia

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga algodao leve / linho |
|---|---:|---:|
| Cintura (amarracao lateral) | 74 cm | +8 cm (franzido) |
| Quadril | 100 cm | +8 cm |
| Coxa alta | 58 cm | +8 cm |
| Joelho | 39 cm | +10 cm |
| Barra (3/4 ou tornozelo) | — | +10 cm |
| Comprimento lateral | 70-100 cm | — |

A caracteristica da calca pescador e o fechamento por amarracao lateral — um lado da cintura tem excesso de tecido que e franzido e amarrado.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `3/4 70 cm / tornozelo 100 cm` | muda comprimento lateral |
| Amarracao | `lateral esquerda / lateral direita / frontal` | define posicao da amarracao no molde |
| Perna | `reta / levemente afunilada` | redimensiona barra |

#### Transformacoes de design

1. Adicionar estampa de listras horizontais — visual de Riviera classico.
2. Transformar em pescador com barra dobrada e pesponto — versao mais estruturada do classico pescador.

---

### CALC-044 — Thai Pant (Calca Tailandesa)

**Familia:** inferior / calca / praia e lazer
**Subfamilia:** thai pant / wrap pant
**Silhueta e fit:** oversized — painel frontal extra que envolve e amarra; sem gancho convencional; uma das pecas mais livres de tamanho

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecido fluido |
|---|---:|---:|
| Cintura | universal (ajuste por amarracao) | — |
| Painel frontal (largura) | 90 cm | — |
| Comprimento lateral | 100 cm | — |
| Largura do painel de perna | 70 cm | — |

A thai pant e construida em 2-3 paineis grandes que se enrolam em torno do corpo — o molde define dimensoes dos paineis, nao medidas de corpo convencionais.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Numero de paineis | `2 paineis / 3 paineis` | define o numero de blocos de tecido |
| Comprimento | `tornozelo / midi` | muda comprimento dos paineis |
| Largura do painel frontal | `80 cm / 90 cm / 100 cm` | define amplitude do enrolamento |

#### Transformacoes de design

1. Thai pant com borda bordada ou com franja — versao festiva e resort.
2. Transformar em thai pant de seda com estampa balinesa — versao premium de praia.

#### Observacao tecnica

A thai pant nao tem gancho convencional — o painel frontal e enrolado entre as pernas e amarrado. O molde consiste em dois ou tres retangulos com acabamento de borda. A funcionalidade depende do modo de amarracao, nao da construcao do molde.

---

## GRUPO 6 — Calcas Especiais

---

### CALC-045 — Harem Pant

**Familia:** inferior / calca / especial
**Subfamilia:** harem estruturado
**Silhueta e fit:** oversized — gancho muito baixo com volume estruturado; diferente do saruel leve; mais estrutura e menos fluido

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecido plano estruturado | Folga malha pesada |
|---|---:|---:|---:|
| Cintura (elastico) | 74 cm | +4 cm | +2 cm |
| Quadril + gancho baixo | 100 cm | +16 cm | +12 cm |
| Coxa (ponto de maximo volume) | 58 cm | +20 cm | +16 cm |
| Joelho | 39 cm | +8 cm | +5 cm |
| Tornozelo (puno) | 24 cm | +2 cm | 0 |
| Profundidade de gancho | 27 cm | +12 a +16 cm | +10 a +14 cm |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Estrutura da perna | `construido com franzidos / franzido no puno / franzido na cintura` | define onde o volume e distribuido |
| Cos | `elastico simples / cos largo franzido / cos largo com cord` | altera painel de cos |
| Tornozelo | `puno elastico 6 cm / barra aberta / franzido com elastico` | altera painel de barra |

#### Transformacoes de design

1. Harem com franzido concentrado no joelho — volume aparece e some ao longo da perna.
2. Transformar em harem de calca de danca — franzidos mais abertos, tecido de jersey, movimentacao amplificada.

---

### CALC-046 — Bloomers

**Familia:** inferior / calca / especial
**Subfamilia:** bloomers / calcao bufante
**Silhueta e fit:** oversized — shorts ou calca curta muito volumosa; franzida na cintura e na barra; visual balloon ou bufante

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga tecido fluido | Reducao elastica (cintura e barra) |
|---|---:|---:|---:|
| Cintura (elastico total) | 74 cm | +14 cm | -8 cm |
| Quadril | 100 cm | +16 cm | 0 |
| Coxa alta (ponto de volume) | 58 cm | +18 cm | 0 |
| Barra (franzida) | 36 cm (coxa media) | +14 cm | -8 cm |
| Comprimento lateral | 38-50 cm | — | — |

O efeito bufante e criado pelo volume excessivo na circunferencia franzida na barra.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `mini 38 cm / shorts 44 cm / midi 50 cm` | muda comprimento lateral |
| Franzido | `franzido leve / franzido maximo` | varia o excesso de tecido em cintura e barra |
| Tecido | `chiffon / seda / algodao leve / malha jersey` | ajusta folgas conforme caimento |

#### Transformacoes de design

1. Bloomers com camadas de voile sobrepostas — efeito romantico ou de bale.
2. Transformar em bloomers com cinto de veludo — versao editorial e fashion.

---

### CALC-047 — Gaucho Pant

**Familia:** inferior / calca / especial
**Subfamilia:** gaucho / pantalonas
**Silhueta e fit:** relaxed — comprimento midi (ate o meio da panturrilha); barra larga; inspirado no gaucho argentino e no vestuario de equitacao

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano fluido | Folga tecnico estruturado |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | +3 cm |
| Quadril | 100 cm | +8 cm | +6 cm |
| Coxa alta | 58 cm | +10 cm | +8 cm |
| Joelho | 39 cm | +14 cm | +12 cm |
| Barra (alargada) | — | +18 cm | +16 cm |
| Comprimento lateral | 72-82 cm | — | — |

Comprimento de midi alto: termina entre o joelho e o meio da panturrilha.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `midi 72 cm / midi baixo 80 cm` | muda comprimento lateral |
| Barra | `reta ampla / levemente franzida / com preguica` | define acabamento da barra |
| Cintura | `cos liso / elastico embutido / cos franzido` | altera painel de cos |
| Tecido | `fluido (crepe, viscose) / estruturado (denim, gabardine)` | ajusta folgas |

#### Transformacoes de design

1. Gaucho com bolso faca e cos anatômico — versao que transita entre praia e cidade.
2. Transformar em gaucho com barra franzida por elastico — efeito balloon na barra para versao fashion.

---

### CALC-048 — Culottes

**Familia:** inferior / calca / especial
**Subfamilia:** culottes classico
**Silhueta e fit:** relaxed — aparencia de saia; perna larga e curta (acima ou no joelho); hibrido de saia e calca

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano | Folga malha fluida |
|---|---:|---:|---:|
| Cintura | 72 cm | +4 cm | +2 cm |
| Quadril | 100 cm | +10 cm | +7 cm |
| Coxa alta (ponto de volume) | 58 cm | +14 cm | +10 cm |
| Barra (largura) | — | +20 cm | +16 cm |
| Comprimento lateral | 52-65 cm | — | — |

O efeito de saia e criado pela perna muito larga e curta — visualmente indistinguivel de saia em movimento.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `mini culottes 52 cm / culottes joelho 60 cm / culottes baixo 65 cm` | muda comprimento lateral |
| Cintura | `alta com ziper lateral / alta elastico / media` | define fechamento e painel de cos |
| Perna | `uniforme / levemente afunilada na barra` | redimensiona barra |
| Preguica | `sem preguica / com preguica frente / com preguica frente e costas` | adiciona volume extra na cintura |

#### Transformacoes de design

1. Culottes com forro de funcao — forro evita transparencia em tecidos leves.
2. Transformar em culottes com abertura lateral fenda de 10 cm — visual assimetrico e contemporaneo.

#### Observacao tecnica

Culottes construido sem gancho convencional (como saia dividida) cria problemas de mobilidade em subida de escadas. O molde correto mantem gancho minimo de 5-7 cm de profundidade para funcionalidade. A aparencia de saia e obtida pela largura da barra, nao pela ausencia de gancho.

---

### CALC-049 — Knickerbockers (Balonê)

**Familia:** inferior / calca / especial
**Subfamilia:** knickerbocker / plus fours
**Silhueta e fit:** relaxed — perna franzida abaixo do joelho por elastico; volume de balao na coxa; comprimento 3/4

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano encorpado | Reducao elastica |
|---|---:|---:|---:|
| Cintura | 74 cm | +4 cm | 0 |
| Quadril | 100 cm | +8 cm | 0 |
| Coxa alta | 58 cm | +12 cm | 0 |
| Joelho (ponto de maximo volume) | 39 cm | +14 cm | 0 |
| Abaixo do joelho (franzido) | 34 cm | +12 cm | -8 cm |
| Comprimento lateral | 68-75 cm | — | — |

O efeito de balao: muito volume no joelho; franzido abaixo do joelho por elastico que prende a perna.

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `abaixo do joelho 68 cm / medio 72 cm` | muda comprimento lateral |
| Franzido abaixo do joelho | `franzido por elastico / franzido por cinto / puno largo` | altera o acabamento abaixo do joelho |
| Volume de coxa | `moderado +10 cm / generoso +14 cm / maximo +18 cm` | redimensiona coxa e joelho |
| Cintura | `liso com fechamento / elastico total` | altera painel de cos |

#### Transformacoes de design

1. Knickerbocker em tartan (xadrez escoces) com cinto de couro — versao classica inglesa de golfe.
2. Transformar em knickerbocker de esporte urbano em nylon — versao contemporanea streetwear com volume no joelho.

---

### CALC-050 — Bermuda de Alfaiataria

**Familia:** inferior / calca / especial
**Subfamilia:** bermuda social
**Silhueta e fit:** regular — comprimento abaixo do joelho em tecido de alfaiataria; comportamento de calca social com comprimento de shorts longo

#### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo M | Folga plano alfaiataria | Folga tecnico |
|---|---:|---:|---:|
| Cintura | 72 cm | +4 cm | +2 cm |
| Quadril | 100 cm | +6 cm | +4 cm |
| Coxa alta | 58 cm | +7 cm | +5 cm |
| Joelho (barra da bermuda) | 39 cm | +9 cm | +7 cm |
| Comprimento lateral | 54-60 cm | — | — |

#### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `acima do joelho 50 cm / no joelho 54 cm / abaixo do joelho 60 cm` | muda comprimento lateral |
| Barra | `bainha dobrada 3 cm / barra virada visivel / barra cortada com vivo` | define acabamento |
| Fechamento | `braguilha / ziper lateral / elastico costas` | altera gancho frente |
| Bolso | `faca / americana / faca + costas` | adiciona paineis de bolso |
| Pences frente | `sem pence / 1 pence / 2 pregas abertas` | adiciona volume na cintura |

#### Transformacoes de design

1. Bermuda de alfaiataria com linho — versao resort de alto padrao para ambiente de praia ou verão urbano.
2. Transformar em bermuda com cinto integrado e fivela metalica — versao masculina classica de summer office.

#### Observacao tecnica

A bermuda de alfaiataria sem forro pode revelar a entreperna ao sentar. Em tecidos planos claros, o forro de entreperna (apenas no assento, ate 10 cm abaixo do gancho) e recomendado. A barra deve ter bainha de pelo menos 3 cm para dar peso e caimento ao tecido estruturado.

---

## Tabela-resumo — 50 Calcas PHYLLOS

| ID | Nome | Grupo | Silhueta | Tecido Principal |
|---|---|---|---|---|
| CALC-001 | Calca Reta Classica de Alfaiataria | Alfaiataria | regular | plano/crepe |
| CALC-002 | Calca Slim de Alfaiataria | Alfaiataria | slim | plano com elastano |
| CALC-003 | Calca Wide Leg de Alfaiataria | Alfaiataria | relaxed | crepe/gabardine |
| CALC-004 | Palazzo | Alfaiataria | oversized | crepe fluido/viscose |
| CALC-005 | Cigarrete | Alfaiataria | slim | plano/elastano |
| CALC-006 | Calca Cropped de Alfaiataria | Alfaiataria | regular | plano/crepe |
| CALC-007 | Bootcut de Alfaiataria | Alfaiataria | regular | gabardine/crepe |
| CALC-008 | Flare de Alfaiataria | Alfaiataria | regular | crepe/viscose |
| CALC-009 | Paperbag (Cintura Franzida) | Alfaiataria | relaxed | crepe leve |
| CALC-010 | Calca de Pregas (Pleated Trouser) | Alfaiataria | relaxed | gabardine/linho |
| CALC-011 | Jogger Refinada | Performance | relaxed | malha tecnica |
| CALC-012 | Legging Lisa | Performance | fitted | tecnico 4 vias |
| CALC-013 | Legging com Bolso | Performance | fitted | tecnico 4 vias |
| CALC-014 | Legging de Compressao | Performance | compressao | tecnico compressao |
| CALC-015 | Calca 3/4 de Performance | Performance | fitted-regular | malha/tecnico |
| CALC-016 | Cargo Tecnica de Performance | Performance | regular | tecnico DWR |
| CALC-017 | Calca Windbreaker | Performance | regular | nylon/tafeta |
| CALC-018 | Calca de Trail Running | Performance | regular | tecnico 4 vias |
| CALC-019 | Calca de Ciclismo | Performance | compressao | tecnico compressao |
| CALC-020 | Calca de Ginastica/Academia | Performance | fitted | malha/tecnico |
| CALC-021 | Baggy | Casual/Streetwear | oversized | denim/canvas |
| CALC-022 | Cargo Multi-Bolso | Casual/Streetwear | regular-relaxed | canvas/denim |
| CALC-023 | Biker/Moto | Casual/Streetwear | slim-fitted | couro vegetal/denim |
| CALC-024 | Patchwork | Casual/Streetwear | variavel | misto |
| CALC-025 | Barrel Leg (Tonelinha) | Casual/Streetwear | relaxed | plano/denim |
| CALC-026 | Parachute Pant | Casual/Streetwear | oversized | nylon/ripstop |
| CALC-027 | Carpenter (Carpinteiro) | Casual/Streetwear | regular | denim/canvas |
| CALC-028 | Skater | Casual/Streetwear | regular-relaxed | denim/canvas |
| CALC-029 | Relaxed (Chino Relaxado) | Casual/Streetwear | relaxed | algodao/chino |
| CALC-030 | Chino | Casual/Streetwear | regular | algodao/chino |
| CALC-031 | Calca Operacional com Reforco | Trabalho/Uniforme | regular | canvas/brim |
| CALC-032 | Cargo Operacional | Trabalho/Uniforme | regular | canvas/cordura |
| CALC-033 | Gardine Reta (Uniforme Classico) | Trabalho/Uniforme | regular | gardine/microfibra |
| CALC-034 | Calca com Elastico Total | Trabalho/Uniforme | regular | plano/malha |
| CALC-035 | Calca com Joelheira Integrada | Trabalho/Uniforme | regular | canvas/brim |
| CALC-036 | Calca de Corte e Costura | Trabalho/Uniforme | regular | plano anti-estatico |
| CALC-037 | Calca de Brigada | Trabalho/Uniforme | regular | tecnico FR |
| CALC-038 | Calca de Cozinha | Trabalho/Uniforme | regular | algodao xadrez |
| CALC-039 | Beach Pant | Praia/Lazer | relaxed-oversized | secagem rapida |
| CALC-040 | Calca de Linho Reta | Praia/Lazer | regular | linho/linho-algodao |
| CALC-041 | Calca de Linho Wide Leg | Praia/Lazer | relaxed | linho fluido |
| CALC-042 | Saruel | Praia/Lazer | oversized | tecido oriental fluido |
| CALC-043 | Calca Pescador | Praia/Lazer | relaxed | algodao leve/linho |
| CALC-044 | Thai Pant | Praia/Lazer | oversized | tecido fluido |
| CALC-045 | Harem Pant | Especial | oversized | plano estruturado |
| CALC-046 | Bloomers | Especial | oversized | chiffon/jersey leve |
| CALC-047 | Gaucho Pant | Especial | relaxed | crepe/viscose/denim |
| CALC-048 | Culottes | Especial | relaxed | plano/malha fluida |
| CALC-049 | Knickerbockers (Balonê) | Especial | relaxed | plano encorpado |
| CALC-050 | Bermuda de Alfaiataria | Especial | regular | plano/crepe |

---

## Regras globais de graduacao — Calcas

Ajuste por tamanho (de PP a GG, intervalo de um tamanho):

| Regiao | Variacao por tamanho |
|---|---|
| Cintura | +/- 4 cm total |
| Quadril | +/- 4 cm total |
| Coxa | +/- 2 cm total |
| Joelho | +/- 1,5 cm total |
| Barra | +/- 1 cm total |
| Gancho profundidade | +/- 0,4 cm por tamanho |
| Comprimento lateral | manter constante por grade regular; criar grade de altura separada |

Distribuicao do ganho de quadril:
- 35% em costura lateral frente
- 35% em costura lateral costas
- 20% em gancho / centro costas
- 10% em pence ou cos

---

## Regras de margem de costura — Calcas

| Regiao | Margem |
|---|---|
| Costuras laterais | 1,5 cm |
| Entreperna | 1,2 cm |
| Gancho | 1,2 cm |
| Cintura para cos | 1,0 cm |
| Boca de bolso | 0,7 cm |
| Bainha padrao | 3,0 cm |
| Bainha em tecido pesado | 4,0 cm |
| Cos — unioes | 1,0 cm |
| Cos — fechamento interno | 0,7 cm |

---

## Lacunas a preencher antes de qualquer piloto

1. Medidas reais do corpo-alvo PHYLLOS por tamanho (PP / P / M / G / GG), separado por feminino, masculino e unissex.
2. Comportamento real dos tecidos por familia (elasticidade em urdume, trama e vies; recuperacao pos-tensao; encolhimento).
3. Confirmacao de comprimentos por grade de altura (baixa / media / alta).
4. Validacao de profundidade de gancho em prova sentada para cada grupo (alfaiataria, performance, especial).
5. Definicao de nomenclatura de tamanhos definitiva PHYLLOS.
6. Preferencia de fechamento confirmada por ICP por grupo de uso.
