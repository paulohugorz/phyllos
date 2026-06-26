# PHYLLOS DPP Integrado - QA Anti-Greenwashing v0

**Data:** 2026-06-25  
**Status:** criterios bloqueantes para MVP  
**Relacionado:** [prd-dpp-integrado-v0.md](prd-dpp-integrado-v0.md), [dpp-data-contract-v0.md](dpp-data-contract-v0.md)

---

## 1. Principio editorial

Todo DPP publico deve comunicar:

> Este passaporte mostra o que a marca declarou, calculou ou documentou sobre esta peca. Indicadores nao sao auditoria ambiental nem ACV oficial, exceto quando explicitamente documentado. Estimativas usam fatores medios ou declarados e devem ser lidas com essa limitacao.

## 2. Riscos

| Risco | Descricao | Probabilidade | Impacto | Bloqueio |
|---|---|---:|---:|---|
| GW1 | Indicador calculado parece fato auditado | alta | alto | label obrigatorio |
| GW2 | Marca declara fator baixo sem evidencia | alta | alto | limites e exigencia de documento |
| GW3 | Campo ausente some da pagina publica | media | alto | lacuna visivel |
| GW4 | Texto livre cria claim "sustentavel" | alta | medio | template publico sem campo livre |
| GW5 | Certificacao expirada aparece como valida | media | alto | badge expirado ou bloqueio |
| GW6 | Score verde comunica falsa precisao | baixa | alto | score publico proibido |
| GW7 | Dados de amostra sao publicados como lote real | media | medio | versao, lote e data visiveis |
| GW8 | Fator de impacto sem fonte vira numero aparentemente confiavel | alta | alto | fonte textual obrigatoria por fator |

## 3. Hard gates

### AG1 - Indicador ausente

Indicador ausente nunca aparece como numero. A UI deve exibir `nao informado` ou uma lacuna equivalente.

### AG2 - Indicador calculado

Indicador calculado deve exibir:

> Estimativa com fator medio de referencia setorial.

Se o fator foi declarado pela marca:

> Fator declarado pela marca, nao auditado.

### AG3 - Score composto

Nao existe nota verde, ranking ambiental, selo automatico ou score composto publico na V1.

### AG4 - Claim livre

A pagina publica nao deve renderizar campo livre de marketing. Nome, categoria, composicao, indicadores, fonte e limitacoes devem vir de dados estruturados.

### AG5 - Certificacao expirada

Certificacao vencida nao pode aparecer como valida. A UI deve exibir `certificado expirado` ou bloquear a publicacao se o claim depender dela.

### AG6 - Versao e lote

Todo DPP publico deve mostrar:

- data de publicacao;
- versao do DPP;
- lote ou codigo relacionado;
- fonte/limite dos indicadores.

### AG7 - Fonte do fator

Agua, energia e carbono calculados devem ter fonte textual por fator. Proxy interno, demo ou "nao usar em piloto" bloqueia publicacao.

## 4. Checklist de QA

Antes de publicar:

- composicao soma 100%;
- campos obrigatorios estao pelo menos `declarado`;
- todo indicador tem badge;
- estimativas aparecem como estimativas;
- fontes dos fatores de agua, energia e carbono aparecem na pagina publica;
- campo ausente aparece como lacuna ou bloqueia publicacao;
- QR abre a pagina publica correta;
- pagina publica nao exige login;
- pagina publica nao possui claim livre de sustentabilidade;
- certificacoes mostram numero e validade quando documentadas;
- DPP revogado mostra aviso e nao apaga historico.

## 5. Criterios de teste

Unitarios:

- calculo com area 1 m2, perda 20%, gramatura 200 g/m2 e fatores conhecidos gera resultado deterministico;
- perda `>= 100%` falha;
- composicao diferente de 100 falha;
- fator negativo falha;
- status `documentado` nao regride para `declarado` sem acao administrativa.

Integracao:

- tentativa de publicar DPP com obrigatorio ausente retorna erro;
- publicacao com obrigatorios completos retorna QR/link;
- pagina publica renderiza badges;
- revogacao altera estado publico para aviso.

## 6. Copy base dos flashcards

### Composicao

Titulo: `De que e feita`  
Badge: `declarado pela marca` ou `documentado`  
Texto:

> O tecido e composto por fibras informadas pela marca. Quando houver documento, a composicao aparece como documentada.

### Carbono

Titulo: `Carbono estimado por peca`  
Badge: `estimativa calculada`  
Texto:

> Calculado com base no peso do tecido e fatores de referencia. Nao e uma ACV oficial.

### Agua

Titulo: `Agua estimada por peca`  
Badge: `estimativa calculada`  
Texto:

> A pegada hidrica varia conforme origem da fibra, cultivo, tingimento e processo produtivo.

### Perda de corte

Titulo: `Aproveitamento do tecido`  
Badge: `declarado pela marca` ou `documentado`  
Texto:

> A perda de corte indica a parcela de tecido que nao vira a peca principal. Retalhos podem ser reaproveitados, doados ou reciclados quando houver processo definido.

### Fabricacao

Titulo: `Onde foi feito`  
Badge: `declarado pela marca` ou `documentado`  
Texto:

> Localizacao declarada pela marca. Etapas produtivas detalhadas aparecem quando a cadeia estiver documentada.

### Certificacoes

Titulo: `Certificacoes`  
Badge: `documentado` ou `declarado`  
Texto:

> Certificacoes devem incluir numero e validade quando documentadas.

### Cuidado e durabilidade

Titulo: `Como cuidar e o que fazer depois`  
Texto:

> Instrucoes de cuidado, reparo e fim de vida ajudam a prolongar uso e reduzir descarte precoce.

### Transparencia

Titulo: `Sobre este passaporte`  
Texto:

> Os dados mostrados foram declarados, calculados ou documentados pela marca. Estimativas usam fatores medios ou declarados. Nenhum indicador e auditado por terceiros exceto onde indicado.
