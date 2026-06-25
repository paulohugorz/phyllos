# Backlog Codex - DPP Integrado

**Data:** 2026-06-25  
**Status:** plano de execucao a partir do PRD v0  
**Relacionado:** [prd-dpp-integrado-v0.md](prd-dpp-integrado-v0.md)

---

## 1. Observacao sobre o repo atual

O briefing recebido cita `app/main.py`, `app/services/dpp_calculator.py`, `app/models/models.py` e `templates/dpp_public.html` como destinos de implementacao.

No checkout atual, a raiz `app/` existe como estrutura, mas esta vazia. A implementacao FastAPI/DPP existente esta em `_legado/app/`, incluindo:

- `_legado/app/main.py`;
- `_legado/app/api/routes.py`;
- `_legado/app/models/models.py`;
- `_legado/app/templates/dpp_consumer.html`;
- `_legado/app/templates/etiqueta.html`.

Decisao recomendada antes de codar backend:

1. escolher se a V1 continua evoluindo em `_legado/app`; ou
2. promover/migrar `_legado/app` para `app/` como backend ativo; ou
3. criar um backend novo e enxuto em `app/`, usando `_legado/app` apenas como referencia.

## 2. Execucao imediata ja concluida neste ciclo

- PRD v0 criado em `produto/decisoes/prd-dpp-integrado-v0.md`.
- Contrato de dados criado em `produto/decisoes/dpp-data-contract-v0.md`.
- QA anti-greenwashing criado em `produto/decisoes/dpp-anti-greenwashing-qa-v0.md`.
- Este backlog criou a ponte entre PRD e implementacao.

## 3. Proxima execucao no Codex

### P0 - Fonte de verdade e prototipo

- Atualizar `phyllos/dpp-studio.html` de 4 etapas para 7 etapas.
- Incluir estados: `ausente`, `declarado`, `calculado`, `documentado`, `verificado`.
- Remover ou renomear qualquer status `estimado` solto para `calculado` com label de estimativa.
- Adicionar checklist visual de publicacao.
- Exibir rodape anti-greenwashing no preview publico.

### P1 - Calculo deterministico

Destino recomendado apos decisao de backend:

- `app/services/dpp_calculator.py` ou `_legado/app/services/dpp_calculator.py`.

Funcoes:

- validar composicao somando 100%;
- converter gramatura g/m2 para kg/m2;
- calcular area total, area perdida, peso, agua, energia e carbono;
- validar perda menor que 100%;
- retornar resultado com status `calculado` e label publico.

### P2 - Validadores anti-greenwashing

Destino recomendado:

- `app/validators/dpp_validators.py` ou `_legado/app/validators/dpp_validators.py`.

Regras:

- impedir publicacao com obrigatorio ausente;
- bloquear score verde publico;
- exigir label para indicador calculado;
- tratar certificacao expirada;
- marcar fator declarado como nao auditado;
- impedir fator fora de limite sem documento.

### P3 - Schema e modelos

Destino recomendado:

- `app/models/models.py` ou `_legado/app/models/models.py`;
- `app/schemas/schemas.py` ou `_legado/app/schemas/schemas.py`.

Adicionar ou revisar:

- campos de evidencia por campo relevante;
- `versao_dpp`;
- `data_publicacao`;
- `data_atualizacao`;
- `area_peca_m2`;
- `perda_corte_pct`;
- `gramatura_g_m2`;
- fatores de impacto;
- status de certificacao.

### P4 - Endpoints

Destino recomendado:

- `app/api/routes.py` ou `_legado/app/api/routes.py`.

Endpoints:

- criar/atualizar produto com dados DPP;
- calcular indicadores;
- publicar DPP com gate de completude;
- revogar DPP;
- gerar QR;
- renderizar pagina publica.

### P5 - Testes

Destino recomendado:

- `tests/test_dpp_calculator.py`;
- `tests/test_dpp_validators.py`.

Casos:

- composicao soma 100%;
- composicao soma diferente falha;
- perda 20% gera resultado esperado;
- perda >= 100 falha;
- campo ausente bloqueia publicacao;
- indicador calculado sem label falha;
- certificacao expirada nao aparece como valida.

## 4. Pergunta de decisao para o founder

Antes da implementacao backend, decidir:

> A V1 tecnica sera evoluida dentro de `_legado/app` para preservar o que ja existe, ou vamos promover esse backend para `app/` e tratar `_legado` apenas como arquivo historico?

Recomendacao: para velocidade e menor risco, evoluir `_legado/app` primeiro se a publicacao Railway atual ainda depende dele. Depois migrar com testes.
