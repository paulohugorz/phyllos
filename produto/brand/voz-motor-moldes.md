# Voz do Motor de Moldes — PHYLLOS

**Versao:** 1.0  
**Data:** 2026-06-11  
**Owner:** Brand / CMO  
**Status:** Aprovado para uso interno e interface do motor

---

## 1. Como a Phyllos apresenta cada molde base ao usuario

### O enquadramento correto

O motor de moldes nao e um banco de templates. Ele e um ponto de partida construido a partir de um corpo real — o seu. A linguagem de apresentacao deve refletir isso: nao e "escolha um template", e "por onde voce quer comecar".

A palavra "template" esta proibida na interface. Alternativas aprovadas: "base", "ponto de partida", "estrutura", "molde base", "forma".

O ICP — criadores independentes, alfaiates, micro-marcas, estilistas sem atelie — sabe o que quer construir. Nao precisa ser convencido. Precisa de clareza e velocidade. A voz do motor e a de um parceiro tecnico que respeita o conhecimento de quem usa, sem ser frio nem tutorial demais.

### Copy de apresentacao para cada peca base

Abaixo, o nome humano (interface), o nome tecnico interno e o texto de apresentacao na tela de selecao.

---

**Calca reta**
Nome tecnico: `calca-reta-classica`
Nome na interface: **Calca reta**

> Uma calca que fecha bem no quadril, cai direto pela perna e funciona em qualquer composicao. O ponto de partida mais solicitado — e o mais adaptavel.

---

**Jogger**
Nome tecnico: `jogger-elastico`
Nome na interface: **Jogger**

> Construida para quem se move. Cava ampla, cintura ajustada, punho que segura. Funciona no estudio, na rua e no percurso entre os dois.

---

**Shorts**
Nome tecnico: `shorts-basico`
Nome na interface: **Shorts**

> Curto, funcional, sem excesso. A base e neutra o suficiente para virar treino, praia ou editorial — depende do que voce adiciona.

---

**Camiseta**
Nome tecnico: `camiseta-basica`
Nome na interface: **Camiseta**

> O ponto de partida mais democratico da costura. Ajuste o caimento, o comprimento, a manga — e voce tem uma peca nova a cada parametro.

---

**Camisa**
Nome tecnico: `camisa-social-base`
Nome na interface: **Camisa**

> Estrutura classica, pronta para ser desconstruida. Gola, pala, manga e corpo ja parametrizados. Voce decide o que fica e o que muda.

---

**Moletom**
Nome tecnico: `moletom-fechado`
Nome na interface: **Moletom**

> Tecido pesado, caimento generoso, conforto sem abrir mao de proporcao. A base certa para quem trabalha com malha e quer precisao no molde.

---

**Saia**
Nome tecnico: `saia-reta-base`
Nome na interface: **Saia**

> Reta, limpa, ajustavel do quadril a barra. Uma das bases com mais variacao de resultado a partir do mesmo molde — muda o tecido, muda a peca.

---

**Blazer**
Nome tecnico: `blazer-estruturado`
Nome na interface: **Blazer**

> Alfaiataria acessivel. O molde base do blazer e o mais exigente em precisao — e o que mais valoriza o trabalho de quem costura bem.

---

## 2. Como o motor fala com o usuario

### Tom da interface

- **Tecnico-acessivel:** usa termos corretos de modelagem (gancho, cava, pala, comprimento de tronco) sem explicar o que e gancho para quem ja sabe.
- **Direto:** frases curtas. Sem prefacio. O usuario veio para fazer, nao para ler.
- **Humano, nao assistente:** o motor nao e um chatbot prestativo. E um parceiro de construcao. Nao usa "Olha que legal!" nem "Otima escolha!".
- **Sem jargao de software:** nada de "clique aqui para prosseguir", "fluxo concluido", "input invalido". Tudo em linguagem de atelie.

### Mensagens de confirmacao

Quando o molde e gerado com sucesso:

> "Molde gerado. Confira as vistas, revise as medidas criticas e, se quiser ajustar algum ponto, e so descrever."

Versao curta (notificacao, email):

> "Seu molde esta pronto para corte."

Para um molde com customizacao complexa:

> "Molde gerado com as adaptacoes que voce pediu. Revisamos o gancho e a largura de quadril — veja se o resultado e o que voce esperava antes de plotar."

---

### Mensagens de erro ou dado faltante

Quando uma medida critica nao foi informada:

> "Para gerar o molde desta calca, precisamos do comprimento de tronco. Voce tem essa medida?"

Quando a combinacao de medidas gera uma proporcao fora do esperado:

> "Essas medidas resultam em uma cava bem fechada. Isso pode ser intencional — mas se nao for, vale checar a medida de busto antes de continuar."

Quando o usuario descreve algo que o motor nao consegue interpretar:

> "Nao entendi bem essa parte. Pode descrever de outra forma? Por exemplo: 'manga 3/4 com punho elasticado' ou 'barra reta, sem bainha'."

Quando falta informacao e o motor pode estimar:

> "Nao informou o comprimento da manga. Vou usar o padrao para o seu tamanho de busto — mas voce pode ajustar depois."

---

### Mensagens de sugestao tecnica

O motor pode sugerir ajustes quando as medidas indicam uma necessidade tecnica. O tom e de consultor de modelagem, nao de sistema de validacao.

> "Com esse quadril em relacao a cintura, recomendo aumentar o gancho em 1 cm para garantir conforto na cava traseira."

> "Esse comprimento de tronco e um pouco acima da media para essa tabela. Se quiser, posso ajustar a pala traseira para manter o equilíbrio visual."

> "Para esse tipo de tecido, uma costura francesa vai exigir uma margem maior. Quer que eu adicione 1,5 cm em vez de 1 cm?"

---

### Como o motor se apresenta

O motor nao e uma ferramenta. Nao e um assistente. Nao tem nome proprio.

Ele e descrito, quando necessario, como **"o motor de modelagem da Phyllos"** — ou simplesmente como **"o motor"** em contexto interno. Na interface, ele nao se apresenta. Ele age.

A primeira tela nao diz "Bem-vindo ao motor de moldes da Phyllos". Ela diz:

> "Por onde voce quer comecar?"

E apresenta as 8 bases.

---

## 3. Nomenclatura das pecas no catalogo

### Nomes aprovados para a interface (portugues, humanos, nao tecnicos)

| Posicao | Nome na interface | Nome tecnico interno       |
|---------|-------------------|----------------------------|
| 1       | Calca reta        | calca-reta-classica        |
| 2       | Jogger            | jogger-elastico            |
| 3       | Camiseta          | camiseta-basica            |
| 4       | Camisa            | camisa-social-base         |
| 5       | Moletom           | moletom-fechado            |
| 6       | Shorts            | shorts-basico              |
| 7       | Saia              | saia-reta-base             |
| 8       | Blazer            | blazer-estruturado         |

### Hierarquia visual de apresentacao

A ordem nao e alfabetica nem por complexidade tecnica. E por frequencia de uso e por progressao de aprendizado.

**Primeiro bloco — bases de entrada** (maior volume de uso, menor barreira tecnica):
- Camiseta
- Calca reta
- Shorts

**Segundo bloco — bases de movimento** (publico de performance e streetwear):
- Jogger
- Moletom

**Terceiro bloco — bases estruturadas** (alfaiataria, trabalho com trama):
- Camisa
- Saia
- Blazer

Na interface, os tres blocos podem ser apresentados com titulos discretos ou como uma grade unica sem rotulos — decisao de UX, nao de marca. O que importa e que **Camiseta, Calca reta e Shorts aparecem primeiro**, pois reduzem o tempo de primeira conversao.

Cada peca na grade exibe: nome, uma linha de descricao (os textos da secao 1) e, quando disponivel, uma imagem de referencia ou vista esquematica do molde.

O usuario nao "seleciona" — ele "escolhe por onde comecar". O botao de acao e **"Comecar com essa base"**, nao "Selecionar" ou "Usar template".

---

## 4. Manifesto do motor de moldes

Para usar na landing page, no pitch e no one-pager.

---

Modelagem sempre foi conhecimento guardado. Aprendia quem tinha atelie, mestre ou tempo. Quem nao tinha, terceirizava ou desistia. A Phyllos construiu o motor de moldes para mudar esse calculo: voce descreve o que quer construir — em linguagem simples, com as medidas reais do seu corpo ou do seu cliente — e recebe um molde 2D parametrizado, pronto para corte, sem intermediario e sem CAD. Nao e automacao de moda. E acesso a precisao tecnica para quem ja sabe o que quer fazer com ela.

---

## Regras de voz: o que dizer e o que nao dizer

| Dizer                                  | Nao dizer                              |
|----------------------------------------|----------------------------------------|
| Molde base                             | Template                               |
| Ponto de partida                       | Modelo pre-definido                    |
| Comecar com essa base                  | Selecionar / Usar                      |
| Corpo real                             | Manequim padrao                        |
| Precisao tecnica                       | Resultado perfeito                     |
| Ajustar / adaptar                      | Customizar (evitar anglicismo excessivo)|
| Por onde voce quer comecar?            | Bem-vindo! Escolha uma opcao abaixo    |
| Medida critica nao informada           | Erro / Campo obrigatorio               |
| Recomendo aumentar o gancho            | Sugestao automatica gerada             |
| Veja se o resultado e o que esperava   | Confira se esta correto                |

---

**Handoffs recomendados:**
- UX/Produto: aplicar nomenclatura, hierarquia de grade e textos de interface.
- Growth/Marketing: usar o manifesto na landing page e no pitch deck.
- Product Agent: registrar nomes tecnicos internos como padrao de nomenclatura do catalogo de moldes.
- CMO: aprovar antes de publicar qualquer variacao do manifesto em canal externo.
