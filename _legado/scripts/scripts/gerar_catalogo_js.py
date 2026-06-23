#!/usr/bin/env python3
"""
Lê os catálogos markdown e gera js/catalogo-moldes.js
com todos os padrões no formato que moldes/index.html usa.
"""

import re, json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------- helpers ----------

def slug(text):
    t = text.lower().strip()
    t = re.sub(r'[áàãâä]', 'a', t)
    t = re.sub(r'[éèêë]', 'e', t)
    t = re.sub(r'[íìîï]', 'i', t)
    t = re.sub(r'[óòõôö]', 'o', t)
    t = re.sub(r'[úùûü]', 'u', t)
    t = re.sub(r'[ç]', 'c', t)
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')

def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

def detect_shape(title, silhueta, prefix):
    t = (title + ' ' + (silhueta or '')).lower()
    t = re.sub(r'[áàãâ]','a',t); t = re.sub(r'[éèê]','e',t)
    t = re.sub(r'[íìî]','i',t);  t = re.sub(r'[óòõô]','o',t)
    t = re.sub(r'[úùû]','u',t);  t = re.sub(r'ç','c',t)

    if prefix in ('CALC',):
        if any(x in t for x in ['wide leg','palazzo','pantalona','culottes','culotte','gaucho','bloomers','knicker']):
            return 'wide'
        if any(x in t for x in ['slim','skinny','cigarrete','cigarette','compressao']):
            return 'slim'
        if any(x in t for x in ['flare','bootcut','boca de sino','boca-de-sino']):
            return 'flare'
        if any(x in t for x in ['jogger','punho elastico','elastico total','thai pant','pescador']):
            return 'jogger'
        if any(x in t for x in ['saruel','harem','thai','bloomers']):
            return 'harem'
        if any(x in t for x in ['barrel leg','barrel']):
            return 'barrel'
        if any(x in t for x in ['legging','3/4','ciclismo','compressao']):
            return 'slim'
        return 'straight'

    if prefix in ('VEST',):
        if any(x in t for x in ['evase','evasê','a-line','aline','trapezio','trapézio']):
            return 'evase'
        if any(x in t for x in ['sereia','mermaid']):
            return 'mermaid'
        if any(x in t for x in ['wrap','envelope','kimono','cruzado']):
            return 'wrap'
        if any(x in t for x in ['empire','babydoll','baby doll','godê','gode','camadas','rodado','flare']):
            return 'empire'
        if any(x in t for x in ['tubo','pencil','lapis','lapiz','ajustado','bustier']):
            return 'pencil'
        if any(x in t for x in ['oversized','camisetao','camisetão','shift','solto']):
            return 'shift'
        return 'straight'

    if prefix in ('SAIA',):
        if any(x in t for x in ['lapis','lapiz','pencil','tubo']):
            return 'pencil'
        if any(x in t for x in ['rodada','circle','full','circulo']):
            return 'circle'
        if any(x in t for x in ['evase','evasê','a-line','plissada','babado','camadas','gode','godê']):
            return 'evase'
        return 'straight'

    return 'straight'

# ---------- parsers ----------

def parse_medidas(block):
    """Extrai a primeira tabela de medidas de um bloco de texto."""
    rows = {}
    for line in block.splitlines():
        if '|' not in line or '---' in line or 'Regiao' in line or 'Região' in line:
            continue
        parts = [p.strip() for p in line.split('|') if p.strip()]
        if len(parts) >= 3:
            regiao = parts[0].lower()
            try:
                corpo_str = parts[1].replace('cm', '').replace(',', '.').strip()
                folga_str = parts[2].replace('cm', '').replace(',', '.').replace('+', '').strip()
                corpo = float(re.search(r'[\d.]+', corpo_str).group())
                folga = float(re.search(r'[\d.]+', folga_str).group()) if re.search(r'[\d.]+', folga_str) else 0
                rows[regiao] = {'corpo': corpo, 'folga': folga, 'final': corpo + folga}
            except:
                pass
    return rows

def calcas_defaults(m):
    def qm(regiao, sub=0):
        for k, v in m.items():
            if regiao in k:
                return round((v['final'] / 4) + sub, 1)
        return 0

    cintura = qm('cintura')
    quadril = qm('quadril')
    coxa = qm('coxa')
    joelho = qm('joelho')
    barra = qm('barra', 0)

    # profundidade gancho
    gancho = 28.0
    for k, v in m.items():
        if 'gancho' in k or 'profundidade' in k:
            gancho = round(v['final'], 1)
            break

    # inseam / comprimento lateral
    inseam = 76
    lateral = 106

    return {
        'waistFront':  max(round(cintura - 0.5, 1), 14),
        'waistBack':   max(round(cintura + 0.5, 1), 14),
        'hipFront':    max(round(quadril - 0.5, 1), 20),
        'hipBack':     max(round(quadril + 0.5, 1), 20),
        'thighFront':  max(round(coxa - 0.5, 1), 12),
        'thighBack':   max(round(coxa + 0.5, 1), 12),
        'kneeWidth':   max(round(joelho, 1), 10),
        'hemWidth':    max(round(barra, 1), 10),
        'crotchDepth': gancho,
        'inseam':      inseam,
        'sideLength':  lateral,
        'dartDepth':   0,
    }

def shirt_defaults(m, length=64, sleeve=0):
    def qm(regiao, sub=0):
        for k, v in m.items():
            if regiao in k:
                return round((v['final'] / 4) + sub, 1)
        return 0

    busto = qm('busto', 0)
    if busto == 0:
        busto = qm('torax', 0)
    if busto == 0:
        busto = 25.0

    cintura = qm('cintura', 0) or round(busto - 1.5, 1)
    hem = qm('barra', 0) or cintura

    return {
        'bustFront': max(round(busto - 0.5, 1), 18),
        'bustBack':  max(round(busto + 0.5, 1), 18),
        'waistFront': max(round(cintura - 0.5, 1), 15),
        'waistBack':  max(round(cintura + 0.5, 1), 15),
        'hemFront':  max(round(hem - 0.5, 1), 16),
        'hemBack':   max(round(hem + 0.5, 1), 16),
        'shoulder': 13, 'neckWidth': 7, 'neckDepth': 10,
        'armholeDepth': 22, 'waistDepth': 40,
        'bodyLength': length,
        'sleeveLength': sleeve,
        'sleeveBicep': 17, 'sleeveHem': 13, 'placketWidth': 0,
    }

def skirt_defaults(m, length=72):
    def qm(regiao, sub=0):
        for k, v in m.items():
            if regiao in k:
                return round((v['final'] / 4) + sub, 1)
        return 0

    cintura = qm('cintura', 0) or 19
    quadril = qm('quadril', 0) or 26
    barra = qm('barra', 0) or quadril

    return {
        'waistFront': max(round(cintura - 0.5, 1), 13),
        'waistBack':  max(round(cintura + 0.5, 1), 13),
        'hipFront':   max(round(quadril - 0.5, 1), 18),
        'hipBack':    max(round(quadril + 0.5, 1), 18),
        'hemFront':   max(round(barra - 0.5, 1), 16),
        'hemBack':    max(round(barra + 0.5, 1), 16),
        'hipDepth': 20, 'length': length,
        'dartFront': 1, 'dartBack': 2,
    }

def dress_defaults(m, length=104, sleeve=0):
    d = shirt_defaults(m, length, sleeve)
    # add hip and hem
    def qm(regiao, sub=0):
        for k, v in m.items():
            if regiao in k:
                return round((v['final'] / 4) + sub, 1)
        return 0
    quadril = qm('quadril', 0) or round(d['bustFront'] + 1.5, 1)
    d['hipFront'] = max(round(quadril - 0.5, 1), 20)
    d['hipBack']  = max(round(quadril + 0.5, 1), 20)
    d['waistDepth'] = 39
    return d

# ---------- catalog parsers ----------

FAMILY_MAP = {
    'CALC': ('calcas',  'pants'),
    'CAMT': ('tops',    'shirt'),
    'CAMS': ('tops',    'shirt'),
    'REGT': ('tops',    'top'),
    'BLUS': ('tops',    'top'),
    'MOLS': ('tops',    'shirt'),
    'VEST': ('vestidos','dress'),
    'SAIA': ('saias',   'skirt'),
    'JAQT': ('jaquetas','jacket'),
    'MACA': ('vestidos','dress'),
}

def mk_controls_pants(d):
    def mk(k, label, mn, mx):
        return {'key': k, 'label': label, 'min': mn, 'max': mx}
    return [
        mk('waistFront','Cintura frente meia', 13, 26),
        mk('waistBack', 'Cintura costas meia', 13, 28),
        mk('hipFront',  'Quadril frente meia', 18, 36),
        mk('hipBack',   'Quadril costas meia', 18, 38),
        mk('thighFront','Coxa frente meia',    10, 26),
        mk('thighBack', 'Coxa costas meia',    10, 28),
        mk('kneeWidth', 'Joelho meia',          9, 24),
        mk('hemWidth',  'Barra meia',           9, 24),
        mk('crotchDepth','Profundidade gancho',22, 38),
        mk('inseam',    'Entreperna',          60, 88),
        mk('sideLength','Comprimento lateral', 88,118),
    ]

def mk_controls_shirt(d):
    def mk(k, label, mn, mx):
        return {'key': k, 'label': label, 'min': mn, 'max': mx}
    return [
        mk('bustFront', 'Busto frente meia',   18, 38),
        mk('bustBack',  'Busto costas meia',   18, 40),
        mk('waistFront','Cintura frente meia', 14, 36),
        mk('waistBack', 'Cintura costas meia', 14, 38),
        mk('hemFront',  'Barra frente meia',   16, 44),
        mk('hemBack',   'Barra costas meia',   16, 46),
        mk('shoulder',  'Ombro',               10, 18),
        mk('bodyLength','Comprimento total',   44,118),
        mk('sleeveLength','Comprimento manga',  0, 66),
    ]

def mk_controls_skirt(d):
    def mk(k, label, mn, mx):
        return {'key': k, 'label': label, 'min': mn, 'max': mx}
    return [
        mk('waistFront','Cintura frente meia', 13, 24),
        mk('waistBack', 'Cintura costas meia', 13, 26),
        mk('hipFront',  'Quadril frente meia', 18, 36),
        mk('hipBack',   'Quadril costas meia', 18, 38),
        mk('hemFront',  'Barra frente meia',   14, 64),
        mk('hemBack',   'Barra costas meia',   14, 66),
        mk('hipDepth',  'Linha do quadril',    16, 26),
        mk('length',    'Comprimento',         34,110),
    ]

def mk_controls(draft, d):
    if draft == 'pants':
        return mk_controls_pants(d)
    elif draft in ('shirt', 'top', 'jacket', 'dress'):
        return mk_controls_shirt(d)
    elif draft == 'skirt':
        return mk_controls_skirt(d)
    return mk_controls_shirt(d)

def parse_catalog(path, prefix):
    """Parse a markdown catalog and return list of pattern dicts."""
    text = read(path)

    # Split on pattern headers like "### CALC-001 —" or "### CALC-001 —"
    pattern_re = re.compile(
        r'###\s+(' + prefix + r'-\d+)\s+[—–-]+\s+(.+?)(?=\n)',
        re.MULTILINE
    )

    entries = []
    matches = list(pattern_re.finditer(text))

    for i, m in enumerate(matches):
        pid = m.group(1)
        title = m.group(2).strip()

        # Block of text for this entry
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]

        # Family and subfamily
        familia_match = re.search(r'\*\*Familia\*\*[:\s]+(.+)', block)
        familia_str = familia_match.group(1).strip() if familia_match else ''

        silhueta_match = re.search(r'\*\*Silhueta e fit\*\*[:\s]+(.+)', block, re.IGNORECASE)
        silhueta = silhueta_match.group(1).strip() if silhueta_match else ''

        # Transformations as mukai-style notes
        trans = re.findall(r'^\d+\.\s+(.+?)$', block, re.MULTILINE)
        mukai = trans[:3] if trans else [f'Base parametrizada: {title.lower()}.']

        # Observação técnica
        obs_match = re.search(r'####\s+Observacao tecnica\s*\n+(.+?)(?=\n##|\Z)', block, re.DOTALL)
        obs = obs_match.group(1).strip()[:180] if obs_match else ''

        # Pieces
        pieces_match = re.search(r'\*\*Paineis\*\*[:\s]+(.+?)$|\*\*Pecas\*\*[:\s]+(.+?)$|[Pp]aineis[:\s]+(.+?)$', block, re.MULTILINE)
        pieces = ''
        if pieces_match:
            pieces = (pieces_match.group(1) or pieces_match.group(2) or pieces_match.group(3) or '').strip()

        # Measurements
        medidas = parse_medidas(block)

        # Determine family and draft from prefix
        family, draft = FAMILY_MAP.get(prefix, ('tops', 'shirt'))

        # Refine draft for some cases
        if prefix in ('REGT', 'BLUS'):
            draft = 'top'
        if prefix == 'MACA':
            draft = 'dress'
        if prefix == 'JAQT':
            draft = 'jacket'

        # Defaults based on draft type
        if draft == 'pants':
            defaults = calcas_defaults(medidas) if medidas else calcas_defaults({})
            length_hint = None
            sleeve_hint = 0
        elif draft in ('shirt', 'top'):
            length = 42 if draft == 'top' else 64
            sleeve = 0 if draft == 'top' else 15
            # hints from title
            if 'manga longa' in title.lower():
                sleeve = 60
            elif 'manga curta' in title.lower() or 'regata' in title.lower():
                sleeve = 0
            elif 'moletom' in title.lower() or 'cardigan' in title.lower() or 'sueter' in title.lower():
                sleeve = 62
                length = 68
            elif 'camisa' in title.lower():
                sleeve = 15
                length = 72
            defaults = shirt_defaults(medidas, length, sleeve)
        elif draft == 'dress':
            length = 104
            if 'mini' in title.lower() or 'tenis' in title.lower():
                length = 72
            elif 'longo' in title.lower():
                length = 140
            elif 'midi' in title.lower():
                length = 110
            defaults = dress_defaults(medidas, length)
        elif draft == 'skirt':
            length = 72
            if 'mini' in title.lower():
                length = 44
            elif 'longo' in title.lower() or 'maxi' in title.lower():
                length = 105
            elif 'midi' in title.lower():
                length = 82
            defaults = skirt_defaults(medidas, length)
        elif draft == 'jacket':
            defaults = shirt_defaults(medidas, 72, 61)
            defaults['sleeveLength'] = 61
            defaults['sleeveBicep'] = 22
            defaults['sleeveHem'] = 13
        else:
            defaults = shirt_defaults(medidas, 64, 0)

        controls = mk_controls(draft, defaults)

        # Search keywords from title + silhueta + familia_str
        search_words = ' '.join([pid, title, silhueta, familia_str]).lower()
        search_words = re.sub(r'[^a-zA-Z0-9\s]', ' ', search_words)

        # Badge from title (first 2 words)
        words = title.split()
        badge = words[1] if len(words) > 1 else words[0]

        # Summary
        summary = f'{silhueta}.' if silhueta else f'Base parametrizada para {title.lower()}.'
        if len(summary) > 120:
            summary = summary[:117] + '...'

        shape = detect_shape(title, silhueta, prefix)

        entry = {
            'id': slug(f'{pid}-{title}'),
            'catalogId': pid,
            'family': family,
            'title': title,
            'badge': badge[:12],
            'draft': draft,
            'shape': shape,
            'summary': summary,
            'search': search_words[:200],
            'mukai': mukai[:3],
            'pieces': pieces or 'Ver catálogo de moldes PHYLLOS.',
            'defaults': defaults,
            'controls': controls,
        }
        entries.append(entry)

    return entries

# ---------- main ----------

catalogs = [
    ('docs/patternmaking/catalogo-calcas.md', 'CALC'),
    ('docs/patternmaking/catalogo-camisas-tops.md', 'CAMT'),
    ('docs/patternmaking/catalogo-camisas-tops.md', 'CAMS'),
    ('docs/patternmaking/catalogo-camisas-tops.md', 'REGT'),
    ('docs/patternmaking/catalogo-camisas-tops.md', 'BLUS'),
    ('docs/patternmaking/catalogo-camisas-tops.md', 'MOLS'),
    ('docs/patternmaking/catalogo-vestidos.md', 'VEST'),
    ('docs/patternmaking/catalogo-saias-externas.md', 'SAIA'),
    ('docs/patternmaking/catalogo-saias-externas.md', 'JAQT'),
    ('docs/patternmaking/catalogo-saias-externas.md', 'MACA'),
]

all_entries = []
for rel_path, prefix in catalogs:
    full_path = os.path.join(BASE, rel_path)
    if os.path.exists(full_path):
        entries = parse_catalog(full_path, prefix)
        all_entries.extend(entries)
        print(f'{prefix}: {len(entries)} entradas')
    else:
        print(f'AVISO: {full_path} não encontrado')

print(f'\nTotal: {len(all_entries)} padrões gerados')

# Write JS
out_path = os.path.join(BASE, 'js', 'catalogo-moldes.js')
os.makedirs(os.path.dirname(out_path), exist_ok=True)

js_entries = json.dumps(all_entries, ensure_ascii=False, indent=2)

js_content = f"""// Catálogo de moldes PHYLLOS — gerado automaticamente
// {len(all_entries)} tipos parametrizados
// Não editar manualmente — regenerar com scripts/gerar_catalogo_js.py

const catalogoMoldes = {js_entries};
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f'Salvo em {out_path}')
