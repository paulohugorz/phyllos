const pptxgen = require("pptxgenjs");

const C = {
  bg:     "0d0d0d",
  card:   "1a1a1a",
  border: "2a2a2a",
  green:  "4caf82",
  text:   "e8e8e0",
  muted:  "888888",
  accent: "c9a96e",
  white:  "f5f5f0",
  red:    "c04040",
  darkGreen: "0f1a12",
  darkGold:  "1a1200",
};

const FONT_TITLE  = "Cambria";
const FONT_BODY   = "Calibri";

const W = 10;    // slide width inches
const H = 5.625; // slide height inches

function makeShadow() {
  return { type: "outer", color: "000000", blur: 8, offset: 2, angle: 45, opacity: 0.3 };
}

function addLogo(slide) {
  // Φ PHYLLOS wear — top left
  slide.addText([
    { text: "Φ", options: { color: C.green, fontSize: 13, bold: true } },
    { text: "  PHYLLOS ", options: { color: C.white, fontSize: 11, bold: false } },
    { text: "wear", options: { color: C.muted, fontSize: 9 } },
  ], { x: 0.3, y: 0.18, w: 2.5, h: 0.32, fontFace: FONT_BODY, margin: 0 });
}

function addSlideNum(slide, n, total) {
  slide.addText(`${String(n).padStart(2,"0")} / ${String(total).padStart(2,"0")}`, {
    x: W - 1.0, y: 0.18, w: 0.7, h: 0.25,
    fontFace: FONT_BODY, fontSize: 9, color: C.muted, align: "right", margin: 0,
  });
}

function addKicker(slide, text) {
  slide.addText(text, {
    x: 0.4, y: 0.6, w: 9.2, h: 0.22,
    fontFace: FONT_BODY, fontSize: 8.5, color: C.green,
    charSpacing: 3, bold: false, margin: 0,
  });
}

function addTitle(slide, text, opts = {}) {
  slide.addText(text, {
    x: 0.4, y: 0.82, w: 9.2, h: opts.h || 0.85,
    fontFace: FONT_TITLE, fontSize: opts.size || 26,
    color: C.white, bold: true, margin: 0,
    ...opts,
  });
}

function card(slide, x, y, w, h, opts = {}) {
  slide.addShape(slide.pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h,
    fill: { color: opts.fill || C.card },
    line: { color: opts.borderColor || C.border, width: 0.7 },
    rectRadius: 0.08,
    shadow: makeShadow(),
  });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 1 — O QUE É
// ─────────────────────────────────────────────────────────────────
function slide1(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 1, 8);
  addKicker(s, "01 · O QUE É A PHYLLOS");

  // Hero card background
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.35, y: 0.78, w: 9.3, h: 1.95,
    fill: { color: "0f1a12" },
    line: { color: "2d4a36", width: 0.7 },
    rectRadius: 0.1,
  });

  // Big Φ watermark
  s.addText("Φ", {
    x: 7.8, y: 0.7, w: 1.8, h: 1.6,
    fontFace: FONT_TITLE, fontSize: 110, color: "1e3a22",
    bold: false, align: "center", valign: "middle", margin: 0,
  });

  // Main tagline
  s.addText([
    { text: "A PHYLLOS cria o ", options: { color: C.text } },
    { text: "passaporte digital", options: { color: C.green, bold: true } },
    { text: " das roupas.", options: { color: C.text } },
    { text: "\nCada peça ganha um QR que conta de onde vem,\no que tem dentro e quanto impacta o planeta.", options: { color: C.muted } },
  ], {
    x: 0.55, y: 0.88, w: 7.5, h: 1.7,
    fontFace: FONT_TITLE, fontSize: 16.5, margin: 0,
  });

  // Tags row
  const tags = ["SaaS B2B", "Moda + Regulação", "Brasil → Europa", "2026"];
  const tagColors = [C.green, C.green, C.green, C.accent];
  tags.forEach((t, i) => {
    const tx = 0.35 + i * 2.35;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: tx, y: 2.82, w: 2.2, h: 0.3,
      fill: { color: "101a12", transparency: 0 },
      line: { color: "2d4a36", width: 0.6 },
      rectRadius: 0.15,
    });
    s.addText(t, {
      x: tx, y: 2.82, w: 2.2, h: 0.3,
      fontFace: FONT_BODY, fontSize: 8.5, color: tagColors[i],
      align: "center", valign: "middle", margin: 0,
    });
  });

  // 3 bottom cards
  const cards = [
    { label: "QUEM PAGA", val: "Marcas de Moda", desc: "Independentes, ateliês,\npequenas e médias" },
    { label: "O QUE ENTREGAMOS", val: "QR + Passaporte", desc: "Página pública com dados\nverificáveis por peça" },
    { label: "POR QUE AGORA", val: "Lei em vigor", desc: "UE exige DPP têxtil\nobrigatório ~2028" },
  ];
  cards.forEach((c2, i) => {
    const cx = 0.35 + i * 3.2;
    card(s, cx, 3.22, 3.0, 2.1);
    s.addText(c2.label, { x: cx+0.18, y: 3.32, w: 2.65, h: 0.22, fontFace: FONT_BODY, fontSize: 7.5, color: C.muted, charSpacing: 2, margin: 0 });
    s.addText(c2.val,   { x: cx+0.18, y: 3.54, w: 2.65, h: 0.42, fontFace: FONT_TITLE, fontSize: 17, color: C.white, bold: true, margin: 0 });
    s.addText(c2.desc,  { x: cx+0.18, y: 3.96, w: 2.65, h: 1.2, fontFace: FONT_BODY, fontSize: 11, color: C.muted, margin: 0 });
  });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 2 — O PROBLEMA
// ─────────────────────────────────────────────────────────────────
function slide2(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 2, 8);
  addKicker(s, "02 · O PROBLEMA");
  addTitle(s, "A moda é opaca por padrão.\nIsso está virando problema de negócio.", { h: 1.1, size: 22 });

  // Callout
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.35, y: 2.05, w: 9.3, h: 0.7,
    fill: { color: "0f1a12" },
    line: { color: "2d4a36", width: 0.7 },
    rectRadius: 0.08,
  });
  s.addText([
    { text: "Regulação EU ESPR (~2028): ", options: { bold: true, color: C.green } },
    { text: "toda peça têxtil vendida na Europa precisará ter passaporte digital com composição, origem e rastreabilidade.", options: { color: C.text } },
  ], { x: 0.55, y: 2.1, w: 9.0, h: 0.6, fontFace: FONT_BODY, fontSize: 10.5, valign: "middle", margin: 0 });

  // Two columns
  const leftItems = [
    "Ficha técnica no Excel ou papel",
    "Composição na cabeça do fornecedor",
    "Consumidor pergunta, marca não sabe",
    "Buyer europeu exige, marca perde contrato",
    "Certificação custa R$20–60k",
  ];
  const rightItems = [
    "Dados organizados em sistema único",
    "QR na etiqueta responde o que a marca sabe",
    "Status claro: declarado, calculado, verificado",
    "Buyer lê o link e fecha o pedido",
    "Começa em R$149 por peça",
  ];

  // Left card — bad
  card(s, 0.35, 2.87, 4.55, 2.5, { fill: "1a0a0a", borderColor: "4a2020" });
  s.addText("HOJE", { x: 0.53, y: 2.97, w: 1.2, h: 0.24, fontFace: FONT_BODY, fontSize: 8, color: C.red, charSpacing: 2, bold: true, margin: 0 });
  leftItems.forEach((item, i) => {
    s.addText([
      { text: "✗  ", options: { color: C.red, bold: true } },
      { text: item, options: { color: C.text } },
    ], { x: 0.5, y: 3.25 + i * 0.39, w: 4.2, h: 0.35, fontFace: FONT_BODY, fontSize: 10.5, margin: 0 });
  });

  // Right card — good
  card(s, 5.1, 2.87, 4.55, 2.5, { fill: "0a150d", borderColor: "2d4a36" });
  s.addText("COM PHYLLOS", { x: 5.28, y: 2.97, w: 2.5, h: 0.24, fontFace: FONT_BODY, fontSize: 8, color: C.green, charSpacing: 2, bold: true, margin: 0 });
  rightItems.forEach((item, i) => {
    s.addText([
      { text: "✓  ", options: { color: C.green, bold: true } },
      { text: item, options: { color: C.text } },
    ], { x: 5.25, y: 3.25 + i * 0.39, w: 4.2, h: 0.35, fontFace: FONT_BODY, fontSize: 10.5, margin: 0 });
  });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 3 — A SOLUÇÃO
// ─────────────────────────────────────────────────────────────────
function slide3(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 3, 8);
  addKicker(s, "03 · A SOLUÇÃO");
  addTitle(s, "PHYLLOS DPP Studio: arquivo técnico entra, passaporte sai.", { h: 0.72, size: 21 });

  s.addText("DPP = Digital Product Passport", {
    x: 0.4, y: 1.55, w: 9.2, h: 0.28, fontFace: FONT_BODY, fontSize: 10, color: C.muted, margin: 0,
  });

  // Callout box
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.35, y: 1.87, w: 9.3, h: 0.6,
    fill: { color: "0f1a12" }, line: { color: "2d4a36", width: 0.7 }, rectRadius: 0.08,
  });
  s.addText("Não é auditoria. Não é consultoria. É software que organiza o que a marca já sabe e publica com QR — sem prometer mais do que está documentado.", {
    x: 0.55, y: 1.9, w: 9.0, h: 0.54, fontFace: FONT_BODY, fontSize: 10, color: C.text, valign: "middle", italic: true, margin: 0,
  });

  // Table header
  const colX = [0.35, 3.85, 7.1];
  const colW = [3.45, 3.2, 2.55];
  const headers = ["O QUE A MARCA TRAZ", "O QUE A PHYLLOS ENTREGA", "STATUS"];
  headers.forEach((h2, i) => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: colX[i], y: 2.56, w: colW[i] - 0.05, h: 0.3,
      fill: { color: "1e1e1e" }, line: { color: C.border, width: 0.5 },
    });
    s.addText(h2, {
      x: colX[i] + 0.12, y: 2.56, w: colW[i] - 0.2, h: 0.3,
      fontFace: FONT_BODY, fontSize: 7.5, color: C.muted, charSpacing: 1.5, valign: "middle", bold: true, margin: 0,
    });
  });

  const rows = [
    ["Composição dos tecidos", "Campo verificável no passaporte", { text: "Declarado", color: C.accent }],
    ["Fornecedor + nota fiscal", "Rastreabilidade básica", { text: "Documentado", color: C.accent }],
    ["Peso da peça + gramatura", "Cálculo de água, carbono, energia", { text: "Calculado", color: C.green }],
    ["Certificado GOTS / OEKO-TEX", "Selo de verificação", { text: "Verificado", color: C.green }],
    ["Nada ainda", "Campo aparece como ausente — sem greenwashing", { text: "Ausente", color: C.muted }],
  ];

  rows.forEach((row, i) => {
    const ry = 2.86 + i * 0.48;
    const bg = i % 2 === 0 ? "161616" : "131313";
    // Row background spanning all cols
    s.addShape(pres.shapes.RECTANGLE, {
      x: 0.35, y: ry, w: 9.3, h: 0.45,
      fill: { color: bg }, line: { color: C.border, width: 0.3 },
    });
    s.addText(row[0], { x: colX[0]+0.12, y: ry+0.04, w: colW[0]-0.25, h: 0.38, fontFace: FONT_BODY, fontSize: 10.5, color: C.text, valign: "middle", margin: 0 });
    s.addText(row[1], { x: colX[1]+0.12, y: ry+0.04, w: colW[1]-0.25, h: 0.38, fontFace: FONT_BODY, fontSize: 10.5, color: C.muted, valign: "middle", margin: 0 });
    const st = row[2];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: colX[2]+0.1, y: ry+0.08, w: 1.5, h: 0.28,
      fill: { color: "1e1e1e" }, line: { color: C.border, width: 0.5 }, rectRadius: 0.14,
    });
    s.addText(st.text, {
      x: colX[2]+0.1, y: ry+0.08, w: 1.5, h: 0.28,
      fontFace: FONT_BODY, fontSize: 9, color: st.color, align: "center", valign: "middle", bold: true, margin: 0,
    });
  });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 4 — COMO FUNCIONA
// ─────────────────────────────────────────────────────────────────
function slide4(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 4, 8);
  addKicker(s, "04 · COMO FUNCIONA");
  addTitle(s, "Sete passos. Uma sessão de 60 minutos.\nUm passaporte digital pronto.", { h: 0.95, size: 21 });

  // Flow steps
  const steps = ["01\nFicha técnica", "02\nMaterial", "03\nLote", "04\nÁrea/perda", "05\nCálculo", "06\nEvidências", "07\nQR/Passaporte"];
  const stepW = 1.15;
  const arrowW = 0.18;
  const totalW = steps.length * stepW + (steps.length - 1) * arrowW;
  const startX = (W - totalW) / 2;

  steps.forEach((step, i) => {
    const sx = startX + i * (stepW + arrowW);
    const isLast = i === steps.length - 1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: sx, y: 2.12, w: stepW, h: 0.72,
      fill: { color: isLast ? "0f2018" : C.card },
      line: { color: isLast ? C.green : C.border, width: isLast ? 1.2 : 0.7 },
      rectRadius: 0.07,
    });
    const [num, name] = step.split("\n");
    s.addText([
      { text: num, options: { color: C.green, fontSize: 7.5, bold: true, breakLine: true } },
      { text: name, options: { color: isLast ? C.green : C.white, fontSize: 9, bold: isLast } },
    ], { x: sx, y: 2.12, w: stepW, h: 0.72, fontFace: FONT_BODY, align: "center", valign: "middle", margin: 0 });

    if (!isLast) {
      s.addText("→", {
        x: sx + stepW, y: 2.34, w: arrowW, h: 0.28,
        fontFace: FONT_BODY, fontSize: 12, color: C.border, align: "center", margin: 0,
      });
    }
  });

  // Two info cards
  const t1Items = ["Nome e código da peça", "Composição de fibras (%)", "País de fabricação", "Instruções de lavagem", "Orientação de descarte"];
  const t2Items = ["Gramatura + área → carbono calculado", "Fornecedor + NF → documentado", "Certificado GOTS → verificado"];

  card(s, 0.35, 3.0, 4.55, 2.38);
  s.addText("DADOS MÍNIMOS — TIER 1", { x: 0.53, y: 3.1, w: 4.2, h: 0.24, fontFace: FONT_BODY, fontSize: 7.5, color: C.muted, charSpacing: 1.5, bold: true, margin: 0 });
  t1Items.forEach((item, i) => {
    s.addText([
      { text: "✓  ", options: { color: C.green, bold: true } },
      { text: item, options: { color: C.text } },
    ], { x: 0.5, y: 3.38 + i * 0.36, w: 4.2, h: 0.33, fontFace: FONT_BODY, fontSize: 10, margin: 0 });
  });
  s.addText("→ QR gerado em ~45 min", { x: 0.5, y: 5.16, w: 4.2, h: 0.22, fontFace: FONT_BODY, fontSize: 9.5, color: C.green, bold: true, margin: 0 });

  card(s, 5.1, 3.0, 4.55, 2.38);
  s.addText("COM MAIS DADOS — TIER 2 / 3", { x: 5.28, y: 3.1, w: 4.2, h: 0.24, fontFace: FONT_BODY, fontSize: 7.5, color: C.muted, charSpacing: 1.5, bold: true, margin: 0 });
  t2Items.forEach((item, i) => {
    s.addText([
      { text: "+  ", options: { color: C.accent, bold: true } },
      { text: item, options: { color: C.text } },
    ], { x: 5.25, y: 3.38 + i * 0.52, w: 4.2, h: 0.45, fontFace: FONT_BODY, fontSize: 10.5, margin: 0 });
  });
  s.addText("Diferencial competitivo frente a quem só declara", { x: 5.25, y: 5.0, w: 4.2, h: 0.38, fontFace: FONT_BODY, fontSize: 9.5, color: C.muted, italic: true, margin: 0 });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 5 — MERCADO
// ─────────────────────────────────────────────────────────────────
function slide5(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 5, 8);
  addKicker(s, "05 · MERCADO");
  addTitle(s, "Um mercado global que vai ter que se adaptar de qualquer jeito.", { h: 0.7, size: 21 });

  // 3 big number cards
  const bigCards = [
    { label: "MARCAS INDEPENDENTES NO BRASIL", val: "~12.000", desc: "Com 1–5 SKUs ativas; as maiores já sentem pressão de buyers internacionais" },
    { label: "REGULAÇÃO EU OBRIGATÓRIA", val: "~2028", desc: "DPP têxtil exigido para vender na Europa. Cria urgência para exportadores" },
    { label: "POTENCIAL SaaS B2B — FASE 3", val: "USD 2,5M", desc: "ARR estimado com múltiplos clientes e API para plataformas" },
  ];
  bigCards.forEach((bc, i) => {
    const cx = 0.35 + i * 3.2;
    card(s, cx, 1.82, 3.0, 1.55);
    s.addText(bc.label, { x: cx+0.16, y: 1.92, w: 2.7, h: 0.24, fontFace: FONT_BODY, fontSize: 7, color: C.muted, charSpacing: 1.5, bold: true, margin: 0 });
    s.addText(bc.val, { x: cx+0.16, y: 2.16, w: 2.7, h: 0.55, fontFace: FONT_TITLE, fontSize: 28, color: C.white, bold: true, margin: 0 });
    s.addText(bc.desc, { x: cx+0.16, y: 2.7, w: 2.7, h: 0.64, fontFace: FONT_BODY, fontSize: 9.5, color: C.muted, margin: 0 });
  });

  // Bar chart - ARR progression
  s.addText("PROJEÇÃO DE ARR POR FASE", { x: 0.4, y: 3.52, w: 4, h: 0.22, fontFace: FONT_BODY, fontSize: 7.5, color: C.muted, charSpacing: 1.5, bold: true, margin: 0 });

  const bars = [
    { label: "Piloto", pct: 3,  val: "Gratuito" },
    { label: "Fase 1", pct: 12, val: "R$149–299/DPP" },
    { label: "Fase 2", pct: 30, val: "R$490/mês/marca" },
    { label: "Fase 3", pct: 100,val: "USD 400K–2,5M ARR" },
  ];
  const trackW = 4.2;
  bars.forEach((bar, i) => {
    const by = 3.82 + i * 0.4;
    s.addText(bar.label, { x: 0.4, y: by, w: 0.9, h: 0.32, fontFace: FONT_BODY, fontSize: 9.5, color: C.muted, align: "right", valign: "middle", margin: 0 });
    // Track
    s.addShape(pres.shapes.RECTANGLE, { x: 1.42, y: by+0.1, w: trackW, h: 0.14, fill: { color: "1e1e1e" }, line: { color: C.border, width: 0.3 } });
    // Fill
    const fillW = Math.max(0.1, trackW * bar.pct / 100);
    s.addShape(pres.shapes.RECTANGLE, { x: 1.42, y: by+0.1, w: fillW, h: 0.14, fill: { color: C.green }, line: { color: C.green, width: 0 } });
    s.addText(bar.val, { x: 5.72, y: by, w: 2.4, h: 0.32, fontFace: FONT_BODY, fontSize: 9.5, color: C.text, valign: "middle", margin: 0 });
  });

  // Analogy callout
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.35, y: 4.46, w: 9.3, h: 0.95,
    fill: { color: "0f1a12" }, line: { color: "2d4a36", width: 0.7 }, rectRadius: 0.08,
  });
  s.addText([
    { text: "Analogia: ", options: { bold: true, color: C.green } },
    { text: "Pense como o sistema de NF-e para o varejo. Antes da lei, ninguém usava. Quando a lei chegou, todo mundo precisou. ", options: { color: C.text } },
    { text: "A PHYLLOS quer ser a empresa que já está operando quando a lei apertar.", options: { color: C.white, bold: true } },
  ], { x: 0.55, y: 4.52, w: 9.0, h: 0.83, fontFace: FONT_BODY, fontSize: 10.5, valign: "middle", margin: 0 });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 6 — MODELO DE NEGÓCIO
// ─────────────────────────────────────────────────────────────────
function slide6(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 6, 8);
  addKicker(s, "06 · MODELO DE NEGÓCIO");
  addTitle(s, "Três rotas de receita, escalonáveis.", { h: 0.62, size: 24 });

  // Table
  const colX2 = [0.35, 2.9, 5.45, 7.65];
  const colW2 = [2.5, 2.5, 2.15, 1.9];
  const hdrs = ["MODELO", "PARA QUEM", "PREÇO", "QUANDO"];
  hdrs.forEach((h2, i) => {
    s.addShape(pres.shapes.RECTANGLE, { x: colX2[i], y: 1.72, w: colW2[i]-0.05, h: 0.3, fill: { color: "1e1e1e" }, line: { color: C.border, width: 0.5 } });
    s.addText(h2, { x: colX2[i]+0.12, y: 1.72, w: colW2[i]-0.2, h: 0.3, fontFace: FONT_BODY, fontSize: 7.5, color: C.muted, charSpacing: 1.5, bold: true, valign: "middle", margin: 0 });
  });

  const rows2 = [
    ["Por passaporte", "Marca com 1–3 SKUs testando", "R$149–299 / DPP", "Pós-piloto", C.green],
    ["Assinatura mensal", "Marca ativa, múltiplos SKUs", "R$490/mês (até 10 SKUs)", "Fase 2", C.accent],
    ["API / Plataforma", "Marketplace, buyer, B2B", "Contrato anual USD 20–200K", "Fase 3", C.muted],
  ];
  rows2.forEach((row, i) => {
    const ry2 = 2.02 + i * 0.6;
    const bg2 = i % 2 === 0 ? "161616" : "131313";
    s.addShape(pres.shapes.RECTANGLE, { x: 0.35, y: ry2, w: 9.3, h: 0.55, fill: { color: bg2 }, line: { color: C.border, width: 0.3 } });
    row.slice(0, 4).forEach((cell, j) => {
      const color = j === 0 ? C.white : j === 3 ? row[4] : C.text;
      s.addText(cell, { x: colX2[j]+0.12, y: ry2+0.05, w: colW2[j]-0.2, h: 0.45, fontFace: FONT_BODY, fontSize: 10.5, color, valign: "middle", bold: j === 0, margin: 0 });
    });
  });

  // Two highlight cards
  card(s, 0.35, 3.85, 4.55, 1.55);
  s.addText("CUSTO DE INFRAESTRUTURA HOJE", { x: 0.53, y: 3.95, w: 4.2, h: 0.22, fontFace: FONT_BODY, fontSize: 7, color: C.muted, charSpacing: 1.5, bold: true, margin: 0 });
  s.addText("R$0/mês", { x: 0.5, y: 4.17, w: 4.2, h: 0.55, fontFace: FONT_TITLE, fontSize: 34, color: C.green, bold: true, margin: 0 });
  s.addText("FastAPI + SQLite local + Claude Code.\nZero gasto fixo até ter usuário pagante.", { x: 0.5, y: 4.72, w: 4.2, h: 0.62, fontFace: FONT_BODY, fontSize: 10, color: C.muted, margin: 0 });

  card(s, 5.1, 3.85, 4.55, 1.55);
  s.addText("MARGEM MARGINAL", { x: 5.28, y: 3.95, w: 4.2, h: 0.22, fontFace: FONT_BODY, fontSize: 7, color: C.muted, charSpacing: 1.5, bold: true, margin: 0 });
  s.addText("~Zero", { x: 5.25, y: 4.17, w: 4.2, h: 0.55, fontFace: FONT_TITLE, fontSize: 34, color: C.accent, bold: true, margin: 0 });
  s.addText("Custo marginal próximo de zero por DPP gerado.\nCada novo cliente paga quase tudo de margem.", { x: 5.25, y: 4.72, w: 4.2, h: 0.62, fontFace: FONT_BODY, fontSize: 10, color: C.muted, margin: 0 });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 7 — ESTÁGIO ATUAL
// ─────────────────────────────────────────────────────────────────
function slide7(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 7, 8);
  addKicker(s, "07 · ESTÁGIO ATUAL");
  addTitle(s, "MVP construído. Piloto ativo. Primeiros DPPs reais em andamento.", { h: 0.7, size: 21 });

  const tl = [
    { date: "Junho 2026 — Concluído", title: "Backend DPP funcional", desc: "API FastAPI, endpoints de publicação, QR real e flashcards públicos", done: true },
    { date: "Junho 2026 — Concluído", title: "DPP Studio v0 — interface web", desc: "Fluxo de 7 etapas funcional no browser. Formulário guiado.", done: true },
    { date: "Julho 2026 — Agora", title: "Piloto assistido com 3–5 marcas", desc: "Sessão gratuita de 60 min. Marca sai com QR real e link público.", done: false, now: true },
    { date: "Q3 2026", title: "Primeira receita + decisão de modelo", desc: "Por DPP (R$149–299) ou assinatura (R$490/mês)", done: false },
    { date: "2027–2028", title: "API + SaaS B2B", desc: "Marketplace, plataformas e buyers como clientes. USD 400K–2,5M ARR.", done: false },
  ];

  const dotX = 0.55;
  const lineX = dotX + 0.065;
  const contentX = 0.9;
  const startY = 1.72;
  const rowH = 0.74;

  tl.forEach((item, i) => {
    const iy = startY + i * rowH;
    const dotColor = item.done ? C.green : item.now ? C.accent : C.border;
    // Dot
    s.addShape(pres.shapes.OVAL, { x: dotX, y: iy + 0.06, w: 0.13, h: 0.13, fill: { color: dotColor }, line: { color: dotColor, width: 0 } });
    // Vertical line (except last)
    if (i < tl.length - 1) {
      s.addShape(pres.shapes.LINE, { x: lineX, y: iy + 0.19, w: 0, h: rowH - 0.05, line: { color: C.border, width: 0.8 } });
    }
    s.addText(item.date, { x: contentX, y: iy, w: 8.7, h: 0.22, fontFace: FONT_BODY, fontSize: 8.5, color: item.now ? C.accent : C.muted, margin: 0 });
    s.addText(item.title, { x: contentX, y: iy + 0.21, w: 8.7, h: 0.24, fontFace: FONT_BODY, fontSize: 12, color: C.white, bold: true, margin: 0 });
    s.addText(item.desc, { x: contentX, y: iy + 0.44, w: 8.7, h: 0.26, fontFace: FONT_BODY, fontSize: 9.5, color: C.muted, margin: 0 });
  });
}

// ─────────────────────────────────────────────────────────────────
// SLIDE 8 — PRÓXIMOS PASSOS
// ─────────────────────────────────────────────────────────────────
function slide8(pres) {
  const s = pres.addSlide();
  s.pres = pres;
  s.background = { color: C.bg };
  addLogo(s);
  addSlideNum(s, 8, 8);
  addKicker(s, "08 · PRÓXIMOS PASSOS");
  addTitle(s, "Três decisões de go/no-go nos próximos 30 dias.", { h: 0.62, size: 24 });

  const cols = [
    {
      label: "GO",
      color: C.green,
      fill: "0a150d",
      border: "2d4a36",
      items: ["Marca traz Tier 1 em <45 min", "QR compartilhado no Instagram\nou com buyer", "Alguém usa o QR sem ser a marca"],
    },
    {
      label: "INVESTIGAR",
      color: C.accent,
      fill: "14100a",
      border: "4a3a1a",
      items: ["Onboarding passa de 90 min", "QR entregue mas não usado", "Confusão entre DPP e auditoria"],
    },
    {
      label: "PIVOTAR",
      color: C.red,
      fill: "140a0a",
      border: "4a2020",
      items: ["Ninguém traz dados em 90 min", "Valor citado é organização interna", "Exigem integração antes de adotar"],
    },
  ];

  cols.forEach((col, i) => {
    const cx2 = 0.35 + i * 3.22;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: cx2, y: 1.72, w: 3.05, h: 3.05,
      fill: { color: col.fill }, line: { color: col.border, width: 0.8 }, rectRadius: 0.1,
    });
    s.addText(col.label, { x: cx2+0.18, y: 1.82, w: 2.7, h: 0.34, fontFace: FONT_BODY, fontSize: 10, color: col.color, bold: true, charSpacing: 2, margin: 0 });
    col.items.forEach((item, j) => {
      s.addText(item, { x: cx2+0.18, y: 2.26 + j * 0.78, w: 2.7, h: 0.7, fontFace: FONT_BODY, fontSize: 11, color: C.text, margin: 0 });
    });
  });

  // Final quote
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.35, y: 4.88, w: 9.3, h: 0.62,
    fill: { color: "0f2018" }, line: { color: "2d4a36", width: 0.7 }, rectRadius: 0.08,
  });
  s.addText('"Você já sabe o que tem na sua peça. A PHYLLOS deixa qualquer pessoa descobrir isso com um QR."', {
    x: 0.55, y: 4.9, w: 9.0, h: 0.58,
    fontFace: FONT_TITLE, fontSize: 12.5, color: C.white, italic: true, valign: "middle", align: "center", margin: 0,
  });
}

// ─────────────────────────────────────────────────────────────────
// MAIN
// ─────────────────────────────────────────────────────────────────
(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "PHYLLOS";
  pres.title = "PHYLLOS — Apresentação para Empresário";
  pres.subject = "DPP Studio — Passaporte Digital para Moda";

  slide1(pres);
  slide2(pres);
  slide3(pres);
  slide4(pres);
  slide5(pres);
  slide6(pres);
  slide7(pres);
  slide8(pres);

  await pres.writeFile({ fileName: "outputs/phyllos-apresentacao.pptx" });
  console.log("✓ PPTX gerado: outputs/phyllos-apresentacao.pptx");
})();
