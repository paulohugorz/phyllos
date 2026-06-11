# Fashion OS v2 — Especificação de Produto: Interface Web
**PRD-001 | v1.0 | 2026-06-10 | Product Director PHYLLOS**

## Leitura Executiva

O Fashion OS v1 opera via terminal e resolve o problema de armazenamento estruturado. O gargalo atual é que a fundadora precisa lembrar comandos, ler Markdown bruto e não tem visualização do estado do pipeline. A Fase 2 resolve isso com interface visual mínima — não um ERP, mas uma tela de trabalho que espelha como a fundadora já pensa: por coleção, por peça, por etapa.

---

## 1. User Stories — MVP (P0/P1)

### US-01 — Criar e visualizar coleção (P0)
**Como** fundadora, **quero** criar uma coleção com nome, temporada e descrição, **para** organizar peças dentro de um contexto visual claro.

**Critérios de aceite:**
- Formulário: Nome*, Temporada*, Descrição* (todos obrigatórios)
- Coleção aparece imediatamente na lista sem reload
- Cada coleção mostra contador de peças ("3 peças")
- Status editável: Planejamento / Em Desenvolvimento / Em Produção / Lançada
- Nome da coleção deve ser único por temporada (sistema bloqueia duplicata)

### US-02 — Cadastrar peça (P0)
**Como** fundadora, **quero** cadastrar uma peça nova dentro de uma coleção, **para** ter o registro estruturado sem digitar comandos no terminal.

**Critérios de aceite:**
- Formulário acessível a partir do detalhe da coleção
- SKU gerado automaticamente se não preenchido (formato: PH + ano + sequencial)
- Sistema impede duas peças com o mesmo SKU
- Status inicial obrigatório: Conceito

### US-03 — Visualizar e editar ficha técnica (P0)
**Como** fundadora, **quero** preencher a ficha técnica de uma peça dentro da interface, **para** ter todos os dados de produção organizados sem abrir Markdown.

**Critérios de aceite:**
- Ficha acessível como aba no detalhe da peça
- Campos organizados em seções: Identificação, Materiais, Construção, Acabamentos, Tamanhos
- Sistema salva rascunho automaticamente a cada 30 segundos
- Indicador de completude: "Ficha 7/12 campos preenchidos"
- Ficha só pode ser marcada "Finalizada" quando todos os campos obrigatórios estão preenchidos

### US-04 — Exportar ficha técnica em PDF (P1)
**Como** fundadora, **quero** exportar a ficha técnica como PDF, **para** enviar para fornecedores sem formatar nada manualmente.

**Critérios de aceite:**
- PDF gerado em menos de 5 segundos
- PDF contém: logo PHYLLOS, nome da coleção, SKU, todos os campos preenchidos, data de exportação
- Nome do arquivo: `PHYLLOS_[SKU]_ficha_[YYYYMMDD].pdf`
- PDF gerado client-side (não depende de impressão do browser)

### US-05 — Galeria de imagens por peça (P1)
**Como** fundadora, **quero** fazer upload de imagens de referência e sketches em cada peça, **para** ter a referência visual junto com os dados técnicos.

**Critérios de aceite:**
- Upload aceita JPG, PNG e PDF (máx 10MB por arquivo)
- Limite: 20 arquivos por peça
- Imagem tem tipo: Referência / Sketch / Frente / Costas / Detalhe / Foto Final
- Imagem marcada como "Principal" aparece no card da peça na lista

---

## 2. Wireframes Textuais

### Tela 1 — Lista de Coleções (Home)
```
+----------------------------------------------------------+
| PHYLLOS Fashion OS                      [+ Nova Coleção] |
+----------------------------------------------------------+
| Coleções (3)                                             |
|                                                          |
| SS26 Essencial Run          [Em Desenvolvimento]    [>]  |
| 12 peças · Atualizada em 08 jun 2026                     |
|                                                          |
| SS26 Trail Essencial              [Planejamento]    [>]  |
| 0 peças · Criada em 03 jun 2026                          |
+----------------------------------------------------------+
```

### Tela 2 — Detalhe de Coleção
```
+----------------------------------------------------------+
| < Coleções   SS26 Essencial Run     [Em Desenvolvimento] |
+----------------------------------------------------------+
| [+ Nova Peça]                    Filtrar: [Todos v]      |
|                                                          |
| PH001 · Calça Performance                  [Piloto] [>] |
| PH002 · Calça Dia a Dia                  [Conceito] [>]  |
+----------------------------------------------------------+
```

### Tela 3 — Detalhe de Peça
```
+----------------------------------------------------------+
| < SS26 Essencial Run    PH001 · Calça Performance        |
| Status: [Piloto v]                   [Exportar PDF]      |
+----------------------------------------------------------+
| [Dados Gerais] [Ficha Técnica] [Galeria]                 |
+----------------------------------------------------------+
| SKU        PH001           Nome  Calça Performance       |
| Coleção    SS26 Essencial  Custo R$ 95,00                |
| Preço      R$ 380,00       Status Piloto                 |
| [Editar Dados]                                           |
+----------------------------------------------------------+
```

### Tela 4 — Ficha Técnica
```
+----------------------------------------------------------+
| Ficha Técnica       [Completude: 8/12]   [Exportar PDF]  |
+----------------------------------------------------------+
| MATERIAIS                                                |
| Composição   78% poliéster reciclado / 22% el...         |
| Gramatura    240 g/m2                                    |
| Fornecedor   Malharia Têxtil Sul                         |
|                                                          |
| CONSTRUÇÃO                                               |
| Tipo costura  Flatlock                                   |
| Acabam. lat.  —               [campo obrigatório]        |
|                                                          |
| [Salvar Rascunho]      [Marcar como Finalizada]          |
| Último salvo: 14:32                                      |
+----------------------------------------------------------+
```

---

## 3. Fluxo Principal: Nova Coleção → PDF Exportado

```
[Home] → [+ Nova Coleção] → [Modal: Nome, Temporada, Descrição]
  → [Detalhe da Coleção — estado vazio]
  → [+ Nova Peça] → [Modal: Nome, Categoria, Preço-alvo, Custo-alvo]
  → [Detalhe da Peça — aba Dados Gerais]
  → [aba Ficha Técnica] → [preenche campos] → [salva rascunho automático]
  → [Marcar como Finalizada] → [confirmação]
  → [Exportar PDF] → [download: PHYLLOS_PH001_ficha_20260610.pdf]
```

---

## 4. Campos e Validações

### Coleção
| Campo | Tipo | Obrigatório | Validação |
|---|---|---|---|
| Nome | Texto (60) | Sim | Único por temporada |
| Temporada | Dropdown | Sim | SS/FW + ano (ex: SS26) |
| Descrição | Texto (300) | Sim | Mín 10 chars |
| Status | Dropdown | Sim | Planejamento (inicial) |

### Peça
| Campo | Tipo | Obrigatório | Validação |
|---|---|---|---|
| SKU | Texto (10) | Sim | Único global, PH + 3 dígitos |
| Nome | Texto (80) | Sim | Mín 3 chars |
| Coleção | Referência | Sim | Deve existir |
| Categoria | Dropdown | Sim | Superior / Inferior / Completo / Acessório |
| Preço-alvo | Número | Não | > 0 |
| Custo-alvo | Número | Não | > 0 e < preço |

**Estados de peça:** Conceito → Design → Ficha Técnica → Piloto → Aprovação → Produção → Lançada
**Regra:** transição para "Produção" requer ficha técnica com status Finalizada.

### Ficha Técnica — Campos Obrigatórios por Seção

**Materiais:** composição tecido principal, gramatura
**Construção:** tipo de costura, acabamento lateral, cós descrição
**Acabamentos:** etiqueta interna, instruções de lavagem
**Tamanhos:** tabela de tamanhos (upload), grade de tamanhos (ao menos 1)

---

## 5. Edge Cases e Estados Vazios

| Situação | O que o sistema exibe |
|---|---|
| Zero coleções | "Nenhuma coleção ainda. Crie a primeira coleção para começar." + botão CTA |
| Coleção sem peças | "Nenhuma peça nesta coleção. Adicione a primeira peça para começar [Nome]." |
| Ficha incompleta tentando ser Finalizada | Destaca seções com pendências; não avança |
| Exportação PDF com ficha incompleta | Permite; rodapé: "Documento em revisão — não finalizado" |
| Peça tentando ir para Produção sem ficha finalizada | Sistema bloqueia; mensagem explica o que falta |
| Upload > 10MB | "Este arquivo tem X MB. O limite é 10 MB por imagem." |
| Limite de 20 arquivos | "Limite atingido. Exclua um arquivo para adicionar novos." |

---

## 6. O que Deixar para a Fase 3+

| Feature | Por que não é MVP | Quando entra |
|---|---|---|
| Pipeline Kanban 22 etapas | Complexidade desproporcional para poucos SKUs agora | Fase 3 |
| Dashboard de métricas | Sem dados suficientes de produção | Fase 3 |
| Histórico de versões de ficha | Requer colaboração, hoje é uso solo | Fase 3 |
| Acesso multi-usuário | +40% de escopo sem valor imediato | Fase 3 |
| Calculadora de custo/margem integrada | Finance Agent opera separado, não duplicar | Fase 3 |
| IA integrada na interface | Claude Code já faz isso via terminal | Fase 4 |
| App mobile / responsividade completa | Founder opera em desktop | Fase 3 |
| Exportação Excel/CSV | PDF cobre caso de uso do fornecedor | Fase 3 |

---

## KPIs da Fase 2

| KPI | Baseline | Meta |
|---|---|---|
| Tempo para criar peça + ficha | 15–20 min via terminal | < 8 min via interface |
| Fichas técnicas completas (100% obrigatórios) | 0 (sem controle) | 100% das peças em Produção |
| PDFs exportados por ciclo | 0 (manual) | 1 por peça, sem intervenção técnica |
| Taxa de SKU duplicado | Não medida | 0 após validação |

---

## Handoffs

- **CTO:** arquitetura técnica, stack de PDF server-side, campos `medidas` como JSON
- **Design Lead:** UI baseada nos wireframes, paleta PHYLLOS (Obsidian #0F0F0D, Linen #E8E4DC, Gold #B89A6A, tipografia Cormorant Garamond + Jost)
- **Supply Chain Agent:** validar campos da ficha contra o que fornecedores precisam para cotar
- **Finance Agent:** confirmar se preço-alvo e custo-alvo cobrem as necessidades do CMV
