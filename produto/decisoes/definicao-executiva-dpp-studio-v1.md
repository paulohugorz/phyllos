# PHYLLOS DPP Studio V1 - Definicao Executiva

**Data:** 2026-06-25
**Status:** decisao executiva para piloto V1
**Relacionado:** [tese-produto-dpp-integrado-phyllos.md](tese-produto-dpp-integrado-phyllos.md), [prd-dpp-integrado-v0.md](prd-dpp-integrado-v0.md), [dpp-data-contract-v0.md](dpp-data-contract-v0.md)
**Versao de interface vigente:** [dpp-studio-versao-canonica-2026-06-25.md](dpp-studio-versao-canonica-2026-06-25.md)

## 1. Recorte exato da V1

A PHYLLOS V1 e um estudio web que recebe dados tecnicos de uma peca de moda, calcula indicadores por unidade e publica um passaporte digital com QR e flashcards para o consumidor -- sem editar molde, sem fazer ACV oficial e sem prometer conformidade regulatoria.

Qualquer funcionalidade que nao caiba nessa frase e candidata a corte ou fase futura.

## 2. Usuario primario da primeira validacao

Founder ou gestor de produto de marca independente brasileira, com lotes de 50-300 pecas, que ja tem ficha tecnica e quer colocar QR na etiqueta antes de julho de 2026.

Prioridade de recrutamento:

- marcas que ja recebem perguntas de composicao, origem ou impacto;
- marcas que mencionaram INMETRO, exportacao ou perguntas de consumidor;
- marcas capazes de trazer ficha tecnica real para um piloto manual.

## 3. Job-to-be-done

> Quando tenho uma peca pronta para vender, quero gerar um QR com o que sei sobre ela -- sem parecer que estou mentindo, sem contratar consultoria e sem montar um PLM.

Feature nova so entra na V1 se ajudar alguem a publicar um QR confiavel mais rapido ou aumentar a confianca do que foi publicado.

## 4. Dentro e fora da V1

Dentro:

- cadastro de peca com area, lote e perda de corte;
- cadastro de material com composicao e gramatura;
- calculo deterministico de peso, agua, energia e carbono;
- status de evidencia por campo;
- gate anti-greenwashing antes de publicar;
- QR e URL publica por peca;
- flashcards com badges de evidencia;
- dashboard simples de completude interno.

Fora:

- edicao ou geracao de molde;
- parser automatico de DXF/AAMA/ASTM;
- score verde ou nota composta de sustentabilidade;
- ACV ISO 14040/44 ou auditoria ambiental;
- auth, multi-tenant e faturamento;
- integracao automatica com Audaces, Lectra ou ERPs;
- declaracao garantida de conformidade regulatoria.

## 5. Promessa comercial

Promessa correta:

> Publique o que voce sabe sobre a sua peca -- com honestidade sobre o que e estimado, o que e documentado e o que ainda falta.

Copy de produto:

> PHYLLOS organiza os dados tecnicos que voce ja tem, calcula o impacto estimado por peca e gera um passaporte digital com QR para a etiqueta -- sem exagerar o que ainda nao foi verificado.

Nunca dizer:

- produto sustentavel;
- carbono certificado;
- conformidade EU ESPR garantida;
- zero impacto;
- score verde.

## 6. Metrica primaria do piloto

5 marcas geram um DPP completo com seus proprios dados em menos de 30 minutos e pelo menos 3 declaram intencao de pagar para repetir.

Metricas de suporte:

- nenhum piloto interpreta estimativa como dado verificado;
- pelo menos 1 piloto coloca o QR em etiqueta real;
- tempo medio por peca menor ou igual a 30 minutos.

## 7. Decisoes operacionais para o proximo ciclo

Identidade publica: usar o dominio Phyllos existente e posicionar DPP Studio como produto principal da V1 enquanto Fashion OS completo nao lanca.

Entrada de dados: formulario manual no piloto; uploads entram como anexos de evidencia, nao como parser.

Fonte dos fatores: agua, energia e carbono precisam de fonte documentada por fator antes de publicacao. Proxy de demonstracao nao e publicavel.

## 8. Versao operacional atual

A interface vigente do DPP Studio e o bundle em `phyllos/dpp-studio.html`, adotado a partir de `/Users/paulonascimento/Downloads/dpp-studio.html`.

Hash SHA-256:

```text
560add24d6e31860fee858805644270b31e030b0a5d0d5ab273d21d52194b8c2
```

Essa versao e a referencia para demos, ajustes e validacao ate nova decisao explicita do founder.

Status de publicacao:

- GitHub remoto: atualizado no commit `6559b48`;
- Netlify: aguardando permissao/liberacao para publicar como ultima versao;
- resposta operacional: nao declarar Netlify atualizado ate validar a URL final.
