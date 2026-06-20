# Catalogo de Moldes Base — PHYLLOS

Versao: 1.0  
Data: 2026-06-11  
Responsavel: Design Lead  
Referencia de formato: `docs/patternmaking/calca-performance-alfaiataria-molde-v0.md`

---

## Como usar este catalogo

Cada entrada e uma **arquitetura parametrizada**, nao um molde pronto. O motor de moldes usa esses modelos como ponto de partida quando o usuario descreve uma peca em linguagem natural.

Formula de medida final valida para todas as bases:

```text
medida_final = corpo + folga_vestibilidade + folga_movimento - reducao_elastica
```

As coordenadas sao sempre em centimetros. Origem no topo esquerdo de cada peca. `x` cresce para fora do corpo; `y` cresce para baixo.

Tolerancia padrao de construcao: +/- 0,7 cm em curvas; +/- 0,5 cm em retas.

---

## BASE 01 — Calca Reta Classica

**Familia:** inferior / calca  
**Variantes contempladas:** feminino, masculino, unissex

### ICP de uso

Quem usa: pessoa que trabalha em ambiente presencial ou hibrido, se desloca com frequencia e precisa de uma calca que nao sinalize "esporte" nem "escritorio formal".  
Quando: dia inteiro, da manha ao deslocamento noturno.  
Como: com tenis, mule, sandalia ou bota — depende de quem usa.

### Medidas-chave e folgas por tipo de tecido

Corpo-base: tamanho M, altura 168 cm para feminino / 175 cm para masculino.

| Regiao | Corpo fem. | Corpo masc. | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|---:|
| Cintura natural | 74 cm | 82 cm | +3 cm | +1 cm | +2 cm |
| Quadril maior | 100 cm | 100 cm | +5 cm | +2 cm | +3 cm |
| Coxa alta | 58 cm | 61 cm | +6 cm | +3 cm | +5 cm |
| Joelho | 39 cm | 42 cm | +10 cm | +6 cm | +8 cm |
| Barra | 24 cm | 26 cm | +10 cm | +6 cm | +8 cm |
| Profundidade gancho | 27 cm | 31 cm | +1,5 cm | +0,5 cm | +1 cm |
| Entreperna | 76 cm | 82 cm | 0 | 0 | 0 |
| Comprimento lateral | 106 cm | 112 cm | 0 | 0 | 0 |

**Formula de cintura unissex:**  
`cintura_molde = cintura_corpo + folga_plano`

**Formula de barra reta:**  
`barra_molde = (barra_joelho * 0,95) + tolerancia_tecido`

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente (x2 espelhadas) | volume de abdomen, bolso opcional | eixo vertical | lateral, entreperna, gancho frente |
| Costas (x2 espelhadas) | volume de gluteo e coxa | eixo vertical | lateral, entreperna, gancho costas |
| Cos frente | estabilidade visual | paralelo ao comprimento | lateral, cintura frente |
| Cos costas | opcoes: liso ou elastico | paralelo ao comprimento | lateral, cintura costas |

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Abertura de barra | `tubo estreito / reta / boca-de-sino suave` | redimensiona pontos da barra e joelho |
| Altura de cintura | `media / alta / muito alta` | move linha de cintura -2 / 0 / +4 cm da cintura natural |
| Bolso | `nenhum / faca / americana / cargo lateral` | adiciona paineis de bolso e recorte na frente |
| Fechamento | `ziper frente / ziper lateral / elastico total` | altera regiao do gancho frente e cos |
| Cos | `liso plano / anatomico / embutido` | muda altura e forma do cos |
| Versao de genero | `feminino / masculino / unissex` | ajusta profundidade de gancho e inclinacao de quadril |

### Diferencas por versao

**Feminino:** gancho frente mais raso (27 cm), inclinacao lateral do quadril mais pronunciada, cos com leve curva na cintura.  
**Masculino:** gancho frente mais fundo (31 cm), largura de joelho maior (+3 cm), entreperna mais longa (+6 cm), braguilha obrigatoria.  
**Unissex:** gancho intermediario (29 cm), largura de quadril neutra, sem pinces em nenhum lado, fechamento por elastico ou ziper lateral.

### Transformacoes de design possiveis

1. "Quero uma calca reta com recorte de yoke nas costas e dois bolsos de ressalto na lateral da coxa" — adiciona painel de yoke separado nas costas + recorte horizontal no gancho + caixa de bolso externo.
2. "Quero transformar em calca wide leg, abertura de barra de 60 cm" — aumenta pontos de barra e joelho proporcionalmente, mantendo gancho e cintura originais.
3. "Adicionar painel de malha tecnica na entreperna e coxa interna para mobilidade" — insere painel contrastante de formato triangular entre as costuras de entreperna frente e costas.

---

## BASE 02 — Calca Jogger / Elastico Total

**Familia:** inferior / calca  
**Variantes contempladas:** feminino, masculino, unissex

### ICP de uso

Quem usa: pessoa que treina, trabalha em casa, viaja, ou transita entre academia e rua no mesmo dia.  
Quando: da manha ao fim do dia; uso de deslocamento e descanso ativo.  
Como: com tenis de corrida, sandalia slide ou tenis limpo — pelo visual, pode sair da academia direto para cafe ou reuniao informal.

### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo base M | Folga malha | Folga tecnico (stretch 4 vias) | Reducao elastica tipica |
|---|---:|---:|---:|---:|
| Cintura (cos elastico) | 74 cm | +2 cm | +0 cm | -8 a -12 cm |
| Quadril | 100 cm | +4 cm | +2 cm | 0 |
| Coxa alta | 58 cm | +4 cm | +2 cm | 0 |
| Joelho | 39 cm | +5 cm | +3 cm | 0 |
| Barra (puno elastico) | 24 cm | +2 cm | +0 cm | -6 a -8 cm |
| Profundidade gancho | 27 cm | +2 cm | +1 cm | 0 |
| Entreperna | 76 cm | +1 cm | 0 | 0 |
| Comprimento lateral | 106 cm | 0 | 0 | 0 |

**Formula do cos jogger:**  
`comprimento_cos_molde = cintura_corpo + 2 cm`  
`comprimento_elastico = cintura_corpo - 4 cm` (elastico de 3 cm de largura)

**Formula do puno barra:**  
`comprimento_puno_molde = barra_corpo * 1,1`  
`comprimento_elastico_puno = barra_corpo * 0,75`

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente (x2) | volume frente, bolso kangaroo opcional | eixo vertical | lateral, entreperna, gancho frente |
| Costas (x2) | volume costas, bolso de ressalto opcional | eixo vertical | lateral, entreperna, gancho costas |
| Cos (tubo dobrado) | canal de elastico com dobra | paralelo ao comprimento | lateral, costura de fechamento |
| Puno barra (x2) | acabamento e compressao leve de tornozelo | perpendicular ao comprimento do puno | costura de fechamento circular |
| Bolso lateral opcional (x2) | funcionalidade de rua | fio reto | abertura, base |

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Altura de cos | `baixo (6 cm) / medio (8 cm) / alto (12 cm)` | muda altura do painel de cos e reposiciona origem |
| Tipo de elastico | `simples / duplo canal / cord de ajuste` | adiciona casas no cos para cordon |
| Puno | `com puno elastico / sem puno barra reta` | remove painel de puno e altera barra para reta ou barra dobrada |
| Bolso | `nenhum / lateral simples / kangaroo frente / ziper lateral` | adiciona paineis |
| Painel de entreperna | `padrao / painel tecnico de mobilidade` | insere gusset triangular ou painel de 4 vias |
| Largura de perna | `afunilada / reta / relaxada` | redimensiona coxa, joelho e barra |

### Diferencas por versao

**Feminino:** cintura mais alta, gancho frente raso, proporcao de quadril maior, puno opcional mais estreito.  
**Masculino:** gancho mais fundo +3 a +4 cm, largura de coxa maior, cos mais reto sem curva, braguilha dispensada (fechamento elastico total).  
**Unissex:** gancho intermediario, largura de quadril neutra, sem pinces.

### Transformacoes de design possiveis

1. "Quero um jogger com painel lateral de tecido plano contrastante, tipo track pant" — insere painel vertical de 8 a 10 cm de largura correndo da cintura ate o puno, substituindo parte da costura lateral.
2. "Quero transformar em bermuda jogger abaixo do joelho com puno" — encurta comprimento lateral para `joelho + 12 cm`, mantendo puno e cos iguais.
3. "Quero adicionar bolso ziper embutido na costura lateral" — reorganiza a lateral para virar abertura de ziper de 20 cm a partir do quadril, com saco de bolso preso no cos.

---

## BASE 03 — Shorts Masculino Funcional

**Familia:** inferior / shorts  
**Variantes contempladas:** masculino como principal; adaptacao unissex descrita

### ICP de uso

Quem usa: homem que treina (corrida, funcional, academia) ou usa no dia a dia em clima quente; transita entre treino e rua.  
Quando: manha de treino, fim de semana ativo, viagem.  
Como: com camiseta performance ou polo, tenis de corrida ou tenis clean.

### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo base M masc. | Folga malha | Folga tecnico |
|---|---:|---:|---:|
| Cintura (elastico) | 82 cm | +2 cm | +0 cm |
| Quadril | 100 cm | +6 cm | +4 cm |
| Coxa alta | 61 cm | +6 cm | +4 cm |
| Comprimento lateral | 25 cm (acima do joelho) | 0 | 0 |
| Profundidade gancho | 31 cm | +1,5 cm | +1 cm |
| Abertura de perna | — | definida por comprimento + coxa | — |

**Formula comprimento shorts:**  
`comprimento_lateral_molde = altura_corpo * 0,148` (padrao acima do joelho, ajustavel)

**Formula abertura de perna:**  
`abertura_perna = (coxa_molde / 2) + 2 cm de folga de saida`

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente (x2) | volume abdominal e abertura de perna | eixo vertical | lateral, entreperna, gancho frente |
| Costas (x2) | volume de gluteo | eixo vertical | lateral, entreperna, gancho costas |
| Cos (tubo elastico) | canal de elastico + cord opcional | paralelo | lateral |
| Forro interno (opcional, x2) | suporte e cobertura | eixo vertical | costura propria de forro |
| Bolso lateral (x2) | chaves, cartao | eixo reto | abertura, base |
| Bolso ziper traseiro (opcional) | seguranca em corrida | eixo reto | abertura ziper, base |

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `curto (23 cm) / medio (26 cm) / longo (30 cm)` | muda comprimento lateral e abertura de perna |
| Forro | `sem forro / forro solto / forro com bolso integrado` | adiciona painel interno |
| Bolso | `nenhum / lateral / ziper costas / faca lateral` | adiciona recorte e paineis |
| Abertura de perna | `fechada / com fenda lateral / com vivo elastico` | altera extremidade do painel |
| Cos | `elastico simples / cord / cos duplo` | muda painel do cos |
| Corte de perna | `reto / ligeiramente afunilado / abertura de fenda 5 cm` | redimensiona barra e entreperna |

### Diferencas por versao

**Masculino (principal):** gancho fundo, quadril mais neutro, forro opcional, cos com cord.  
**Adaptacao feminino:** gancho frente mais raso, quadril com folga maior (+2 cm), comprimento opcional mais longo, forro mais frequente.  
**Unissex:** gancho intermediario, quadril neutro, sem forro obrigatorio, abertura de perna simples.

### Transformacoes de design possiveis

1. "Quero transformar em short 5 polegadas de corrida com forro compressao integrado" — encurta comprimento lateral para 14 cm, adiciona forro de malha compressao cortado 1 cm mais curto, insere abertura de perna com elastico fino de 0,6 cm.
2. "Quero adicionar painel lateral de malha mesh para ventilacao" — substitui a costura lateral por painel de 6 cm de mesh perfurado correndo da cintura ate a barra.
3. "Quero transformar em short bermuda estilo boardshort com cordao e sem elastico costas" — aumenta comprimento para 45 cm, remove elastico de costas, adiciona braguilha falsa frente e cord de ajuste na frente do cos.

---

## BASE 04 — Camiseta Basica Gola Redonda

**Familia:** superior / camiseta  
**Variantes contempladas:** fitted, regular e oversized descritas como sub-bases

### ICP de uso

Quem usa: qualquer perfil PHYLLOS — usada como camada de base, peça unica ou layer.  
Quando: treino de baixa a media intensidade, deslocamento, trabalho informal, fim de semana.  
Como: sozinha, por dentro de blazer, sob camisa aberta.

### Medidas-chave e folgas por tipo de tecido

Corpo-base: tamanho M, altura 168/175 cm.

| Regiao | Corpo fem. M | Corpo masc. M | Folga fitted | Folga regular | Folga oversized |
|---|---:|---:|---:|---:|---:|
| Busto / peito | 94 cm | 100 cm | +2 cm | +8 cm | +20 cm |
| Cintura na peca | 74 cm | 82 cm | +2 cm | +10 cm | +22 cm |
| Quadril na peca | 100 cm | 100 cm | +4 cm | +12 cm | +24 cm |
| Largura de ombro | 39 cm | 44 cm | -1 cm | 0 | +4 cm |
| Cava (altura) | 20 cm | 22 cm | -1 cm | 0 | +3 cm |
| Manga (comprimento) | 60 cm | 65 cm | 0 | 0 | +5 cm |
| Comprimento corpo | 60 cm | 65 cm | -2 cm | 0 | +8 cm |
| Largura gola | 6 cm rente | 6 cm rente | 0 | 0 | +1 cm |

**Formula largura de ombro para oversized:**  
`ombro_molde = ombro_corpo + folga_oversized / 4`  
(cai fora do ombro real, intencional)

**Formula largura de manga:**  
`manga_base = (cava_molde / 2) + folga_tecido`

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente | volume de busto e abdomen | eixo vertical | ombro, lateral, cava |
| Costas | volume de costas | eixo vertical | ombro, lateral, cava |
| Manga (x2) | cobertura de braco | eixo vertical de manga | cava, barra de manga |
| Gola (tubo ou nervura) | acabamento de gola | perpendicular ao comprimento da gola | costura de fechamento |

**Variante sem manga:** remove painel de manga; cava recebe acabamento de nervura ou virada simples.  
**Variante sleeveless crop:** encurta corpo, remove manga, cava mais funda +3 cm.

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Silhueta | `fitted / regular / oversized` | redimensiona todos os pontos de largura |
| Manga | `sem manga / manga curta / manga 3/4 / manga comprida` | muda comprimento do painel de manga |
| Gola | `nervura fina 1,5 cm / nervura larga 3 cm / gola dobrada` | muda altura e costura do painel de gola |
| Comprimento | `cropped / regular / longo / maxi` | muda comprimento do painel de corpo |
| Costura | `lateral / lateral e ombro / tubular (costura unica)` | reorganiza onde as emendas ficam |
| Recorte de cava | `classica / cava funda / cava americana / raglan` | altera formato do painel de manga e cava |

### Diferencas por versao

**Feminino:** cava levemente mais curta, estreitamento suave na cintura (mesmo em regular), gola sem diferenca.  
**Masculino:** ombro maior, cava mais rasa, sem estreitamento de cintura em nenhuma silhueta.  
**Unissex:** ombro intermediario, silhueta tubular sem estreitamento, comprimento padrao masculino.

### Transformacoes de design possiveis

1. "Quero uma camiseta de manga curta com recorte raglan e contraste de cor no ombro e manga" — substitui a cava classica por linha diagonal de raglan, separando frente e costas em dois paineis cada, com manga integrada ao raglan.
2. "Quero transformar em camiseta de corrida com painel de mesh nas costas inteiras" — substitui o painel de costas por malha mesh vazada, mantendo frente em jersey principal.
3. "Quero uma long tee oversized com fenda lateral de 12 cm na barra" — aumenta comprimento corpo +8 cm, insere fenda aberta nas laterais a partir da barra, aplica vivo duplo de 0,5 cm na abertura.

---

## BASE 05 — Camisa Social Base

**Familia:** superior / camisa  
**Variantes contempladas:** feminino, masculino, unissex; sem pinces como padrao

### ICP de uso

Quem usa: pessoa que trabalha em ambiente com algum codigo de vestimenta (reunioes, cliente, conferencia) e precisa de camisa que nao exija cuidado excessivo.  
Quando: dia de trabalho inteiro, viagem de negocios, evento casual-formal.  
Como: por dentro de calca reta ou jogger estruturado; aberta sobre camiseta; com blazer leve.

### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo fem. M | Corpo masc. M | Folga plano | Folga tecnico stretch |
|---|---:|---:|---:|---:|
| Busto / peito | 94 cm | 100 cm | +10 cm | +4 cm |
| Cintura na peca | 74 cm | 82 cm | +12 cm | +6 cm |
| Quadril na peca | 100 cm | 100 cm | +12 cm | +6 cm |
| Ombro | 39 cm | 44 cm | 0 | 0 |
| Manga comprida | 60 cm | 65 cm | +2 cm | +1 cm |
| Largura puno | 16 cm | 20 cm | 0 | 0 |
| Comprimento corpo frente | 65 cm | 75 cm | 0 | 0 |
| Comprimento corpo costas | 67 cm | 76 cm | 0 | 0 |

**Regra de caimento reto (sem pinces):**  
A largura da cintura no molde e igual a largura do busto — sem reducao na cintura. Isso garante caimento reto em todos os tipos de corpo sem necessidade de pence.

**Formula de cava camisa:**  
`altura_cava = (comprimento_ombro_a_busto * 0,52) + 2 cm de facilidade`

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente direita | volume frente + abertura de botao | eixo vertical | ombro, lateral, cava, barra |
| Frente esquerda | volume frente + casa de botao | eixo vertical | ombro, lateral, cava, barra |
| Costas (1 peca ou com cala) | volume de costas + movimento | eixo vertical | ombro, lateral, cava |
| Manga (x2) | cobertura de braco + puno | eixo vertical de manga | cava, puno |
| Puno (x2) | acabamento e botao de puno | perpendicular | costura de fechamento |
| Gola (colarinho + base) | estrutura de colarinho | paralelo | costura de montagem |
| Plastrao frente (opcional) | estabilidade da abertura de botao | eixo vertical | integrado na frente |

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Colarinho | `classico / padre / mao / band collar` | muda painel de gola; band collar remove ponta |
| Puno | `simples botao / duplo (frances) / elastico` | muda painel de puno |
| Manga | `comprida / 3/4 / curta` | encurta painel de manga |
| Barra | `reta / arredondada / cortada assimetrica` | muda contorno inferior dos paineis de frente |
| Costas | `lisa / cala central / yoke com cala` | adiciona painel de yoke nas costas e franzido abaixo |
| Bolso | `nenhum / bolso peitoral esquerdo simples` | adiciona painel aplicado na frente esquerda |
| Abertura | `frente total / frente parcial 30 cm` | define comprimento da abertura com botoes |

### Diferencas por versao

**Feminino:** ombro discretamente mais estreito, barra arredondada como padrao, colarinho ligeiramente menor.  
**Masculino:** ombro maior, barra reta como padrao, colarinho classsico, puno duplo opcao padrao.  
**Unissex:** ombro intermediario, barra reta, sem pinces, colarinho band collar como padrao para neutralidade.

### Transformacoes de design possiveis

1. "Quero uma camisa com abertura dupla (botoes frente e costas), tecido de algodao tecnico" — adiciona segunda abertura centralizada nas costas espelhando a frente, ambas com plastrao interno de entretela leve.
2. "Quero transformar em camisa cropped oversized com ombro caidico e barra assimetrica" — aumenta folga de ombro +8 cm, encurta corpo frente para 52 cm e costas para 60 cm, define barra com desnivel de 8 cm frente-costas.
3. "Quero adicionar recorte de painel contrastante na cava e parte superior das costas" — insere linha de corte horizontal 8 cm abaixo da costura de ombro nas costas e frente, separando yoke superior em tecido contrastante.

---

## BASE 06 — Moletom / Sweatshirt

**Familia:** superior / moletom  
**Variantes contempladas:** sem capuz (crew neck) como base; com capuz como variante descrita

### ICP de uso

Quem usa: qualquer perfil PHYLLOS em transicao de clima, pos-treino, trabalho em casa ou deslocamento urbano.  
Quando: manha fria, saida pos-treino, trabalho remoto, final de semana.  
Como: com calca jogger, calca reta ou saia — funciona como layer externo leve.

### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo base M | Folga regular | Folga oversized | Reducao elastica (ribana) |
|---|---:|---:|---:|---:|
| Busto | 94/100 cm | +12 cm | +24 cm | — |
| Cintura na peca | 74/82 cm | +12 cm | +24 cm | — |
| Quadril na peca | 100 cm | +12 cm | +24 cm | — |
| Ombro | 39/44 cm | 0 | +5 cm | — |
| Manga comprida | 60/65 cm | +2 cm | +5 cm | — |
| Punho (ribana) | 16/20 cm | 0 | 0 | -5 a -7 cm |
| Barra corpo (ribana) | 74/82 cm | +4 cm | +4 cm | -6 a -8 cm |
| Comprimento corpo | 60/65 cm | 0 | +6 cm | — |

**Formula da ribana de punho:**  
`comprimento_ribana_molde = circunferencia_puno_corpo`  
`comprimento_elastico_costurado = circunferencia_puno_corpo - 5 cm`

**Formula da ribana de barra:**  
`comprimento_ribana_molde = (busto_molde / 2) + 2 cm de emenda`  
`comprimento_ribana_costurado = comprimento_ribana_molde - 7 cm`

### Arquitetura de paineis — versao crew neck

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente | volume principal | eixo vertical | ombro, lateral, cava |
| Costas | volume de costas | eixo vertical | ombro, lateral, cava |
| Manga (x2) | cobertura de braco | eixo vertical de manga | cava, puno |
| Ribana de puno (x2) | acabamento de punho | perpendicular | costura circular |
| Ribana de barra | acabamento inferior | perpendicular | costura circular |
| Ribana de gola (crew neck) | acabamento de gola | perpendicular | costura circular de gola |

### Arquitetura adicional para variante com capuz

| Painel adicional | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Capuz frente (x2) | volume e conforto do capuz | eixo vertical do capuz | costura central de capuz, costura de montagem no pescoco |
| Capuz costas (1 peca) | fechamento traseiro do capuz | eixo vertical | costura central de capuz |
| Cord ou elastico de fechamento | ajuste de abertura | — | casa de cord na borda do capuz |

**Formula do capuz:**  
`altura_capuz = (cabeca_comprimento_frente_a_nuca + 6 cm) * 1,05`  
`largura_capuz = (circunferencia_cabeca / 2) + 3 cm`

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Gola | `crew neck / capuz / gola alta dobrada / gola roll` | adiciona ou substitui painel de gola/capuz |
| Silhueta | `regular / oversized / cropped` | redimensiona todos os paineis de corpo e manga |
| Abertura | `pullover / ziper total frente / ziper 1/4` | adiciona abertura e painel de plastrao no frente |
| Bolso | `nenhum / kangaroo frente / bolso lateral` | adiciona recorte e paineis de bolso |
| Ribana | `com ribana classica / sem ribana barra dobrada` | substitui ribana por barra dobrada simples |
| Manga | `comprida / 3/4 / sem manga` | altera comprimento de manga; sem manga adiciona acabamento de cava |

### Diferencas por versao

**Feminino:** estreitamento leve de ombro, comprimento de corpo opcao cropped como variante principal, ribana de barra mais estreita.  
**Masculino:** ombro mais largo, corpo mais longo, capuz com abertura maior, cord mais espesso.  
**Unissex:** silhueta oversized neutraliza as diferencas; capuz e ombro em medida intermediaria.

### Transformacoes de design possiveis

1. "Quero um moletom com recorte de painel nas costas em tecido diferente, tipo color block vertical" — divide as costas em dois paineis verticais por uma costura central, cada lado em tecido ou cor diferente.
2. "Quero transformar em sweatshirt com capuz e bolso canguru dividido em dois compartimentos" — adiciona capuz conforme variante descrita + bolso canguru com divisoria central costurada formando dois bolsos independentes.
3. "Quero um moletom crop assimetrico, barra mais curta na frente e mais longa nas costas, sem ribana" — encurta frente para 52 cm, mantem costas em 60 cm, substitui ribana por barra dobrada simples com desnivel frontal.

---

## BASE 07 — Saia Reta Midi

**Familia:** inferior / saia  
**Variantes contempladas:** feminino como base; adaptacao unissex descrita

### ICP de uso

Quem usa: pessoa que trabalha, sai a noite ou circula em ambientes mistos e quer uma peca inferior que combine com camiseta, camisa ou blusa estruturada.  
Quando: dia de trabalho, evento semi-formal, jantar, deslocamento urbano.  
Como: com camisa aberta, camiseta fitted ou blusa de malha; sapato, sandalia ou tenis clean.

### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo base M | Folga plano | Folga malha | Folga tecnico |
|---|---:|---:|---:|---:|
| Cintura | 74 cm | +2 cm | +1 cm | +1 cm |
| Quadril maior | 100 cm | +4 cm | +2 cm | +3 cm |
| Comprimento lateral | 70 cm (midi) | 0 | 0 | 0 |
| Largura de barra | igual ao quadril | + 0 cm reta | +2 cm | +1 cm |

**Regra midi:** comprimento de 65 a 75 cm, medido da cintura. Ajustavel por descricao do usuario.

**Formula de abertura de barra para saia reta:**  
`barra_molde = quadril_molde` (mantida — sem alargamento no corte reto)

**Regra de fechamento:** saia reta exige fechamento; padrao e ziper invisivel na costura lateral esquerda de 22 cm.

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente | volume de abdomen e quadril frente | eixo vertical | lateral, cos/cintura |
| Costas | volume de quadril e gluteo | eixo vertical | lateral, cos/cintura, ziper |
| Cos frente | estabilidade visual | paralelo | lateral, cintura |
| Cos costas | estabilidade e ziper | paralelo | lateral, cintura, ziper |

**Variante sem cos:** barra de cintura acabada com virada de 1,5 cm ou elastico embutido.

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Comprimento | `mini (45 cm) / midi (70 cm) / maxi (95 cm)` | muda comprimento do painel e barra |
| Abertura de barra | `reta / levemente alargada / franzida` | muda ponto de barra frente e costas |
| Fechamento | `ziper invisivel lateral / ziper costas / elastico total` | altera posicao do ziper e cos |
| Fenda | `nenhuma / fenda costas / fenda lateral` | adiciona abertura no painel correspondente |
| Bolso | `nenhum / bolso faca oculto na lateral` | adiciona painel de bolso na costura lateral |
| Cintura | `cos costurado / sem cos / elastico embutido` | altera painel de cintura |

### Diferencas por versao

**Feminino (base):** curva de quadril acentuada, diferenca de cintura para quadril de 26 cm como padrao, fenda mais frequente.  
**Adaptacao unissex:** curva de quadril mais neutra, diferenca cintura-quadril de 18 cm, elastico total na cintura, sem fenda como padrao.

### Transformacoes de design possiveis

1. "Quero transformar em saia envelope com sobreposicao de duas frentes cruzadas na frente" — divide o painel de frente em dois paineis triangulares sobrepostos com fechamento por amarracao ou broche oculto; costas em peca unica.
2. "Quero uma saia midi com fenda frontal central de 30 cm, tecido de alfaiataria" — insere abertura no eixo central do painel de frente de 30 cm a partir da barra, com acabamento de vivo duplo de 0,5 cm.
3. "Quero transformar em saia midi assimetrica, barra em diagonal de 50 cm na frente a 80 cm nas costas" — redesenha a barra como curva diagonal; comprimento de frente = 50 cm, costas = 80 cm, diferenca absorvida em curva suave na costura lateral.

---

## BASE 08 — Blazer Desconstruido

**Familia:** externo / blazer  
**Variantes contempladas:** feminino, masculino, unissex

### ICP de uso

Quem usa: pessoa que precisa sinalizar autoridade ou apresentacao profissional sem abrir mao de conforto em deslocamento ou dia longo.  
Quando: reuniao presencial, evento, viagem de negocios, situacao em que a camiseta sozinha nao e suficiente.  
Como: sobre camiseta, camisa ou moletom fino; com calca reta, jogger estruturado ou saia midi.

### Medidas-chave e folgas por tipo de tecido

| Regiao | Corpo fem. M | Corpo masc. M | Folga plano desconstruido | Folga tecnico desconstruido |
|---|---:|---:|---:|---:|
| Busto / peito | 94 cm | 100 cm | +8 cm | +5 cm |
| Cintura na peca | 74 cm | 82 cm | +8 cm | +5 cm |
| Quadril na peca | 100 cm | 100 cm | +10 cm | +6 cm |
| Ombro | 39 cm | 44 cm | +1 cm | +0,5 cm |
| Manga comprida | 60 cm | 65 cm | +2 cm | +1,5 cm |
| Comprimento corpo | 68 cm | 74 cm | 0 | 0 |
| Cava (altura) | 22 cm | 24 cm | +1 cm | +0,5 cm |

**Definicao de desconstruido no molde:**
- sem entretela pesada — entretela fusivel leve ou termocolante de gramatura < 50 g/m2;
- sem ombreiras;
- sem forro pesado — forro solto de viscose ou bemberg se necessario, ou sem forro;
- solapas e lapela existem mas sem espinha interna rigida;
- costura de ombro estabilizada por fita de tecido, nao entretela de ombro.

**Formula de lapela:**  
`comprimento_lapela = comprimento_corpo_frente * 0,4`  
`largura_lapela_base = 6 cm` (ajustavel por descricao)

### Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura |
|---|---|---|---|
| Frente (x2) | volume frente + lapela integrada | eixo vertical | ombro, lateral, cava, abertura central |
| Frente lateral (x2, opcional) | define caimento e bolso peitoral | eixo vertical | costura de princess frente |
| Costas (1 peca ou com costura central) | volume de costas | eixo vertical | ombro, lateral, cava |
| Costas lateral (x2) | caimento de costas | eixo vertical | costura de princess costas |
| Manga (x2) | cobertura de braco | eixo vertical de manga | cava, barra de manga |
| Manga de baixo (x2) | manga 2 pecas | eixo vertical | costura interna de manga |
| Lapela / revers | acabamento de abertura | eixo de lapela | costura de gola + lapela |
| Gola (se houver) | acabamento do pescoco | paralelo | costura de montagem |
| Bolso peitoral (opcional) | detalhe visual | eixo vertical | aplicado na frente esquerda |
| Bolso inferior (x2, opcional) | funcionalidade | eixo horizontal | aplicado ou de embutir |
| Forro (opcional, x4) | conforto interno | eixo vertical | costura independente do forro |

### Parâmetros variaveis

| Parametro | Valores possiveis | Impacto no molde |
|---|---|---|
| Lapela | `sem lapela (collarless) / lapela classsica / lapela xale` | define formato do painel de frente e revers |
| Comprimento | `cropped (52 cm) / padrao (68 cm) / longo (85 cm)` | muda comprimento do painel de frente e costas |
| Botoes | `sem botao / 1 botao / 2 botoes / duplo` | define marcacao de casa e botao; duplo adiciona largura de frente |
| Manga | `manga comprida / 3/4 / sem manga (colete)` | remove painel de manga; colete fecha cava com acabamento |
| Costura de princess | `sem princess (reto) / com princess frente / com princess frente e costas` | adiciona paineis laterais, permite cintura levemente definida sem pence |
| Bolso | `nenhum / peitoral / inferior embutido / inferior de ressalto` | adiciona paineis de bolso |
| Forro | `sem forro / forro parcial costas / forro total` | adiciona estrutura de forro independente |
| Entretela | `minima (lapela + ombro) / standard desconstruido / nenhuma` | define lista de pinos de termocolante |

### Diferencas por versao

**Feminino:** cava ligeiramente mais curta, comprimento padrao de 68 cm, lapela xale como opcao principal, costura de princess com leve definicao de cintura de +2 cm.  
**Masculino:** ombro 1 cm maior, cava mais profunda, comprimento de 74 cm, lapela classsica como opcao principal, sem reducao de cintura no caimento reto.  
**Unissex:** ombro intermediario, sem princess (corte reto), lapela collarless ou classsica mini, comprimento de 70 cm, sem definicao de cintura.

### Transformacoes de design possiveis

1. "Quero um blazer desconstruido sem lapela, sem botao, tecido de malha dupla com acabamento de borda viva" — remove painel de lapela e gola, fecha a frente em linha reta sem sobreposicao, aplica borda cortada a fio sem virada (funciona em tecido que nao desfria).
2. "Quero transformar em colete desconstruido com costas em malha tecnica e frente em tecido plano" — remove paineis de manga, fecha cava com ribana de 2 cm, substitui paineis de costas por malha tecnica de 4 vias, mantem frente em tecido plano principal.
3. "Quero adicionar detalhe de manga destacavel por ziper, transformando blazer em colete quando necessario" — insere ziper de dois vias na linha da cava, criando separacao funcional entre manga e corpo; cada manga recebe acabamento de ziper e remate independente.

---

## Tabela-resumo do Catalogo

| ID | Nome base | Familia | Genero base | Sub-bases |
|---|---|---|---|---|
| BASE 01 | Calca Reta Classica | inferior / calca | fem / masc / unissex | fitted, regular |
| BASE 02 | Calca Jogger / Elastico Total | inferior / calca | fem / masc / unissex | afunilado, relaxado |
| BASE 03 | Shorts Masculino Funcional | inferior / shorts | masc / adaptacao unissex | curto, medio, longo |
| BASE 04 | Camiseta Basica Gola Redonda | superior / camiseta | fem / masc / unissex | fitted, regular, oversized |
| BASE 05 | Camisa Social Base | superior / camisa | fem / masc / unissex | caimento reto |
| BASE 06 | Moletom / Sweatshirt | superior / moletom | fem / masc / unissex | crew neck, capuz |
| BASE 07 | Saia Reta Midi | inferior / saia | fem / adaptacao unissex | mini, midi, maxi |
| BASE 08 | Blazer Desconstruido | externo / blazer | fem / masc / unissex | cropped, padrao, longo, colete |

---

## Regras globais de graduacao

Validas para todas as bases. Ajuste por tamanho (de P a GG, intervalo de um tamanho):

| Regiao | Variacao por tamanho |
|---|---|
| Busto / peito | +/- 4 cm total |
| Cintura | +/- 4 cm total |
| Quadril | +/- 4 cm total |
| Ombro | +/- 1 cm total |
| Coxa (pecas inferiores) | +/- 2 cm total |
| Comprimento de corpo | manter constante por grade regular; criar grade de altura separada |
| Comprimento de manga | manter constante por grade regular; criar grade de manga separada |
| Gancho profundidade | +/- 0,4 cm por tamanho |

Distribuicao padrao de ganho de busto / peito:
- 30% em costura lateral frente;
- 30% em costura lateral costas;
- 20% em cava;
- 20% em ajustes de ombro e costura de princess se existir.

---

## Regras de margem de costura globais

Estas margens se aplicam a todas as bases salvo indicacao contraria na ficha de cada peca:

| Regiao | Margem |
|---|---|
| Costuras laterais | 1,5 cm |
| Ombro | 1,2 cm |
| Cava | 1,0 cm |
| Entreperna | 1,2 cm |
| Gancho | 1,2 cm |
| Cintura para cos | 1,0 cm |
| Gola / pescoco | 0,7 cm |
| Barra de corpo | 3,0 cm padrao; 4,0 cm em pecas pesadas |
| Barra de manga | 2,5 cm padrao |
| Abertura de bolso | 0,7 cm |

---

## Proximas lacunas a preencher

Os seguintes dados nao estavam disponiveis na criacao deste catalogo e devem ser coletados antes de qualquer piloto fisico:

1. Medidas reais de corpo-alvo PHYLLOS (mapa dimensional por tamanho P, M, G, GG, separado por fem/masc/unissex).
2. Comportamento real dos tecidos assumidos (elasticidade em urdume, trama e vies; recuperacao pos-tensao).
3. Encolhimento pos-lavagem por familia de tecido.
4. Preferencias de fechamento confirmadas por ICP (pesquisa ou entrevista).
5. Validacao de comprimentos por grade de altura (baixa / media / alta), especialmente para calcas e saias.
6. Definicao de grade de tamanhos e nomenclatura final PHYLLOS (P/M/G/GG ou numerica).
