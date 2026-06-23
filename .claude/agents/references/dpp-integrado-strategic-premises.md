# PHYLLOS DPP Integrado - Premissas Estrategicas Vigentes

**Data:** 2026-06-23
**Status:** fonte vigente para roadmap tecnologico interno
**Substitui no curto prazo:** prioridade anterior de MVP centrado em Motor de Moldes / Parametric Pattern Engine

---

## 1. Decisao central

A V1 da PHYLLOS deve ser um **software de DPP integrado ao workflow tecnico da moda**, nao uma ferramenta propria de modelagem.

O produto deve receber arquivos e especificacoes que marcas, modelistas, atelies e faccoes ja produzem e transformar esses dados em:

- DPP interno;
- calculos de consumo, area, perda e indicadores;
- estados de evidencia;
- QR de etiqueta;
- flashcards publicos para consumidor.

## 2. O que sai da V1

- Editar molde.
- Ajustar desenho.
- Criar molde parametrico.
- Resolver encaixe automaticamente.
- Validar geometria de modelagem.
- Substituir Audaces, Lectra, Gerber, CLO, Valentina, CAD, PLM ou ERP.

Esses pontos podem voltar no futuro como integracoes ou modulos, mas nao devem bloquear a primeira tecnologia interna.

## 3. O que entra na V1

- Upload ou input manual de arquivo tecnico.
- Cadastro de produto.
- Cadastro de materia-prima.
- Area tecnica por peca ou por encaixe.
- Perda de corte.
- Quantidade do lote.
- Fatores de agua, energia, carbono e durabilidade.
- Calculo por peca.
- Status de dado: ausente, declarado, calculado, documentado, verificado, publicavel.
- QR e pagina publica em flashcards.

## 4. Produto em uma frase

PHYLLOS transforma arquivos tecnicos de moda e especificacoes de produto em passaportes digitais verificaveis para pecas acabadas.

## 5. Categoria

**DPP middleware para moda.**

Uma camada de traducao entre modelagem, ficha tecnica, materia-prima e consumidor.

## 6. Principio anti-greenwashing

Nenhum indicador deve aparecer como verdade absoluta se for estimado, declarado ou incompleto.

Todo flashcard publico precisa carregar um status de evidencia:

- declarado;
- calculado;
- documentado;
- verificado;
- indisponivel.

## 7. Formula base da V1

```text
area_total_requerida = area_peca / (1 - perda_pct)
area_perdida = area_total_requerida - area_peca
peso_peca = area_total_requerida * gramatura_kg_m2
agua_peca = peso_peca * agua_litros_kg
energia_peca = peso_peca * energia_kwh_kg
carbono_peca = peso_peca * carbono_kgco2e_kg
```

## 8. Handoff esperado dos lideres

- Product Director: escopo, ICP, jornada e criterios de aceite.
- Technology Director: arquitetura, stack, seguranca, APIs e backlog tecnico.
- Digital Products Lead: UX, prototipo, pagina publica e fluxo de QR.
- Data Intelligence Lead: modelo de dados, dicionario de metricas e eventos.
- Materials Lead: fatores, materiais, evidencias e metodologia de indicadores.
- Supply Chain / Operations: lote, producao, perda, responsabilidades e fluxo operacional.
- QA: testes, validacao de calculo, regressao, acessibilidade e criterios go/no-go.
- CFO: custo interno, runway, etapas de investimento e gatilhos de contratacao externa se necessario.

