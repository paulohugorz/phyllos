# ADR-001 - Motor de imagem realista do Fashion OS

Data: 2026-06-10
Status: proposta aprovada para Fase 3
Dono: CTO + CPO + Visual Briefer

## Contexto

O gerador atual do Fashion OS cria um croqui SVG local. Ele e util para demonstrar fluxo, SKU temporario e metadados basicos sem custo de API, mas nao responde a necessidade de imagem realista da PHYLLOS.

Para imagem realista de moda, o sistema precisa representar:

- proporcao corporal;
- caimento por tecido;
- folga de vestibilidade;
- cintura, gancho, entreperna, barra e pences;
- gola, manga, punho, pala, bolsos, fechamento e acabamento;
- textura, gramatura, elasticidade, brilho e memoria do material;
- contexto de uso sem estetica artificial de banco de imagem.

## Decisao

O SVG local permanece apenas como rascunho tecnico e fallback offline.

O Motor de Imagens realista deve usar uma arquitetura em tres camadas:

1. Banco de termos de moda: taxonomia curada com nomes tecnicos, sinonimos, atributos visuais, restricoes e compatibilidades.
2. Prompt compiler: transforma ficha tecnica + taxonomia em prompt fotorealista, prompt negativo e parametros de consistencia.
3. Gerador visual: ComfyUI ou servico equivalente com workflow de image generation, preferencialmente com ControlNet/IP-Adapter/LoRA quando houver referencias proprias.

## Avaliacao da tecnologia atual

| Tecnologia | Responde a necessidade? | Papel correto |
|---|---|---|
| SVG local no navegador | Nao para realismo | Rascunho, wireframe visual, demo publica sem custo |
| Prompt textual simples | Parcial | Entrada inicial, insuficiente sem vocabulario tecnico |
| ComfyUI local | Sim, com GPU/workflow | Motor de imagem realista e controlavel |
| Stable Diffusion/SDXL/FLUX via ComfyUI | Sim, se guiado por referencias | Gerar foto/croqui realista com controle de pose, tecido e estilo |
| Blender/CLO/Valentina | Sim para apoio tecnico, nao para foto final sozinho | Volume, molde, simulacao e referencia estrutural |
| Banco de imagens externo | Parcial | Referencia e benchmark, nao imagem final proprietaria |

## Requisitos para realismo

- A ficha da peca deve sair com campos estruturados, nao apenas texto livre.
- Cada termo de moda precisa ter definicao, categoria, atributos visuais e exemplos de uso em prompt.
- O sistema deve separar termos tecnicos de termos esteticos.
- O prompt deve incluir camera, luz, pose, contexto, tecido, construcao e negativos.
- A imagem deve ser validada por agentes de design, modelagem, materiais e visual.

## Pipeline recomendado

1. Usuario descreve a peca em linguagem natural.
2. Product Designer extrai categoria, silhueta, fit, tecido, construcao e acabamentos.
3. Curadores especialistas buscam termos na taxonomia.
4. Prompt Compiler monta:
   - prompt editorial realista;
   - prompt tecnico de produto;
   - prompt negativo;
   - checklist de fidelidade.
5. Motor ComfyUI gera variantes.
6. Visual Briefer e Fit Technical Designer validam realismo.
7. Imagem aprovada vira referencia da peca no Fashion OS.

## Implicacao

Antes de investir em GPU ou API, a prioridade e montar o banco de conhecimento de moda. Sem isso, qualquer gerador produz uma imagem bonita, mas tecnicamente vaga.
