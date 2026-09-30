# Execution Brief — LPs segmentadas Vereda A/B

**Decision ID:** VEREDA-LP-AB-2026-09-30  
**Direcionamento do founder:** construir duas landing pages para cada segmento comercial do site Vereda e publicar todas na Netlify para testes A/B.  
**Bloco:** B0/B1 — descoberta de mensagem e aquisição assistida.  
**Ambiente-alvo:** `vereda-dpp.netlify.app`.

## Resultado esperado

Dez landing pages publicadas e verificadas, cobrindo os cinco segmentos selecionáveis no formulário atual: moda/têxteis/confecção, calçados/couro, agro, manufatura e cooperativas. Cada segmento terá:

- variante A orientada a risco, lacunas e prontidão;
- variante B orientada a acesso a mercado, negociação e oportunidade;
- URL direta por variante;
- rota de distribuição 50/50 persistente no navegador;
- identificação de segmento, variante e UTMs no lead capturado;
- eventos locais compatíveis com `dataLayer`, sem envio para terceiros nesta entrega.

## Não objetivos

- declarar certificação, conformidade ou prontidão regulatória;
- inventar clientes, depoimentos, resultados, percentuais ou prazos universais;
- ativar mídia paga, CRM, e-mail ou ferramenta externa de analytics;
- escolher a variante vencedora antes de haver amostra real.

## Fatos, hipóteses e lacunas

- **Fato:** o formulário público atual contém cinco segmentos comerciais e a opção “Outro”.
- **Fato:** a Vereda apresenta Gap Map, Readiness Report, Evidence Vault e Buyer Data Pack como entregáveis variáveis conforme o escopo.
- **Hipótese A:** mensagens de redução de risco convertem melhor empresas já pressionadas por requisitos.
- **Hipótese B:** mensagens de acesso a mercado convertem melhor empresas em prospecção comercial.
- **Lacuna:** não existe volume mínimo, canal, orçamento ou métrica-base aprovado; a decisão de vencedor dependerá de dados reais.

## Owners e dependências

| Ação | Owner funcional | Dependência | Evidência |
|---|---|---|---|
| Mensagem por segmento | Marketing / Product Marketing | posicionamento Vereda vigente | matriz de copy e manifesto de rotas |
| Experiência e acessibilidade | Product Design / Frontend | identidade V2 e ativos existentes | páginas responsivas e QA automatizado |
| Captura e atribuição | Demand Gen / Frontend | Netlify Forms | campos ocultos e submissão reconhecida |
| Publicação | DevOps / Release | site Netlify `vereda-dpp` | deploy ID e URLs HTTPS |
| Validação independente | QA/Release | build completo | relatório de QA local e inspeção ao vivo |

## Compliance, risco e evidência

- **Risco afetado:** claim comercial ou regulatório sem sustentação.
- **Controle preventivo:** copy condicional, ausência de promessa de certificação/conformidade e explicitação de exemplos ilustrativos.
- **Controle detectivo:** varredura de claims, teste de conteúdo e conferência das páginas publicadas.
- **Evidência esperada:** fontes versionadas, manifesto de variantes, QA local, deploy Netlify e verificação HTTPS/conteúdo.
- **Owner do controle:** Marketing/Product Marketing para claims; QA/Release para teste; founder para aceitação da mensagem e go/no-go de mídia.
- **Retenção:** manter fontes, manifesto, relatório e deploy na história do repositório/Netlify.
- **Revisão independente:** necessária antes de escalar mídia ou declarar uma variante vencedora.
- **Exceção humana:** qualquer promessa de conformidade, garantia de acesso a mercado ou uso de logo/depoimento de cliente exige aprovação do founder e evidência específica.

## Critérios de aceite

1. 10 variantes acessíveis em URLs estáveis e 5 rotas de distribuição A/B.
2. Um único H1, navegação por teclado, foco visível, labels e validação compreensível.
3. Sem rolagem horizontal em 360, 390, 768 e 1440 px.
4. Formulário identifica `segment`, `variant`, `landing_page` e UTMs.
5. Nenhum claim apresenta exemplo como cliente real, certificação ou conclusão de conformidade.
6. Preview e produção publicados; produção conferida por status e conteúdo, não apenas HTTP 200.

## Métrica do experimento

Conversão primária: `leads válidos / sessões da variante`. Métricas auxiliares: clique no CTA, início do formulário e taxa de conclusão. A decisão de vencedor deve considerar qualidade do lead e tamanho de amostra, não somente contagem bruta.
