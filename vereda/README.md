# Landing page Vereda V2

Versão local estática da landing page institucional da Vereda.

## Prévia

Na raiz do repositório:

```bash
python3 -m http.server 4173 --directory vereda
```

Abra `http://localhost:4173/`.

## Formulário

O formulário preserva o contrato observado na landing pública: nome `diagnostico-vereda`, POST para `/obrigado/`, honeypot `bot-field` e campos `name`, `company`, `email`, `segment` e `sku_volume`. Em prévia local, o JavaScript informa explicitamente que os dados não foram enviados. O processamento precisa ser validado no ambiente Netlify antes da publicação.

## Landing pages A/B por segmento

A matriz em `/lp/` contém duas hipóteses para cada segmento comercial do formulário:

- `/lp/textil-confeccao/a/` e `/b/`;
- `/lp/calcados-couro/a/` e `/b/`;
- `/lp/agro/a/` e `/b/`;
- `/lp/manufatura/a/` e `/b/`;
- `/lp/cooperativas/a/` e `/b/`.

A rota sem variante, por exemplo `/lp/agro/`, distribui A/B em 50/50 e persiste a escolha no navegador. `?variant=a` ou `?variant=b` força uma versão para QA. O formulário `diagnostico-vereda-lp` registra segmento, variante, landing page e UTMs. Os eventos `vereda_landing_view`, `vereda_cta_click`, `vereda_form_start` e `vereda_lead_submitted` entram em `window.dataLayer` para integração futura, sem transmissão externa nesta versão.

Para regenerar e validar:

```bash
cd vereda
node scripts/build-lps.mjs
node scripts/build-dist.mjs
VEREDA_PREVIEW_URL=http://127.0.0.1:4174 node scripts/qa-lps.mjs
```

## Ativos

- `assets/brand/vereda-wordmark-v2-referencia-raster.png`: recorte raster de referência do wordmark V2, sem transparência.
- `assets/images/hero-territorio.webp`: imagem ilustrativa gerada por IA para o hero.
- `assets/images/processo-industrial.webp`: imagem ilustrativa gerada por IA para contextos operacionais.
- `assets/images/fibras-materiais.webp`: imagem ilustrativa gerada por IA para materialidade.

As três fotografias são ilustrativas e não comprovam cliente, instalação, localização, composição ou certificação.
