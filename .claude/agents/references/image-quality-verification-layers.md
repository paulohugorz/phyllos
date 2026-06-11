# Camadas de verificacao de qualidade de imagem - Fashion OS

Esta referencia orienta o Motor de Imagens, o Prompt Compiler Fashion, o Visual Briefer e o Image Realism QA da PHYLLOS.

Problema que resolve: imagens geradas podem parecer bonitas, mas sair desalinhadas, com corpo distorcido, peca torta, costuras sem logica, bolsos inventados, barra desigual, cintura inclinada, textura errada ou caimento falso. A imagem so pode virar referencia de produto se passar por verificacao tecnica em camadas.

## Regra central

Imagem de moda para produto nao e aprovada por beleza. Ela e aprovada por fidelidade.

Toda imagem deve ser avaliada contra:

- corpo e pose;
- eixo anatomico;
- alinhamento da roupa;
- modelagem e fit;
- tecido e textura;
- construcao;
- fidelidade ao briefing;
- contexto visual;
- coerencia PHYLLOS.

Se a imagem falhar em anatomia, alinhamento estrutural da peca ou fidelidade de produto, ela deve ser reprovada mesmo que esteja visualmente atraente.

## Contrato de alinhamento antes de gerar

Antes de gerar imagem, o Prompt Compiler deve produzir um contrato minimo:

- tipo de imagem: tecnico/e-commerce, editorial, lifestyle ou prova de caimento;
- enquadramento: corpo inteiro, meio corpo, detalhe ou flat lay;
- orientacao do corpo: frente, costas, lateral, tres quartos;
- pose permitida;
- eixo do corpo: cabeca, coluna, quadril e pes coerentes;
- eixo da peca: centro frente/costas, cintura, barra, laterais e simetria;
- partes obrigatoriamente visiveis;
- partes que nao podem ser ocultadas por cabelo, mao, bolsa, sombra, dobra ou corte;
- detalhes proibidos: bolsos, ziperes, pregas, logos, costuras ou recortes nao previstos;
- negativo de alinhamento.

Sem esse contrato, a imagem nao deve ser enviada ao gerador.

## Camada 0 - Completude de entrada

Checar se existem dados suficientes:

- categoria da peca;
- silhueta;
- tecido;
- cor;
- fit;
- folgas/reducoes;
- comprimento;
- fechamento;
- bolsos;
- manga/gola/cos/barra;
- tipo de pose;
- uso da imagem;
- restricoes de marca.

Falha critica: prompt gerado com "calca elegante", "camisa moderna" ou outro termo vago sem especificar fit, tecido, eixo, pose e detalhes construtivos.

## Camada 1 - Controle de composicao

A imagem precisa facilitar verificacao.

Para imagem tecnica/e-commerce:

- corpo inteiro ou peca inteira visivel;
- camera na altura do torso/quadril, sem contra-plongee extremo;
- lente natural, sem fisheye;
- pose neutra;
- fundo simples;
- luz suficiente para ver costuras, barra, cintura e caimento;
- sem objeto cobrindo a peca.

Para imagem editorial:

- pode ter movimento e contexto, mas nao pode esconder a estrutura central da peca;
- se a pose distorce o gancho, a cava, a barra ou o cos, gerar uma variante tecnica separada.

## Camada 2 - Alinhamento anatomico

Verificar:

- cabeca proporcional ao corpo;
- ombros nivelados quando a pose pedir simetria;
- coluna sem torcao impossivel;
- quadril coerente com postura;
- bracos e maos anatomicos;
- pernas com comprimento semelhante;
- pes apoiados de forma plausivel;
- sem membros extras, dedos deformados ou articulacoes quebradas.

Falhas criticas:

- torso torcido sem coerencia;
- quadril e ombro em eixos impossiveis;
- pernas em comprimentos diferentes sem perspectiva justificavel;
- maos deformadas em area que toca ou cobre a peca;
- pose que cria falsa leitura do caimento.

## Camada 3 - Alinhamento da roupa

Verificar a peca como objeto tecnico.

### Calcas, shorts e saias

- cos horizontal ou intencionalmente inclinado conforme design;
- centro frente/costas centralizado;
- gancho sem repuxo incoerente;
- laterais descem de forma continua;
- pernas com largura e comprimento coerentes;
- barra alinhada;
- bolsos simetricos e na posicao prevista;
- zíper, braguilha ou fechamento no lugar correto.

### Camisas, blusas, tops e vestidos

- linha de ombro coerente;
- gola/decote centralizados;
- cava encaixada no corpo;
- manga esquerda e direita compativeis;
- punhos alinhados;
- pences ou recortes com direcao plausivel;
- barra regular;
- abertura frontal ou transpasse no eixo correto.

Falhas criticas:

- cos torto sem intencao;
- barra com comprimentos diferentes;
- costura lateral quebrada;
- manga de tamanhos diferentes;
- gola deslocada;
- bolso inventado;
- recorte que comeca em um lado e desaparece no outro.

## Camada 4 - Modelagem, fit e tensao

Conferir contra Fit Engine e Pattern Engine:

- folga corresponde ao briefing;
- reducao elastica nao cria compressao exagerada;
- tecido nao cola no corpo se foi definido como plano/estruturado;
- tecido nao fica rigido se foi definido como fluido;
- dobras nascem de pontos plausiveis: cotovelo, joelho, gancho, cintura, lateral, cava;
- tensao aparece onde haveria tensao real;
- movimento nao contradiz a peca.

Falhas criticas:

- tecido flutuando sem gravidade;
- calca sem gancho real;
- manga sem cava;
- cintura sem volume corporal;
- peca "pintada no corpo";
- caimento impossivel para a gramatura.

## Camada 5 - Tecido, textura e luz

Verificar:

- textura visivel e coerente;
- brilho conforme material;
- peso visual plausivel;
- elasticidade representada sem deformacao falsa;
- transparencia apenas se prevista;
- luz revela o tecido sem plastificar;
- sombra nao cria costura falsa.

Falhas criticas:

- tecido tecnico parecendo plastico barato;
- linho sem textura;
- malha de compressao sem tensao;
- alfaiataria sem estrutura;
- brilho de couro/seda em tecido matte.

## Camada 6 - Construcao e detalhes

Verificar:

- costuras previstas existem e estao no lugar;
- pences, recortes, palas, pregas e bolsos sao plausiveis;
- linha de fio sugerida visualmente nao contradiz queda/estampa;
- fechamento nao muda de lado sem motivo;
- etiquetas, logos e aviamentos nao foram inventados;
- componentes pequenos nao deformam a peca.

Falha critica: imagem inventa um detalhe que mudaria o produto real.

## Camada 7 - Fidelidade ao briefing

Comparar imagem com:

- ficha da peca;
- prompt positivo;
- prompt negativo;
- taxonomia;
- referencia de modelagem;
- contrato de alinhamento.

Pergunta obrigatoria: se uma modelista ou confecção olhasse esta imagem, entenderia o produto correto ou seria induzida a erro?

## Camada 8 - Coerencia PHYLLOS

Verificar:

- elegancia funcional;
- visual nao elitista nem exclusivamente executivo;
- performance consciente sem cara de academia generica;
- contexto de vida real;
- ausencia de estetica de banco de imagem;
- ausencia de sensualizacao gratuita;
- ausencia de elementos que distraiam do produto.

## Score de aprovacao

Cada camada recebe:

- 0 = reprovado;
- 1 = aceitavel com ressalva;
- 2 = aprovado.

Imagem aprovada:

- nenhuma falha critica;
- minimo 14 pontos em 8 camadas principais;
- Camada 2, 3, 4 e 7 precisam ser 2 para imagem de referencia de produto;
- imagem editorial pode aceitar 1 em composicao tecnica, mas nao em anatomia, roupa, fit ou fidelidade.

## Template de relatorio QA

```markdown
# QA de Imagem - PHYLLOS

## Status
[Aprovada / Aprovada com ressalvas / Reprovada]

## Uso permitido
[referencia de produto / editorial / rascunho interno / nao usar]

## Score por camada
| Camada | Nota | Problema | Acao |
|---|---:|---|---|
| 0 Entrada |  |  |  |
| 1 Composicao |  |  |  |
| 2 Anatomia |  |  |  |
| 3 Roupa |  |  |  |
| 4 Fit/modelagem |  |  |  |
| 5 Tecido |  |  |  |
| 6 Construcao |  |  |  |
| 7 Fidelidade |  |  |  |
| 8 PHYLLOS |  |  |  |

## Falhas criticas
- ...

## Ajuste no prompt positivo
- ...

## Ajuste no prompt negativo
- ...

## Ajuste no controle visual
- pose:
- enquadramento:
- referencia:
- mascara/area:
- seed/variacao:

## Decisao
...
```

## Ciclo de correcao

### Se o problema e anatomico

- reduzir pose dramatica;
- usar pose frontal, lateral ou tres quartos neutra;
- pedir corpo inteiro com proporcoes naturais;
- aplicar referencia de pose quando houver;
- reforcar negativo de membros deformados, torso torcido, maos ruins e pernas assimetricas.

### Se o problema e roupa desalinhada

- simplificar fundo e pose;
- pedir eixo central visivel;
- exigir cos horizontal, centro frente alinhado, costuras laterais continuas e barra regular;
- gerar imagem tecnica/e-commerce antes da editorial;
- usar referencia de silhueta, mascara ou controle de contorno quando possivel.

### Se o problema e modelagem/fit

- voltar ao Pattern Engine;
- declarar folga por regiao;
- incluir tensao/dobra esperada;
- remover termos conflitantes, como "loose" junto de "compression";
- gerar variante em pose funcional especifica.

### Se o problema e tecido

- reforcar composicao, textura, brilho, gramatura e caimento;
- incluir negativos de material errado;
- usar close-up tecnico separado quando a textura for decisiva.

## Banco de negativos de alinhamento

Usar conforme o caso:

```text
misaligned garment, crooked waistband, twisted center front, uneven hem, mismatched pant legs, broken side seam, floating fabric, painted-on clothing, warped seams, inconsistent pockets, invented zipper, asymmetric sleeves, displaced collar, distorted neckline, impossible drape, bad anatomy, extra limbs, deformed hands, twisted torso, broken joints, fisheye distortion, extreme perspective, cropped garment, hidden waistband, hidden seams, stock photo look, generic activewear, plastic fabric texture
```

## Banco de positivos de alinhamento

Usar conforme o caso:

```text
full garment visible, centered body axis, natural anatomical proportions, straight posture, clear center front, aligned waistband, even hem, continuous side seams, symmetrical pockets, realistic fabric tension, garment follows body volume, visible construction details, coherent pattern seams, neutral lens, product-focused fashion photography, technical e-commerce reference, clean silhouette
```
