import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const root = path.resolve(process.cwd());
const outputRoot = path.join(root, 'lp');
const baseUrl = 'https://vereda-dpp.netlify.app';

const segments = [
  {
    slug: 'textil-confeccao',
    label: 'Moda, têxteis e confecção',
    audience: 'Marcas, confecções e operações têxteis',
    image: '/assets/images/fibras-materiais.webp',
    imageAlt: 'Detalhe ilustrativo de fibras e trama de tecido cru',
    imageCaption: 'Imagem ilustrativa de materialidade; não comprova composição, origem ou cliente.',
    example: 'Produto têxtil / referência ilustrativa',
    code: 'TXT-DEMO-01',
    heroA: 'Descubra o que falta antes que uma pergunta do buyer vire um bloqueio.',
    leadA: 'A Vereda conecta composição, origem, fornecedores e documentos para mostrar o que já pode ser apresentado e o que ainda precisa de evidência antes da próxima conversa comercial.',
    heroB: 'Transforme dados de produto em uma resposta que acompanha a próxima negociação.',
    leadB: 'Organize informações técnicas e evidências em uma leitura clara para compradores e parceiros, sem inflar o que ainda não está comprovado.',
    problems: [
      ['Dados espalhados', 'Ficha técnica, planilha, e-mail e declaração de fornecedor raramente contam a mesma história.'],
      ['Pressão de resposta', 'Compradores pedem composição, origem e documentos em ritmos que a operação nem sempre acompanha.'],
      ['Risco de excesso', 'Uma afirmação sem fonte pode criar mais risco do que uma lacuna apresentada com transparência.'],
    ],
    topics: [
      ['Composição do produto', 'Evidência vinculada', 'Manter vínculo com a versão vigente', 'ok'],
      ['Origem declarada', 'Evidência ausente', 'Solicitar documento ou registrar limite', 'gap'],
      ['Fornecedor', 'Revisão pendente', 'Concluir revisão cadastral', 'pending'],
      ['Mercado pretendido', 'Escopo em evolução', 'Definir requisitos aplicáveis', 'pending'],
    ],
    fit: [
      'Precisa responder a compradores com mais consistência.',
      'Já possui fichas, planilhas ou documentos parciais.',
      'Quer preparar dados para DPP conforme o contexto aplicável.',
    ],
  },
  {
    slug: 'calcados-couro',
    label: 'Calçados e couro',
    audience: 'Marcas, fabricantes e operações de calçados e couro',
    image: '/assets/images/fibras-materiais.webp',
    imageAlt: 'Detalhe ilustrativo de material fibroso em tom natural',
    imageCaption: 'Imagem ilustrativa de materialidade; não comprova composição, origem ou cliente.',
    example: 'Calçado / referência ilustrativa',
    code: 'CAL-DEMO-01',
    heroA: 'Veja onde a documentação do calçado ainda quebra antes de responder ao mercado.',
    leadA: 'A Vereda organiza materiais, componentes, origem, fornecedores e registros para tornar lacunas e dependências visíveis antes que virem urgência comercial.',
    heroB: 'Apresente materiais, origem e evidências do calçado com mais clareza.',
    leadB: 'Prepare uma base de informação que ajuda compradores e parceiros a entender o produto, a fonte dos dados e os limites do que está comprovado.',
    problems: [
      ['Produto em partes', 'Cabedal, forro, palmilha, solado e embalagem podem depender de fontes e documentos diferentes.'],
      ['Cadeia fragmentada', 'Fabricantes, fornecedores e marcas precisam alinhar versões, responsáveis e registros.'],
      ['Destino variável', 'As exigências mudam conforme produto, operação e mercado; um checklist genérico não resolve tudo.'],
    ],
    topics: [
      ['Materiais por componente', 'Evidência vinculada', 'Confirmar versão técnica vigente', 'ok'],
      ['Origem do produto', 'Revisão pendente', 'Validar fonte e responsável', 'pending'],
      ['Fornecedor crítico', 'Evidência ausente', 'Solicitar registro de suporte', 'gap'],
      ['Mercado pretendido', 'Escopo em evolução', 'Mapear requisitos aplicáveis', 'pending'],
    ],
    fit: [
      'Precisa reunir dados de componentes e fornecedores.',
      'Atende compradores, importadores ou parceiros comerciais.',
      'Quer preparar um caminho auditável sem prometer certificação.',
    ],
  },
  {
    slug: 'agro',
    label: 'Agro',
    audience: 'Produtores, marcas e operações do agro',
    image: '/assets/images/hero-territorio.webp',
    imageAlt: 'Estrada sinuosa em território montanhoso litorâneo, em imagem ilustrativa',
    imageCaption: 'Imagem ilustrativa; não representa fazenda, território, rota ou cliente real.',
    example: 'Lote agro / referência ilustrativa',
    code: 'AGR-DEMO-01',
    heroA: 'Encontre as lacunas de origem e cadeia antes que o mercado de destino as encontre.',
    leadA: 'A Vereda reúne registros de origem, cadeia, responsáveis e documentos para mostrar o que está sustentado e o que precisa ser preparado para uma operação comercial específica.',
    heroB: 'Transforme registros da cadeia em uma resposta verificável para novos mercados.',
    leadB: 'Organize a informação que compradores e parceiros precisam consultar, com fonte, estado da análise e próximos passos claramente identificados.',
    problems: [
      ['Origem sem vínculo', 'O dado existe, mas nem sempre está ligado ao lote, ao documento e à versão correta.'],
      ['Cadeia com múltiplos elos', 'Coleta, beneficiamento, armazenagem e comercialização geram registros em sistemas diferentes.'],
      ['Destino muda a análise', 'Produto e mercado pretendido determinam quais requisitos precisam entrar no escopo.'],
    ],
    topics: [
      ['Origem do lote', 'Evidência vinculada', 'Manter vínculo com o registro vigente', 'ok'],
      ['Participantes da cadeia', 'Revisão pendente', 'Confirmar cadastros e responsabilidades', 'pending'],
      ['Documento de suporte', 'Evidência ausente', 'Solicitar registro ao owner', 'gap'],
      ['Mercado de destino', 'Escopo em evolução', 'Definir requisitos aplicáveis', 'pending'],
    ],
    fit: [
      'Opera com lotes, origem e múltiplos participantes.',
      'Quer preparar informação para um mercado de destino definido.',
      'Precisa evidenciar limites e pendências sem criar falsa certeza.',
    ],
  },
  {
    slug: 'manufatura',
    label: 'Manufatura',
    audience: 'Fabricantes e operações industriais',
    image: '/assets/images/processo-industrial.webp',
    imageAlt: 'Interior industrial organizado com bobinas metálicas, em imagem ilustrativa',
    imageCaption: 'Infraestrutura ilustrativa; não representa instalação, processo ou cliente real.',
    example: 'Produto industrial / referência ilustrativa',
    code: 'MAN-DEMO-01',
    heroA: 'Identifique o ponto fraco entre especificação, processo e evidência.',
    leadA: 'A Vereda conecta dados de materiais, processos, fornecedores e documentos para revelar dependências antes de uma diligência ou negociação.',
    heroB: 'Converta registros industriais em informação pronta para a conversa comercial.',
    leadB: 'Estruture especificações e evidências para que compradores e parceiros consultem o que importa sem navegar por planilhas, pastas e versões conflitantes.',
    problems: [
      ['Versões conflitantes', 'Especificações, desenhos e certificados podem circular sem uma referência vigente comum.'],
      ['Dependência de fornecedor', 'Uma informação crítica pode existir fora da empresa e sem owner definido para obtê-la.'],
      ['Resposta manual', 'Cada nova solicitação repete a busca por dados que já deveriam estar conectados.'],
    ],
    topics: [
      ['Especificação do material', 'Evidência vinculada', 'Controlar revisão vigente', 'ok'],
      ['Processo declarado', 'Revisão pendente', 'Confirmar fonte e owner', 'pending'],
      ['Fornecedor crítico', 'Evidência ausente', 'Solicitar documento de suporte', 'gap'],
      ['Mercado pretendido', 'Escopo em evolução', 'Mapear requisitos aplicáveis', 'pending'],
    ],
    fit: [
      'Recebe questionários de compradores e parceiros.',
      'Possui especificações e documentos em múltiplos repositórios.',
      'Precisa preparar evidência para um destino comercial específico.',
    ],
  },
  {
    slug: 'cooperativas',
    label: 'Cooperativas',
    audience: 'Cooperativas, associações e redes de produtores',
    image: '/assets/images/hero-territorio.webp',
    imageAlt: 'Estrada sinuosa conectando áreas de um território, em imagem ilustrativa',
    imageCaption: 'Imagem ilustrativa; não representa território, cooperativa, rota ou cliente real.',
    example: 'Rede cooperada / referência ilustrativa',
    code: 'COOP-DEMO-01',
    heroA: 'Torne visíveis as lacunas entre o registro individual e a resposta coletiva.',
    leadA: 'A Vereda organiza informações, responsáveis e documentos compartilhados para mostrar o que a rede já consegue sustentar e onde ainda existem ausências.',
    heroB: 'Transforme registros distribuídos em uma apresentação coerente da rede.',
    leadB: 'Prepare uma leitura comum para compradores e parceiros, preservando a fonte, o contexto e os limites da informação de cada participante.',
    problems: [
      ['Registros heterogêneos', 'Cada participante pode registrar origem, produção e documentos de maneira diferente.'],
      ['Responsabilidade difusa', 'Sem owner claro, pendências passam de participante em participante sem conclusão.'],
      ['Resposta coletiva frágil', 'A rede precisa apresentar consistência sem apagar as diferenças entre seus membros.'],
    ],
    topics: [
      ['Cadastro dos participantes', 'Revisão pendente', 'Definir owner por registro', 'pending'],
      ['Origem declarada', 'Evidência vinculada', 'Manter vínculo com o participante', 'ok'],
      ['Documento compartilhado', 'Evidência ausente', 'Solicitar evidência ao responsável', 'gap'],
      ['Mercado pretendido', 'Escopo em evolução', 'Alinhar requisitos e governança', 'pending'],
    ],
    fit: [
      'Reúne dados de múltiplos participantes ou unidades.',
      'Precisa responder comercialmente como rede.',
      'Quer deixar responsabilidades e ausências consultáveis.',
    ],
  },
];

const variants = {
  a: {
    label: 'Variante A · Readiness',
    hypothesis: 'A mensagem orientada a risco e lacunas gera mais conversas entre empresas sob pressão de requisitos.',
    cta: 'Mapear lacunas',
    sectionKicker: 'Antes da exigência virar urgência',
    sectionTitle: 'O problema não é faltar informação. É não saber qual informação sustenta a decisão.',
    contactTitle: 'Mapeie as lacunas antes da próxima exigência.',
  },
  b: {
    label: 'Variante B · Acesso a mercado',
    hypothesis: 'A mensagem orientada a oportunidade gera mais conversas entre empresas buscando compradores e parceiros.',
    cta: 'Preparar a próxima negociação',
    sectionKicker: 'Antes da próxima conversa comercial',
    sectionTitle: 'Quem apresenta a fonte, o contexto e o limite da informação conversa em outro nível.',
    contactTitle: 'Prepare a informação para a próxima negociação.',
  },
};

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

function proofRows(topics) {
  return topics.map(([topic, state, , status]) => `
            <div class="lp-proof-row">
              <dt>${escapeHtml(topic)}</dt>
              <dd><span class="lp-state ${status === 'gap' ? 'is-gap' : status === 'pending' ? 'is-pending' : ''}">${escapeHtml(state)}</span></dd>
            </div>`).join('');
}

function recordRows(topics) {
  return topics.map(([topic, state, action, status]) => `
          <div class="lp-record">
            <strong>${escapeHtml(topic)}</strong>
            <span><span class="lp-state ${status === 'gap' ? 'is-gap' : status === 'pending' ? 'is-pending' : ''}">${escapeHtml(state)}</span></span>
            <p>${escapeHtml(action)}</p>
          </div>`).join('');
}

function landingPage(segment, variantKey) {
  const variant = variants[variantKey];
  const isA = variantKey === 'a';
  const hero = isA ? segment.heroA : segment.heroB;
  const lead = isA ? segment.leadA : segment.leadB;
  const route = `/lp/${segment.slug}/${variantKey}/`;
  const canonical = `${baseUrl}/lp/${segment.slug}/a/`;
  const description = `${lead} Diagnóstico e organização de evidências para ${segment.label.toLowerCase()}.`;
  const robots = isA ? 'index, follow' : 'noindex, follow';

  return `<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(hero)} | Vereda</title>
  <meta name="description" content="${escapeHtml(description)}">
  <meta name="robots" content="${robots}">
  <meta name="theme-color" content="#F7F7F3">
  <link rel="canonical" href="${canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="${escapeHtml(hero)} | Vereda">
  <meta property="og:description" content="${escapeHtml(description)}">
  <meta property="og:url" content="${baseUrl}${route}">
  <link rel="icon" type="image/png" href="/assets/brand/vereda-wordmark-v2-referencia-raster.png">
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="/lp/lp.css">
  <script src="/lp/lp.js" defer></script>
</head>
<body class="lp-body" data-segment="${segment.slug}" data-variant="${variantKey}" data-landing-page="${route}">
  <a class="skip-link" href="#conteudo">Pular para o conteúdo</a>

  <header class="lp-header">
    <div class="lp-header-inner">
      <a class="brand" href="/" aria-label="Vereda — página inicial">
        <img src="/assets/brand/vereda-wordmark-v2-referencia-raster.png" width="477" height="96" alt="Vereda">
      </a>
      <span class="lp-header-context">${escapeHtml(segment.label)} · ${escapeHtml(variant.label)}</span>
      <nav class="lp-header-nav" aria-label="Navegação da landing page">
        <a href="#como-funciona">Como funciona</a>
        <a class="button button-small" href="#conversa" data-track-cta="cabecalho">${escapeHtml(variant.cta)}</a>
      </nav>
    </div>
  </header>

  <main id="conteudo">
    <section class="lp-hero" aria-labelledby="lp-title">
      <div class="lp-hero-copy">
        <p class="eyebrow lp-eyebrow">${escapeHtml(segment.audience)} · inteligência regulatória e tecnológica</p>
        <h1 id="lp-title">${escapeHtml(hero).replace(/(lacunas|resposta|evidências|informação|registros|mercados|negociação|produto)/i, '<strong>$1</strong>')}</h1>
        <p class="lp-hero-lead">${escapeHtml(lead)}</p>
        <div class="lp-hero-actions">
          <a class="button" href="#conversa" data-track-cta="hero">${escapeHtml(variant.cta)}</a>
          <a class="lp-text-link" href="#exemplo" data-track-cta="hero-secundario">Ver exemplo ilustrativo</a>
        </div>
      </div>

      <div class="lp-hero-proof">
        <figure class="lp-hero-figure">
          <img src="${segment.image}" width="1536" height="1024" alt="${escapeHtml(segment.imageAlt)}" fetchpriority="high">
          <figcaption>${escapeHtml(segment.imageCaption)}</figcaption>
        </figure>
        <aside class="lp-proof-card" aria-labelledby="proof-title">
          <div class="lp-proof-head">
            <div>
              <p class="micro-label">Demonstração com dados fictícios</p>
              <h2 id="proof-title">Leitura inicial · ${escapeHtml(segment.code)}</h2>
            </div>
            <span class="lp-variant-chip">${variantKey.toUpperCase()}</span>
          </div>
          <dl class="lp-proof-list">${proofRows(segment.topics)}</dl>
        </aside>
      </div>
    </section>

    <section class="lp-trust-strip" aria-label="Entregáveis possíveis">
      <div class="lp-trust-inner">
        <div class="lp-trust-item"><span>01 / Ler</span><strong>Gap Map</strong></div>
        <div class="lp-trust-item"><span>02 / Priorizar</span><strong>Readiness Report</strong></div>
        <div class="lp-trust-item"><span>03 / Organizar</span><strong>Evidence Vault</strong></div>
        <div class="lp-trust-item"><span>04 / Compartilhar</span><strong>Buyer Data Pack</strong></div>
      </div>
    </section>

    <section class="lp-section" aria-labelledby="problem-title">
      <div class="lp-section-head">
        <p class="section-index lp-section-index">01 / ${escapeHtml(variant.sectionKicker)}</p>
        <h2 id="problem-title">${escapeHtml(variant.sectionTitle)}</h2>
        <p>O diagnóstico considera produto, operação, mercado pretendido e registros disponíveis. O escopo real depende do contexto da empresa.</p>
      </div>
      <div class="lp-problem-grid">
        ${segment.problems.map(([title, copy], index) => `<article class="lp-problem-card"><span>0${index + 1}</span><h3>${escapeHtml(title)}</h3><p>${escapeHtml(copy)}</p></article>`).join('\n        ')}
      </div>
    </section>

    <section class="lp-section lp-section-dark" id="como-funciona" aria-labelledby="flow-title">
      <div class="lp-section-head">
        <p class="section-index lp-section-index">02 / Como atuamos</p>
        <h2 id="flow-title">Da pergunta comercial à próxima ação verificável.</h2>
        <p>A tecnologia ajuda a manter informação, documento, owner e revisão conectados. Ela não transforma automaticamente uma declaração em comprovação.</p>
      </div>
      <div class="lp-flow">
        <article class="lp-step"><h3>Entender o contexto</h3><p>Produto, operação, mercado pretendido e registros existentes entram na mesma leitura.</p></article>
        <article class="lp-step"><h3>Mapear lacunas</h3><p>Ausências, conflitos e dependências ficam visíveis sem score genérico de prontidão.</p></article>
        <article class="lp-step"><h3>Organizar evidências</h3><p>Fontes, documentos, responsáveis e versões passam a acompanhar cada informação.</p></article>
        <article class="lp-step"><h3>Preparar a resposta</h3><p>O conteúdo pertinente à negociação é apresentado com contexto e limite de comprovação.</p></article>
      </div>
    </section>

    <section class="lp-section lp-section-alt" id="exemplo" aria-labelledby="evidence-title">
      <div class="lp-evidence-layout">
        <div class="lp-evidence-copy">
          <p class="section-index lp-section-index">03 / Exemplo ilustrativo</p>
          <h2 id="evidence-title">Veja a informação junto da evidência e da próxima ação.</h2>
          <p>Este quadro usa dados fictícios para mostrar a estrutura da análise. Não representa cliente, diagnóstico concluído, certificação ou conformidade.</p>
        </div>
        <div class="lp-evidence-panel" aria-label="Exemplo fictício de organização de evidências">
          <div class="lp-evidence-panel-head">
            <div><p class="micro-label">${escapeHtml(segment.example)}</p><strong>${escapeHtml(segment.code)}</strong></div>
            <span class="lp-variant-chip">Exemplo fictício</span>
          </div>
          ${recordRows(segment.topics)}
        </div>
      </div>
    </section>

    <section class="lp-section" aria-labelledby="fit-title">
      <div class="lp-section-head">
        <p class="section-index lp-section-index">04 / Quando faz sentido</p>
        <h2 id="fit-title">Uma conversa útil começa pelo contexto certo.</h2>
      </div>
      <div class="lp-fit-grid">
        <article class="lp-fit-card">
          <h3>Esta leitura pode ajudar sua operação se você:</h3>
          <ul>${segment.fit.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
        </article>
        <article class="lp-fit-card is-muted">
          <h3>O que a conversa inicial não representa:</h3>
          <ul>
            <li>certificação ou parecer jurídico;</li>
            <li>garantia de conformidade ou acesso a mercado;</li>
            <li>diagnóstico completo antes da definição do escopo;</li>
            <li>validação automática de declarações sem evidência.</li>
          </ul>
        </article>
      </div>
    </section>

    <section class="lp-contact" id="conversa" aria-labelledby="contact-title">
      <div class="lp-contact-grid">
        <div class="lp-contact-copy">
          <p class="section-index lp-section-index">05 / Próximo passo</p>
          <h2 id="contact-title">${escapeHtml(variant.contactTitle)}</h2>
          <p>Conte o contexto da sua empresa. A primeira conversa serve para delimitar produto, destino, registros disponíveis e o possível escopo de trabalho.</p>
          <p class="lp-expectation">Segmento desta página: <strong>${escapeHtml(segment.label)}</strong><br>Hipótese em teste: ${escapeHtml(variant.hypothesis)}</p>
        </div>

        <form class="lp-form" name="diagnostico-vereda-lp" method="post" action="/obrigado/" data-netlify="true" netlify-honeypot="bot-field" novalidate aria-label="Agendar conversa com a Vereda">
          <input type="hidden" name="form-name" value="diagnostico-vereda-lp">
          <input type="hidden" name="segment" value="${segment.slug}">
          <input type="hidden" name="variant" value="${variantKey}">
          <input type="hidden" name="landing_page" value="${route}">
          <input type="hidden" name="utm_source" value="">
          <input type="hidden" name="utm_medium" value="">
          <input type="hidden" name="utm_campaign" value="">
          <input type="hidden" name="utm_content" value="">
          <input type="hidden" name="utm_term" value="">
          <p hidden><label>Não preencha: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>

          <div class="lp-form-grid">
            <div class="lp-field">
              <label for="name-${segment.slug}-${variantKey}">Nome</label>
              <input id="name-${segment.slug}-${variantKey}" name="name" type="text" autocomplete="name" maxlength="120" required aria-describedby="name-${segment.slug}-${variantKey}-error">
              <span class="lp-field-error" id="name-${segment.slug}-${variantKey}-error" aria-live="polite"></span>
            </div>
            <div class="lp-field">
              <label for="company-${segment.slug}-${variantKey}">Empresa</label>
              <input id="company-${segment.slug}-${variantKey}" name="company" type="text" autocomplete="organization" maxlength="160" required aria-describedby="company-${segment.slug}-${variantKey}-error">
              <span class="lp-field-error" id="company-${segment.slug}-${variantKey}-error" aria-live="polite"></span>
            </div>
            <div class="lp-field lp-field-full">
              <label for="email-${segment.slug}-${variantKey}">E-mail corporativo</label>
              <input id="email-${segment.slug}-${variantKey}" name="email" type="email" autocomplete="email" maxlength="254" placeholder="nome@empresa.com" required aria-describedby="email-${segment.slug}-${variantKey}-error">
              <span class="lp-field-error" id="email-${segment.slug}-${variantKey}-error" aria-live="polite"></span>
            </div>
            <div class="lp-field">
              <label for="target-${segment.slug}-${variantKey}">Mercado pretendido <span>(opcional)</span></label>
              <input id="target-${segment.slug}-${variantKey}" name="target_market" type="text" maxlength="120" placeholder="Ex.: Brasil, União Europeia">
            </div>
            <div class="lp-field">
              <label for="volume-${segment.slug}-${variantKey}">Volume de produtos/SKUs <span>(opcional)</span></label>
              <select id="volume-${segment.slug}-${variantKey}" name="sku_volume">
                <option value="" selected>Não informado</option>
                <option value="ate-10">Até 10</option>
                <option value="11-50">11–50</option>
                <option value="51-200">51–200</option>
                <option value="200-mais">200+</option>
              </select>
            </div>
          </div>
          <button class="button" type="submit">${escapeHtml(variant.cta)}</button>
          <p class="lp-form-status" role="status" aria-live="polite" aria-atomic="true" data-form-status></p>
          <p class="lp-form-note">Usaremos estas informações para responder à sua solicitação. Não envie documentos confidenciais por este formulário.</p>
        </form>
      </div>
    </section>
  </main>

  <footer class="lp-footer">
    <a class="brand" href="/" aria-label="Vereda — página inicial"><img src="/assets/brand/vereda-wordmark-v2-referencia-raster.png" width="477" height="96" loading="lazy" alt="Vereda"></a>
    <p>Inteligência regulatória e tecnológica para acesso a mercados.</p>
    <a href="/">Conhecer a Vereda</a>
  </footer>
</body>
</html>
`;
}

function routerPage(segment) {
  return `<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, follow">
  <title>Vereda para ${escapeHtml(segment.label)}</title>
  <link rel="canonical" href="${baseUrl}/lp/${segment.slug}/a/">
  <script src="/lp/router.js"></script>
</head>
<body>
  <p>Direcionando para a experiência Vereda de ${escapeHtml(segment.label)}. <a href="./a/">Continuar</a>.</p>
</body>
</html>
`;
}

function directoryPage() {
  return `<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Matriz de landing pages | Vereda</title>
  <link rel="icon" type="image/png" href="/assets/brand/vereda-wordmark-v2-referencia-raster.png">
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="/lp/lp.css">
</head>
<body>
  <main class="lp-directory">
    <a class="brand" href="/"><img src="/assets/brand/vereda-wordmark-v2-referencia-raster.png" width="477" height="96" alt="Vereda"></a>
    <p class="section-index" style="margin-top:4rem">Matriz de experimento</p>
    <h1>Landing pages por segmento e hipótese.</h1>
    <p class="lp-directory-intro">Use as URLs A e B em campanhas separadas ou a rota 50/50 para distribuição persistente no navegador. Esta página de controle não é indexada.</p>
    <div class="lp-directory-grid">
      ${segments.map((segment) => `<article class="lp-directory-card"><p class="micro-label">${escapeHtml(segment.slug)}</p><h2>${escapeHtml(segment.label)}</h2><div class="lp-directory-actions"><a href="./${segment.slug}/a/">Variante A</a><a href="./${segment.slug}/b/">Variante B</a><a href="./${segment.slug}/">Rota 50/50</a></div></article>`).join('\n      ')}
    </div>
  </main>
</body>
</html>
`;
}

await mkdir(outputRoot, { recursive: true });
await writeFile(path.join(outputRoot, 'index.html'), directoryPage());

const manifest = [];
for (const segment of segments) {
  const segmentDir = path.join(outputRoot, segment.slug);
  await mkdir(segmentDir, { recursive: true });
  await writeFile(path.join(segmentDir, 'index.html'), routerPage(segment));
  for (const variantKey of Object.keys(variants)) {
    const variantDir = path.join(segmentDir, variantKey);
    await mkdir(variantDir, { recursive: true });
    await writeFile(path.join(variantDir, 'index.html'), landingPage(segment, variantKey));
    manifest.push({
      segment: segment.slug,
      segment_label: segment.label,
      variant: variantKey,
      hypothesis: variants[variantKey].hypothesis,
      route: `/lp/${segment.slug}/${variantKey}/`,
      title: variantKey === 'a' ? segment.heroA : segment.heroB,
    });
  }
}

await writeFile(path.join(outputRoot, 'manifest.json'), `${JSON.stringify({ generated_at: '2026-09-30', experiment: 'VEREDA-LP-AB-2026-09-30', variants: manifest }, null, 2)}\n`);
process.stdout.write(`Geradas ${manifest.length} landing pages em ${outputRoot}\n`);
