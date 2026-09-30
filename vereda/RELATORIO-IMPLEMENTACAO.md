# Relatório de implementação — landing page Vereda V2

**Data:** 29/09/2026  
**Estado:** implementada e verificada localmente; não publicada.

## Resultado

A landing page foi reconstruída como experiência institucional multissetorial, com seis seções, uma única conversão para “Agendar conversa”, demonstração fictícia de evidências, FAQ e formulário compatível com Netlify Forms. A direção visual adotada foi “arquitetura de decisão”: fundo claro predominante, tipografia sem serifa, grid editorial, divisórias finas, informação organizada por estados e fotografia aplicada como contexto material.

## Marca e direção de arte

- A paleta aplicada é a indicada no briefing como derivada da página 9 do PDF: Branco Mineral `#F7F7F3`, Cinza Névoa `#EEE7E3`, Carvão `#1E2422`, Verde Técnico `#78A58F`, Azul Aço `#637C8D` e Atenção `#E77355`. A paleta divergente do DOCX não foi misturada.
- O wordmark usado é o recorte raster fiel fornecido no pacote. Sua proporção foi preservada por dimensões intrínsecas e `height: auto`; não houve redesenho, filtro, vetorização aproximada ou remoção de fundo.
- O SVG original e as variantes transparentes/negativas do wordmark continuam pendentes. O raster é adequado para esta prévia sobre fundo claro, mas não substitui o arquivo oficial de produção em todos os contextos.
- As funções tipográficas do manual foram preservadas como tokens `display`, `text` e `data`. Como não há arquivos ou famílias verificáveis, a implementação usa uma pilha neutra de Helvetica/Arial e não a apresenta como tipografia oficial V2.
- O ZIP recebido está truncado. Os ativos anteriores ao ponto de corrupção foram recuperados, mas o PDF foi extraído como arquivo inválido e o DOCX não estava na parte recuperável. Assim, a revisão visual integral das 38 páginas não pôde ser refeita nesta execução; a implementação se baseou no briefing completo, nos tokens recuperados, no wordmark e nos ativos visuais.

## Imagens

As três fotografias locais foram fornecidas no kit e registradas no manifesto como geradas por IA nesta tarefa:

- `hero-territorio.webp`: contexto territorial no hero, com estrada preservada como ponto focal.
- `processo-industrial.webp`: contexto ilustrativo de operação e manufatura.
- `fibras-materiais.webp`: detalhe material na seção de evidências.

Todas aparecem com dimensões reservadas, `object-fit`, ponto focal e legenda factual. Elas não são apresentadas como registro de cliente, localização real, composição comprovada, instalação ou certificação.

## Conteúdo e precisão comercial

- A proposta comercial aparece antes da metodologia.
- Moda, agro, manufatura e cooperativas são contextos de análise, não setores declarados como clientes.
- Nenhum score, percentual de prontidão, prazo regulatório universal, certificação, depoimento, logo de cliente ou resultado comercial foi inventado.
- Gap Map, Readiness Report, Evidence Vault e Buyer Data Pack aparecem com explicação de função e sem promessa de entrega obrigatória em uma conversa inicial.
- A demonstração da camiseta é identificada como fictícia em todas as abas. “Verificado no exemplo” é explicitamente diferenciado de certificação ou conformidade.

## Formulário e privacidade

- Preservados: `method="post"`, nome `diagnostico-vereda`, `form-name`, honeypot `bot-field`, ação `/obrigado/` e campos `name`, `company`, `email`, `segment` e `sku_volume`.
- Nome, empresa, e-mail e segmento são obrigatórios; volume de SKUs é opcional.
- O seletor mantém os valores anteriores de moda e calçados e adiciona agro, manufatura e cooperativas. Como o receptor observado é Netlify Forms, os novos valores não quebram um schema fechado no frontend; consumidores externos ainda precisam ser confirmados antes da publicação.
- Em localhost, o envio é bloqueado e informa claramente que nenhuma solicitação foi processada.
- Em ambiente não local, o JavaScript envia ao endpoint real, verifica uma resposta com `data-submission-received` e só então informa sucesso.
- A página `/obrigado/` foi revisada para a solicitação de conversa.
- O processamento real de leads em produção não foi testado e permanece como gate de publicação.

## Acessibilidade e comportamento

- Um único H1 e ordem coerente de títulos.
- Menu móvel com `aria-expanded`, fechamento por `Escape`, fechamento ao sair do cabeçalho e foco perceptível.
- Abas com `tablist`, `tab`, `tabpanel`, seleção visível e navegação por setas, `Home` e `End`.
- FAQ implementado com `details`/`summary` nativos.
- Labels visíveis, mensagens ligadas por `aria-describedby`, foco no primeiro campo inválido e região de status.
- Preferência `prefers-reduced-motion` respeitada.
- Âncoras antigas úteis preservadas: `#piloto`, `#metodo`, `#entregaveis`, `#desafios`, `#prova` e `#passaporte`.

## Validação executada

O script `scripts/capture-preview.mjs` verificou 360, 390, 768 e 1440 px:

- sem rolagem horizontal;
- um único H1;
- todas as imagens carregadas, incluindo as imagens lazy após entrarem na área de visualização;
- menu móvel abrindo e fechando por `Escape`;
- todas as abas ativáveis;
- FAQ expansível;
- erros obrigatórios do formulário;
- aviso correto de não envio na prévia local;
- ausência de erros de console e de recursos quebrados.

Evidências salvas:

- `previews/vereda-desktop-1440.png`
- `previews/vereda-mobile-390.png`
- `previews/qa-results.json`

## Pendências para publicação

1. Substituir o wordmark raster pelo arquivo oficial vetorial/transparente quando disponível.
2. Aplicar as famílias tipográficas oficiais após receber arquivos e licenças verificáveis.
3. Repetir a conferência lado a lado com o PDF íntegro, especialmente páginas 7, 9, 10, 13, 16, 25, 26, 31, 35 e 37.
4. Validar o recebimento real do Netlify Forms, a notificação ao owner comercial e os novos valores de segmento.
5. Revisar canonical e metadados no domínio final caso a publicação não use `vereda-dpp.netlify.app`.
