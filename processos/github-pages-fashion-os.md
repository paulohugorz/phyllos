# Fashion OS — organização para GitHub Pages

Este patch reorganiza a biblioteca de imagens para funcionar em GitHub Pages.

## Por que mudou

GitHub Pages serve arquivos estáticos. Ele não executa SQLite, Netlify Functions, Express ou Python no servidor. Por isso, a biblioteca SQLite fica guardada para evolução futura, mas a página usa um export JSON estático.

## Estrutura sugerida

```text
meu-primeiro-repo/
├── index.html
├── assets/
│   └── fashion-os/
│       ├── fashion_image_catalog.json
│       └── fashion_image_library.sqlite
├── js/
│   ├── fashion-os-catalog.js
│   └── fashion-os-page-hook.js
├── docs/
│   └── GITHUB_PAGES_FASHION_OS_STRUCTURE.md
└── examples/
    └── github-pages-demo.html
```

## Como integrar no index.html

Antes do fechamento de `</body>`, adicione:

```html
<script src="./js/fashion-os-catalog.js"></script>
<script src="./js/fashion-os-page-hook.js"></script>
```

Na área do formulário, garanta que existam estes elementos ou adapte os seletores no arquivo `js/fashion-os-page-hook.js`:

```html
<form id="fashion-os-form">
  <textarea id="fashion-prompt" name="prompt"></textarea>
  <input type="hidden" id="fashion-enriched-prompt" name="enrichedPrompt" />
  <button type="submit">Gerar imagem</button>
</form>

<section id="fashion-os-references"></section>
```

## Fluxo da geração de imagem

```text
Prompt do usuário
↓
Busca em assets/fashion-os/fashion_image_catalog.json
↓
Ranking por categoria, material, acabamento, silhueta e alinhamento PHYLLOS
↓
Prompt enriquecido
↓
Gerador de imagem
↓
Retorno com referências + imagem gerada
```

## Exemplo

Pedido:

> calça masculina que pareça de alfaiataria mas seja flexível

O sistema busca referências de calça, alfaiataria, conforto, elastano, performance, tecido técnico e uso urbano.

## Comandos para o Codex aplicar

```bash
git checkout -b feature/github-pages-fashion-catalog
# copiar os arquivos deste patch para a raiz do repo
git add assets/fashion-os js docs examples
git commit -m "Organize Fashion OS catalog for GitHub Pages"
git push origin feature/github-pages-fashion-catalog
```

Depois, abrir PR ou mergear na `main`.

## Observação sobre imagens

O catálogo está com URLs placeholder. Substitua por imagens próprias, licenciadas ou autorizadas. A estrutura já está pronta para receber `image_url`, `source_url`, `rights_status` e metadados técnicos.
