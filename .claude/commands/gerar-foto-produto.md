# /gerar-foto-produto

Gere briefing e prompt de imagem de produto usando o Motor de Imagens do Fashion OS.

Referencias obrigatorias:
- `.claude/agents/references/fashion-os-platform-specialization.md`
- `.claude/agents/references/positioning-rationale-2026-06.md`

Fluxo:
fotos-videos → design-tecnico → ficha-tecnica

Entrada:
```text
$ARGUMENTS
```

Antes de gerar o prompt, identificar ou declarar premissas para:
- categoria da peca;
- tecido;
- elasticidade;
- folga de vestibilidade;
- peso, altura e proporcoes corporais quando informados;
- tipo de imagem: editorial, e-commerce, lifestyle, viagem, trabalho, alongamento, caminhada ou academia leve.

Entregue:
- diagnostico visual;
- prompt principal;
- prompt negativo;
- parametros de corpo, tecido, caimento e contexto;
- riscos de imagem irrealista;
- proximos dados necessarios para ficha tecnica e modelagem.
