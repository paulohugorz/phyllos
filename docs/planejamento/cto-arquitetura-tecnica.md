# Architecture Decision Record — Fashion OS Interface Web (Fase 2)
**Data:** 2026-06-10 | **CTO, PHYLLOS** | **Status:** Aprovado para execução

## 1. Decisão de Stack: Next.js 14 (App Router) + Tailwind CSS

### Veredicto: Next.js. Streamlit rejeitado.

**Problemas que eliminam o Streamlit:**
- Cada interação re-executa o script inteiro → galeria instável acima de 20 registros
- Sem controle de rotas reais (`/colecoes/3/pecas` não existe em Streamlit)
- Não tem suporte nativo a WebSocket (necessário para streaming do ComfyUI na Fase 3)
- Não é deployável como produto SaaS sem reescrita completa

**Stack final:**
```
Frontend:    Next.js 14.2.x — App Router
CSS:         Tailwind CSS 3.4.x
Componentes: shadcn/ui (headless, sem vendor lock-in)
PDF:         @react-pdf/renderer 3.x (client-side, sem dependência de servidor)
Estado:      React Context + SWR
TypeScript:  sim — schemas Pydantic são fonte de verdade para os types
Runtime:     Node.js 20 LTS
Package mgr: pnpm
```

---

## 2. Arquitetura — Diagrama Textual

```
Browser (localhost:3000)
└── Next.js App Router (frontend/)
    ├── app/layout.tsx         ← Shell: sidebar + header
    ├── app/page.tsx           ← Dashboard: métricas + atalhos
    ├── app/colecoes/
    │   ├── page.tsx           ← Lista de coleções
    │   ├── nova/page.tsx      ← Formulário de criação
    │   └── [id]/
    │       ├── page.tsx       ← Detalhe da coleção + lista peças
    │       └── pecas/
    │           ├── nova/page.tsx       ← Formulário peça
    │           └── [codigo]/page.tsx  ← Detalhe peça + ficha + PDF
    ├── app/galeria/page.tsx   ← Grid de imagens global
    └── app/api/imagens/route.ts  ← Proxy upload → FastAPI

    lib/
    ├── api-client.ts          ← Wrapper fetch tipado
    └── types.ts               ← Types espelhando schemas Pydantic

              ↓ fetch() sobre HTTP

FastAPI (localhost:8000) — SEM ALTERAÇÃO EXCETO:
├── GET/POST  /colecoes          (existente)
├── GET/POST/PATCH /pecas        (existente)
├── GET/POST  /fichas-tecnicas   (existente)
├── POST /imagens/upload/{peca_id}  ← NOVO
├── GET  /imagens/{peca_id}         ← NOVO
└── /static/images/*               ← NOVO (StaticFiles mount)
```

---

## 3. Estrutura de Pastas — Delta (o que criar)

```
/meu-primeiro-repo/
├── frontend/                     ← NOVO: raiz do projeto Next.js
│   ├── package.json
│   ├── next.config.ts
│   ├── tailwind.config.ts
│   ├── components.json           ← config shadcn/ui
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx              ← Dashboard
│   │   ├── globals.css           ← tokens PHYLLOS
│   │   ├── colecoes/
│   │   │   ├── page.tsx
│   │   │   ├── nova/page.tsx
│   │   │   └── [id]/
│   │   │       ├── page.tsx
│   │   │       └── pecas/
│   │   │           ├── nova/page.tsx
│   │   │           └── [codigo]/page.tsx
│   │   ├── galeria/page.tsx
│   │   └── api/imagens/route.ts
│   ├── components/
│   │   ├── ui/                   ← shadcn/ui gerados
│   │   ├── layout/sidebar.tsx
│   │   ├── layout/header.tsx
│   │   ├── colecao-card.tsx
│   │   ├── colecao-form.tsx
│   │   ├── peca-card.tsx
│   │   ├── peca-form.tsx
│   │   ├── ficha-tecnica-form.tsx
│   │   ├── ficha-tecnica-pdf.tsx ← @react-pdf/renderer
│   │   ├── pdf-download-button.tsx ← dynamic import (ssr: false)
│   │   └── image-gallery.tsx
│   └── lib/
│       ├── api-client.ts
│       ├── types.ts
│       └── utils.ts
│
├── app/api/routes_images.py      ← NOVO (único arquivo novo no backend)
└── data/images/{peca_id}/        ← estrutura de diretórios criada no upload
```

**Backend: apenas 3 mudanças em `app/main.py`:**
```python
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.routes_images import router as images_router

app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])
app.include_router(images_router)
app.mount("/static/images", StaticFiles(directory="data/images"), name="images")
```

---

## 4. Plano de Sprints

| Sprint | Entrega | Estimativa | Dependências |
|---|---|---|---|
| 0 | Ambiente: Node.js, pnpm, Next.js init, shadcn, CORS | 3–4h | nenhuma |
| 1 | Tipos TS, api-client, shell de navegação (sidebar + layout) | 6–8h | Sprint 0 |
| 2 | CRUD de coleções (lista, detalhe, criar) | 6–8h | Sprint 1 |
| 3 | CRUD de peças + ficha técnica editável | 6–8h | Sprint 2 |
| 4 | Upload de imagens + galeria (pode paralelo com 2–3) | 6–8h | Sprint 1 |
| 5 | Exportação PDF (`@react-pdf/renderer`) | 4–6h | Sprint 3 |
| 6 | Dashboard + polish + loading skeletons + error states | 4–6h | Sprints 2–5 |
| **Total** | | **37–50h** | |

**Tempo estimado:** 5–7 dias sequencial, 3–4 dias com Sprints 2–3 e Sprint 4 em paralelo.

---

## 5. Decisões Técnicas Pendentes (resolver antes de codar)

| ID | Decisão | Recomendação CTO | Impacto |
|---|---|---|---|
| D1 | Autenticação na Fase 2? | Não — uso interno/localhost | Estrutural no layout.tsx |
| D2 | Campo `medidas`: texto livre ou JSON? | JSON desde já | Sprint 3 — modelo de dados |
| D3 | Convenção de path de imagens | `data/images/{peca_id}/` | Sprint 4 |
| D4 | SQLite vs. PostgreSQL agora? | Manter SQLite (migrar antes da Fase 4) | Sprint 0 |
| D5 | `colecao_id` obrigatório na UI? | Sim (validação frontend, schema backend aceita null) | Sprint 3 |

---

## 6. O que NÃO Refatorar Agora

- `app/main.py` — apenas 3 linhas novas (CORS, StaticFiles, router images)
- `app/api/routes.py` — não tocar
- `app/models/models.py` — não tocar (exceto D2)
- `app/schemas/schemas.py` — não tocar
- `app/core/database.py` — não tocar
- `requirements.txt` — não tocar
- Sem Docker agora — dois processos locais são suficientes
- Sem TypeScript strict mode agora — velocidade primeiro
- Sem testes automatizados agora — entram antes da Fase 4

---

## 7. Preparação para Fases Seguintes (sem construir agora)

**Fase 3 (ComfyUI + Ollama):** campos `prompt_croqui` e `prompt_foto` já existem no modelo `Peca` e estarão no formulário. Novos endpoints `POST /pecas/{codigo}/gerar-croqui` serão adicionados ao FastAPI. Next.js suporta SSE/WebSocket nativamente.

**Fase 4 (MRP):** migrar SQLite → PostgreSQL ANTES deste sprint. Novos modelos `OrdemProducao`, `ItemOrdem`, `Estoque` em `app/models/models.py`.

**Fase 5 (E-commerce):** Next.js com SSG/ISR — sem mudança de stack. `/loja` será novo diretório em `frontend/app/`.
