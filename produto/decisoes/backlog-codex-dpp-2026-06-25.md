# Backlog Codex - DPP Integrado

**Data:** 2026-06-25  
**Status:** em execucao local - ciclo Codex C1-C6 iniciado  
**Relacionado:** [prd-dpp-integrado-v0.md](prd-dpp-integrado-v0.md)

---

## 1. Observacao sobre o repo atual

O briefing recebido cita `app/main.py`, `app/services/dpp_calculator.py`, `app/models/models.py` e `templates/dpp_public.html` como destinos de implementacao.

No checkout original deste ciclo, a raiz `app/` existia como estrutura, mas estava vazia. A implementacao FastAPI/DPP existente estava em `_legado/app/`, incluindo:

- `_legado/app/main.py`;
- `_legado/app/api/routes.py`;
- `_legado/app/models/models.py`;
- `_legado/app/templates/dpp_consumer.html`;
- `_legado/app/templates/etiqueta.html`.

Decisao operacional recebida em 2026-06-25:

1. promover `_legado/app` para `app/` por copia, nao por move;
2. tratar `_legado/` como referencia historica;
3. nao migrar `_legado/app/revenda/` para o backend DPP V1.

## 2. Execucao imediata ja concluida neste ciclo

- PRD v0 criado em `produto/decisoes/prd-dpp-integrado-v0.md`.
- Contrato de dados criado em `produto/decisoes/dpp-data-contract-v0.md`.
- QA anti-greenwashing criado em `produto/decisoes/dpp-anti-greenwashing-qa-v0.md`.
- Este backlog criou a ponte entre PRD e implementacao.
- Backend funcional promovido de `_legado/app` para `app/`, sem migrar `revenda`.
- Modelos, schemas e migracao simples receberam campos DPP: area, perda, lote, versao, datas, gramatura, fatores, indicadores calculados e status de evidencia.
- `app/services/dpp_calculator.py` criado com formula deterministica para area total, area perdida, peso, agua, energia e carbono.
- `app/validators/dpp_validators.py` criado com validacao de composicao 100%, evidencias minimas, GTIN/ficha obrigatorios e alertas de certificacao.
- `app/api/routes.py` atualizado para publicar DPP somente apos calculo e gate anti-greenwashing.
- `app/templates/dpp_consumer.html` atualizado para exibir badges de evidencia nos indicadores publicos e remover comparacoes ambientais nao auditadas.
- Testes unitarios criados em `tests/test_dpp_calculator.py` e `tests/test_dpp_validators.py`.

## 3. Proxima execucao no Codex

### C0 - Pendencias antes de push/deploy

- Revisar se `phyllos/dpp-studio.html` ja reflete QR real e fluxo de 7 etapas no estado atual do repo.
- Instalar dependencias Python de `requirements.txt` ou rodar em ambiente que ja tenha FastAPI/Jinja para validar render do template.
- Decidir se os arquivos novos em `app/` e `tests/` serao commitados neste branch.
- Se aprovado, commitar e subir as alteracoes.

### C1 - Backend promovido para `app/`

Status: concluido localmente.

- Copiar `_legado/app` para `app/`.
- Excluir `revenda` da migracao.
- Preservar templates, rotas, modelos, schemas e servicos necessarios ao DPP.

### C2 - Campos novos em `Peca` e `FichaTecnica`

Status: concluido localmente.

- `Peca`: `area_peca_m2`, `perda_corte_pct`, `lote_quantidade`, `dpp_version`, `data_publicacao`, `data_atualizacao`.
- `FichaTecnica`: `gramatura_g_m2`, fatores de agua/energia/carbono, resultados calculados e `evidencia_statuses`.

### C3 - Calculo deterministico

Status: concluido localmente.

- modulo: `app/services/dpp_calculator.py`.
- teste: `tests/test_dpp_calculator.py`.

### C4 - Validadores anti-greenwashing

Status: concluido localmente.

- modulo: `app/validators/dpp_validators.py`.
- teste: `tests/test_dpp_validators.py`.

### C5 - Endpoint de publicacao DPP

Status: concluido localmente.

- rota: `POST /pecas/{codigo}/dpp/publicar`.
- retorna `422` com erros, alertas e status de evidencia se faltar dado minimo.
- salva resultados calculados antes da publicacao quando o gate passa.

### C6 - Badges no passaporte publico

Status: concluido localmente em `app/templates/dpp_consumer.html`.

- Indicadores publicos exibem badge de evidencia.
- Texto comparativo nao auditado foi removido.
- Carbono, agua, energia e perda de corte aparecem como estimativas calculadas quando disponiveis.

## 4. Verificacao executada

- `python3 -m compileall app tests` com `PYTHONPYCACHEPREFIX=/private/tmp/codex_pycache`: passou.
- `python3 -m unittest discover -s tests`: 4 testes passaram.
- Varredura por textos antigos de promessa ambiental no template publico: sem ocorrencias.
- Validacao Jinja isolada nao executada porque os runtimes locais nao tinham `jinja2` instalado, embora `requirements.txt` declare `jinja2==3.1.5`.

## 5. Fora do ciclo Codex atual

- Parsers DXF/AAMA/ASTM/PDF.
- ISCM publico como score verde.
- Integracoes externas.
- Auth, multi-tenant e faturamento.
- Revenda.
- Pattern Engine e edicao de molde.
