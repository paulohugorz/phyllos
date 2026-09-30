import { createRequire } from 'node:module';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const require = createRequire(import.meta.url);
const { chromium } = require('/Users/paulonascimento/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const root = path.resolve(process.cwd());
const baseUrl = process.env.VEREDA_PREVIEW_URL || 'http://127.0.0.1:4174';
const isLocalPreview = /^https?:\/\/(127\.0\.0\.1|localhost|\[::1\])(?::|\/)/.test(baseUrl);
const previewDir = path.join(root, 'previews');
const manifest = JSON.parse(await readFile(path.join(root, 'lp', 'manifest.json'), 'utf8'));
await mkdir(previewDir, { recursive: true });

const browser = await chromium.launch({
  headless: true,
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
});

const viewports = [
  { name: 'mobile', width: 390, height: 844 },
  { name: 'tablet', width: 768, height: 900 },
  { name: 'desktop', width: 1440, height: 900 },
];

const results = [];

for (const item of manifest.variants) {
  for (const viewport of viewports) {
    const page = await browser.newPage({ viewport });
    const consoleErrors = [];
    const failedRequests = [];
    page.on('console', (message) => {
      if (message.type() === 'error') consoleErrors.push(message.text());
    });
    page.on('requestfailed', (request) => failedRequests.push(`${request.url()} — ${request.failure()?.errorText || 'falha'}`));

    const response = await page.goto(`${baseUrl}${item.route}?utm_source=qa&utm_campaign=lp-ab`, { waitUntil: 'networkidle' });
    if (!response?.ok()) throw new Error(`${item.route} respondeu ${response?.status()}`);

    const images = page.locator('img');
    for (let index = 0; index < await images.count(); index += 1) {
      await images.nth(index).scrollIntoViewIfNeeded();
    }
    await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));

    const layout = await page.evaluate(() => ({
      h1Count: document.querySelectorAll('h1').length,
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      segment: document.body.dataset.segment,
      variant: document.body.dataset.variant,
      formSegment: document.forms['diagnostico-vereda-lp']?.elements.segment.value,
      formVariant: document.forms['diagnostico-vereda-lp']?.elements.variant.value,
      utmSource: document.forms['diagnostico-vereda-lp']?.elements.utm_source.value,
      viewEvent: window.dataLayer?.some((event) => event.event === 'vereda_landing_view'),
    }));

    if (layout.h1Count !== 1) throw new Error(`${item.route}: esperado 1 H1, encontrado ${layout.h1Count}`);
    if (layout.scrollWidth > layout.clientWidth) throw new Error(`${item.route}: rolagem horizontal ${layout.scrollWidth} > ${layout.clientWidth}`);
    if (layout.segment !== item.segment || layout.formSegment !== item.segment) throw new Error(`${item.route}: atribuição de segmento incorreta`);
    if (layout.variant !== item.variant || layout.formVariant !== item.variant) throw new Error(`${item.route}: atribuição de variante incorreta`);
    if (layout.utmSource !== 'qa') throw new Error(`${item.route}: UTM não foi preservada`);
    if (!layout.viewEvent) throw new Error(`${item.route}: evento de visualização ausente`);
    if (consoleErrors.length) throw new Error(`${item.route}: erros no console: ${consoleErrors.join(' | ')}`);
    if (failedRequests.length) throw new Error(`${item.route}: recursos com falha: ${failedRequests.join(' | ')}`);

    if (viewport.name === 'mobile') {
      await page.getByRole('button', { name: /Mapear lacunas|Preparar a próxima negociação/ }).click();
      const invalidMessage = await page.locator('[data-form-status]').innerText();
      if (!invalidMessage.includes('Revise os campos')) throw new Error(`${item.route}: validação obrigatória não apareceu`);

      if (isLocalPreview) {
        await page.getByLabel('Nome', { exact: true }).fill('Teste local');
        await page.getByLabel('Empresa', { exact: true }).fill('Empresa de teste');
        await page.getByLabel('E-mail corporativo').fill('teste@example.com');
        await page.getByRole('button', { name: /Mapear lacunas|Preparar a próxima negociação/ }).click();
        const localMessage = await page.locator('[data-form-status]').innerText();
        if (!localMessage.includes('Prévia local')) throw new Error(`${item.route}: bloqueio de envio local não apareceu`);
      }
    }

    const capture = (
      viewport.name === 'desktop' && item.segment === 'textil-confeccao'
    ) || (
      viewport.name === 'mobile' && item.segment === 'manufatura' && item.variant === 'b'
    );
    let screenshot = null;
    if (capture) {
      screenshot = path.join(previewDir, `lp-${item.segment}-${item.variant}-${viewport.name}.png`);
      await page.screenshot({ path: screenshot, fullPage: true });
    }

    results.push({ route: item.route, viewport: viewport.name, screenshot, layout });
    await page.close();
  }
}

for (const segment of [...new Set(manifest.variants.map((item) => item.segment))]) {
  const page = await browser.newPage();
  await page.goto(`${baseUrl}/lp/${segment}/?variant=a&utm_source=router`, { waitUntil: 'networkidle' });
  const url = new URL(page.url());
  if (url.pathname !== `/lp/${segment}/a/` || url.searchParams.get('utm_source') !== 'router') {
    throw new Error(`Router ${segment} não preservou variante/UTM: ${url.href}`);
  }
  await page.close();
}

await browser.close();

const report = {
  checked_at: new Date().toISOString(),
  base_url: baseUrl,
  pages: manifest.variants.length,
  viewport_checks: results.length,
  router_checks: 5,
  result: 'passed',
  checks: results,
};

await writeFile(path.join(previewDir, 'lp-qa-results.json'), `${JSON.stringify(report, null, 2)}\n`);
process.stdout.write(`QA aprovado: ${report.pages} LPs, ${report.viewport_checks} combinações responsivas e ${report.router_checks} rotas A/B.\n`);
