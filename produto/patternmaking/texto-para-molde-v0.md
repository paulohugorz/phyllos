# Texto para Molde v0

Data: 2026-06-26
Status: iniciado como camada experimental de Pattern Engine.

## Tese

E possivel treinar os agentes a receber uma descricao textual e devolver uma primeira especificacao de molde, desde que o sistema nao pule direto para desenho. O fluxo inicial deve ser:

```text
descricao -> interpretacao tecnica -> base de modelagem -> componentes -> operacoes geometricas -> validacoes -> desenho parametrico
```

## O que existe agora

- Banco de bases e partes Mukai em `data/seed_modelagens.py`.
- Modelos SQL para `moldes_base`, `moldes_partes`, `moldes_derivacoes` e `molde_variacoes`.
- Matcher semantico em `app/services/modelagem_matcher.py`.
- Endpoint inicial `GET /modelagem/referencias/recomendar`.
- Referencia oficial para agentes em `.claude/agents/references/text-to-molde-contract-v0.md`.

## Entrega v0

A v0 nao gera molde final. Ela gera uma especificacao auditavel:

- categoria detectada;
- tecido/construcao inferidos;
- componentes detectados;
- operacoes geometricas sugeridas;
- medidas obrigatorias;
- validacoes obrigatorias;
- recomendacoes de bases/variacoes existentes.

## Exemplo

Entrada:

```text
camisa camp collar de linho com manga curta
```

Saida esperada:

```text
Categoria: camisa
Tecido: plano
Componentes: gola_camp, manga_curta
Operacoes: selecionar base de camisa, abrir decote para gola camp, desenhar manga a partir da cava
Medidas: busto, cintura, quadril, ombro, costas, cava, corpo, manga, braco, boca de manga, decote, pescoco
Validacoes: gola/decote, manga/cava, linha de fio, margem, piques
```

## Criterios de aceitacao

1. A saida precisa separar texto, perfil semantico, medidas, operacoes e validacoes.
2. O agente deve declarar quando a peca exige base composta.
3. O agente deve preferir referencias existentes em vez de inventar uma base inexistente.
4. O resultado deve ser marcado como prototipo tecnico ate passar por modelista, piloto e prova fisica.
5. Cada novo exemplo deve virar caso de teste ou registro de treino.

## Proximos incrementos

1. Criar biblioteca de componentes geometricos: manga, gola, pe de gola, punho, cos, bolso e vista.
2. Ligar cada componente a pontos de controle em coordenadas 2D.
3. Criar `PatternValidator` para encaixes: manga/cava, gola/decote, cintura/cos, bolso/frente.
4. Gerar preview 2D parametrico a partir da especificacao.
5. Exportar folha tecnica imprimivel somente depois das validacoes.

## Limite

Isto nao muda o foco atual da PHYLLOS V1 como DPP middleware. O uso imediato e treinar agentes para entender arquivos tecnicos, explicar escolhas de modelagem e preparar uma futura integracao com ferramentas de molde.
