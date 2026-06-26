# Plano de Curadoria de Moda por Agentes

Objetivo: montar uma equipe grande de agentes de design de moda para curar milhares de termos, tipos de peca, construcao, acabamentos e materiais. O resultado alimenta o banco de referencias do Fashion OS e melhora a qualidade das imagens geradas.

## Equipe recomendada

| Agente | Foco de curadoria | Saida principal |
|---|---|---|
| `fashion-taxonomy-director` | Governanca do vocabulario | padrao de schema, revisao e priorizacao |
| `curador-vocabulario-popular-moda` | Fala de clientes, costureiras e atelies | termos populares normalizados e exemplos reais |
| `tradutor-linguagem-modelagem` | Frases naturais para modelagem | conceitos tecnicos, bases, folgas, tecidos e regras |
| `curador-intencoes-usuario` | Objetivos da usuaria | `user_intent` e prioridades por contexto |
| `validador-semantico-vocabulario` | Qualidade semantica | parecer de duplicidade, confianca e classificacao |
| `arquiteto-vocabulario-sqlite` | Estrutura relacional | tabelas, chaves, indices, seeds e regras de importacao |
| `curador-referencias-culturais-moda` | Historia, cultura e estilo | `style_reference` com aplicacao contemporanea |
| `curador-calcas` | Tipos de calca, fit, cintura, gancho, bolso, barra | termos e compatibilidades de calcas |
| `curador-camisas` | Camisas, blusas, tops e partes superiores | termos de forma, vista, pala e construcao |
| `curador-golas-decotes` | Golas, decotes, colarinhos e aberturas | biblioteca de neckline/collar |
| `curador-mangas-punhos` | Mangas, punhos, cavas e ombros | biblioteca de sleeve/cuff/armhole |
| `curador-acabamentos-costuras` | Costuras, barras, vieses, pespontos, reforcos | biblioteca de acabamento e erro comum |
| `curador-tecidos-texturas` | Tecidos, composicoes, superficies, caimento | termos visuais e tecnicos de material |
| `curador-modelagem-fit` | Folgas, proporcoes, gradação, conforto | ligacao com Fit Engine e Pattern Engine |
| `curador-bolsos-fechamentos` | Bolsos, ziperes, botoes, vistas, cordoes | detalhes funcionais e visuais |
| `curador-silhuetas-estilos` | Silhuetas e linguagem de produto | ponte entre estetica e categoria |
| `prompt-compiler-fashion` | Conversao de ficha + termos em prompt | prompt positivo, negativo e checklist |
| `image-realism-qa` | Validacao de imagem gerada | laudo de realismo, fidelidade e retrabalho |

## Ordem de trabalho

1. Comecar por calcas, camisas e blazers, pois sustentam a primeira familia PHYLLOS.
2. Curar de 100 a 200 termos por categoria antes de ampliar para milhares.
3. Cada termo precisa ter definicao, atributos visuais, atributos tecnicos e prompt negativo.
4. Nenhum termo entra como validado sem revisao cruzada de pelo menos dois agentes.
5. Imagens geradas devem registrar quais termos foram usados, para aprender quais descricoes funcionam.
6. Toda frase popular deve preservar a fala original, o termo normalizado, a intencao provavel e o risco de interpretacao.
7. Todo mapeamento linguagem natural -> conceito tecnico deve declarar confianca antes de entrar em SQLite.

## Critérios de qualidade

- Termo tecnico usado por moda, modelagem, ficha tecnica ou producao.
- Definicao curta e operacional.
- Atributos visuais suficientes para um modelo de imagem.
- Atributos tecnicos suficientes para ficha/modelagem.
- Compatibilidades e incompatibilidades explicitas.
- Linguagem alinhada a PHYLLOS: performance consciente, elegancia confortavel, mobilidade e longevidade.

## Primeira meta

Criar 1.000 termos curados em quatro blocos:

- 250 termos de calcas, saias, vestidos e blazers;
- 250 termos de camisas, tops, golas, mangas e punhos;
- 250 termos de tecidos, texturas, composicoes e caimentos;
- 250 termos de acabamentos, costuras, bolsos, fechamentos e detalhes funcionais.

Meta semantica paralela:

- 150 frases reais de clientes e costureiras normalizadas;
- 50 intencoes canonicas com exemplos;
- 200 mapeamentos termo -> conceito tecnico com confianca;
- 100 exemplos entrada -> saida para treino futuro do motor de IA;
- 30 referencias historicas ou culturais ligadas a silhuetas, componentes e aplicacao PHYLLOS.

## Uso no Motor de Imagens

O prompt final nunca deve dizer apenas "calca bonita realista". Ele deve compor termos como:

`tailored trousers + high waist + hidden elastic back waistband + straight leg + matte stretch crepe + slash pockets + blind hem + clean front + natural seated and standing drape`.

O prompt negativo deve remover erros recorrentes:

`leggings look, denim five-pocket styling, visible sporty waistband, plastic shine, unrealistic fabric folds, extra seams, distorted hands, logo, text, watermark`.
