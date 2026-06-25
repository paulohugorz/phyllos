# Roadmap e Cronograma - PHYLLOS DPP Integrado

**Data:** 2026-06-23
**Status:** plano executivo v0.1
**Premissa:** toda a tecnologia deve ser desenvolvida internamente com apoio de Codex, Claude e agentes PHYLLOS.
**Produto:** DPP middleware para moda - importacao/input tecnico, calculo por peca, evidencia, QR e flashcards.

---

## 1. Decisao executiva dos lideres

Os lideres recomendam abandonar o Motor de Moldes como primeiro produto e concentrar a V1 em DPP integrado.

Motivo: a PHYLLOS consegue desenvolver internamente a primeira versao com Codex/Claude se o escopo for software de dados, calculo, upload, normalizacao, QR e pagina publica. Editar molde, criar CAD ou interpretar geometria complexa eleva risco, prazo e necessidade de especialista externo.

## 2. Capacidade real com Codex e Claude

### O que e viavel internamente agora

- Prototipos HTML/CSS/JS e UX funcional.
- FastAPI ou backend equivalente.
- SQLite local evoluindo para Postgres/Supabase.
- Modelagem de dados.
- Upload e armazenamento de arquivos.
- CRUD de produtos, materiais, lotes e DPPs.
- Calculo deterministico de area, perda, peso, agua, energia e carbono.
- Geracao de QR.
- Pagina publica de flashcards.
- Testes unitarios e regressao basica.
- Documentacao tecnica, ADRs, runbooks e criterios de aceite.

### O que e viavel depois, ainda internamente

- Parser de CSV/XLSX.
- Parser parcial de PDF estruturado.
- Exportacao JSON/CSV.
- Dashboard interno.
- Integracao simples por API.
- Autenticacao e permissoes.
- Multiusuario e multiempresa.

### O que nao deve ser promessa da V1

- Parser robusto de todos os DXF/AAMA/ASTM.
- Calculo oficial de ACV.
- Auditoria ambiental.
- Compliance juridico garantido.
- Integracao nativa com todos os softwares de modelagem.
- Edicao de molde ou desenho.

## 3. Liderancas e responsabilidades

| Lider | Responsabilidade no roadmap | Entregavel principal |
|---|---|---|
| Founder Orchestrator | Sequencia, foco, cortes e go/no-go | plano aprovado e cadencia semanal |
| Product Director | ICP, jornada, escopo, criterios de aceite | PRD do DPP Integrado |
| Technology Director | arquitetura, stack, seguranca, APIs | arquitetura e backlog tecnico |
| Digital Products Lead | UX do Studio e flashcards | prototipo e fluxo navegavel |
| Data Intelligence Lead | modelo de dados, dicionario e metricas | schema e data dictionary |
| Materials Lead | fatores, evidencias e metodologia | matriz de materiais/indicadores |
| Supply Chain / Operations | lote, area, perda, producao e processo | fluxo operacional de dados |
| QA Agent | testes, acessibilidade e regressao | plano de QA e suite minima |
| CFO | custo, runway, milestones e payback | orçamento e gatilhos financeiros |

---

## 4. Arquitetura recomendada

### Stack inicial

- Frontend: HTML/CSS/JS no prototipo; depois app web leve.
- Backend: FastAPI.
- Banco: SQLite no desenvolvimento; Postgres/Supabase quando houver usuario real.
- Arquivos: armazenamento local no MVP; bucket futuro.
- QR: biblioteca server-side ou geracao por endpoint.
- Calculos: modulo deterministico testado, sem IA.
- IA: apenas assistencia interna para extrair/organizar texto quando houver revisao humana.

### Modulos

```text
DPP Studio
├── Product Registry
├── Material Registry
├── Technical File Intake
├── Area/Loss Calculator
├── Indicator Engine
├── Evidence Ledger
├── DPP Publisher
├── QR / Flashcard Viewer
└── QA / Audit Log
```

---

## 5. Cronograma recomendado

### Fase 0 - Alinhamento e base de decisao (semana 1)

Objetivo: travar a tese correta antes de construir.

Entregas:

- Premissa DPP integrada registrada em `.claude/agents/references/dpp-integrado-strategic-premises.md`.
- Roadmap vigente criado.
- PRD v0 registrado em `produto/decisoes/prd-dpp-integrado-v0.md`.
- Criterios de aceite do MVP registrados em `produto/decisoes/prd-dpp-integrado-v0.md`.
- Contrato de dados registrado em `produto/decisoes/dpp-data-contract-v0.md`.
- QA anti-greenwashing registrado em `produto/decisoes/dpp-anti-greenwashing-qa-v0.md`.
- Backlog Codex registrado em `produto/decisoes/backlog-codex-dpp-2026-06-25.md`.
- Lista de 5 usuarios/pilotos-alvo.

Responsaveis:

- Founder Orchestrator.
- Product Director.
- Technology Director.
- Digital Products Lead.

Critério de aceite:

- todos os lideres sabem que V1 nao edita molde;
- backlog inicial organizado por fases;
- riscos juridicos e de greenwashing declarados.

### Fase 1 - Prototipo navegavel e modelo de dados (semanas 2-3)

Objetivo: transformar a tese em fluxo testavel.

Entregas:

- `phyllos/dpp-studio.html` refinado.
- fluxo: upload/input tecnico -> produto -> material -> calculo -> flashcards.
- schema conceitual em SQL/Markdown, a partir de `produto/decisoes/dpp-data-contract-v0.md`.
- dicionario de dados, a partir de `produto/decisoes/dpp-data-contract-v0.md`.
- formulas documentadas.
- criterios de evidencia por campo.

Responsaveis:

- Digital Products Lead.
- Data Intelligence Lead.
- Materials Lead.
- QA Agent.

Uso de Codex/Claude:

- Codex implementa prototipo, schema e validacoes.
- Claude auxilia em PRD, copies, criterios de aceite e entrevistas.

Critério de aceite:

- 3 pessoas entendem o fluxo sem explicacao longa;
- calculos atualizam ao alterar area/perda/material;
- flashcards deixam claro o que e estimado/declarado/documentado.

### Fase 2 - Backend interno MVP (semanas 4-6)

Objetivo: sair de prototipo estatico para app interno funcional.

Entregas:

- FastAPI com entidades: produto, material, arquivo tecnico, lote, indicador, DPP, flashcard.
- SQLite com migrations simples.
- endpoint para calcular indicadores.
- endpoint para gerar DPP rascunho.
- endpoint de pagina publica por slug/codigo.
- upload de arquivo com metadados.
- testes unitarios dos calculos.

Responsaveis:

- Technology Director.
- Data Intelligence Lead.
- QA Agent.
- Tech Spec Writer.

Uso de Codex/Claude:

- Codex desenvolve backend, testes e rotas.
- Claude revisa especificacoes, edge cases e documentacao.

Critério de aceite:

- criar DPP completo por API;
- recalcular indicadores com teste deterministico;
- salvar arquivo/metadados;
- publicar flashcards em rota local.

### Fase 3 - Studio interno e QR funcional (semanas 7-9)

Objetivo: criar a ferramenta utilizavel por uma marca/atelie piloto.

Entregas:

- tela interna de cadastro de produto.
- tela de material/fatores.
- tela de arquivo tecnico e area/perda.
- preview de flashcards.
- QR apontando para pagina publica local/staging.
- status de evidencia por campo.
- exportacao simples JSON/CSV.

Responsaveis:

- Digital Products Lead.
- Frontend Agent.
- Technology Director.
- QA Agent.

Critério de aceite:

- usuario cria DPP sem tocar no codigo;
- QR abre pagina publica;
- campos ausentes aparecem como lacunas;
- interface funciona em desktop e tablet.

### Fase 4 - Piloto com dados reais (semanas 10-12)

Objetivo: validar se a PHYLLOS resolve dor real.

Entregas:

- plano operacional de piloto em `produto/decisoes/phyllos-dpp-v1-estrategia-piloto.md`;
- 3 a 5 produtos reais cadastrados.
- pelo menos 2 tipos de arquivo/input tecnico usados.
- matriz de materiais com fatores reais ou declarados.
- relatorio de lacunas por produto.
- feedback de usuarios piloto.
- decisao go/no-go para MVP publico.

Responsaveis:

- Product Director.
- Materials Lead.
- Supply Chain / Operations.
- Founder Orchestrator.
- QA Agent.

Critério de aceite:

- 5 DPPs rascunho gerados com dados reais;
- onboarding medio abaixo de 60 minutos para dados Tier 1;
- 2 QRs compartilhados espontaneamente em canal real;
- 1 marca pede cadastro de segunda peca;
- usuarios entendem o valor dos flashcards;
- lacunas recorrentes viram backlog;
- nenhuma claim ambiental e publicada sem status de evidencia.

### Fase 5 - MVP fechado / beta privado (meses 4-5)

Objetivo: preparar produto para usuarios externos controlados.

Entregas:

- login simples.
- organizacao/empresa.
- permissoes basicas.
- historico de versoes do DPP.
- storage de arquivos.
- logs de alteracao.
- termos e aviso de dados.
- deploy controlado.

Responsaveis:

- Technology Director.
- Digital Products Lead.
- QA Agent.
- CFO.

Critério de aceite:

- beta com 3 marcas/atelies;
- 20 DPPs gerados;
- custo mensal de infra controlado;
- bugs criticos zerados antes de expandir.

### Fase 6 - Integracoes e parsers (meses 6-8)

Objetivo: reduzir trabalho manual.

Entregas:

- parser CSV/XLSX de encaixe.
- importacao padrao de ficha tecnica.
- leitura parcial de PDF quando estruturado.
- API externa para criar DPP.
- conectores documentados.

Responsaveis:

- Technology Director.
- Data Intelligence Lead.
- QA Agent.

Critério de aceite:

- importar ao menos 2 formatos reais recorrentes;
- reduzir tempo de criacao de DPP em 50%;
- erros de importacao tratados com fallback manual.

---

## 6. Cronograma resumido

| Periodo | Marco | Resultado |
|---|---|---|
| Semana 1 | Alinhamento | tese e lideres sincronizados |
| Semanas 2-3 | Prototipo + dados | fluxo testavel e schema |
| Semanas 4-6 | Backend MVP | API, banco, calculos e DPP rascunho |
| Semanas 7-9 | Studio interno | interface, QR e flashcards |
| Semanas 10-12 | Piloto real | 5 DPPs com dados reais |
| Meses 4-5 | Beta privado | multiusuario basico e deploy |
| Meses 6-8 | Parsers/integracoes | importacao parcial e API |

---

## 7. Backlog por prioridade

### P0 - precisa existir para MVP

- Schema de produto/material/DPP.
- Formula de indicadores.
- Upload de arquivo.
- Input manual de area/perda.
- Cadastro de material com fatores.
- Calculo por peca.
- Status de evidencia.
- QR e pagina publica.
- Testes dos calculos.

### P1 - melhora piloto

- Exportacao JSON/CSV.
- Historico de versao.
- Dashboard de lacunas.
- Templates de flashcards.
- Importacao CSV/XLSX.
- Autenticacao simples.

### P2 - futuro

- Parser DXF/AAMA/ASTM.
- Integracoes nativas com ferramentas de modelagem.
- Assinatura/verificacao.
- JSON-LD completo.
- Multiempresa robusto.
- API para parceiros.

---

## 8. Riscos e mitigacoes

| Risco | Mitigacao |
|---|---|
| Usuario espera que PHYLLOS edite molde | copy e onboarding: "importa dados, nao edita desenho" |
| Indicadores virarem greenwashing | estados de evidencia obrigatorios |
| Dados de area/perda virem chute | campo de origem: arquivo, declarado ou estimado |
| Arquivos tecnicos variam demais | comecar com input manual + CSV/XLSX antes de parser complexo |
| Compliance regulatorio incerto | vender "DPP-ready" e transparencia, nao conformidade garantida |
| Escopo crescer para PLM | manter P0 estreito e go/no-go semanal |

---

## 9. Cadencia de gestao

### Semanal

- segunda: Founder + Product + Tech revisam prioridade.
- quarta: checkpoint tecnico Codex/Claude.
- sexta: demo, bugs, decisoes e prox semana.

### Por fase

- abertura: criterio de aceite escrito.
- meio: risco e ajuste de escopo.
- fechamento: demo + QA + decisao de avancar.

### Artefatos fixos

- PRD.
- ADRs.
- schema.
- backlog.
- changelog.
- plano de QA.
- relatorio de piloto.
- estrategia de piloto.

---

## 10. Proxima acao recomendada

PRD v0, contrato de dados, QA anti-greenwashing, backlog Codex e estrategia de piloto ja foram registrados em `produto/decisoes/`.

Proxima acao operacional: preparar um piloto assistido com 3 a 5 marcas reais usando `produto/decisoes/phyllos-dpp-v1-estrategia-piloto.md` como roteiro. A decisao de ambiente e Railway agora, com `DPP_BASE_URL=https://phyllos-production.up.railway.app`; dominio proprio fica para depois do primeiro sinal real.

Ordem:

1. subir o app no Railway e validar `GET /p/{uuid}`;
2. selecionar 5 marcas independentes com 1 a 3 pecas prontas ou quase prontas;
3. rodar onboarding assistido de 60 minutos com uma peca por marca;
4. publicar DPP Tier 1 por SKU/UUID, com GTIN opcional e status de evidencia visivel;
5. registrar tempo, lacunas, objecoes e uso real do QR em `outputs/piloto-dpp-v1.csv`;
6. decidir entre produto pago por DPP, concierge DPP ou organizacao tecnica/PLM lite.
