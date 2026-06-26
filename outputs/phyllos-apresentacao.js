const pptxgen = require("pptxgenjs");

const C = {
  bg:        "0d0d0d",
  card:      "1a1a1a",
  border:    "2a2a2a",
  green:     "4caf82",
  text:      "e8e8e0",
  muted:     "888888",
  accent:    "c9a96e",
  white:     "f5f5f0",
  red:       "c04040",
  darkGreen: "0f1a12",
  greenBorder: "2d4a36",
};
const FT = "Cambria";
const FB = "Calibri";
const W = 10, H = 5.625;
const TOTAL = 11;

function ms() { return { type:"outer", color:"000000", blur:8, offset:2, angle:45, opacity:0.28 }; }

function addLogo(s) {
  s.addText([
    { text:"Φ",        options:{ color:C.green, fontSize:13, bold:true } },
    { text:"  PHYLLOS ", options:{ color:C.white, fontSize:11 } },
    { text:"wear",     options:{ color:C.muted,  fontSize:9  } },
  ], { x:0.3, y:0.18, w:2.5, h:0.3, fontFace:FB, margin:0 });
}
function addNum(s, n) {
  s.addText(`${String(n).padStart(2,"0")} / ${String(TOTAL).padStart(2,"0")}`, {
    x:W-1.0, y:0.18, w:0.7, h:0.24, fontFace:FB, fontSize:9, color:C.muted, align:"right", margin:0,
  });
}
function addKicker(s, txt) {
  s.addText(txt, { x:0.4, y:0.6, w:9.2, h:0.22, fontFace:FB, fontSize:8.5, color:C.green, charSpacing:3, margin:0 });
}
function addTitle(s, txt, opts={}) {
  s.addText(txt, { x:0.4, y:0.82, w:9.2, h:opts.h||0.82, fontFace:FT, fontSize:opts.sz||25, color:C.white, bold:true, margin:0, ...opts });
}
function rr(s, x,y,w,h, fill, border, r=0.08) {
  s.addShape(s.pres.shapes.ROUNDED_RECTANGLE, { x,y,w,h,
    fill:{ color:fill }, line:{ color:border, width:0.7 }, rectRadius:r, shadow:ms() });
}

// ── SLIDE 1 ── O QUE É ────────────────────────────────────────────
function s1(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,1); addKicker(s,"01 · O QUE É A PHYLLOS");

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:0.78,w:9.3,h:1.95,
    fill:{ color:C.darkGreen }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.1 });
  s.addText("Φ", { x:7.8,y:0.7,w:1.8,h:1.6, fontFace:FT, fontSize:110, color:"1e3a22",
    align:"center", valign:"middle", margin:0 });
  s.addText([
    { text:"A PHYLLOS cria o ", options:{ color:C.text } },
    { text:"passaporte digital", options:{ color:C.green, bold:true } },
    { text:" das roupas.\n", options:{ color:C.text } },
    { text:"Cada peça ganha um QR: origem, composição e impacto — com um escaneamento.", options:{ color:C.muted } },
  ], { x:0.55,y:0.88,w:7.3,h:1.7, fontFace:FT, fontSize:16, margin:0 });

  ["SaaS B2B","Moda + Regulação","Brasil → Europa","2026"].forEach((t,i) => {
    const tx = 0.35 + i*2.35;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:tx,y:2.82,w:2.2,h:0.3,
      fill:{ color:"101a12" }, line:{ color:C.greenBorder, width:0.6 }, rectRadius:0.15 });
    s.addText(t, { x:tx,y:2.82,w:2.2,h:0.3, fontFace:FB, fontSize:8.5, color:C.green, align:"center", valign:"middle", margin:0 });
  });

  const cards = [
    { l:"QUEM PAGA",          v:"Marcas de Moda",  d:"Independentes, ateliês,\npequenas e médias" },
    { l:"O QUE ENTREGAMOS",   v:"QR + Passaporte", d:"Página pública com dados\nverificáveis por peça" },
    { l:"POR QUE AGORA",      v:"Lei em vigor",    d:"UE exige DPP têxtil\nobrigatório ~2028" },
  ];
  cards.forEach((c,i) => {
    const cx=0.35+i*3.2;
    rr(s,cx,3.22,3.0,2.1, C.card, C.border);
    s.addText(c.l, { x:cx+0.18,y:3.32,w:2.65,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:2, margin:0 });
    s.addText(c.v, { x:cx+0.18,y:3.54,w:2.65,h:0.42, fontFace:FT, fontSize:17, color:C.white, bold:true, margin:0 });
    s.addText(c.d, { x:cx+0.18,y:3.96,w:2.65,h:1.2,  fontFace:FB, fontSize:11, color:C.muted, margin:0 });
  });
}

// ── SLIDE 2 ── O PROBLEMA ─────────────────────────────────────────
function s2(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,2); addKicker(s,"02 · O PROBLEMA");
  addTitle(s,"A moda é opaca por padrão.\nIsso está virando problema de negócio.", { h:1.05, sz:22 });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:2.0,w:9.3,h:0.68,
    fill:{ color:C.darkGreen }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.08 });
  s.addText([
    { text:"Regulação EU ESPR (~2028): ", options:{ bold:true, color:C.green } },
    { text:"toda peça têxtil vendida na Europa precisará ter passaporte digital com composição, origem e rastreabilidade.", options:{ color:C.text } },
  ], { x:0.55,y:2.05,w:9.0,h:0.58, fontFace:FB, fontSize:10.5, valign:"middle", margin:0 });

  const left  = ["Ficha técnica no Excel ou papel","Composição na cabeça do fornecedor","Consumidor pergunta, marca não sabe","Buyer europeu exige, marca perde contrato","Certificação custa R$20–60k"];
  const right = ["Dados organizados em sistema único","QR na etiqueta responde o que a marca sabe","Status claro: declarado, calculado, verificado","Buyer lê o link e fecha o pedido","Começa em R$149 por peça"];

  rr(s,0.35,2.82,4.55,2.52, "1a0a0a","4a2020");
  s.addText("HOJE",        { x:0.53,y:2.92,w:1.2,h:0.24, fontFace:FB, fontSize:8, color:C.red, charSpacing:2, bold:true, margin:0 });
  left.forEach((it,i) => s.addText([{ text:"✗  ", options:{ color:C.red, bold:true } },{ text:it, options:{ color:C.text } }],
    { x:0.5,y:3.22+i*0.39,w:4.2,h:0.35, fontFace:FB, fontSize:10.5, margin:0 }));

  rr(s,5.1,2.82,4.55,2.52, "0a150d","2d4a36");
  s.addText("COM PHYLLOS", { x:5.28,y:2.92,w:2.5,h:0.24, fontFace:FB, fontSize:8, color:C.green, charSpacing:2, bold:true, margin:0 });
  right.forEach((it,i) => s.addText([{ text:"✓  ", options:{ color:C.green, bold:true } },{ text:it, options:{ color:C.text } }],
    { x:5.25,y:3.22+i*0.39,w:4.2,h:0.35, fontFace:FB, fontSize:10.5, margin:0 }));
}

// ── SLIDE 3 ── A SOLUÇÃO ──────────────────────────────────────────
function s3(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,3); addKicker(s,"03 · A SOLUÇÃO");
  addTitle(s,"PHYLLOS DPP Studio: arquivo técnico entra, passaporte sai.", { h:0.7, sz:21 });
  s.addText("DPP = Digital Product Passport", { x:0.4,y:1.54,w:9.2,h:0.26, fontFace:FB, fontSize:10, color:C.muted, margin:0 });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:1.85,w:9.3,h:0.58,
    fill:{ color:C.darkGreen }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.08 });
  s.addText("Não é auditoria. Não é consultoria. É software que organiza o que a marca já sabe e publica com QR — sem prometer mais do que está documentado.", {
    x:0.55,y:1.88,w:9.0,h:0.52, fontFace:FB, fontSize:10, color:C.text, italic:true, valign:"middle", margin:0 });

  const cX=[0.35,3.85,7.1], cW=[3.45,3.2,2.55];
  ["O QUE A MARCA TRAZ","O QUE A PHYLLOS ENTREGA","STATUS"].forEach((h,i) => {
    s.addShape(pres.shapes.RECTANGLE, { x:cX[i],y:2.55,w:cW[i]-0.05,h:0.29, fill:{ color:"1e1e1e" }, line:{ color:C.border, width:0.5 } });
    s.addText(h, { x:cX[i]+0.12,y:2.55,w:cW[i]-0.2,h:0.29, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, valign:"middle", margin:0 });
  });

  const rows=[
    ["Composição dos tecidos","Campo verificável no passaporte",{t:"Declarado",c:C.accent}],
    ["Fornecedor + nota fiscal","Rastreabilidade básica",       {t:"Documentado",c:C.accent}],
    ["Peso da peça + gramatura","Cálculo de água, carbono, energia",{t:"Calculado",c:C.green}],
    ["Certificado GOTS/OEKO-TEX","Selo de verificação independente",{t:"Verificado",c:C.green}],
    ["Nada ainda","Campo aparece como ausente — sem greenwashing",{t:"Ausente",c:C.muted}],
  ];
  rows.forEach((r,i) => {
    const ry=2.84+i*0.47, bg=i%2===0?"161616":"131313";
    s.addShape(pres.shapes.RECTANGLE, { x:0.35,y:ry,w:9.3,h:0.44, fill:{ color:bg }, line:{ color:C.border, width:0.3 } });
    s.addText(r[0], { x:cX[0]+0.12,y:ry+0.04,w:cW[0]-0.25,h:0.36, fontFace:FB, fontSize:10.5, color:C.text,  valign:"middle", margin:0 });
    s.addText(r[1], { x:cX[1]+0.12,y:ry+0.04,w:cW[1]-0.25,h:0.36, fontFace:FB, fontSize:10.5, color:C.muted, valign:"middle", margin:0 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:cX[2]+0.1,y:ry+0.08,w:1.5,h:0.27, fill:{ color:"1e1e1e" }, line:{ color:C.border, width:0.5 }, rectRadius:0.14 });
    s.addText(r[2].t, { x:cX[2]+0.1,y:ry+0.08,w:1.5,h:0.27, fontFace:FB, fontSize:9, color:r[2].c, align:"center", valign:"middle", bold:true, margin:0 });
  });
}

// ── SLIDE 4 ── COMO FUNCIONA ──────────────────────────────────────
function s4(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,4); addKicker(s,"04 · COMO FUNCIONA");
  addTitle(s,"Sete passos. Uma sessão de 60 minutos.\nUm passaporte digital pronto.", { h:0.92, sz:21 });

  const steps=["01\nFicha técnica","02\nMaterial","03\nLote","04\nÁrea/perda","05\nCálculo","06\nEvidências","07\nQR/Passaporte"];
  const sw=1.15, aw=0.18;
  const sx0=(W-(steps.length*sw+(steps.length-1)*aw))/2;
  steps.forEach((st,i) => {
    const x=sx0+i*(sw+aw), last=i===steps.length-1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x,y:2.1,w:sw,h:0.72,
      fill:{ color:last?"0f2018":C.card }, line:{ color:last?C.green:C.border, width:last?1.2:0.7 }, rectRadius:0.07 });
    const [n,nm]=st.split("\n");
    s.addText([
      { text:n,  options:{ color:C.green, fontSize:7.5, bold:true, breakLine:true } },
      { text:nm, options:{ color:last?C.green:C.white, fontSize:9, bold:last } },
    ], { x,y:2.1,w:sw,h:0.72, fontFace:FB, align:"center", valign:"middle", margin:0 });
    if (!last) s.addText("→", { x:x+sw,y:2.32,w:aw,h:0.28, fontFace:FB, fontSize:12, color:C.border, align:"center", margin:0 });
  });

  const t1=["Nome e código da peça","Composição de fibras (%)","País de fabricação","Instruções de lavagem","Orientação de descarte"];
  const t2=["Gramatura + área → carbono calculado","Fornecedor + NF → documentado","Certificado GOTS → verificado"];
  rr(s,0.35,2.98,4.55,2.4, C.card, C.border);
  s.addText("DADOS MÍNIMOS — TIER 1", { x:0.53,y:3.08,w:4.2,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  t1.forEach((it,i) => s.addText([{ text:"✓  ", options:{ color:C.green, bold:true } },{ text:it, options:{ color:C.text } }],
    { x:0.5,y:3.36+i*0.36,w:4.2,h:0.33, fontFace:FB, fontSize:10, margin:0 }));
  s.addText("→ QR gerado em ~45 min", { x:0.5,y:5.15,w:4.2,h:0.22, fontFace:FB, fontSize:9.5, color:C.green, bold:true, margin:0 });

  rr(s,5.1,2.98,4.55,2.4, C.card, C.border);
  s.addText("COM MAIS DADOS — TIER 2/3", { x:5.28,y:3.08,w:4.2,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  t2.forEach((it,i) => s.addText([{ text:"+  ", options:{ color:C.accent, bold:true } },{ text:it, options:{ color:C.text } }],
    { x:5.25,y:3.36+i*0.52,w:4.2,h:0.45, fontFace:FB, fontSize:10.5, margin:0 }));
  s.addText("Diferencial competitivo frente a quem só declara", { x:5.25,y:4.98,w:4.2,h:0.36, fontFace:FB, fontSize:9.5, color:C.muted, italic:true, margin:0 });
}

// ── SLIDE 5 ── MERCADO ────────────────────────────────────────────
function s5(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,5); addKicker(s,"05 · MERCADO");
  addTitle(s,"Um mercado global que vai ter que se adaptar de qualquer jeito.", { h:0.68, sz:21 });

  [{ l:"MARCAS INDEPENDENTES BR",v:"~12.000",d:"Com 1–5 SKUs ativas. As maiores já sentem\npressão de buyers internacionais." },
   { l:"REGULAÇÃO EU OBRIGATÓRIA", v:"~2028",  d:"DPP têxtil exigido para vender na Europa.\nCAGR de mercado DPP: 45,7% até 2030." },
   { l:"POTENCIAL SaaS B2B — FASE 3",v:"USD 2,5M",d:"ARR estimado com múltiplos clientes e\nAPI para plataformas e buyers." },
  ].forEach((bc,i) => {
    const cx=0.35+i*3.2;
    rr(s,cx,1.8,3.0,1.6, C.card, C.border);
    s.addText(bc.l, { x:cx+0.16,y:1.9,w:2.7,h:0.24, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
    s.addText(bc.v, { x:cx+0.16,y:2.14,w:2.7,h:0.56, fontFace:FT, fontSize:28, color:C.white, bold:true, margin:0 });
    s.addText(bc.d, { x:cx+0.16,y:2.7,w:2.7,h:0.66, fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });
  });

  s.addText("PROJEÇÃO DE ARR POR FASE", { x:0.4,y:3.52,w:4,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  [{ l:"Piloto",pct:3,  v:"Gratuito" },
   { l:"Fase 1",pct:12, v:"R$149–299/DPP" },
   { l:"Fase 2",pct:30, v:"R$490/mês/marca" },
   { l:"Fase 3",pct:100,v:"USD 400K–2,5M ARR" },
  ].forEach((b,i) => {
    const by=3.82+i*0.4;
    s.addText(b.l, { x:0.4,y:by,w:0.9,h:0.32, fontFace:FB, fontSize:9.5, color:C.muted, align:"right", valign:"middle", margin:0 });
    s.addShape(pres.shapes.RECTANGLE, { x:1.42,y:by+0.1,w:4.2,h:0.14, fill:{ color:"1e1e1e" }, line:{ color:C.border, width:0.3 } });
    s.addShape(pres.shapes.RECTANGLE, { x:1.42,y:by+0.1,w:Math.max(0.1,4.2*b.pct/100),h:0.14, fill:{ color:C.green }, line:{ color:C.green, width:0 } });
    s.addText(b.v, { x:5.72,y:by,w:2.4,h:0.32, fontFace:FB, fontSize:9.5, color:C.text, valign:"middle", margin:0 });
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:4.46,w:9.3,h:0.95,
    fill:{ color:C.darkGreen }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.08 });
  s.addText([
    { text:"Analogia: ", options:{ bold:true, color:C.green } },
    { text:"Pense como o NF-e para o varejo. Antes da lei, ninguém usava. Quando a lei chegou, todo mundo precisou. ", options:{ color:C.text } },
    { text:"A PHYLLOS quer ser a empresa que já está operando quando a lei apertar.", options:{ color:C.white, bold:true } },
  ], { x:0.55,y:4.52,w:9.0,h:0.83, fontFace:FB, fontSize:10.5, valign:"middle", margin:0 });
}

// ── SLIDE 6 ── MODELO DE NEGÓCIO (dados reais de infra) ───────────
function s6(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,6); addKicker(s,"06 · MODELO DE NEGÓCIO");
  addTitle(s,"Três rotas de receita. Margens de software puro.", { h:0.62, sz:23 });

  const cX=[0.35,2.9,5.45,7.65], cW=[2.5,2.5,2.15,1.9];
  ["MODELO","PARA QUEM","PREÇO","QUANDO"].forEach((h,i) => {
    s.addShape(pres.shapes.RECTANGLE, { x:cX[i],y:1.7,w:cW[i]-0.05,h:0.3, fill:{ color:"1e1e1e" }, line:{ color:C.border, width:0.5 } });
    s.addText(h, { x:cX[i]+0.12,y:1.7,w:cW[i]-0.2,h:0.3, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, valign:"middle", margin:0 });
  });
  [
    ["Por passaporte", "Marca com 1–3 SKUs testando",  "R$149–299 / DPP",           "Pós-piloto",  C.green ],
    ["Assinatura mensal","Marca ativa, múltiplos SKUs","R$490/mês (até 10 SKUs)",   "Fase 2",      C.accent],
    ["API / Plataforma","Marketplace, buyer, B2B",      "Contrato anual USD 20–200K","Fase 3",      C.muted ],
  ].forEach((r,i) => {
    const ry=2.0+i*0.58, bg=i%2===0?"161616":"131313";
    s.addShape(pres.shapes.RECTANGLE, { x:0.35,y:ry,w:9.3,h:0.54, fill:{ color:bg }, line:{ color:C.border, width:0.3 } });
    r.slice(0,4).forEach((c,j) => s.addText(c, { x:cX[j]+0.12,y:ry+0.05,w:cW[j]-0.2,h:0.44,
      fontFace:FB, fontSize:10.5, color:j===0?C.white:j===3?r[4]:C.text, valign:"middle", bold:j===0, margin:0 }));
  });

  rr(s,0.35,3.82,2.18,1.58, C.card, C.border);
  s.addText("CUSTO INFRA — PILOTO", { x:0.53,y:3.92,w:1.85,h:0.22, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  s.addText("R$27,50/mês", { x:0.48,y:4.12,w:1.95,h:0.5, fontFace:FT, fontSize:21, color:C.green, bold:true, margin:0 });
  s.addText("Railway Hobby: crédito de uso\ncobre workloads leves.", { x:0.48,y:4.62,w:1.95,h:0.72, fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });

  rr(s,2.65,3.82,2.18,1.58, C.card, C.border);
  s.addText("STEP-FUNCTION OUT/2026", { x:2.83,y:3.92,w:1.85,h:0.22, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  s.addText("R$253/mês", { x:2.78,y:4.12,w:1.95,h:0.5, fontFace:FT, fontSize:21, color:C.accent, bold:true, margin:0 });
  s.addText("Railway Pro + Supabase Pro\nao ativar 1º cliente pagante.", { x:2.78,y:4.62,w:1.95,h:0.72, fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });

  rr(s,4.95,3.82,2.18,1.58, C.card, C.border);
  s.addText("MARGEM BRUTA POR DPP", { x:5.13,y:3.92,w:1.85,h:0.22, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  s.addText("99,9%", { x:5.08,y:4.12,w:1.95,h:0.5, fontFace:FT, fontSize:28, color:C.green, bold:true, margin:0 });
  s.addText("COGS: R$0,01/passaporte.\nInfra nunca comprime margem.", { x:5.08,y:4.62,w:1.95,h:0.72, fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });

  rr(s,7.25,3.82,2.38,1.58, C.card, C.border);
  s.addText("EBITDA 2027 (REVISADO)", { x:7.43,y:3.92,w:2.05,h:0.22, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  s.addText("65,5%", { x:7.38,y:4.12,w:2.05,h:0.5, fontFace:FT, fontSize:28, color:C.green, bold:true, margin:0 });
  s.addText("Revisado com infra real.\nEra 62% na estimativa anterior.", { x:7.38,y:4.62,w:2.05,h:0.72, fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });
}

// ── SLIDE 7 ── ANÁLISE FINANCEIRA ─────────────────────────────────
function s7(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,7); addKicker(s,"07 · ANÁLISE FINANCEIRA");
  addTitle(s,"Investimento mínimo. Retorno assimétrico. Breakeven em 9 meses.", { h:0.7, sz:21 });

  [{ l:"INVESTIMENTO DIRETO TOTAL",  v:"R$4.440",   d:"Até 1º cliente pagante\n(Claude Code + infra + domínio)",   c:C.accent },
   { l:"BREAKEVEN OPERACIONAL",      v:"Mar/2027",   d:"9 meses após cobrar\nFCL acumulado > 0",                   c:C.green  },
   { l:"VPL A 5 ANOS · 25% a.a.",   v:"R$869K",     d:"Cenário base\nTaxa de startup early-stage BR",             c:C.green  },
   { l:"LTV / CAC — ASSINATURA",     v:"19,6×",      d:"Meta SaaS saudável é > 3×\nCAC payback: 1 mês",           c:C.green  },
  ].forEach((k,i) => {
    const kx=0.35+i*2.42;
    rr(s,kx,1.8,2.28,1.48, C.card, C.border);
    s.addText(k.l, { x:kx+0.15,y:1.9,w:2.0,h:0.24, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
    s.addText(k.v, { x:kx+0.15,y:2.12,w:2.0,h:0.52, fontFace:FT, fontSize:26, color:k.c, bold:true, margin:0 });
    s.addText(k.d, { x:kx+0.15,y:2.64,w:2.0,h:0.6,  fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });
  });

  s.addText("TIR (IRR) POR CENÁRIO", { x:0.4,y:3.42,w:4,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, margin:0 });
  [{ l:"Conservador",v:"~180% a.a.",  sub:"Payback 22 meses · VPL R$159K", fill:"14100a",bdr:"4a3a1a", vc:C.accent },
   { l:"Base",       v:"~850% a.a.",  sub:"Payback 9 meses · VPL R$869K",  fill:"0a150d",bdr:"2d4a36", vc:C.green  },
   { l:"Otimista",   v:">2.000% a.a.",sub:"Payback 6 meses · VPL R$4,5M",  fill:"0a1814",bdr:"1d6e56", vc:C.green  },
  ].forEach((sc,i) => {
    const cx=0.35+i*3.22;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:cx,y:3.7,w:3.05,h:1.72,
      fill:{ color:sc.fill }, line:{ color:sc.bdr, width:0.8 }, rectRadius:0.1 });
    s.addText(sc.l.toUpperCase(), { x:cx+0.18,y:3.8,w:2.7,h:0.22, fontFace:FB, fontSize:8, color:sc.vc, charSpacing:2, bold:true, margin:0 });
    s.addText(sc.v, { x:cx+0.18,y:4.02,w:2.7,h:0.52, fontFace:FT, fontSize:24, color:sc.vc, bold:true, margin:0 });
    s.addText(sc.sub, { x:cx+0.18,y:4.54,w:2.7,h:0.82, fontFace:FB, fontSize:10, color:C.muted, margin:0 });
  });

  s.addText("TIR elevada reflete investimento inicial próximo de zero — não ausência de risco. O risco real é de execução e validação de mercado.", {
    x:0.4,y:5.38,w:9.2,h:0.22, fontFace:FB, fontSize:9, color:C.muted, italic:true, margin:0 });
}

// ── SLIDE 8 ── VALUATION E CAPTAÇÃO ──────────────────────────────
function s8(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,8); addKicker(s,"08 · VALUATION E CAPTAÇÃO");
  addTitle(s,"Não captar antes do breakeven. Quando captar, com poder de barganha.", { h:0.7, sz:20 });

  [{ l:"FLOOR · PRÉ-PILOTO",      v:"R$3M",  sub:"Pré Out/2026 · discount 25–30%\nSem ARR comprovado",      fill:"14100a",bdr:"4a3a1a",vc:C.accent },
   { l:"BASE · PÓS 1º CLIENTE",   v:"R$5M",  sub:"Após Out/2026 · discount 20%\n1 cliente pagante confirmado",fill:"0a150d",bdr:"2d4a36",vc:C.green },
   { l:"OTIMISTA · PÓS ARR",      v:"R$8M",  sub:"ARR > R$50K + Q1/2027\nLTV/CAC > 10× medido",            fill:"0a1814",bdr:"1d6e56",vc:C.green },
  ].forEach((vc,i) => {
    const cx=0.35+i*3.22;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:cx,y:1.7,w:3.05,h:1.88,
      fill:{ color:vc.fill }, line:{ color:vc.bdr, width:0.8 }, rectRadius:0.1 });
    s.addText(vc.l, { x:cx+0.18,y:1.8,w:2.7,h:0.24, fontFace:FB, fontSize:7.5, color:vc.vc, charSpacing:1.5, bold:true, margin:0 });
    s.addText(vc.v, { x:cx+0.18,y:2.04,w:2.7,h:0.6,  fontFace:FT, fontSize:34, color:vc.vc, bold:true, margin:0 });
    s.addText(vc.sub, { x:cx+0.18,y:2.64,w:2.7,h:0.9, fontFace:FB, fontSize:10.5, color:C.muted, margin:0 });
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:3.72,w:9.3,h:0.62,
    fill:{ color:C.darkGreen }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.08 });
  s.addText([
    { text:"Comparável: ", options:{ bold:true, color:C.green } },
    { text:"Retraced (DPP compliance de moda, Europa) captou EUR 15M Série A com ~USD 3,2M ARR → ", options:{ color:C.text } },
    { text:"múltiplo de 15× ARR.", options:{ bold:true, color:C.white } },
    { text:" DPP market CAGR 45,7% até 2030.", options:{ color:C.muted } },
  ], { x:0.55,y:3.76,w:9.0,h:0.54, fontFace:FB, fontSize:10, valign:"middle", margin:0 });

  const cX2=[0.35,2.9,5.45,7.65], cW2=[2.5,2.5,2.15,1.9];
  ["MOMENTO","CONDIÇÃO","QUANTO","INSTRUMENTO"].forEach((h,i) => {
    s.addShape(pres.shapes.RECTANGLE, { x:cX2[i],y:4.45,w:cW2[i]-0.05,h:0.27, fill:{ color:"1e1e1e" }, line:{ color:C.border, width:0.5 } });
    s.addText(h, { x:cX2[i]+0.1,y:4.45,w:cW2[i]-0.18,h:0.27, fontFace:FB, fontSize:7, color:C.muted, charSpacing:1.5, bold:true, valign:"middle", margin:0 });
  });
  [["Antes Mar/2027","Apenas se B2B urgente exigir dev","R$100–200K","Exceção"],
   ["Pós Mar/2027","ARR>R$80K + LTV/CAC>5×","R$300–600K","SAFE · cap R$5M"],
   ["Pós Dez/2027","ARR>R$150K + churn<5%","R$1–2M","Série A · equity"],
  ].forEach((r,i) => {
    const ry=4.72+i*0.27, bg=i%2===0?"161616":"131313";
    s.addShape(pres.shapes.RECTANGLE, { x:0.35,y:ry,w:9.3,h:0.26, fill:{ color:bg }, line:{ color:C.border, width:0.3 } });
    r.forEach((c,j) => s.addText(c, { x:cX2[j]+0.1,y:ry+0.03,w:cW2[j]-0.18,h:0.2,
      fontFace:FB, fontSize:9.5, color:j===0?C.white:C.text, valign:"middle", bold:j===0, margin:0 }));
  });
}

// ── SLIDE 9 ── PROTEÇÃO DE PI ─────────────────────────────────────
function s9(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,9); addKicker(s,"09 · PROTEÇÃO DE PROPRIEDADE INTELECTUAL");
  addTitle(s,"Trade secret é a proteção primária. Patente de software é caminho errado.", { h:0.7, sz:20 });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:1.7,w:9.3,h:0.55,
    fill:{ color:"140a0a" }, line:{ color:"4a2020", width:0.7 }, rectRadius:0.08 });
  s.addText([
    { text:"EU AI Act Art. 50 — deadline: 2 de agosto de 2026. ", options:{ bold:true, color:C.red } },
    { text:"Interfaces conversacionais de IA devem informar o usuário. Fichas técnicas geradas por IA precisam de marcação. Penalidade: EUR 35M ou 7% do faturamento global.", options:{ color:C.text } },
  ], { x:0.55,y:1.74,w:9.0,h:0.47, fontFace:FB, fontSize:9.5, valign:"middle", margin:0 });

  const actions=[
    { n:"1", t:"IP Assignment + NDA",              d:"Todo colaborador antes de qualquer conversa externa.\nSem isso a PI pode ser disputada em due diligence.", custo:"R$3–7K",   prazo:"Imediato", c:C.red    },
    { n:"2", t:"Registro de marca INPI",            d:"PHYLLOS classes 25+42, Fashion OS 35+42.\nPrograma prioritário INPI — janela fecha agosto/2026.", custo:"R$6–10K",  prazo:"Agosto/2026",c:C.red },
    { n:"3", t:"Registro de software INPI",         d:"Fashion OS e AAO no e-Software.\nCria prova datada admissível em litígio. Código criptografado.", custo:"R$500–2K", prazo:"7 dias",   c:C.accent },
    { n:"4", t:"Conformidade EU AI Act",            d:"Cláusulas nos Termos de Serviço antes de\nonboarding de cliente europeu. Deadline 02/08/2026.",    custo:"R$2–5K",   prazo:"02/08/2026",c:C.red   },
    { n:"5", t:"Canary data no corpus PLC",         d:"5–10 termos sentinela fabricados. Se aparecerem\nem concorrente: evidência direta de cópia.",         custo:"Zero",     prazo:"Imediato", c:C.green  },
    { n:"6", t:"Secrets em vault (Railway Secrets)","d":"System prompts dos 51 agentes em banco criptografado.\nAPI keys fora de código-fonte.",              custo:"Zero",     prazo:"Imediato", c:C.green  },
  ];
  actions.forEach((a,i) => {
    const col=i%3, row=Math.floor(i/3);
    const cx=0.35+col*3.22, cy=2.38+row*1.4;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:cx,y:cy,w:3.05,h:1.3,
      fill:{ color:C.card }, line:{ color:C.border, width:0.7 }, rectRadius:0.08 });
    s.addText([
      { text:a.n+". ", options:{ color:C.green, bold:true } },
      { text:a.t,      options:{ color:C.white, bold:true } },
    ], { x:cx+0.14,y:cy+0.1,w:2.78,h:0.26, fontFace:FB, fontSize:10.5, margin:0 });
    s.addText(a.d, { x:cx+0.14,y:cy+0.36,w:2.78,h:0.56, fontFace:FB, fontSize:9, color:C.muted, margin:0 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:cx+0.14,y:cy+0.94,w:0.9,h:0.24, fill:{ color:"1e1e1e" }, line:{ color:C.border, width:0.5 }, rectRadius:0.12 });
    s.addText(a.custo, { x:cx+0.14,y:cy+0.94,w:0.9,h:0.24, fontFace:FB, fontSize:8.5, color:a.c, align:"center", valign:"middle", bold:true, margin:0 });
    s.addText(a.prazo, { x:cx+1.1,y:cy+0.96,w:1.8,h:0.2, fontFace:FB, fontSize:9, color:C.muted, margin:0 });
  });
}

// ── SLIDE 10 ── ESTÁGIO ATUAL ─────────────────────────────────────
function s10(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,10); addKicker(s,"10 · ESTÁGIO ATUAL E DECISÕES DO BOARD");
  addTitle(s,"MVP construído. Board deliberou. Piloto em agosto.", { h:0.68, sz:22 });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:1.72,w:4.55,h:3.75, fill:{ color:C.card }, line:{ color:C.border, width:0.7 }, rectRadius:0.1 });
  s.addText("TIMELINE", { x:0.53,y:1.82,w:4.2,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, margin:0 });

  const tl=[
    { d:"Jun/2026 — Concluído",  t:"Backend DPP + Studio v0",        desc:"API + QR real + interface 7 etapas", done:true },
    { d:"Jun/2026 — Concluído",  t:"Análise financeira + board",      desc:"CFO model + 4 deliberações formais", done:true },
    { d:"Jul/2026 — Agora",      t:"Recrutamento das marcas",         desc:"DM para 5 marcas. Meta: 3 em 48h",  now:true  },
    { d:"Ago/2026",              t:"Piloto assistido 3–5 marcas",     desc:"60 min/sessão. Custo: R$27,50/mês", future:true },
    { d:"Out/2026",              t:"1º cliente pagante",              desc:"Infra sobe para R$253/mês",          future:true },
    { d:"Mar/2027",              t:"Breakeven operacional",           desc:"FCL acumulado > 0. Valuation R$5M",  future:true },
  ];
  tl.forEach((it,i) => {
    const iy=2.1+i*0.54, dc=it.done?"4caf82":it.now?"c9a96e":C.border;
    s.addShape(pres.shapes.OVAL, { x:0.53,y:iy+0.05,w:0.11,h:0.11, fill:{ color:dc }, line:{ color:dc, width:0 } });
    if(i<tl.length-1) s.addShape(pres.shapes.LINE, { x:0.585,y:iy+0.16,w:0,h:0.38, line:{ color:C.border, width:0.8 } });
    s.addText(it.d, { x:0.73,y:iy,w:4.0,h:0.2, fontFace:FB, fontSize:8.5, color:it.now?C.accent:C.muted, margin:0 });
    s.addText(it.t, { x:0.73,y:iy+0.19,w:4.0,h:0.2, fontFace:FB, fontSize:11.5, color:C.white, bold:true, margin:0 });
    s.addText(it.desc, { x:0.73,y:iy+0.38,w:4.0,h:0.16, fontFace:FB, fontSize:9, color:C.muted, margin:0 });
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:5.05,y:1.72,w:4.58,h:3.75, fill:{ color:C.card }, line:{ color:C.border, width:0.7 }, rectRadius:0.1 });
  s.addText("DELIBERAÇÕES DO BOARD — 25 JUN 2026", { x:5.22,y:1.82,w:4.2,h:0.22, fontFace:FB, fontSize:7.5, color:C.muted, charSpacing:1.5, bold:true, margin:0 });

  [{ n:"01", t:"Go-on do piloto em agosto/2026",        d:"Data deslocada de julho → agosto.\nCritérios de go/no-go inalterados.",         ok:true },
   { n:"02", t:"Seguir recomendação do CFO",             d:"Breakeven antes de captar.\nFirst hire somente com ARR > R$120K.",              ok:true },
   { n:"03", t:"Política de não captação pré-breakeven", d:"Zero captação antes de Mar/2027.\nExceção apenas para contrato B2B urgente.",   ok:true },
   { n:"04", t:"Valuation revisado",                     d:"R$5M base (pós 1º cliente).\nR$8M otimista (ARR>R$50K + Q1/2027).",            ok:true },
  ].forEach((bd,i) => {
    const by=2.1+i*0.84;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:5.18,y:by,w:4.28,h:0.76, fill:{ color:"0a150d" }, line:{ color:C.greenBorder, width:0.6 }, rectRadius:0.08 });
    s.addText([
      { text:bd.n+" · ", options:{ color:C.green, bold:true } },
      { text:bd.t,       options:{ color:C.white, bold:true } },
    ], { x:5.32,y:by+0.06,w:4.0,h:0.24, fontFace:FB, fontSize:10, margin:0 });
    s.addText(bd.d, { x:5.32,y:by+0.3,w:4.0,h:0.44, fontFace:FB, fontSize:9.5, color:C.muted, margin:0 });
  });
}

// ── SLIDE 11 ── PRÓXIMOS PASSOS ───────────────────────────────────
function s11(pres) {
  const s = pres.addSlide(); s.pres = pres;
  s.background = { color:C.bg };
  addLogo(s); addNum(s,11); addKicker(s,"11 · PRÓXIMOS PASSOS");
  addTitle(s,"Quatro frentes nos próximos 30 dias.", { h:0.62, sz:24 });

  const frentes=[
    { l:"PRODUTO",    c:C.green,  fill:"0a150d",bdr:"2d4a36",
      items:["Recrutar 5 marcas para piloto de agosto","Implementar warm-up cron job Supabase (evitar pausa free tier)","Testar QR em domínio público estável antes de etiqueta física"] },
    { l:"LEGAL / PI", c:C.red,   fill:"140a0a",bdr:"4a2020",
      items:["IP Assignment + NDA com todos os colaboradores — R$3–7K","Protocolar marca PHYLLOS no INPI (classes 25+42) — janela agosto","Conformidade EU AI Act Art. 50 — deadline 02/08/2026"] },
    { l:"FINANCEIRO", c:C.accent,fill:"14100a",bdr:"4a3a1a",
      items:["Confirmar orçamento piloto: R$27,50/mês × 3 meses","Definir forma de cobrança e emissão de NF do 1º DPP","Publicar DPP Schema JSON-LD como OSS (Apache 2.0) — Q3/2026"] },
  ];
  frentes.forEach((fr,i) => {
    const cx=0.35+i*3.22;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:cx,y:1.7,w:3.05,h:2.62,
      fill:{ color:fr.fill }, line:{ color:fr.bdr, width:0.8 }, rectRadius:0.1 });
    s.addText(fr.l, { x:cx+0.18,y:1.8,w:2.7,h:0.28, fontFace:FB, fontSize:9.5, color:fr.c, bold:true, charSpacing:2, margin:0 });
    fr.items.forEach((it,j) => s.addText([
      { text:"→  ", options:{ color:fr.c, bold:true } },
      { text:it,    options:{ color:C.text } },
    ], { x:cx+0.18,y:2.14+j*0.7,w:2.7,h:0.65, fontFace:FB, fontSize:10, margin:0 }));
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:4.44,w:9.3,h:0.42,
    fill:{ color:C.darkGreen }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.08 });
  s.addText([
    { text:"Budget imediato (30 dias): ", options:{ bold:true, color:C.green } },
    { text:"R$12–22K legal/PI  +  R$27,50 infra  =  investimento total pré-piloto de ", options:{ color:C.text } },
    { text:"R$12–26K all-in.", options:{ bold:true, color:C.white } },
  ], { x:0.55,y:4.48,w:9.0,h:0.34, fontFace:FB, fontSize:10.5, valign:"middle", margin:0 });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x:0.35,y:4.94,w:9.3,h:0.5,
    fill:{ color:"0f2018" }, line:{ color:C.greenBorder, width:0.7 }, rectRadius:0.08 });
  s.addText('"Você já sabe o que tem na sua peça. A PHYLLOS deixa qualquer pessoa descobrir isso com um QR."', {
    x:0.55,y:4.96,w:9.0,h:0.46, fontFace:FT, fontSize:12, color:C.white, italic:true, valign:"middle", align:"center", margin:0 });
}

// ── MAIN ──────────────────────────────────────────────────────────
(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "PHYLLOS";
  pres.title  = "PHYLLOS — Apresentação para Diretoria v2";

  s1(pres); s2(pres); s3(pres); s4(pres);
  s5(pres); s6(pres); s7(pres); s8(pres);
  s9(pres); s10(pres); s11(pres);

  await pres.writeFile({ fileName:"outputs/phyllos-apresentacao.pptx" });
  console.log("✓ PPTX gerado: outputs/phyllos-apresentacao.pptx");
})();
