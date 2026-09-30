import { createRequire } from 'node:module';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const require = createRequire(import.meta.url);
const { chromium } = require('/Users/paulonascimento/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const baseUrl = process.env.VEREDA_PREVIEW_URL || 'http://127.0.0.1:4173/';
const outputDir = path.resolve('vereda/previews');
await mkdir(outputDir, { recursive: true });

const browser = await chromium.launch({
  headless: true,
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
});
process.stdout.write('browser-ready\n');
const results = {};

async function verify(viewport, fileName) {
  process.stdout.write(`verify-${viewport.width}-start\n`);
  const page = await browser.newPage({ viewport });
  const consoleErrors = [];
  const failedRequests = [];

  page.on('console', (message) => {
    if (message.type() === 'error') consoleErrors.push(message.text());
  });
  page.on('requestfailed', (request) => {
    failedRequests.push(`${request.url()} — ${request.failure()?.errorText || 'falha'}`);
  });

  const response = await page.goto(baseUrl, { waitUntil: 'networkidle' });
  if (!response?.ok()) throw new Error(`Preview respondeu ${response?.status()}`);
  process.stdout.write(`verify-${viewport.width}-loaded\n`);

  const images = page.locator('img');
  for (let index = 0; index < await images.count(); index += 1) {
    await images.nth(index).scrollIntoViewIfNeeded();
  }
  await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));

  for (const tabName of ['Evidence Vault', 'Buyer Data Pack', 'Gap Map']) {
    await page.getByRole('tab', { name: tabName }).click();
    const selected = await page.getByRole('tab', { name: tabName }).getAttribute('aria-selected');
    if (selected !== 'true') throw new Error(`Aba ${tabName} não ficou ativa`);
  }

  await page.locator('.faq-list summary').first().click();
  const faqOpen = await page.locator('.faq-list details').first().getAttribute('open');
  if (faqOpen === null) throw new Error('FAQ não expandiu');

  await page.getByRole('button', { name: 'Agendar conversa', exact: true }).last().click();
  const invalidMessage = await page.locator('[data-form-status]').innerText();
  if (!invalidMessage.includes('Revise os campos')) throw new Error('Validação obrigatória do formulário não apareceu');

  await page.getByLabel('Nome', { exact: true }).fill('Teste local');
  await page.getByLabel('Empresa', { exact: true }).fill('Empresa de teste');
  await page.getByLabel('E-mail corporativo').fill('teste@example.com');
  await page.getByLabel('Segmento').selectOption('manufatura');
  await page.getByRole('button', { name: 'Agendar conversa', exact: true }).last().click();
  const localMessage = await page.locator('[data-form-status]').innerText();
  if (!localMessage.includes('Prévia local')) throw new Error('Aviso de não envio local não apareceu');

  await page.reload({ waitUntil: 'networkidle' });
  for (let index = 0; index < await images.count(); index += 1) {
    await images.nth(index).scrollIntoViewIfNeeded();
  }
  await page.waitForFunction(() => [...document.images].every((image) => image.complete && image.naturalWidth > 0));

  if (viewport.width <= 960) {
    const menu = page.locator('.menu-button');
    await menu.click();
    if ((await menu.getAttribute('aria-expanded')) !== 'true') throw new Error('Menu móvel não abriu');
    await page.keyboard.press('Escape');
    if ((await menu.getAttribute('aria-expanded')) !== 'false') throw new Error('Menu móvel não fechou com Escape');
  }

  const layout = await page.evaluate(() => ({
    bodyWidth: document.body.getBoundingClientRect().width,
    clientWidth: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    scrollHeight: document.documentElement.scrollHeight,
    headingCount: document.querySelectorAll('h1').length,
    images: [...document.images].map((image) => ({
      src: image.getAttribute('src'),
      naturalWidth: image.naturalWidth,
      naturalHeight: image.naturalHeight,
    })),
  }));

  if (layout.scrollWidth > layout.clientWidth) {
    throw new Error(`Rolagem horizontal: ${layout.scrollWidth}px > ${layout.clientWidth}px`);
  }
  if (layout.headingCount !== 1) throw new Error(`Esperado 1 H1, encontrado ${layout.headingCount}`);
  if (consoleErrors.length) throw new Error(`Erros no console: ${consoleErrors.join(' | ')}`);
  if (failedRequests.length) throw new Error(`Recursos com falha: ${failedRequests.join(' | ')}`);

  const outputPath = fileName ? path.join(outputDir, fileName) : null;
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(100);
  if (outputPath) {
    await page.screenshot({ path: outputPath, fullPage: true });
    process.stdout.write(`verify-${viewport.width}-captured\n`);
  }
  await page.close();

  return { viewport, outputPath, layout };
}

results.width360 = await verify({ width: 360, height: 800 }, null);
results.mobile = await verify({ width: 390, height: 844 }, 'vereda-mobile-390.png');
results.tablet = await verify({ width: 768, height: 900 }, null);
results.desktop = await verify({ width: 1440, height: 900 }, 'vereda-desktop-1440.png');

await browser.close();
await writeFile(path.join(outputDir, 'qa-results.json'), `${JSON.stringify(results, null, 2)}\n`);
process.stdout.write(`${JSON.stringify(results, null, 2)}\n`);
