# Molde v0 - Calca Performance Alfaiataria PHYLLOS

Referencia aplicada: `.claude/agents/references/patternmaking-geometric-algorithmic-principles.md`

Ilustracao tecnica: [illustrations/calca-performance-alfaiataria-molde-v0.svg](illustrations/calca-performance-alfaiataria-molde-v0.svg)

Visualizacao interativa recomendada: [calca-performance-molde-interativo.html](calca-performance-molde-interativo.html)

## Como ler o desenho tecnico

O desenho agora segue uma leitura de modelagem, nao uma ilustracao de roupa pronta.

| Termo no desenho | O que significa | Como medir |
|---|---|---|
| Altura | distancia vertical de uma linha a outra | medir no eixo `y`, de cima para baixo |
| Largura | distancia horizontal entre dois pontos do molde | medir no eixo `x`, da linha interna para a lateral |
| Altura lateral | comprimento pela lateral da calca, da cintura ate a barra | 106 cm no corpo-base |
| Entreperna | comprimento interno da perna, do gancho ate a barra | 76 cm no corpo-base |
| Linha do quadril | linha horizontal onde o molde atinge volume de quadril | 20 cm abaixo da cintura |
| Linha do gancho | profundidade onde o gancho encontra a coxa | 27,5 cm na frente; 29 cm nas costas |
| Extensao de gancho | quanto o gancho avanca horizontalmente para dentro da perna | 4,5 cm na frente; 8,5 cm nas costas |
| Coxa | largura horizontal na linha do gancho/coxa alta | 30,5 cm frente; 33,5 cm costas, em meia peca |
| Joelho | largura horizontal na linha do joelho | 23,5 cm frente; 24,5 cm costas, em meia peca |
| Barra | largura horizontal na boca da perna | 23,5 cm frente; 24,5 cm costas, em meia peca |

Observacao importante: as larguras da frente e das costas sao **meias medidas de molde**. Para chegar na circunferencia pronta, soma-se frente direita + frente esquerda + costas direita + costas esquerda, descontando o que entra em costura.

## 1. Objetivo da peca

Transformar a descricao "calca preta de alfaiataria performance, cintura alta, crepe com elastano, perna reta, bolso faca, frente limpa e elastico embutido nas costas" em uma primeira receita de molde 2D.

Resultado esperado: calca de tecido plano com elastano, aparencia de alfaiataria, conforto sentado, mobilidade para deslocamento/trabalho e acabamento limpo.

Limite: este molde v0 e estudo parametrico. Nao substitui modelista, prova fisica, piloto nem ajuste em corpo real.

## 2. Corpo-alvo e medidas usadas

Base assumida: tamanho M PHYLLOS preliminar.

| Regiao | Medida corporal |
|---|---:|
| Altura | 168 cm |
| Cintura natural | 74 cm |
| Cintura alta da peca | 72 cm |
| Quadril maior | 100 cm |
| Coxa alta | 58 cm |
| Joelho | 39 cm |
| Tornozelo | 24 cm |
| Gancho total sentado | 69 cm |
| Profundidade de gancho | 27 cm |
| Entreperna | 76 cm |
| Comprimento lateral desejado | 106 cm |

## 3. Medidas ausentes

- inclinacao pélvica;
- altura exata do quadril alto;
- distancia cintura-frente ate cintura-costas passando pelo gancho;
- assimetria de quadril/gluteo;
- elasticidade real do tecido no urdume, trama e vies;
- encolhimento apos lavagem;
- transparencia sob tensao.

## 4. Tecido e comportamento esperado

Tecido assumido: crepe com elastano, 220-280 g/m2, elasticidade principal na trama.

Decisoes:

- linha de fio vertical no eixo da perna;
- maior elasticidade orientada no contorno do corpo;
- folga positiva pequena, sem compressao;
- frente limpa sem franzido;
- elasticidade de conforto concentrada no cos costas.

## 5. Familia, base e componentes

Familia: inferior, calca.

Base escolhida: calca base de alfaiataria confortavel, perna reta.

Componentes obrigatorios:

- frente direita/esquerda;
- costas direita/esquerda;
- cos frente limpo;
- cos costas com canal de elastico embutido;
- bolso faca com saco de bolso e espelho;
- braguilha ou fechamento lateral invisivel a decidir no piloto;
- bainha invisivel.

## 6. Medida final por regiao

Formula aplicada:

```text
medida_final = corpo + folga_de_vestibilidade + folga_de_movimento - reducao_elastica
```

| Regiao | Corpo | Folga | Reducao elastica | Medida final | Tolerancia |
|---|---:|---:|---:|---:|---:|
| Cintura alta | 72 | +4 | 0 | 76 | +/- 0,7 |
| Cintura expandida costas | 72 | +8 | 0 | 80 | +/- 1,0 |
| Quadril | 100 | +6 | 0 | 106 | +/- 1,0 |
| Coxa alta | 58 | +6 | 0 | 64 | +/- 1,0 |
| Joelho | 39 | +9 | 0 | 48 | +/- 0,8 |
| Barra | 24 | +24 | 0 | 48 | +/- 0,8 |
| Profundidade de gancho | 27 | +1,5 | 0 | 28,5 | +/- 0,5 |
| Entreperna | 76 | 0 | 0 | 76 | +/- 0,7 |
| Comprimento lateral | 106 | 0 | 0 | 106 | +/- 0,7 |

## 7. Mapa de volume 3D para solucao 2D

| Volume 3D | Problema geometrico | Solucao 2D |
|---|---|---|
| Cintura menor que quadril | Diferenca precisa ser absorvida sem franzir a frente | lateral + pence costas + cos anatomico |
| Gluteo | Costas precisam de mais extensao horizontal de gancho | curva de gancho costas mais longa e funda |
| Abdomen sentado | Frente nao pode cortar ou repuxar | folga de gancho + frente sem pence profunda |
| Coxa em movimento | Caminhar e sentar exigem folga | coxa final 64 cm e entreperna com curva suave |
| Cintura de conforto | Ajuste precisa variar sem parecer esportivo | elastico apenas no cos costas |
| Bolso funcional | Abertura nao pode abrir ou deformar quadril | bolso faca preso no cos e lateral com espelho estavel |

## 8. Arquitetura de paineis

| Painel | Funcao | Linha de fio | Par de costura | Piques |
|---|---|---|---|---|
| Frente | aparencia limpa e bolso faca | eixo vertical da perna | lateral, entreperna, gancho frente | cintura, quadril, joelho, bolso |
| Costas | acomodar gluteo e elastico | eixo vertical da perna | lateral, entreperna, gancho costas | cintura, quadril, joelho |
| Cos frente | estabilidade visual | paralelo ao comprimento | lateral, cintura frente | centro frente, lateral |
| Cos costas | ajuste por elastico | paralelo ao comprimento | lateral, cintura costas | centro costas, lateral, canal |
| Saco de bolso | funcionalidade interna | fio reto conforme frente | abertura bolso, lateral, cos | boca do bolso |
| Espelho de bolso | acabamento da abertura | fio reto | saco de bolso, lateral | boca do bolso |

## 9. Coordenadas do molde base sem margem

Sistema: coordenadas em centimetros. Origem no topo do centro da peca. `x` cresce para fora do corpo. `y` cresce para baixo.

### Frente - meia peca

Medidas distribuidas:

- cintura frente meia: 18,5 cm;
- quadril frente meia: 25,5 cm;
- coxa frente meia: 30,5 cm;
- joelho frente meia: 23,5 cm;
- barra frente meia: 23,5 cm;
- profundidade de gancho frente: 27,5 cm;
- extensao de gancho frente: 4,5 cm.

Pontos:

| Ponto | x | y | Observacao |
|---|---:|---:|---|
| F0 | 0 | 0 | cintura centro frente |
| F1 | 18,5 | 0 | cintura lateral frente |
| F2 | 25,5 | 20 | quadril lateral |
| F3 | 30,5 | 27,5 | coxa/gancho lateral |
| F4 | 4,5 | 27,5 | ponta do gancho frente |
| F5 | 3,0 | 76 | entreperna na barra |
| F6 | 23,5 | 76 | lateral na barra |
| F7 | 3,5 | 52 | joelho entreperna |
| F8 | 23,5 | 52 | joelho lateral |

Curvas:

- gancho frente: F0 desce levemente para F4, com curva concava suave entre y=16 e y=27,5;
- quadril lateral: F1 -> F2 -> F3 com curva progressiva, sem quina;
- entreperna: F4 -> F7 -> F5, suavizar para nao criar bico no gancho.

### Costas - meia peca

Medidas distribuidas:

- cintura costas meia antes de elastico: 19,5 cm;
- cintura costas expandida meia: 21,5 cm;
- quadril costas meia: 27,5 cm;
- coxa costas meia: 33,5 cm;
- joelho costas meia: 24,5 cm;
- barra costas meia: 24,5 cm;
- profundidade de gancho costas: 29 cm;
- extensao de gancho costas: 8,5 cm.

Pontos:

| Ponto | x | y | Observacao |
|---|---:|---:|---|
| C0 | 0 | 0 | cintura centro costas |
| C1 | 19,5 | 0 | cintura lateral costas |
| C2 | 27,5 | 20 | quadril lateral costas |
| C3 | 33,5 | 29 | coxa/gancho lateral |
| C4 | 8,5 | 29 | ponta do gancho costas |
| C5 | 3,0 | 76 | entreperna na barra |
| C6 | 24,5 | 76 | lateral na barra |
| C7 | 4,0 | 52 | joelho entreperna |
| C8 | 24,5 | 52 | joelho lateral |

Curvas:

- gancho costas: C0 -> C4 com curva mais funda que a frente, preservando conforto sentado;
- centro costas sobe +1,5 cm acima de C0 na peca final para acomodar gluteo;
- entreperna: C4 -> C7 -> C5, curva longa sem angulo fechado.

## 10. Transformacoes de design

### Cintura alta

Impacto no molde:

- subir linha de cintura 3 cm acima da cintura natural;
- cos de 4 cm pronto;
- centro costas com leve subida extra para cobertura sentada.

### Frente limpa

Impacto no molde:

- sem elastico na frente;
- pence frente opcional maxima de 1 cm se prova indicar excesso no abdomen;
- fechamento deve ficar discreto: braguilha limpa ou ziper lateral invisivel.

### Elastico embutido nas costas

Impacto no molde:

- cos costas cortado com comprimento expandido de 43 cm total;
- elastico final sugerido 36-38 cm, conforme tensao real;
- canal interno de 3 cm + margem de virada.

### Bolso faca

Impacto no molde:

- boca do bolso: 14 cm, iniciando 3 cm abaixo do cos e 3 cm da lateral;
- saco de bolso preso no cos para estabilidade;
- espelho acompanha abertura para nao revelar forro ao caminhar.

## 11. Molde de corte - margens e marcas

Margens:

- laterais: 1,5 cm;
- entreperna: 1,2 cm;
- gancho: 1,2 cm;
- cintura para aplicar cos: 1,0 cm;
- boca de bolso: 0,7 cm;
- bainha: 4,0 cm;
- cos: 1,0 cm em unioes; 0,7 cm em fechamento interno.

Piques:

- centro frente;
- centro costas;
- lateral na linha de quadril;
- lateral na linha de joelho;
- entreperna frente/costas;
- inicio e fim da boca do bolso;
- centro do cos frente e costas;
- limite do canal de elastico.

## 12. Partes do molde

| Peca | Quantidade | Tecido |
|---|---:|---|
| Frente da calca | cortar 2 espelhadas | tecido principal |
| Costas da calca | cortar 2 espelhadas | tecido principal |
| Cos frente | cortar 1 par ou 1 na dobra | tecido principal + entretela leve |
| Cos costas | cortar 1 par ou 1 na dobra | tecido principal |
| Saco de bolso | cortar 2 pares | forro fino ou tecido principal leve |
| Espelho de bolso | cortar 2 | tecido principal |

## 13. Sequencia operacional resumida

1. Preparar bolsos faca: unir saco + espelho, pespontar boca.
2. Fixar bolso na frente pelo cos e lateral.
3. Fechar pences costas se usadas.
4. Fechar gancho frente e gancho costas.
5. Unir entrepernas.
6. Fechar laterais, conferindo bolso e piques de quadril/joelho.
7. Preparar cos frente limpo e cos costas com canal.
8. Aplicar cos na calca.
9. Inserir elastico costas, distribuir tensao e travar nas laterais.
10. Fazer prova funcional antes da bainha definitiva.
11. Executar bainha invisivel.

## 14. Validacao numerica antes do piloto

Checklist:

- cintura pronta relaxada: 76 cm;
- cintura expandida: 80 cm;
- quadril pronto: 106 cm;
- coxa pronta: 64 cm;
- barra pronta: 48 cm;
- costura lateral frente/costas com mesmo comprimento;
- entreperna frente/costas compativeis, com easing minimo se necessario;
- bolso nao abre em pe;
- gancho nao repuxa sentado;
- linha de fio vertical permanece perpendicular a barra;
- bainha esquerda/direita com mesma altura.

## 15. Testes de mobilidade

Obrigatorios no piloto:

- em pe, postura neutra;
- sentar em cadeira;
- caminhar 20 passos;
- agachar leve;
- subir um degrau;
- colocar maos nos bolsos;
- simular 2 horas sentada: verificar compressao no abdomen e repuxo no gancho.

## 16. Riscos de piloto

| Risco | Causa provavel | Ajuste previsto |
|---|---|---|
| repuxo horizontal no gancho frente | extensao de gancho curta | aumentar F4 +0,5 a +1,0 cm |
| sobra sob gluteo | gancho costas longo ou curva profunda demais | reduzir C4 ou suavizar curva |
| bolso abrindo | boca muito inclinada ou quadril justo | reduzir abertura, reforcar espelho ou aumentar quadril +1 cm |
| cintura costas franzida demais | elastico curto ou tecido grosso | alongar elastico +1 a +2 cm |
| perna torcendo | linha de fio desalinhada | reposicionar eixo vertical no molde |

## 17. Regra inicial de graduacao

Base por tamanho:

- cintura: +/- 4 cm total por tamanho;
- quadril: +/- 4 cm total por tamanho;
- coxa: +/- 2 cm total por tamanho;
- barra: +/- 1 cm total por tamanho;
- gancho: ajustar profundidade +0,4 cm por tamanho acima; -0,4 cm por tamanho abaixo;
- comprimento: manter constante por grade regular; criar grade de altura separada depois.

Distribuicao:

- 35% do ganho em lateral frente;
- 35% do ganho em lateral costas;
- 20% em gancho/centro costas;
- 10% em ajuste de pence/cos.

## 18. Proximos dados a coletar

- medidas reais de corpo-alvo PHYLLOS;
- elasticidade do crepe em trama e urdume;
- recuperacao apos 30 minutos de tensao;
- foto da prova em pe/sentada;
- preferencia de fechamento: braguilha limpa ou ziper lateral;
- largura final de barra desejada por tamanho.
