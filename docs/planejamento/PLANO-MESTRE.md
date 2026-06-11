# PLANO MESTRE — Fashion OS Fase 2
**PHYLLOS | Revisão: 2026-06-10 | Owner: Founder / CEO**

---

## 1. Sumário Executivo

A PHYLLOS tem um Fashion OS v1 funcional operando via terminal com FastAPI + SQLite + 22 agentes Claude. O gargalo hoje é operacional: só funciona para quem domina linha de comando. A Fase 2 converte essa infraestrutura em interface web usável por qualquer membro do time. A stack foi decidida (Next.js 14 + Tailwind + shadcn/ui), o custo de infra é R$0/mês, e o escopo está travado em cinco funcionalidades reais: coleções, peças, ficha técnica editável, galeria de imagens e exportação de PDF. O plano abaixo é sequencial, cada sprint é executável por um agente de código via Claude Code, e o critério de encerramento da Fase 2 é verificável: qualquer membro do time cria coleção + peça + exporta PDF sem abrir terminal em menos de 15 minutos.

---

## 2. Decisões que Precisam ser Tomadas ANTES de Qualquer Código

Todas as decisões abaixo têm prazo contado em dias úteis a partir de **10/06/2026 (quarta-feira)**.

| # | Decisão | Owner | Prazo | Formato de Entrega | Consequência se não decidir |
|---|---|---|---|---|---|
| D1 | Confirmar stack Next.js (CTO já recomendou — founder precisa aprovar formalmente) | CEO + CTO | **Hoje — D+0** | 1 parágrafo em `docs/decisions/D1-stack.md` | Sprint 0 não começa |
| D2 | Campo `medidas` na ficha técnica: texto livre ou JSON estruturado? | CTO + CPO | **D+1 (11/06)** | Comentário no schema `app/schemas/schemas.py` ou nota em `docs/decisions/D2-medidas.md` | Sprint 3 travado no modelo de dados |
| D3 | PDF de referência: uma ficha técnica existente anotada com os campos obrigatórios de output | CPO | **D+2 (12/06)** | PDF físico ou digital anotado, salvo em `docs/referencias/ficha-referencia-anotada.pdf` | Sprint 5 começa sem spec real de layout |
| D4 | Paleta visual e tipografia confirmadas para a interface | Design Lead | **D+1 (11/06)** | Arquivo `frontend/app/globals.css` com tokens CSS (Obsidian #0F0F0D, Linen #E8E4DC, Gold #B89A6A, fontes Cormorant Garamond + Jost) | Sprint 1 começa com placeholder e vai precisar de retrabalho visual |
| D5 | Cloudflare R2: criar conta e bucket, obter credenciais | CEO | **D+2 (12/06)** | Credenciais em `.env` local (nunca commitar) + confirmação verbal | Sprint 4 (upload de imagens) travado |
| D6 | Alembic: configurar controle de migrações antes de qualquer alteração no banco | CTO | **Dentro do Sprint 0** | `alembic/` inicializado no repo, primeira migration gerada | Dívida técnica na transição SQLite → PostgreSQL na Fase 4 |

---

## 3. Plano de Trabalho Fatiado por Dia

### Visão Geral do Calendário

```
Dia 1 (D+0, 10/06) — Sprint 0: Ambiente e fundação
Dia 2 (D+1, 11/06) — Sprint 1: Tipos, API client, shell de navegação
Dia 3 (D+2, 12/06) — Sprint 2: CRUD de coleções
Dia 4 (D+3, 13/06) — Sprint 3: CRUD de peças + ficha técnica
Dia 4 (D+3, 13/06) — Sprint 4: Upload de imagens + galeria (paralelo com Sprint 3)
Dia 5 (D+4, 16/06) — Sprint 5: Exportação de PDF
Dia 6 (D+5, 17/06) — Sprint 6: Dashboard + polish + estados de erro
```

Sprints 3 e 4 podem rodar em paralelo se houver dois agentes disponíveis. Dias úteis; D+4 cai segunda-feira (16/06) por causa do fim de semana.

---

### Sprint 0 — Ambiente e Fundação
**Dia:** 10/06/2026 (hoje)
**Objetivo:** repositório com Next.js rodando, shadcn/ui instalado, CORS habilitado no backend, Alembic inicializado.

**Arquivos a criar:**
```
frontend/package.json
frontend/next.config.ts
frontend/tailwind.config.ts
frontend/components.json          (config shadcn/ui)
frontend/tsconfig.json
frontend/app/layout.tsx           (shell vazio com <html> e <body>)
frontend/app/page.tsx             (placeholder "Fashion OS carregando...")
frontend/app/globals.css          (tokens de cor PHYLLOS — aguarda D4)
frontend/lib/types.ts             (interfaces vazias — preenchidas no Sprint 1)
frontend/lib/api-client.ts        (base URL configurável via env)
frontend/lib/utils.ts             (cn() do shadcn)
alembic.ini
alembic/env.py
alembic/versions/                 (diretório)
docs/decisions/                   (diretório)
docs/decisions/D1-stack.md        (registra a decisão de stack)
.env.local.example                (template de variáveis — sem valores reais)
```

**Arquivos a modificar:**
- `app/main.py` — adicionar 3 linhas: `CORSMiddleware` (allow_origins `http://localhost:3000`), `StaticFiles` para `/static/images`, e importar `images_router` (o router em si é criado no Sprint 4, mas o middleware e StaticFiles podem entrar agora)
- `requirements.txt` — adicionar `alembic==1.13.x`
- `README.md` — adicionar seção "Frontend" com instruções `pnpm install && pnpm dev`

**Critério de conclusão verificável:**
```bash
# Terminal 1 — backend
uvicorn app.main:app --reload
# Deve responder em http://localhost:8000/docs sem erro

# Terminal 2 — frontend
cd frontend && pnpm dev
# Deve responder em http://localhost:3000 sem erro de compilação

# Verificar CORS:
curl -H "Origin: http://localhost:3000" http://localhost:8000/colecoes
# Deve retornar JSON (lista vazia ou com dados) sem erro de CORS

# Verificar Alembic:
alembic current
# Deve retornar "head" sem erro
```

**Agente responsável:** `technology-director`
**Dependência:** D1 aprovada (stack Next.js). D6 configurado durante este sprint.
**Duração estimada:** 3–4 horas de sessão Claude Code.

---

### Sprint 1 — Tipos TypeScript, API Client e Shell de Navegação
**Dia:** 11/06/2026
**Objetivo:** todos os tipos TypeScript espelhando os schemas Pydantic, cliente HTTP tipado, e shell de navegação (sidebar + header) funcional.

**Arquivos a criar:**
```
frontend/lib/types.ts             (interfaces: Colecao, Peca, FichaTecnica, Imagem, status enums)
frontend/lib/api-client.ts        (funções: getColecoes, getColecao, createColecao,
                                   getPecas, getPeca, createPeca,
                                   getFicha, updateFicha — todas tipadas)
frontend/components/layout/sidebar.tsx   (nav: Coleções, Galeria, links ativos)
frontend/components/layout/header.tsx    (breadcrumb + título da página)
frontend/app/layout.tsx           (shell real: sidebar + header + <main>)
frontend/app/colecoes/page.tsx    (placeholder "Carregando coleções...")
frontend/app/galeria/page.tsx     (placeholder "Galeria")
```

**Arquivos a modificar:**
- `frontend/app/globals.css` — aplicar tokens finais de cor (depende D4 entregue hoje)
- `frontend/app/page.tsx` — redirecionar para `/colecoes` ou exibir dashboard placeholder

**Critério de conclusão verificável:**
```bash
# No browser:
# http://localhost:3000 → sidebar visível, header visível, sem erros de console
# http://localhost:3000/colecoes → página carrega sem erro 500
# http://localhost:3000/galeria → página carrega sem erro 500

# TypeScript sem erros:
cd frontend && pnpm tsc --noEmit
# Deve retornar sem erros

# API client funcionando:
# Abrir console do browser em /colecoes e executar:
# import { getColecoes } from '@/lib/api-client'; getColecoes()
# Deve retornar array (vazio ou com dados)
```

**Agente responsável:** `frontend-agent` (layout, componentes) + `technology-director` (types.ts espelhando schemas Pydantic)
**Dependência:** Sprint 0 concluído. D4 entregue.
**Duração estimada:** 6–8 horas.

---

### Sprint 2 — CRUD de Coleções
**Dia:** 12/06/2026
**Objetivo:** lista de coleções funcional, formulário de criação, detalhe da coleção — tudo lendo e escrevendo na API real.

**Arquivos a criar:**
```
frontend/components/colecao-card.tsx         (card com nome, status, contador de peças, data)
frontend/components/colecao-form.tsx         (formulário: nome, temporada, descrição, status)
frontend/app/colecoes/page.tsx               (lista real com fetch de /colecoes + botão Nova Coleção)
frontend/app/colecoes/nova/page.tsx          (formulário de criação com redirect após salvar)
frontend/app/colecoes/[id]/page.tsx          (detalhe: header da coleção + lista vazia de peças)
```

**Arquivos a modificar:**
- `frontend/lib/api-client.ts` — confirmar que `createColecao`, `getColecao` estão completos
- `frontend/app/colecoes/page.tsx` — substituir placeholder por componente real

**Estados de edge case a implementar:**
- Zero coleções: mensagem "Nenhuma coleção ainda. Crie a primeira coleção para começar." + botão CTA
- Loading state: skeleton de 3 cards enquanto fetch roda
- Erro de rede: mensagem "Não foi possível carregar as coleções. Verifique se o backend está rodando."
- Nome duplicado na mesma temporada: mensagem de erro inline no formulário

**Critério de conclusão verificável:**
```bash
# Teste manual (sequência):
# 1. Acessar http://localhost:3000/colecoes — ver estado vazio
# 2. Clicar "Nova Coleção" — formulário abre
# 3. Preencher nome "SS26 Essencial Run", temporada "SS26", descrição com 10+ chars
# 4. Salvar — coleção aparece na lista sem reload completo
# 5. Clicar na coleção — detalhe abre com header correto
# 6. Tentar criar segunda coleção com mesmo nome/temporada — sistema bloqueia

# API confirma:
curl http://localhost:8000/colecoes
# Deve retornar a coleção criada
```

**Agente responsável:** `frontend-agent`
**Dependência:** Sprint 1 concluído.
**Duração estimada:** 6–8 horas.

---

### Sprint 3 — CRUD de Peças + Ficha Técnica Editável
**Dia:** 13/06/2026
**Objetivo:** formulário de peça funcional, detalhe de peça com abas, ficha técnica editável com autosave e indicador de completude.

**Arquivos a criar:**
```
frontend/components/peca-card.tsx                    (card com SKU, nome, status, imagem principal)
frontend/components/peca-form.tsx                    (formulário: SKU auto, nome, categoria, preço, custo)
frontend/components/ficha-tecnica-form.tsx           (seções: Materiais, Construção, Acabamentos, Tamanhos)
frontend/app/colecoes/[id]/pecas/nova/page.tsx       (formulário nova peça dentro de coleção)
frontend/app/colecoes/[id]/pecas/[codigo]/page.tsx   (detalhe: abas Dados Gerais / Ficha Técnica / Galeria)
```

**Arquivos a modificar:**
- `frontend/app/colecoes/[id]/page.tsx` — adicionar lista real de peças com `peca-card.tsx` + botão Nova Peça
- `frontend/lib/api-client.ts` — confirmar `createPeca`, `getPeca`, `updateFicha`

**Comportamentos críticos a implementar:**
- SKU gerado automaticamente no formato `PH` + ano atual + sequencial de 3 dígitos (ex: `PH26001`) se campo vazio
- Autosave da ficha a cada 30 segundos — indicador "Último salvo: HH:MM"
- Indicador de completude "Ficha X/12 campos preenchidos" atualizado em tempo real
- Botão "Marcar como Finalizada" só habilitado quando todos os campos obrigatórios preenchidos
- Transição para status "Produção" bloqueada se ficha não estiver Finalizada

**Decisão D2 se aplica aqui:** campo `medidas` implementado conforme decisão tomada em D+1.

**Critério de conclusão verificável:**
```bash
# Teste manual (sequência):
# 1. Abrir detalhe de coleção criada no Sprint 2
# 2. Clicar "Nova Peça" — formulário abre com SKU pré-preenchido
# 3. Salvar peça — aparece na lista da coleção
# 4. Abrir detalhe da peça — 3 abas visíveis
# 5. Na aba Ficha Técnica, preencher parcialmente — indicador atualiza
# 6. Aguardar 30s — indicador "Último salvo" atualiza
# 7. Tentar marcar Finalizada com campos obrigatórios vazios — sistema bloqueia
# 8. Preencher todos obrigatórios — botão Finalizar habilita e funciona
# 9. Tentar mudar status para "Produção" com ficha não finalizada — sistema bloqueia

# API confirma:
curl http://localhost:8000/pecas
# Deve retornar a(s) peça(s) criada(s)
```

**Agente responsável:** `frontend-agent`
**Dependência:** Sprint 2 concluído. Decisão D2 tomada.
**Duração estimada:** 6–8 horas.

---

### Sprint 4 — Upload de Imagens e Galeria (Paralelo com Sprint 3)
**Dia:** 13/06/2026 (paralelo com Sprint 3 se houver dois agentes)
**Objetivo:** endpoint de upload no backend, componente de galeria no frontend, imagem marcada como principal aparece no card da peça.

**Arquivos a criar (backend):**
```
app/api/routes_images.py    (POST /imagens/upload/{peca_id}, GET /imagens/{peca_id})
data/images/                (diretório criado no primeiro upload — garantir que existe)
```

**Arquivos a criar (frontend):**
```
frontend/components/image-gallery.tsx    (grid de imagens, upload drag-and-drop, tipos, marcar principal)
frontend/app/api/imagens/route.ts        (proxy Next.js → FastAPI para upload)
```

**Arquivos a modificar:**
- `app/main.py` — adicionar `images_router` e `StaticFiles` mount (se não feito no Sprint 0)
- `frontend/app/colecoes/[id]/pecas/[codigo]/page.tsx` — aba Galeria usa `image-gallery.tsx`
- `frontend/components/peca-card.tsx` — exibe imagem principal se existir

**Configuração necessária:**
- Variável de ambiente `NEXT_PUBLIC_API_URL=http://localhost:8000` em `frontend/.env.local`
- Se Cloudflare R2 estiver disponível (D5 entregue): backend salva em R2 via boto3 SDK + variáveis `CF_R2_ACCESS_KEY`, `CF_R2_SECRET_KEY`, `CF_R2_BUCKET`, `CF_R2_ENDPOINT` em `.env` do backend
- Se R2 não estiver disponível: salva em `data/images/{peca_id}/` localmente (funcional para uso interno)

**Critério de conclusão verificável:**
```bash
# Teste manual:
# 1. Abrir detalhe de uma peça, aba Galeria
# 2. Fazer upload de uma imagem JPG (< 10MB) — imagem aparece na galeria
# 3. Fazer upload de uma imagem > 10MB — mensagem de erro clara
# 4. Marcar imagem como Principal — aparece no card da peça na lista da coleção
# 5. Definir tipo "Sketch" para uma imagem — tipo aparece na galeria
# 6. Tentar upload do 21o arquivo — mensagem "Limite atingido"

# API confirma:
curl http://localhost:8000/imagens/{peca_id}
# Deve retornar lista de imagens com metadados
```

**Agente responsável:** `technology-director` (backend) + `frontend-agent` (componente galeria)
**Dependência:** Sprint 1 concluído. D5 entregue (Cloudflare R2) — opcional para começar.
**Duração estimada:** 6–8 horas.

---

### Sprint 5 — Exportação de PDF
**Dia:** 16/06/2026 (segunda-feira)
**Objetivo:** botão "Exportar PDF" no detalhe da peça gera e faz download de PDF client-side com layout PHYLLOS.

**Arquivos a criar:**
```
frontend/components/ficha-tecnica-pdf.tsx      (@react-pdf/renderer — layout completo)
frontend/components/pdf-download-button.tsx    (dynamic import com ssr: false)
frontend/public/logo-phyllos.png               (logo para o PDF — inserir ativo real)
```

**Arquivos a modificar:**
- `frontend/package.json` — adicionar `@react-pdf/renderer@^3.x`
- `frontend/app/colecoes/[id]/pecas/[codigo]/page.tsx` — integrar `pdf-download-button.tsx`

**Layout do PDF (conforme spec CPO):**
- Logo PHYLLOS no topo direito
- Nome da coleção + SKU + nome da peça no cabeçalho
- Seções: Identificação, Materiais, Construção, Acabamentos, Tamanhos
- Apenas campos preenchidos aparecem (campos vazios omitidos)
- Rodapé: data de exportação + "Documento em revisão" se ficha não Finalizada
- Nome do arquivo: `PHYLLOS_[SKU]_ficha_[YYYYMMDD].pdf`

**Referência:** usar ficha anotada entregue em D3 como especificação de layout.

**Critério de conclusão verificável:**
```bash
# Teste manual:
# 1. Abrir detalhe de peça com ficha preenchida (criada nos sprints anteriores)
# 2. Clicar "Exportar PDF"
# 3. PDF faz download em menos de 5 segundos
# 4. Verificar: nome do arquivo segue padrão PHYLLOS_PH26001_ficha_20260616.pdf
# 5. Verificar: PDF contém logo, coleção, SKU, todos os campos preenchidos, data
# 6. Abrir PDF em leitor externo (Preview/Acrobat) — legível, sem artefato
# 7. Mostrar PDF para founder — "aceitaria enviar para fornecedor?" deve ser Sim

# Não depende de servidor para gerar:
# Desligar backend (Ctrl+C no uvicorn) e tentar exportar PDF
# Deve funcionar (client-side rendering)
```

**Agente responsável:** `frontend-agent`
**Dependência:** Sprint 3 concluído. D3 entregue (ficha de referência).
**Duração estimada:** 4–6 horas.

---

### Sprint 6 — Dashboard, Polish e Estados de Erro
**Dia:** 17/06/2026 (terça-feira)
**Objetivo:** dashboard com métricas básicas, loading skeletons em todas as páginas, estados de erro tratados, experiência completa sem fallback para terminal.

**Arquivos a criar:**
```
frontend/app/page.tsx    (dashboard real: total de coleções, peças por status, atalhos rápidos)
frontend/components/ui/skeleton.tsx     (se não instalado pelo shadcn)
frontend/components/ui/alert.tsx        (mensagens de erro e sucesso)
```

**Arquivos a modificar:**
- Todos os `page.tsx` — adicionar loading skeletons e error boundaries
- `frontend/components/colecao-card.tsx` — estados hover, focus acessível
- `frontend/components/peca-card.tsx` — idem
- `README.md` — atualizar com instruções completas de uso da interface

**Critério de conclusão verificável (teste de aceitação da Fase 2):**
```bash
# Critério 1 — Operacional:
# Pedir para alguém do time (ou o próprio founder) seguir o fluxo do zero:
# Home → Nova Coleção → Nova Peça → Preencher Ficha → Exportar PDF
# Tempo máximo: 15 minutos. Sem abrir terminal. Sem consultar documentação técnica.

# Critério 2 — Cobertura de dados:
# Todas as peças da coleção ativa (SS26 Essencial Run ou equivalente)
# devem estar cadastradas na plataforma com ficha ao menos iniciada.

# Critério 3 — PDF utilizável:
# Mostrar o PDF exportado para o fornecedor atual (ou simular o envio).
# Resposta esperada: "posso cotar com isso" sem pedir reformatação.

# Verificação técnica final:
cd frontend && pnpm tsc --noEmit   # zero erros TypeScript
cd frontend && pnpm build          # build de produção sem erro
```

**Agente responsável:** `frontend-agent` + `digital-products-lead` (validação dos critérios de aceite)
**Dependência:** Sprints 2, 3, 4 e 5 concluídos.
**Duração estimada:** 4–6 horas.

---

## 4. Mapa de Riscos

Ordenados por probabilidade × impacto (maior primeiro).

### Risco 1 — PDF inferior ao template Markdown atual
**Probabilidade:** Alta | **Impacto:** Alto
O PDF gerado pelo `@react-pdf/renderer` pode ter layout inferior ao template Markdown que o time já usa. Se isso acontecer, o time ignora a plataforma e volta ao terminal.
**Mitigação:**
- Decisão D3 (ficha de referência anotada) é pré-requisito obrigatório para o Sprint 5.
- Testar o PDF com o fornecedor real antes de declarar Sprint 5 concluído.
- Se o `@react-pdf/renderer` não entregar a qualidade mínima, avaliar `pdfmake` ou `jsPDF` como alternativa antes de encerrar o sprint — não depois.
- Critério verificável: o founder deve responder "sim, enviaria para fornecedor" antes do sprint ser fechado.

### Risco 2 — Scope creep técnico durante os sprints
**Probabilidade:** Alta | **Impacto:** Médio
Cada sprint vai gerar ideias de feature nova (histórico de versões, comentários, filtros, dashboard de métricas). O agente de código não tem autonomia para rejeitar; o founder pode aprovar sem perceber que está postergando o critério de encerramento.
**Mitigação:**
- Qualquer feature não listada neste plano vai para o arquivo `docs/planejamento/fase3-backlog.md` sem discussão.
- Antes de iniciar qualquer sprint, o agente deve confirmar: "Esta tarefa está no escopo do Sprint X?" Se a resposta for não, registrar em backlog e prosseguir.
- A regra do CEO é explícita: integração com agentes Claude é Fase 3. Qualquer código que chame `claude` ou `anthropic` dentro de `frontend/` é bloqueado nesta fase.

### Risco 3 — Nenhum usuário real testando durante o build
**Probabilidade:** Média | **Impacto:** Alto
A interface pode ser construída "corretamente" segundo os wireframes e ser inutilizável na prática. Sem teste real durante o desenvolvimento, o problema aparece só no Sprint 6 — tarde demais para redesign.
**Mitigação:**
- Ao final dos Sprints 2 e 3 (não só no 6), o founder executa o fluxo principal por 10 minutos.
- Feedback capturado em `docs/feedback/sprint-[n]-fundadora.md` com no máximo 3 itens de ajuste.
- Itens de ajuste entram no sprint seguinte como tarefa de polish, não como novo sprint.

### Risco 4 — Dívida técnica de SQLite bloqueando a Fase 4
**Probabilidade:** Baixa | **Impacto:** Alto
Sem Alembic configurado agora, qualquer alteração futura no schema (Fase 4: MRP, estoque) exige migração manual com risco de corrupção de dados.
**Mitigação:**
- Alembic é obrigatório no Sprint 0, não opcional. A primeira migration deve ser gerada a partir do schema atual do SQLAlchemy.
- Comando de verificação no critério de conclusão do Sprint 0: `alembic current` deve retornar `head`.
- Toda alteração de schema nas Fases seguintes usa `alembic revision --autogenerate` — documentar isso no README agora.

### Risco 5 — Perda de dados do SQLite (arquivo local)
**Probabilidade:** Baixa | **Impacto:** Alto
O banco SQLite está no disco local do founder. Um acidente (formatação, falha de HD) zera o Fashion OS inteiro.
**Mitigação:**
- CFO recomenda: Litestream para replicação contínua do SQLite para Cloudflare R2 (~R$5/mês).
- Alternativa imediata e gratuita: script de backup diário via cron para Google Drive ou Time Machine.
- Implementar no Sprint 0 como tarefa de 1 hora: `scripts/backup-db.sh` com cron entry documentado.
- Não esperar perder dados para implementar.

---

## 5. O que NÃO Está Neste Plano

Lista explícita do que foi decidido deixar para depois, com justificativa.

| Feature | Decisão | Por quê | Quando entra |
|---|---|---|---|
| Autenticação (login/senha) | Fora da Fase 2 | Uso interno/localhost. Adicionar autenticação agora é +2 dias de esforço sem valor operacional imediato | Fase 3 (quando houver colaborador externo) |
| Histórico de versões de ficha técnica | Fora | Requer colaboração multi-usuário. Hoje é uso solo. Complexidade desproporcional | Fase 3 |
| Dashboard de status com métricas reais | Fora (Sprint 6 tem dashboard básico) | Sem dados de produção suficientes ainda para métricas significativas | Fase 3 |
| Pipeline Kanban de 22 etapas | Fora | Complexidade desproporcional para o volume atual de SKUs | Fase 3 |
| Comentários e anotações por peça | Fora | Feature de colaboração, não de uso solo | Fase 3 |
| Busca full-text | Fora | Sem volume de dados suficiente para justificar | Fase 3 |
| Integração com agentes Claude na interface | Fora | A interface cadastra e exporta; agentes operam via terminal. Misturar agora é scope creep estrutural | Fase 4 |
| Geração de imagem (ComfyUI / Stable Diffusion) | Fora | Fase 3 inteira. Requer GPU, endpoints novos, WebSocket | Fase 3 |
| MRP, ordem de produção, estoque | Fora | Fase 4. Requer migração para PostgreSQL antes | Fase 4 |
| App mobile / responsividade completa | Fora | Founder opera em desktop | Fase 3 |
| Exportação Excel/CSV | Fora | PDF cobre o caso de uso do fornecedor inteiramente | Fase 3 |
| Deploy em cloud (Vercel, Railway) | Fora | Uso interno/localhost é suficiente para Fase 2 | Fase 5 (vendas) |
| Multi-tenancy / `brand_id` isolado | Fora (mas arquitetura considera) | Strategy recomenda arquitetura SaaS-ready sem expor ainda. CTO deve validar se o schema atual já suporta isolamento futuro | Fase 3 (decisão Q4 2026) |
| Calculadora de custo/margem integrada | Fora | Finance Agent opera separado. Não duplicar | Fase 3 |
| Comunicação pública sobre o Fashion OS | Fora | CMO é explícita: sem âncora visual, a história não tem entrega. Capturar bastidores agora, publicar após primeira ficha técnica real exportada | ~4–8 semanas |

---

## 6. Gatilhos de Revisão do Plano

O plano deve ser revisado quando qualquer um destes marcos for atingido. Não por data.

| # | Gatilho | Ação |
|---|---|---|
| G1 | Sprint 3 concluído e o founder testa o fluxo por 10 minutos | Registrar feedback em `docs/feedback/sprint-3-fundadora.md`. Se mais de 2 itens críticos, revisar Sprints 4–6 antes de prosseguir. |
| G2 | Sprint 5 concluído e PDF apresentado para fornecedor | Se fornecedor pede reformatação, suspender Sprint 6 e reabrir Sprint 5 com novo layout. |
| G3 | Critérios de aceite da Fase 2 todos verificados | Abrir planejamento da Fase 3. Não antes. |
| G4 | Qualquer sprint ultrapassar 2x a estimativa de tempo | Revisar escopo do sprint, não a estimativa. Reduzir escopo, não alongar o dia. |
| G5 | Decision D2 (campo `medidas`) não entregue antes do Sprint 3 começar | Bloquear Sprint 3 até decisão. Não improvisar modelo de dados sem spec. |
| G6 | Founder decide adicionar feature fora do escopo deste plano | Registrar em `docs/planejamento/fase3-backlog.md` e retornar ao sprint atual. Se a feature for de segurança ou integridade de dados, escalar para CTO com urgência. |
| G7 | Primeira coleção SS26 completamente cadastrada na plataforma com fichas técnicas geradas | Acionar CMO para iniciar captura de conteúdo de bastidores (conforme plano de comunicação). |

---

## 7. Primeira Ação — Próximas 2 Horas (a partir de 10/06/2026)

O founder deve fazer exatamente o seguinte, nesta ordem, para desbloquear o Sprint 0:

**Ação 1 — Aprovar stack (30 minutos):**
```bash
mkdir -p /Users/paulonascimento/meu-primeiro-repo/docs/decisions
```
Criar o arquivo `docs/decisions/D1-stack.md` com o texto:
```
# D1 — Decisão de Stack: Next.js 14

Data: 2026-06-10
Decisão: Next.js 14.2.x com App Router, Tailwind CSS 3.4, shadcn/ui, TypeScript.
Streamlit rejeitado conforme ADR do CTO (ver docs/planejamento/cto-arquitetura-tecnica.md).
Aprovado por: [nome do founder]
```
Salvar e commitar. Isso autoriza formalmente o Sprint 0 a começar.

**Ação 2 — Verificar pré-requisitos do ambiente (30 minutos):**
```bash
node --version    # deve ser 20.x LTS
pnpm --version    # se não instalado: npm install -g pnpm
python --version  # deve ser 3.10+
uvicorn app.main:app --reload  # backend deve subir em http://localhost:8000/docs
```
Se qualquer um falhar, resolver antes de passar o Sprint 0 para o agente.

**Ação 3 — Criar conta Cloudflare R2 (30 minutos, pode ser paralelo):**
- Acessar https://dash.cloudflare.com, criar conta gratuita se não existir
- Criar bucket `phyllos-fashion-os`
- Gerar API token com permissão `Object Read & Write` no bucket
- Salvar credenciais em `.env` local (nunca commitar):
```
CF_R2_ACCESS_KEY=...
CF_R2_SECRET_KEY=...
CF_R2_BUCKET=phyllos-fashion-os
CF_R2_ENDPOINT=https://[account_id].r2.cloudflarestorage.com
```

**Ação 4 — Confirmar com CPO os campos obrigatórios da ficha técnica (30 minutos):**
Abrir uma ficha técnica existente (pasta `templates/`) e anotar: quais campos são obrigatórios, quais aparecem no PDF, quais são opcionais. Salvar como `docs/referencias/ficha-campos-mvp.md`. Isso alimenta o Sprint 3 e o Sprint 5.

Ao concluir estas 4 ações, o Sprint 0 pode começar imediatamente via Claude Code sem nenhum bloqueio adicional.

---

## Apêndice — Referência de Paths do Projeto

```
/meu-primeiro-repo/
├── app/
│   ├── main.py                    (modificar no Sprint 0 e Sprint 4)
│   ├── api/routes.py              (NÃO tocar)
│   ├── api/routes_images.py       (criar no Sprint 4)
│   ├── models/models.py           (NÃO tocar, exceto D2)
│   ├── schemas/schemas.py         (NÃO tocar)
│   └── core/database.py           (NÃO tocar)
├── frontend/                      (criar no Sprint 0)
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── globals.css
│   │   ├── colecoes/...
│   │   ├── galeria/page.tsx
│   │   └── api/imagens/route.ts
│   ├── components/
│   │   ├── ui/                    (shadcn/ui gerados)
│   │   ├── layout/sidebar.tsx
│   │   ├── layout/header.tsx
│   │   ├── colecao-card.tsx
│   │   ├── colecao-form.tsx
│   │   ├── peca-card.tsx
│   │   ├── peca-form.tsx
│   │   ├── ficha-tecnica-form.tsx
│   │   ├── ficha-tecnica-pdf.tsx
│   │   ├── pdf-download-button.tsx
│   │   └── image-gallery.tsx
│   └── lib/
│       ├── api-client.ts
│       ├── types.ts
│       └── utils.ts
├── data/images/                   (criar no Sprint 4)
├── alembic/                       (criar no Sprint 0)
├── scripts/backup-db.sh           (criar no Sprint 0)
├── docs/
│   ├── decisions/D1-stack.md      (criar antes do Sprint 0)
│   ├── decisions/D2-medidas.md    (criar até D+1)
│   ├── referencias/ficha-referencia-anotada.pdf  (entregar até D+2)
│   ├── referencias/ficha-campos-mvp.md           (criar hoje)
│   ├── feedback/                  (criar no Sprint 3)
│   └── planejamento/fase3-backlog.md              (criar quando necessário)
├── requirements.txt               (adicionar alembic no Sprint 0)
└── README.md                      (atualizar no Sprint 0 e Sprint 6)
```

---

*Documento gerado em 2026-06-10. Próxima revisão: gatilho G1 (após Sprint 3 testado pelo founder) ou gatilho G4 (sprint que ultrapassar 2x a estimativa).*
