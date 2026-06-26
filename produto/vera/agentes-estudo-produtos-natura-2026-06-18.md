# Vera - pauta de estudo dos produtos Natura

Data da coleta: 2026-06-18

Fonte primária: páginas oficiais da Natura informadas pelo usuário.

Objetivo: orientar os agentes da Vera a estudar cinco produtos Natura e transformar esse estudo em atendimento consultivo, conteúdo para Instagram/WhatsApp, combos de venda e mensagens com cuidado de compliance.

## Status operacional

- O remote Git `vera` aponta para `https://github.com/paulohugorz/Vera`, mas o branch `vera/main` ainda contém apenas estrutura inicial (`README.md`, `docs/README.md`, `src/README.md`).
- Não foi encontrada uma célula de agentes da Vera versionada no projeto atual.
- Este documento registra a primeira pauta de estudo para os agentes da Vera dentro deste workspace.

## Banco de dados do portfolio

Este briefing foi quebrado em estrutura de banco de dados em `data/vera/portfolio/`.

Arquivos criados:

- `data/vera/portfolio/schema.sql`: modelo relacional em SQLite para separar produto, oferta, fatos, venda, atendimento, campanha, combos, compliance e verificações.
- `data/vera/portfolio/seed_natura_2026-06-18.sql`: primeiro snapshot com os cinco produtos Natura.
- `data/vera/portfolio/README.md`: regra operacional para novos produtos e consultas úteis.

A partir de agora, o texto deste briefing deve ser tratado como material de leitura; a fonte estruturada para agentes deve ser o banco do portfolio.

## Produtos em estudo

| Produto | Código | Linha | Preço coletado | Avaliação coletada | Link |
|---|---:|---|---:|---|---|
| Desodorante Perfume Ilía Secreto Feminino 50 ml | NATBRA-83314 | Ilía | R$199,90 | 4,7/5 em 1152 avaliações | https://www.natura.com.br/p/desodorante-perfume-ilia-secreto-feminino-50-ml/NATBRA-83314 |
| Desodorante Colônia Kaiak Aventura Intensa Masculino 100 ml | NATBRA-171117 | Kaiak | R$199,90 | 4,8/5 em 96 avaliações | https://www.natura.com.br/p/desodorante-colonia-kaiak-aventura-intensa-masculino-100-ml/NATBRA-171117 |
| Multiprotetor Antissinais FPS 50 Chronos 50 ml | NATBRA-134189 | Chronos | R$110,00 | 4,6/5 em 58 avaliações | https://www.natura.com.br/p/multiprotetor-antissinais-fps-50-chronos-50-ml/NATBRA-134189 |
| Sérum Intensivo Preenchedor Hidratante Chronos Derma 30 ml | NATBRA-169233 | Chronos Derma | R$205,00 | 5/5 em 12 avaliações | https://www.natura.com.br/p/serum-intensivo-preenchedor-hidratante-chronos-derma-30-ml/NATBRA-169233 |
| Água Micelar Demaquilante Suave Chronos Derma 150 ml | NATBRA-133503 | Chronos Derma | R$85,00 | 4,9/5 em 9 avaliações | https://www.natura.com.br/p/agua-micelar-demaquilante-suave-chronos-derma-150-ml/NATBRA-133503 |

Observação: preços, estoque, selos, edição limitada, avaliações e claims podem mudar. Antes de publicar ou vender, verificar novamente na página oficial.

## Missões por agente

### Agente de perfumaria

Estudar Ilía Secreto e Kaiak Aventura Intensa para criar argumentos de venda, comparativos simples e respostas de objeção.

Entregáveis:

- ficha curta de cada fragrância;
- linguagem de venda para WhatsApp;
- roteiro de stories e reels;
- perguntas para descobrir gosto olfativo;
- limites de promessa sobre fixação, projeção e desempenho.

### Agente de skincare

Estudar Chronos/Chronos Derma para montar rotina simples de limpeza, tratamento e proteção.

Entregáveis:

- ordem sugerida de uso;
- cliente ideal para cada produto;
- objeções prováveis sobre preço, oleosidade, necessidade e resultado;
- alertas de linguagem para não transformar cosmético em promessa médica;
- lista de lacunas a verificar diretamente na página oficial.

### Agente de conteúdo e vendas

Transformar o estudo em pauta comercial.

Entregáveis:

- matriz produto x cliente ideal x gancho;
- 10 perguntas de atendimento consultivo;
- 8 ideias de conteúdo;
- 5 combos de venda;
- checklist pré-publicação.

## Síntese por produto

### Ilía Secreto Feminino 50 ml

Posicionamento: fragrância feminina sofisticada, intensa e marcante, com contraste entre força e delicadeza. Boa para clientes que querem presença, mistério e sensualidade com elegância.

Dados de estudo:

- Floral adocicado intenso.
- A página cita flores brancas, fava-tonka e café arábica.
- A página descreve uma fragrância com dualidade entre força e delicadeza.
- A página cita fixação média de 10 horas, variável conforme pele e ambiente.
- Melhor comunicação: noite, outono/inverno, ocasiões especiais, cliente que gosta de perfume presente.

Perguntas de diagnóstico:

- Você prefere perfumes marcantes ou leves?
- Quer usar de dia, à noite ou em ocasiões especiais?
- Você costuma gostar de fragrâncias adocicadas?
- Procura algo elegante, sensual ou discreto?
- Sua pele costuma segurar bem perfume?

Objeções e respostas:

- "Tenho medo de ser forte demais." Resposta: "Ele é intenso e marcante; vale começar com poucas borrifadas e testar na pele."
- "Perfume doce me enjoa." Resposta: "Ele tem lado floral adocicado, então é melhor provar antes. A fava-tonka e o café arábica dão personalidade, sem depender só do doce."
- "Fixa mesmo 10 horas?" Resposta: "A página cita fixação média de 10 horas, mas isso varia por pele, clima e quantidade aplicada."

### Kaiak Aventura Intensa Masculino 100 ml

Posicionamento: fragrância masculina fresca, aromática e frutal, com energia de aventura. Serve para dia a dia e para sair.

Dados de estudo:

- Deo colônia masculina.
- Família olfativa aromática; subfamília frutal.
- A página cita frutas aquosas, notas aromáticas, madeiras úmidas e pimentas.
- A página apresenta como edição limitada.
- A página cita embalagem feita com material reciclado.
- O uso sugerido na página inclui punhos, pescoço e atrás das orelhas.

Perguntas de diagnóstico:

- Você prefere perfume fresco, doce ou amadeirado?
- Quer usar no trabalho, dia a dia ou para sair?
- Já gosta da linha Kaiak?
- Procura presente seguro ou algo mais exclusivo por ser edição limitada?

Objeções e respostas:

- "Kaiak é muito comum." Resposta: "Esse é o Aventura Intensa, edição limitada com frutas aquosas, madeiras úmidas e pimentas. Mantém o frescor da linha com proposta mais intensa."
- "Será que dura?" Resposta: "Ele é deo colônia; desempenho varia por pele e ambiente. A aplicação nos pontos indicados ajuda na perfumação."
- "Serve para presente?" Resposta: "Sim, especialmente para quem gosta de perfume fresco, esportivo e versátil."

### Multiprotetor Antissinais FPS 50 Chronos 50 ml

Posicionamento: protetor diário com proposta antissinais. Deve ser estudado como último passo da rotina da manhã.

Dados de estudo:

- A página/título menciona FPS 50 e FPUVA 18.
- Preço coletado: R$110,00.
- Avaliações coletadas: 4,6/5 em 58 avaliações.
- Reviews citados na página mencionam hidratação, toque seco e conforto sob maquiagem.

Lacunas a verificar:

- benefícios oficiais completos;
- modo de uso;
- frequência de reaplicação;
- indicação por tipo de pele;
- advertências oficiais de proteção solar.

Objeções e respostas:

- "Tenho medo de ficar oleoso." Resposta: "Algumas avaliações da página citam toque seco e que não fica pesado sob maquiagem, mas vale testar na sua pele."
- "Preciso usar todo dia?" Resposta: "Protetor solar costuma ser o último passo da rotina da manhã; confirmar modo de uso oficial antes de orientar."

### Sérum Intensivo Preenchedor Hidratante Chronos Derma 30 ml

Posicionamento: tratamento de hidratação e preenchimento para cliente focada em linhas finas, sinais e pele com aspecto desidratado.

Dados de estudo:

- A página cita +75% ácido hialurônico para a pele.
- A página cita 100% pele mais hidratada e fortalecida em até 14 dias.
- A página cita +92% preenchimento imediato.
- A página cita que preenche e hidrata diferentes camadas da pele, reduzindo rugas e linhas finas.
- A página cita resultados comprovados por dermatologistas.

Regra de publicação:

- Sempre preservar as notas/rodapés ¹²³ quando usar percentuais, prazo de 14 dias ou claims de comprovação.
- Não prometer eliminação definitiva de rugas, cura, tratamento médico ou resultado igual para todas as pessoas.

Objeções e respostas:

- "R$205 é caro." Resposta: "Ele é o produto de tratamento da rotina. Se a prioridade for hidratação, linhas finas e pele mais fortalecida, ele vira o investimento central."
- "Tira rugas?" Resposta: "A linguagem correta é que ajuda a preencher, hidratar e reduzir a aparência de rugas e linhas finas, conforme a descrição oficial. Não é tratamento médico."

### Água Micelar Demaquilante Suave Chronos Derma 150 ml

Posicionamento: etapa de limpeza e demaquilante suave, especialmente útil para quem usa maquiagem ou quer uma rotina simples de cuidado facial.

Dados de estudo:

- Preço coletado: R$85,00.
- Avaliações coletadas: 4,9/5 em 9 avaliações.
- O schema da página classifica em maquiagem.

Lacunas a verificar:

- benefícios oficiais completos;
- modo de uso;
- tipo de pele indicado;
- se remove maquiagem à prova d'água;
- necessidade ou não de enxágue.

## Rotina consultiva Chronos

Manhã:

1. Água micelar, se fizer sentido para limpeza leve.
2. Sérum hidratante/preenchedor.
3. Multiprotetor FPS 50.

Noite:

1. Água micelar para remover maquiagem e impurezas.
2. Sérum hidratante/preenchedor.

## Perguntas de atendimento consultivo

1. Você está procurando perfume, skincare ou um combo?
2. Para perfume, prefere algo mais intenso ou mais leve?
3. Você gosta de fragrâncias florais adocicadas?
4. O perfume seria para uso diário, para sair ou para presentear?
5. Você prefere uma fragrância sofisticada/enigmática ou fresca/aromática?
6. Na rotina facial, você já usa protetor todos os dias?
7. Você usa maquiagem por cima do protetor?
8. Sua prioridade hoje é hidratação, preenchimento, sinais, linhas finas, limpeza ou demaquilante?
9. Você prefere produto com muitas avaliações ou aceita testar novidades?
10. Quer montar uma rotina simples com limpeza, tratamento e proteção?

## Ideias de conteúdo

1. Ilía Secreto: perfume para quem quer sofisticação e presença.
2. Kaiak Aventura Intensa: aromático frutal para dia a dia e para sair.
3. Comparativo de perfumes: floral adocicado intenso x aromático frutal.
4. Rotina Chronos em 3 passos: limpar, tratar e proteger.
5. O que os reviews dizem sobre o Multiprotetor Chronos FPS 50: hidratação, toque seco e maquiagem.
6. Sérum Chronos Derma: ácido hialurônico, preenchimento imediato e hidratação em até 14 dias¹²³.
7. Como escolher presente Natura pelo estilo da pessoa.
8. Produtos com boas avaliações: notas, preços e para quem indicar.

## Combos de venda

| Combo | Produtos | Uso comercial |
|---|---|---|
| Perfume feminino + skincare | Ilía Secreto + Sérum Chronos Derma | Cliente que quer cuidado e presença para ocasiões especiais |
| Masculino presenteável | Kaiak Aventura Intensa + Multiprotetor Chronos FPS 50 | Presente masculino com perfume fresco e cuidado diário |
| Rotina facial Chronos | Água Micelar + Sérum + Multiprotetor | Cliente que quer rotina simples de limpar, tratar e proteger |
| Maquiagem e pele | Água Micelar + Multiprotetor FPS 50 | Cliente que usa maquiagem e quer limpeza + proteção |
| Casal / presente duplo | Ilía Secreto + Kaiak Aventura Intensa | Presente duplo com uma fragrância feminina marcante e uma masculina fresca |

## Checklist antes de publicar

- Verificar preço e estoque no dia da publicação.
- Verificar se edição limitada do Kaiak ainda está vigente.
- Verificar benefícios oficiais do Multiprotetor e da Água Micelar.
- Preservar notas ¹²³ dos claims numéricos do sérum.
- Distinguir review de promessa oficial: usar "clientes citam", "avaliações mencionam", "pode agradar".
- Não prometer fixação garantida, resultado dermatológico garantido, cura, reversão de envelhecimento ou eliminação definitiva de rugas.
- Em protetor solar, confirmar modo de uso, reaplicação, FPUVA/FPS e advertências oficiais.

## Próximas tarefas dos agentes

1. Agente de perfumaria: transformar Ilía e Kaiak em 3 scripts de WhatsApp, 3 stories e 2 reels.
2. Agente de skincare: verificar lacunas oficiais de Multiprotetor e Água Micelar e revisar linguagem de claims do sérum.
3. Agente de conteúdo e vendas: montar calendário de 7 dias com um conteúdo por dia e CTA de atendimento.
4. Agente de atendimento: criar respostas curtas para as 10 perguntas consultivas.
5. Agente de compliance: revisar todas as copys antes de publicação.
