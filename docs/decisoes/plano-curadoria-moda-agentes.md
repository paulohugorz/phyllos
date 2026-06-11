# Plano de Curadoria de Moda por Agentes

Objetivo: montar uma equipe grande de agentes de design de moda para curar milhares de termos, tipos de peca, construcao, acabamentos e materiais. O resultado alimenta o banco de referencias do Fashion OS e melhora a qualidade das imagens geradas.

## Equipe recomendada

| Agente | Foco de curadoria | Saida principal |
|---|---|---|
| `fashion-taxonomy-director` | Governanca do vocabulario | padrao de schema, revisao e priorizacao |
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

## Uso no Motor de Imagens

O prompt final nunca deve dizer apenas "calca bonita realista". Ele deve compor termos como:

`tailored trousers + high waist + hidden elastic back waistband + straight leg + matte stretch crepe + slash pockets + blind hem + clean front + natural seated and standing drape`.

O prompt negativo deve remover erros recorrentes:

`leggings look, denim five-pocket styling, visible sporty waistband, plastic shine, unrealistic fabric folds, extra seams, distorted hands, logo, text, watermark`.
