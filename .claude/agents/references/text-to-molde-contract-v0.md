# Text-to-Molde Contract v0

Status: experimental, interno, nao MVP DPP V1.

Objetivo: treinar agentes a transformar descricao natural de peca em uma especificacao tecnica auditavel antes de qualquer desenho. O agente nao deve "imaginar um molde"; ele deve construir uma cadeia verificavel:

```text
texto -> perfil semantico -> base Mukai/catalogo -> componentes -> operacoes geometricas -> validacoes -> desenho parametrico
```

Esta referencia complementa:

- [patternmaking-geometric-algorithmic-principles.md](patternmaking-geometric-algorithmic-principles.md)
- [patternmaking-construction-techniques-marlene-mukai.md](patternmaking-construction-techniques-marlene-mukai.md)
- [fashion-os-platform-specialization.md](fashion-os-platform-specialization.md)

## Fonte operacional atual

O primeiro motor executavel e `app/services/modelagem_matcher.py`.

Endpoint de uso:

```text
GET /modelagem/referencias/recomendar?q=<descricao>
```

Saida esperada:

- `perfil`: interpretacao semantica da frase;
- `especificacao_texto_molde`: contrato v0 da traducao texto -> molde;
- `estrategia_medidas`: base unica ou base composta;
- `recomendacoes`: variacoes de moldes existentes que servem como referencia.

## Contrato de saida

```json
{
  "versao": "text_to_molde_v0",
  "status": "prototipo_tecnico_nao_molde_final",
  "input": "camisa camp collar de linho com manga curta",
  "perfil": {
    "categoria_input": "camisa",
    "tipo_tecido": "plano",
    "componentes_detectados": ["gola_camp", "manga_curta"],
    "operacoes_geometricas": [
      "selecionar_base_camisa",
      "gerar_frente_costas",
      "abrir_decote_frente_para_gola_camp",
      "desenhar_gola_sem_pe_rigido",
      "desenhar_manga_a_partir_da_cava"
    ],
    "validacoes_obrigatorias": [
      "validar_compatibilidade_manga_cava",
      "validar_compatibilidade_gola_decote"
    ]
  },
  "medidas_obrigatorias": [
    "busto",
    "cintura",
    "quadril",
    "ombro",
    "largura_costas",
    "cava",
    "comprimento_corpo",
    "comprimento_manga",
    "largura_braco",
    "boca_manga",
    "contorno_decote",
    "largura_pescoco"
  ],
  "componentes": ["gola_camp", "manga_curta"],
  "operacoes_geometricas": [
    "selecionar_base_camisa",
    "gerar_frente_costas",
    "abrir_decote_frente_para_gola_camp",
    "desenhar_gola_sem_pe_rigido",
    "desenhar_manga_a_partir_da_cava"
  ],
  "validacoes_obrigatorias": [
    "validar_compatibilidade_manga_cava",
    "validar_compatibilidade_gola_decote"
  ],
  "limites": [
    "nao_substitui_modelista_prova_fisica_ou_piloto",
    "nao_gera_molde_1_1_sem_medidas_completas",
    "toda_geometria_deve_declarar_folga_linha_de_fio_margem_e_piques"
  ]
}
```

## Regras para agentes

1. Nunca pular direto do texto para uma imagem.
2. Sempre declarar a base escolhida ou declarar que a base e composta.
3. Separar medida corporal, folga, reducao elastica e medida final.
4. Cada componente detectado precisa virar uma operacao geometrica ou uma pendencia.
5. Toda operacao geometrica precisa ter validacao correspondente.
6. Se faltar medida critica, devolver pendencia antes de prometer molde.
7. Se a peca for composta, como macacao, combinar referencias em vez de forcar uma base inexistente.
8. Para desenho tecnico, preferir fonte 2D parametrica interativa como verdade operacional.

## Vocabulos iniciais

Categorias:

- `calca`
- `saia`
- `camisa`
- `blusa`
- `vestido`
- `casaco`
- `macacao`

Componentes:

- `gola_camp`
- `gola_colarinho`
- `pe_de_gola`
- `manga_curta`
- `manga_longa`
- `manga_raglan`
- `manga_bufante`
- `punho`
- `carcela`
- `vista_abertura`
- `bolso_faca`
- `bolso_cargo`
- `cos`
- `ziper`
- `pence`
- `recorte_princesa`
- `lapela`

Operacoes devem ser verbos tecnicos, por exemplo:

- `selecionar_base_camisa`
- `desenhar_manga_a_partir_da_cava`
- `casar_cabeca_da_manga_com_cava`
- `abrir_decote_frente_para_gola_camp`
- `adicionar_recorte_de_bolso_faca_espelho_e_saco`
- `distribuir_intake_de_pence_por_regiao`

## Validacoes minimas

Obrigatorias para qualquer especificacao:

- separar medida corporal, folga e medida final;
- declarar linha de fio por parte;
- declarar margem de costura por operacao;
- marcar piques, dobras e pontos de controle.

Obrigatorias quando houver componentes:

- manga: validar compatibilidade manga/cava;
- gola: validar compatibilidade gola/decote;
- bolso: validar abertura, volume e ordem de montagem;
- fechamento: validar transpasse, ziper, botoes e ordem de montagem;
- calca/macacao: validar gancho, entreperna, joelho e barra;
- macacao: validar comprimento de torso e prova sentada.

## Protocolo de treino

Cada novo exemplo deve registrar:

1. frase original;
2. perfil semantico esperado;
3. base ou bases recomendadas;
4. componentes detectados;
5. operacoes geometricas;
6. medidas obrigatorias;
7. validacoes;
8. falhas aceitaveis da v0;
9. decisao humana final.

Exemplo:

```text
Entrada: camisa camp collar de linho com manga curta
Base: camisa feminina social + transformacao de gola
Componentes: gola_camp, manga_curta, vista_abertura
Risco: gola sem pe rigido precisa perimetro de decote compativel
Validar: gola/decote, manga/cava, linha de fio, margem e piques
```

## Limite de produto

Este contrato nao altera a tese vigente da PHYLLOS V1 como DPP middleware. Ele e uma camada de aprendizado e interpretacao tecnica para agentes, util quando o Fashion OS precisar ler arquivos de modelagem, explicar risco de corte, estimar area/perda ou preparar uma futura integracao com ferramentas de molde.
