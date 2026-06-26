# Roadmap PHYLLOS Create / Fashion OS

**Atualizado em:** 2026-06-11
**Status em 2026-06-23:** roadmap historico substituido no curto prazo por `roadmap/roadmap-dpp-integrado-phyllos.md`.
**Premissa historica:** V1 e Parametric Pattern Engine, nao CAD industrial.

> Nota: este roadmap permanece como registro da tese anterior de Motor de Moldes. A prioridade vigente de desenvolvimento interno passa a ser PHYLLOS DPP Integrado: importacao/input de arquivos tecnicos, calculo de area/perda/indicadores, estados de evidencia, QR e flashcards para consumidor.

O Fashion OS continua como infraestrutura tecnica da PHYLLOS. O produto a validar agora e mais estreito: transformar parametros estruturados, medidas e tecido em molde 2D parametrizado, validavel, imprimivel e evolutivo.

## Arquitetura de produto

```text
PHYLLOS Create
├── Playbook  -> conhecimento de modelagem
├── Engine    -> motor parametrico e validadores
├── Library   -> bases, componentes e versoes
└── SaaS      -> interface para usuario
```

Ordem de construcao:

```text
Playbook -> Engine -> Library -> SaaS
```

## Fase 0 - Base existente

- [x] FastAPI + SQLite
- [x] Agentes Claude e Codex estruturados
- [x] Referencias de modelagem e construcao
- [x] Prototipo tecnico de calca performance em coordenadas
- [x] Catalogo de moldes/base publicado
- [x] Voz do Motor de Moldes definida
- [x] Risk & Scope Review do MVP documentado

## Mes 1 - Saia reta parametrica

- [ ] `playbook.db` ou estrutura inicial de regras
- [ ] `dependency_graph` para propagacao de medidas
- [ ] endpoint `/molde`
- [ ] JSON minimo de entrada: medidas corporais, folgas, tecido, elasticidade, base e comprimento
- [ ] separacao entre medida corporal, folga e medida final do molde
- [ ] calculo parametrico para saia reta
- [ ] SVG estatico gerado sob demanda
- [ ] testes unitarios e golden pattern da saia reta

## Mes 2 - Blusa basica + PDF A4

- [ ] segunda base parametrica: blusa basica
- [ ] gerador de PDF A4
- [ ] tesselation inicial
- [ ] marcas de montagem, margens, overlap e paginacao
- [ ] suite automatica de testes de impressao/paginacao
- [ ] visual diff basico entre golden patterns

## Mes 3 - Calca reta + validadores

- [ ] terceira base parametrica: calca reta
- [ ] `PatternValidator`
- [ ] validacao de curvas, comprimentos, limites e auto-intersecoes
- [ ] `compatibility_matrix` para componentes
- [ ] teste com 5 costureiras/modelistas
- [ ] feedback estruturado de prova fisica

## Mes 4 - Biblioteca modular

- [ ] componentes reutilizaveis: frente, costas, cos, bolso, gola, manga, punho, recorte
- [ ] metadados por base e componente
- [ ] compatibilidades e incompatibilidades
- [ ] estimativa simples de consumo de tecido
- [ ] arquitetura preparada para P/M/G/GG, mesmo sem expor grading completo

## Mes 5 - Historico, projetos e usuarios

- [ ] versionamento de bases e moldes gerados
- [ ] historico de parametros
- [ ] projetos salvos por usuario
- [ ] auditoria de qual versao foi usada em cada prova/producao
- [ ] primeiros fluxos de conta/projeto no SaaS

## Mes 6 - Linguagem natural

- [ ] camada textual que converte pedidos em parametros estruturados
- [ ] perguntas de desambiguacao quando houver mais de uma interpretacao tecnica
- [ ] AI Composer para combinar base + componentes
- [ ] validacao obrigatoria pelo PatternValidator antes de gerar saida

## Fora da V1

- [ ] preview em tempo real
- [ ] ComfyUI para imagem
- [ ] personas/modelos digitais
- [ ] MRP, ordem de producao e estoque
- [ ] CAD industrial
- [ ] e-commerce
- [ ] marketplace
- [ ] SaaS amplo antes da prova de uso

## Criterio de saida do MVP

O MVP so esta validado quando:

- uma base simples gera molde correto por parametros;
- o SVG e o PDF A4 sao imprimiveis e montaveis;
- o PatternValidator bloqueia pelo menos os erros geometricos mais obvios;
- pelo menos 3 usuarios reais cortaram, costuraram ou validaram fisicamente uma peca gerada pelo motor;
- os problemas encontrados viraram ajustes numericos documentados no Playbook/Engine.
