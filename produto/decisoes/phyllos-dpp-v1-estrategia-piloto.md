# PHYLLOS DPP V1 - Estrategia de Piloto

**Data:** 2026-06-25
**Status:** plano operacional v0.1 para piloto assistido
**Owner:** Founder / Product
**Relacionado:** [prd-dpp-integrado-v0.md](prd-dpp-integrado-v0.md), [dpp-anti-greenwashing-qa-v0.md](dpp-anti-greenwashing-qa-v0.md), [backlog-codex-dpp-2026-06-25.md](backlog-codex-dpp-2026-06-25.md)

Legenda:

- `[F]` fato estabelecido no produto/repo.
- `[H]` hipotese a testar.
- `[R]` risco.
- `[REC]` recomendacao operacional.

---

## 1. Objetivo do piloto

[F] O backend DPP ja possui endpoints funcionais para publicacao e QR (`POST /pecas/{codigo}/dpp/publicar`, `GET /pecas/{codigo}/qr` e `GET /dpp/{identifier}/qr`) segundo o backlog vigente. O piloto nao deve esperar nova tese de produto; deve testar dados reais, onboarding e uso do QR.

[H] A pergunta principal do piloto nao e "quanto o mercado pagaria?" ainda. A pergunta principal e:

> Marcas pequenas conseguem trazer dados suficientes para publicar um DPP honesto e util em menos de 60 minutos?

[REC] Rodar um piloto assistido com 3 a 5 marcas independentes, gratuito, com uma peca por marca no primeiro ciclo.

---

## 2. Decisoes executivas confirmadas

### Ambiente publico

[REC] Usar Railway agora.

Configuracao:

- `DPP_BASE_URL=https://phyllos-production.up.railway.app`;
- dominio proprio somente depois do primeiro sinal real;
- sem depender de DNS novo para iniciar o piloto.

Prerequisito tecnico:

- app rodando em producao no Railway;
- `GET /p/{uuid}` retornando pagina publica;
- QR apontando para URL publica real.

### Identificador

[REC] Usar SKU interno/codigo PHYLLOS no piloto, com GTIN opcional.

Regra:

- se a marca tiver GTIN, registrar;
- se nao tiver, publicar pelo `dpp_uuid` gerado pela PHYLLOS;
- o QR aponta para `/p/{uuid}`;
- o SKU/codigo interno continua sendo a chave operacional de onboarding.

### Escopo minimo

[REC] Tier 1 obrigatorio, Tier 2 opcional.

Tier 1 publica o DPP com status `declarado`. Tier 2 adiciona indicadores calculados quando area, gramatura, perda e fatores estiverem disponiveis.

### Registro do piloto

[REC] Registrar o piloto em CSV no repo:

```text
outputs/piloto-dpp-v1.csv
```

Motivo: zero dependencia externa, historico no git e reutilizacao futura como evidencia de pesquisa.

### Oferta

[REC] Gratuito, assistido, com QR ativo por 90 dias mesmo se a marca nao virar cliente.

Isso reduz friccao na abordagem e evita que o piloto pareca armadilha comercial.

### Regua executiva

Continuar se:

- 2 ou mais marcas compartilharem o QR espontaneamente;
- onboarding medio ficar abaixo de 60 minutos;
- pelo menos 1 marca pedir para cadastrar uma segunda peca sem precisar de assistencia intensa.

---

## 3. Quem convidar primeiro

[REC] Perfil ideal: marca independente com 1 a 5 SKUs lancados ou em fase final de desenvolvimento, que ja tenha ficha tecnica em algum formato e esteja sendo cobrada por buyers, plataformas ou seguidores sobre composicao, origem, cuidado ou rastreabilidade.

| Perfil | Por que incluir | Por que evitar ou postergar |
|---|---|---|
| Marca independente pequena | Decisao rapida, founder e usuario, pressao real de buyer/cliente | - |
| Founder de moda pre-lancamento | Alta motivacao para diferenciacao | Sem produto fisico nao testa QR em etiqueta real |
| Atelie de costura sob medida | Conhece producao profundamente | Sem lote, sem GTIN e dados difusos podem alongar onboarding |
| Marca media estabelecida | Dados mais estruturados | Ciclo juridico/comercial lento para primeiro piloto |

[H] Marcas respondendo a alguma exigencia de rastreabilidade textil ou pedido formal de buyer terao mais urgencia do que marcas interessadas apenas em narrativa de sustentabilidade.

[R] A referencia a INMETRO Portaria 459 e prazo de 31/07/2026 precisa ser validada em fonte oficial ou assessoria juridica antes de virar copy publica, contrato ou promessa comercial. Ate la, usar como premissa de investigacao, nao como afirmacao de conformidade.

---

## 4. Caso de uso a testar

[REC] Selecionar marca independente que vai lancar 1 a 3 pecas em ate 60 dias e quer:

- colocar QR na etiqueta, embalagem ou tag;
- responder "o que tem nessa roupa?" com um link escaneavel;
- mostrar algo concreto no Instagram, WhatsApp ou conversa com buyer;
- organizar dados tecnicos sem prometer sustentabilidade nao comprovada.

[F] O sistema ja trabalha com flashcards e status de evidencia. Isso e suficiente para testar transparencia honesta sem auditoria, certificacao ou ACV oficial.

[H] O momento de valor mais importante e quando o usuario percebe que pode publicar um DPP com dados incompletos, desde que o passaporte mostre claramente o que e declarado, calculado, documentado ou ausente.

---

## 5. Dados minimos para DPP util

### Tier 1 - Publicavel em ate 45 minutos

Status padrao: `declarado`.

| Campo | Obrigatorio para piloto | Observacao |
|---|---:|---|
| Nome da peca | sim | Nome comercial ou tecnico |
| Codigo da peca | sim | SKU interno ou GTIN |
| Composicao de fibras | sim | Percentuais devem somar 100% |
| Pais de fabricacao | sim | Pode ser etapa principal |
| Instrucoes de cuidado/lavagem | sim | Texto, etiqueta ou foto transcrita |
| Fim de vida/descarte | sim | Mesmo que seja orientacao simples |

### Tier 2 - Calculado

Adiciona agua, carbono, energia e perda estimados.

| Campo | Uso | Status esperado |
|---|---|---|
| Area da peca em m2 ou peso em gramas | calculo de peso/indicadores | `declarado` ou `documentado` |
| Gramatura do tecido | calculo de peso | `declarado` ou `documentado` |
| Percentual de perda de corte | calculo de consumo | `declarado`, `calculado` ou `documentado` |
| Fornecedor de tecido e pais | rastreabilidade basica | `declarado` ou `documentado` |

### Tier 3 - Documentado ou verificado

Eleva status de evidencia.

| Evidencia | Exemplos |
|---|---|
| Certificacao de material | GOTS, OCS, GRS, OEKO-TEX |
| Documento de origem | nota fiscal, pedido, ficha do fornecedor |
| Conformidade social | ABVTEX, SA8000, declaracao do fornecedor |

[R] Muitas marcas chegarao somente com composicao e pais. Isso ainda pode gerar DPP Tier 1 valido, desde que a pagina publica diga "declarado pela marca" e nunca comunique verificacao.

---

## 6. Linguagem de valor

### Versao direta

> Voce ja sabe o que tem na sua peca. O DPP deixa qualquer pessoa descobrir isso com um QR.

### Versao regulatoria

> A pressao por rastreabilidade textil esta crescendo. O DPP organiza os dados da sua peca em uma pagina clara, com o nivel de evidencia de cada informacao.

### Versao comercial

> Buyer perguntou sobre composicao e origem? Em vez de mandar email solto, voce envia um link com os dados da peca e o nivel de certeza de cada campo.

[REC] Comecar pela versao direta. Usar a versao regulatoria apenas como contexto e sem prometer conformidade juridica. Usar a versao comercial quando o usuario vende para loja, marketplace ou buyer.

Nao dizer:

> O DPP prova que sua marca e sustentavel.

Motivo: a V1 organiza, calcula e publica evidencias; ela nao audita sustentabilidade.

---

## 7. Objecoes provaveis e respostas

| Objecao | Resposta operacional | Sinal de produto |
|---|---|---|
| Minha ficha tecnica esta no Excel, papel ou na cabeca | A gente transcreve junto. Voce traz o que tem, mesmo incompleto. | Se mais de 50% travar aqui, onboarding precisa de concierge ou template melhor |
| Consumidor nao le QR | O QR tambem resolve para buyer e para a propria marca: e o arquivo tecnico publicado. | Caso B2B pode ser mais forte que B2C |
| Nao tenho todos os dados | O sistema mostra exatamente o que existe e o que falta. Dado ausente aparece como ausente, nao como zero. | Diferencial anti-greenwashing |
| Nao quero prometer sustentabilidade sem prova | E exatamente para isso que existe status de evidencia. O DPP nao afirma mais do que voce sabe. | Boa objecao; indica cliente educado |
| Quanto custa ou quanto tempo leva? | Neste piloto e gratuito e assistido. A meta e sair com QR e link em ate uma sessao. | Aprendizado vem antes de precificacao |

---

## 8. Oferta piloto

[REC] Servico assistido gratuito para os primeiros 3 a 5 usuarios.

Estrutura:

- sessao de onboarding de 60 minutos;
- coleta dos dados Tier 1 e tentativa de Tier 2;
- geracao de DPP usando backend atual;
- entrega de QR funcional, link publico e flashcards com status de evidencia;
- QR ativo por 90 dias mesmo se a marca nao virar cliente;
- sessao de feedback de 30 minutos;
- autorizacao de case, podendo ser anonimizado.

Por que gratuito agora:

[F] O formulario e o fluxo de onboarding ainda nao foram testados com usuario real.

[H] O aprendizado principal e descobrir se usuarios conseguem trazer dados suficientes para gerar algo util. Pesquisa declarativa nao substitui a experiencia de montar o DPP com uma peca real.

Hipoteses de preco pos-piloto:

- se Tier 1 gerar valor claro: R$149 a R$299 por DPP;
- alternativa mensal: R$490/mes para ate 10 SKUs;
- se o valor real for o servico assistido: projeto ou hora de consultoria, com PHYLLOS como output operacional.

---

## 9. Roteiro de piloto - 7 dias

### Dias 1 e 2 - Identificar e abordar

Abordar 5 marcas independentes com produto fisico desenvolvido ou em finalizacao de producao.

Priorizar:

- marca com 1 a 3 pecas prontas ou quase prontas;
- founder que responde diretamente;
- pressao de buyer, plataforma, cliente ou rastreabilidade;
- ficha tecnica minima ja existente.

Canal: DM no Instagram ou LinkedIn do founder. Sem formulario e sem deck.

Mensagem base:

> Estou desenvolvendo uma ferramenta que gera passaporte digital para pecas de moda: QR + pagina de rastreabilidade a partir da ficha tecnica. Procuro 5 marcas para testar gratuitamente antes de lancar. Voce tem 1 a 3 pecas prontas ou quase prontas? Se sim, leva menos de 1h e voce sai com o QR pronto.

Complemento se houver interesse:

> O QR fica ativo por 90 dias mesmo se voce nao virar cliente depois do piloto.

Meta: 3 confirmacoes em 48 horas.

### Dias 3 e 4 - Onboarding de dados

Pedir antes da sessao:

1. nome e codigo de 1 peca, podendo ser SKU interno;
2. composicao de fibras com percentual de cada material;
3. pais onde foi fabricada;
4. instrucoes de lavagem ou foto da etiqueta;
5. se tiver: fornecedor do tecido, peso da peca, gramatura e perda de corte.

Na sessao:

- preencher o backend ao vivo com o usuario;
- registrar onde demorou;
- registrar quais campos causaram confusao;
- identificar se Tier 2 e possivel;
- marcar o status de evidencia de cada campo.

Metrica: tempo total de coleta + quantidade de campos ausentes no final.

### Dias 5 e 6 - Gerar e entregar DPP

Gerar via backend:

```text
POST /pecas/{codigo}/dpp/publicar
GET /pecas/{codigo}/qr
GET /p/{uuid}
```

Entregar:

- QR em PNG para teste;
- link publico do DPP;
- flashcards com status de evidencia visivel;
- nota curta explicando `declarado`, `calculado`, `documentado` e `verificado`.

Orientacao ao usuario:

> Voce pode usar esse QR em etiqueta, embalagem, Instagram, link na bio ou conversa com buyer. O status de cada dado aparece no passaporte. Nao afirme mais do que esta documentado.

[R] QR para impressao fisica so deve ser usado depois de rota publica estavel, dominio e imagem do QR serem testados fora do ambiente local.

Metrica: o usuario compartilhou o QR em algum canal nas 48 horas seguintes?

### Dia 7 - Coleta de sinal e decisao

Sessao de 30 minutos:

1. O QR recebido e util para alguma situacao real que voce enfrentava? Qual?
2. O que faltou para ser ainda mais util?
3. Se isso custasse R$200 por peca, voce pagaria? Por que sim ou por que nao?
4. Quem mais na sua rede precisaria disso?

Decisao:

- continuar se 2 ou mais usuarios compartilharem o QR espontaneamente, o onboarding medio ficar abaixo de 60 minutos e ao menos 1 marca pedir segunda peca;
- investigar se nenhum QR for usado em canal real ou se o onboarding medio passar de 90 minutos;
- mudar escopo se o bloqueio central for levantamento de dados, organizacao interna de ficha tecnica ou integracao com ferramenta existente.

---

## 10. Sinais de decisao

### Continuar

- Usuario fornece dados Tier 1 em menos de 45 minutos sem ajuda intensa.
- QR e compartilhado espontaneamente em Instagram, WhatsApp, buyer, embalagem ou etiqueta.
- Usuario diz que o DPP resolve um problema real sem ser induzido.
- Pelo menos 1 scan do QR ocorre por terceiro.
- Pelo menos 1 marca pede para cadastrar uma segunda peca.

### Pausar e investigar

- Nenhum dos 5 usuarios consegue fornecer Tier 1 completo em 90 minutos.
- QR e entregue, mas nao usado em nenhum canal em 7 dias.
- Usuario confunde DPP com auditoria/certificacao mesmo apos explicacao.

### Mudar escopo

- Dados existem, mas processo e lento: priorizar servico gerenciado/concierge.
- Valor citado e organizacao interna da ficha tecnica: avaliar PLM lite, nao DPP publico.
- Usuarios exigem integracao antes de adotar: priorizar conectores simples.

---

## 11. Registro minimo do piloto

Usar `outputs/piloto-dpp-v1.csv` com estas colunas:

| Campo | Tipo | Exemplo |
|---|---|---|
| marca | texto | Marca A |
| contato | texto | founder / email / IG |
| peca | texto | Camisa linho cru |
| SKU/GTIN | texto | CAM-LIN-001 |
| Tier alcancado | enum | Tier 1, Tier 2, Tier 3 |
| tempo_onboarding_min | numero | 52 |
| campos_ausentes | numero | 3 |
| qr_entregue | sim/nao | sim |
| link_publico | URL | - |
| QR compartilhado | sim/nao | sim |
| canal_de_uso | texto | WhatsApp com buyer |
| resposta_preco_R$200 | texto | pagaria / nao pagaria / talvez |
| objecao_principal | texto | nao tenho todos os dados |
| proxima_acao | texto | pedir fornecedor do tecido |

---

## 12. Artefatos de entrega ao usuario

Cada piloto deve sair com:

- link publico do DPP;
- QR funcional;
- 4 a 6 flashcards publicos;
- explicacao de status de evidencia;
- lista curta de lacunas;
- orientacao de uso sem claim indevido;
- pedido de feedback e indicacao.

Copy curta para status:

> Declarado: informado pela marca. Calculado: derivado de dados tecnicos e fatores. Documentado: apoiado por arquivo, certificado ou fornecedor. Verificado: revisado por terceiro ou fonte independente.

---

## 13. Proxima decisao

Ao fim dos 5 primeiros pilotos, decidir uma das tres rotas:

1. **Produto pago por DPP:** se QR e link forem usados e onboarding for rapido.
2. **Concierge DPP:** se valor existir, mas coleta de dados exigir acompanhamento.
3. **PLM lite / organizacao tecnica:** se usuarios valorizarem mais organizar ficha tecnica do que publicar QR.

Go/no-go minimo:

- 3 pilotos concluidos;
- 2 DPPs compartilhados em canal real;
- tempo medio de onboarding abaixo de 60 minutos;
- 1 pedido de segunda peca;
- zero ocorrencias de claim ambiental sem status de evidencia.

---

## 14. Sequencia minima de execucao

Hoje/amanha:

1. subir o app no Railway;
2. configurar `DPP_BASE_URL`;
3. confirmar que `GET /p/{uuid}` retorna pagina publica.

Esta semana:

1. usar `outputs/piloto-dpp-v1.csv` como registro;
2. finalizar DM de abordagem;
3. separar os 5 perfis de marca.

Proxima semana:

1. enviar 5 DMs;
2. agendar 3 onboardings;
3. publicar os primeiros DPPs Tier 1/Tier 2.
