A PHYLLOS V1 é um estúdio web que recebe dados técnicos de uma peça de moda, calcula indicadores por unidade e publica um passaporte digital com QR e flashcards para o consumidor — sem editar molde, sem fazer ACV oficial e sem prometer conformidade regulatória.

# Phyllos — Base de Conhecimento e Estratégia

Repositório de documentos estratégicos, estudos e referências operacionais da **Phyllos**. Independente de ambiente técnico — serve como memória de longo prazo para o founder e o futuro time.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `estrategia/` | Plano mestre, documentos por área (CEO, CFO, CMO, CPO, CTO), análise de risco |
| `produto/brand/` | Voz de marca, identidade visual, frentes de comunicação |
| `produto/patternmaking/` | Catálogos de peças, moldes base, especificações técnicas |
| `pesquisa/` | Análise de mercado, personas, estudos de ICP |
| `processos/` | Fluxos operacionais e mapeamentos |
| `roadmap/` | Roadmap do Fashion OS e fases de produto |
| `templates/` | Ficha técnica, ordem de produção, checklist de qualidade |
| `prompts/` | Prompts de croquis técnicos e fotografia editorial |
| `dados/` | Base de coleções (CSV), catálogo de imagens (JSON) |
| `assets/` | Deck de investidor, imagens de referência geradas e curadas |
| `vera/` | Sistema operacional da VERA — agentes, empresas, roadmap |
| `_legado/` | Código de aplicação preservado (FastAPI, HTML, scripts) |

## Comandos Claude disponíveis

```text
/gerar-molde   — gera molde paramétrico a partir de medidas e tecido
/nova-colecao  — estrutura uma nova coleção cápsula
/criar-peca    — especifica uma peça com ficha técnica
/gerar-foto-produto — cria prompt de imagem para a peça
```
