# /gerar-molde

Transforme uma descricao de peca e medidas em parametros estruturados para o Motor de Moldes.

Referencias obrigatorias:
- `.claude/agents/references/motor-moldes-strategic-premises.md`
- `.claude/agents/references/fashion-os-platform-specialization.md`
- `.claude/agents/references/patternmaking-geometric-algorithmic-principles.md`
- `.claude/agents/references/patternmaking-construction-techniques-marlene-mukai.md`

Fluxo:
modelagem -> curador-modelagem-fit -> design-tecnico -> ficha-tecnica -> qualidade

Entrada:
```text
$ARGUMENTS
```

Entregue:
- peca base recomendada, priorizando saia reta quando o pedido estiver aberto ou for primeiro teste;
- medidas obrigatorias e medidas faltantes;
- separacao entre medida corporal, folga e medida final do molde;
- tecido, elasticidade e premissas de caimento;
- folgas ou reducoes elasticas;
- dependencias entre medidas;
- riscos de incompatibilidade entre componentes;
- mapa 3D -> 2D;
- partes do molde;
- margens, piques e linha de fio;
- riscos de modelagem;
- criterios de prova fisica;
- JSON inicial sugerido para endpoint `/molde`;
- proximos ajustes necessarios antes de SVG/PDF A4.

Nao prometa molde perfeito. Nao trate linguagem natural como fonte unica de verdade. Trate toda saida como prototipo tecnico ate passar por corte, costura e prova.
