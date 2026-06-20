/**
 * Fashion OS Catalog Search - GitHub Pages compatible.
 * Runs fully in the browser using /assets/fashion-os/fashion_image_catalog.json.
 * No Netlify, Node, serverless function or SQLite runtime required.
 */
(function () {
  const DEFAULT_CATALOG_URL = './assets/fashion-os/fashion_image_catalog.json';

  const SYNONYMS = {
    calca: ['calça', 'pants', 'trousers', 'bottom', 'bottoms'],
    calça: ['calca', 'pants', 'trousers', 'bottom', 'bottoms'],
    masculina: ['masculino', 'male', 'menswear', 'homem'],
    masculino: ['masculina', 'male', 'menswear', 'homem'],
    alfaiataria: ['tailoring', 'tailored', 'business casual', 'social'],
    flexivel: ['flexível', 'stretch', 'elastano', 'elasticidade', 'conforto'],
    flexível: ['flexivel', 'stretch', 'elastano', 'elasticidade', 'conforto'],
    suor: ['antiodor', 'quick-dry', 'moisture', 'respirável', 'respirabilidade'],
    calor: ['verão', 'tropical', 'leve', 'respirável', 'quick-dry'],
    techwear: ['performance', 'técnico', 'tecnológico', 'technical'],
    camisa: ['shirt', 'overshirt', 'top'],
    camiseta: ['t-shirt', 'tee', 'top'],
    blazer: ['tailoring', 'jacket', 'alfaiataria'],
  };

  let catalogCache = null;

  function normalizeText(value) {
    return String(value || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9\s-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function expandTokens(query) {
    const base = normalizeText(query).split(' ').filter(Boolean);
    const expanded = new Set(base);
    base.forEach((token) => {
      (SYNONYMS[token] || []).forEach((syn) => {
        normalizeText(syn).split(' ').forEach((part) => expanded.add(part));
      });
    });
    return Array.from(expanded).filter(Boolean);
  }

  function inferIntent(query) {
    const q = normalizeText(query);
    return {
      wantsPants: /calca|pants|trouser|bottom/.test(q),
      wantsMale: /masculin|homem|male|menswear/.test(q),
      wantsTailoring: /alfaiat|tailor|social|business/.test(q),
      wantsFlex: /flex|stretch|elastan|confort/.test(q),
      wantsHeat: /calor|salvador|verao|tropical|suor|respir/.test(q),
    };
  }

  async function loadFashionCatalog(url = DEFAULT_CATALOG_URL) {
    if (catalogCache) return catalogCache;
    const response = await fetch(url, { cache: 'force-cache' });
    if (!response.ok) throw new Error(`Não foi possível carregar catálogo: ${response.status}`);
    const data = await response.json();
    catalogCache = Array.isArray(data) ? { items: data } : data;
    return catalogCache;
  }

  function scoreItem(item, tokens, intent) {
    const haystack = normalizeText([
      item.search_text,
      item.title,
      item.category_name,
      item.category_slug,
      item.garment_name,
      item.silhouette,
      item.gender_expression,
      item.materials,
      item.material_families,
      item.finishes,
      item.finish_types,
      item.tags,
      item.brand_reference,
      item.climate_use,
      item.product_goal_fit,
    ].join(' '));

    let score = 0;
    tokens.forEach((token) => {
      if (haystack.includes(token)) score += 2;
    });

    if (intent.wantsPants && /(calca|calcas|pants|trousers|bottom)/.test(haystack)) score += 10;
    if (intent.wantsMale && /(masculin|male|homem|menswear|unissex)/.test(haystack)) score += 5;
    if (intent.wantsTailoring && /(alfaiat|tailor|business casual|social)/.test(haystack)) score += 8;
    if (intent.wantsFlex && /(elastano|stretch|flex|confort|poliamida|viscose|tencel|lyocell)/.test(haystack)) score += 8;
    if (intent.wantsHeat && /(quick-dry|respir|antiodor|moisture|leve|tropical|verao|coolmax)/.test(haystack)) score += 6;

    score += Number(item.phyllos_alignment_score || 0) * 1.5;
    score += Number(item.technical_score || 0);
    score += Number(item.aesthetic_score || 0);

    return score;
  }

  async function searchFashionCatalog(query, options = {}) {
    const { limit = 12, catalogUrl = DEFAULT_CATALOG_URL } = options;
    const catalog = await loadFashionCatalog(catalogUrl);
    const tokens = expandTokens(query);
    const intent = inferIntent(query);

    return (catalog.items || [])
      .map((item) => ({ ...item, score: scoreItem(item, tokens, intent) }))
      .filter((item) => item.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }

  function buildEnrichedFashionPrompt(userPrompt, references) {
    const topRefs = references.slice(0, 5);
    const materials = [...new Set(topRefs.flatMap((r) => String(r.materials || '').split(',').map((x) => x.trim()).filter(Boolean)))];
    const finishes = [...new Set(topRefs.flatMap((r) => String(r.finishes || '').split(',').map((x) => x.trim()).filter(Boolean)))];
    const silhouettes = [...new Set(topRefs.map((r) => r.silhouette).filter(Boolean))];

    return [
      `Pedido do usuário: ${userPrompt}`,
      'Direção PHYLLOS/Fashion OS: roupa urbana premium, funcional, confortável, técnica, durável e minimalista.',
      materials.length ? `Materiais de referência: ${materials.slice(0, 8).join(', ')}.` : '',
      finishes.length ? `Acabamentos sugeridos: ${finishes.slice(0, 10).join(', ')}.` : '',
      silhouettes.length ? `Silhuetas de referência: ${silhouettes.slice(0, 5).join(', ')}.` : '',
      'A imagem deve parecer produto real de moda, com caimento coerente, construção viável e acabamento visível.',
    ].filter(Boolean).join('\n');
  }

  function renderFashionResults(container, references) {
    const el = typeof container === 'string' ? document.querySelector(container) : container;
    if (!el) return;
    el.innerHTML = references.map((item) => `
      <article class="fashion-ref-card">
        <div class="fashion-ref-thumb">${item.view_type || 'ref'}</div>
        <div>
          <strong>${item.garment_name || item.title || 'Referência'}</strong>
          <p>${item.category_name || ''} · ${item.silhouette || ''} · score ${Math.round(item.score || 0)}</p>
          <small>${item.materials || ''}</small><br/>
          <small>${item.finishes || ''}</small>
        </div>
      </article>
    `).join('');
  }

  window.FashionOSCatalog = {
    loadFashionCatalog,
    searchFashionCatalog,
    buildEnrichedFashionPrompt,
    renderFashionResults,
  };
})();
