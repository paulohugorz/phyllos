# DPP Studio - Versao Canonica do Prototipo

**Data:** 2026-06-25
**Status:** fonte vigente para interface DPP Studio
**Owner:** Founder / Product / Technology
**Arquivo canonico no repo:** `phyllos/dpp-studio.html`
**Arquivo de origem adotado:** `/Users/paulonascimento/Downloads/dpp-studio.html`
**SHA-256 canonico:** `560add24d6e31860fee858805644270b31e030b0a5d0d5ab273d21d52194b8c2`
**Commit de adoção:** `6559b48` (`Consome bundle fornecido do DPP Studio`)

---

## 1. Decisao

A partir desta data, a PHYLLOS deve trabalhar apenas sobre a ultima versao do DPP Studio fornecida pelo founder em `Downloads/dpp-studio.html`.

Essa versao foi copiada para `phyllos/dpp-studio.html` e validada por hash contra:

- arquivo de origem em `Downloads`;
- arquivo local no repositorio;
- arquivo remoto no GitHub.

Os tres hashes bateram com o SHA-256 canonico acima.

## 2. O que muda para os agentes

Todos os agentes devem considerar `phyllos/dpp-studio.html` como a fonte de verdade da interface atual.

Nenhum agente deve:

- voltar ao prototipo anterior em HTML/CSS/JS separado;
- reconstruir a tela antiga de 7 etapas sem pedido explicito do founder;
- tratar `style.css` ou `main.js` como fonte da UI do DPP Studio atual;
- reintroduzir PHYLLOS como marca de roupa, colecao ou motor de moldes como tese principal;
- publicar nova versao sem verificar se ela deriva deste bundle ou se ha nova decisao substituindo este arquivo.

## 3. Natureza tecnica da versao

O arquivo atual e um HTML bundled/autonomo:

- contem manifest, template e assets embutidos;
- renderiza a aplicacao via JavaScript no navegador;
- nao depende da estrutura anterior de `style.css` + `main.js` para a tela principal;
- e mais dificil de editar manualmente que o prototipo anterior.

Por isso, qualquer mudanca de UI deve escolher explicitamente um de dois caminhos:

1. editar o bundle com controle de regressao e registrar novo hash; ou
2. reconstruir uma fonte editavel equivalente e gerar novo bundle, mantendo paridade visual e funcional.

## 4. Escopo funcional representado

A versao canonica atual materializa o DPP Studio como prototipo interativo para:

- intencao da peca;
- selecao de tipo de peca;
- selecao e composicao de materiais;
- especificacoes dimensionais;
- calculo de area, massa e indicadores;
- dossie lateral;
- QR/passaporte em prototipo.

Esse prototipo nao invalida a tese DPP middleware. Ele e a interface de trabalho mais recente para demonstrar a transicao entre especificacao tecnica, material, calculo de indicadores e passaporte.

## 5. Relacao com backend e roadmap

O backend DPP, o schema, os endpoints e o publisher publico continuam no roadmap. A interface bundled e a referencia visual/funcional imediata, mas nao substitui:

- contrato de dados;
- validacoes anti-greenwashing;
- persistencia;
- DPP publico por URL;
- QR real;
- evidencias documentais;
- deploy de producao.

## 6. Netlify e publicacao

O arquivo foi commitado e pushado para `main`.

Publicacao Netlify como ultima versao ainda depende de permissao/liberacao. Tentativas registradas:

- deploy anonimo bloqueado por limite diario;
- login Netlify autorizado;
- site `phyllos-dpp-studio` criado e vinculado localmente;
- deploy de producao retornou `Forbidden`.

Enquanto a Netlify nao liberar permissao, considerar o GitHub remoto como fonte publicada de codigo, mas nao como deploy publico final.

## 7. Como validar antes de responder "esta na ultima versao"

Rodar:

```bash
shasum -a 256 /Users/paulonascimento/Downloads/dpp-studio.html phyllos/dpp-studio.html
```

Resultado esperado para ambos:

```text
560add24d6e31860fee858805644270b31e030b0a5d0d5ab273d21d52194b8c2
```

Se a pergunta envolver remoto GitHub:

```bash
curl -sS -L https://raw.githubusercontent.com/paulohugorz/phyllos/main/phyllos/dpp-studio.html -o /private/tmp/phyllos-remote-dpp-studio.html
shasum -a 256 /private/tmp/phyllos-remote-dpp-studio.html
```

Se a pergunta envolver Netlify, nao assumir sucesso por push. Verificar o HTML servido pela URL final e comparar com o hash quando possivel.

## 8. Criterio de substituicao futura

Esta versao so deixa de ser canonica quando houver nova decisao explicita do founder, com:

- novo arquivo ou fonte;
- novo hash;
- nova data;
- motivo da troca;
- status de deploy.
