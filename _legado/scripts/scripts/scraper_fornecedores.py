"""
Scraper + seed do catálogo de fornecedores de matérias-primas sustentáveis.

Fontes com scraping automático:
  - Etno Botânica (etnobotanica-loja.com.br) — WooCommerce HTML estático
  - Dalila Têxtil / Ilumiara (ecommerce.dalilatextil.com.br) — e-commerce estático

Demais fornecedores (ITACOOP, NCC, Cataguases etc.) são inseridos como seed manual
com os dados consolidados da pesquisa de mercado.

Uso:
  cd /Users/paulonascimento/meu-primeiro-repo
  python scripts/scraper_fornecedores.py
"""

import sys
import os
import re
import time
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from app.core.database import engine, Base
from app.models.models import Fornecedor, ProdutoFornecedor, CertificacaoFornecedor

Base.metadata.create_all(bind=engine)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_or_create_fornecedor(db: Session, dados: dict) -> Fornecedor:
    f = db.query(Fornecedor).filter(Fornecedor.codigo == dados["codigo"]).first()
    if f:
        print(f"  [skip] Fornecedor já existe: {dados['codigo']} — {dados['nome']}")
        return f
    f = Fornecedor(**dados)
    db.add(f)
    db.flush()
    print(f"  [+] Fornecedor criado: {dados['codigo']} — {dados['nome']}")
    return f


def add_produto(db: Session, fornecedor_id: int, dados: dict):
    exists = (
        db.query(ProdutoFornecedor)
        .filter(
            ProdutoFornecedor.fornecedor_id == fornecedor_id,
            ProdutoFornecedor.nome == dados["nome"],
        )
        .first()
    )
    if exists:
        return
    p = ProdutoFornecedor(fornecedor_id=fornecedor_id, **dados)
    db.add(p)


def add_cert(db: Session, fornecedor_id: int, dados: dict):
    exists = (
        db.query(CertificacaoFornecedor)
        .filter(
            CertificacaoFornecedor.fornecedor_id == fornecedor_id,
            CertificacaoFornecedor.tipo == dados["tipo"],
        )
        .first()
    )
    if exists:
        return
    c = CertificacaoFornecedor(fornecedor_id=fornecedor_id, **dados)
    db.add(c)


def _preco_float(texto: str) -> float | None:
    """Extrai o menor valor de uma faixa 'R$15,00–R$3.570,00'."""
    nums = re.findall(r"[\d.,]+", texto.replace(".", "").replace(",", "."))
    try:
        return float(nums[0]) if nums else None
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Scraper — Etno Botânica
# ---------------------------------------------------------------------------

ETNO_CATEGORY_MAP = {
    "malha": "malha",
    "planos": "tecido_plano",
    "lona": "lona",
    "seda": "tecido_plano",
    "modal": "tecido_plano",
    "linho": "tecido_plano",
    "fio": "fio",
}

ETNO_COMPOSICAO_MAP = {
    "algodão orgânico": "100% Algodão Orgânico",
    "cânhamo": "Cânhamo/Algodão",
    "seda": "100% Seda Natural",
    "modal": "MODAL",
    "linho": "Linho",
    "poliamida": "Poliamida Biodegradável/Modal",
}


def _inferir_tipo(categoria: str) -> str:
    cat_lower = categoria.lower()
    for key, tipo in ETNO_CATEGORY_MAP.items():
        if key in cat_lower:
            return tipo
    return "tecido_plano"


def _inferir_composicao(categoria: str, nome: str) -> str:
    texto = (categoria + " " + nome).lower()
    if "cânhamo" in texto or "hemp" in texto:
        return "Cânhamo/Algodão ou Cânhamo/Modal"
    if "seda" in texto or "silk" in texto:
        return "100% Seda Natural ou misto"
    if "modal" in texto and "algodão" not in texto:
        return "100% MODAL"
    if "linho" in texto or " ln " in texto:
        return "Linho ou Linho/Modal"
    if "poliamida" in texto or "pa bio" in texto:
        return "Poliamida Biodegradável/Modal/Elastano"
    return "100% Algodão Orgânico"


def scrape_etno_botanica(db: Session):
    print("\n=== Etno Botânica ===")
    url = "https://etnobotanica-loja.com.br/tecidos/"

    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
    except Exception as e:
        print(f"  [erro] {e}")
        return

    soup = BeautifulSoup(r.text, "lxml")

    f = get_or_create_fornecedor(db, {
        "codigo": "FOR-002",
        "nome": "Etno Botânica",
        "tipo": "distribuidor",
        "estado": "MG/SP",
        "cidade": "Belo Horizonte / São Paulo",
        "elo_cadeia": json.dumps(["fio", "malha", "tecido_plano"]),
        "produto_principal": "Fios, tecidos planos e malhas em fibras naturais e orgânicas",
        "escala": "amostra",
        "publico_alvo": "b2b",
        "status": "confirmado",
        "nota_confianca": 3,
        "site": "https://etnobotanica-loja.com.br",
        "email_contato": "contato@etnobotanica.com.br",
        "observacoes": (
            "Boa para amostras e desenvolvimento de pequenos lotes. "
            "Declara fomento à agricultura familiar orgânica. "
            "Validar certificados por artigo antes de comprar."
        ),
    })

    # WooCommerce: categorias em <h2> e produtos em <li class="product">
    produtos_inseridos = 0
    categoria_atual = "Geral"

    for elem in soup.find_all(["h2", "li"]):
        if elem.name == "h2":
            categoria_atual = elem.get_text(strip=True)
            continue

        if elem.name == "li" and "product" in elem.get("class", []):
            nome_tag = elem.find(["h2", "h3", "span"], class_=re.compile(r"product.*title|woocommerce-loop-product__title"))
            if not nome_tag:
                nome_tag = elem.find(["h2", "h3"])
            if not nome_tag:
                continue

            nome = nome_tag.get_text(strip=True)

            preco_tag = elem.find("span", class_=re.compile(r"woocommerce-Price-amount|price"))
            preco_texto = preco_tag.get_text(strip=True) if preco_tag else ""
            preco = _preco_float(preco_texto) if preco_texto else None

            # Extrai código entre parênteses: "Jersey Ne 30/1 (2050)"
            cod_match = re.search(r"\((\d+)\)", nome)
            codigo_forn = cod_match.group(1) if cod_match else None

            tipo = _inferir_tipo(categoria_atual)
            composicao = _inferir_composicao(categoria_atual, nome)

            add_produto(db, f.id, {
                "nome": nome,
                "codigo_fornecedor": codigo_forn,
                "tipo": tipo,
                "composicao": composicao,
                "tingimento": "sem_tingimento",
                "preco_referencia": preco,
                "unidade_preco": "metro",
                "disponivel": "sim",
                "fonte": "scraping",
                "observacoes": f"Categoria: {categoria_atual}",
            })
            produtos_inseridos += 1

    # Fallback: se o scraping não encontrou produtos via WooCommerce, insere os
    # produtos confirmados pela pesquisa manual
    if produtos_inseridos == 0:
        print("  [aviso] WooCommerce não detectado — inserindo produtos via seed manual")
        _seed_etno_produtos_manual(db, f.id)
    else:
        print(f"  [{produtos_inseridos} produtos via scraping]")

    add_cert(db, f.id, {
        "tipo": "A validar",
        "apresentado": "pendente",
        "escopo": "fibra/tecido",
        "nivel_confianca": "medio",
        "evidencia": "Declaração no site. Pedir Scope Certificate e Transaction Certificate por lote.",
    })

    db.commit()


def _seed_etno_produtos_manual(db: Session, fornecedor_id: int):
    """Produtos confirmados pela pesquisa (fallback quando scraping não retorna dados)."""
    produtos = [
        # Malhas 100% Algodão Orgânico
        ("Ribana Moletom 2×1 (2065)", "2065", "malha", "100% Algodão Orgânico", 15.0),
        ("Moletom OW CO/Pet (2650)", "2650", "malha", "100% Algodão Orgânico", 15.0),
        ("Morley 2×1 Ne 40/1 (2188)", "2188", "malha", "100% Algodão Orgânico", 15.0),
        ("Ribana 2×1 Ne 40/1 (2168)", "2168", "malha", "100% Algodão Orgânico", 15.0),
        ("Suedine Leve Ne 40/1 (2138)", "2138", "malha", "100% Algodão Orgânico", 15.0),
        ("Jersey Leve Ne 40/1 (2101)", "2101", "malha", "100% Algodão Orgânico", 15.0),
        ("Ribana 2×1 Ne 30/1 (2060)", "2060", "malha", "100% Algodão Orgânico", 15.0),
        ("Jersey Ne 30/1 Penteado (2050)", "2050", "malha", "100% Algodão Orgânico", 15.0),
        # Malhas Cânhamo
        ("Jersey Cotton/Hemp (6200)", "6200", "malha", "Algodão/Cânhamo", 15.0),
        ("Jersey Hemp (5002)", "5002", "malha", "100% Cânhamo", 15.0),
        # Tecidos Planos 100% Algodão Orgânico
        ("Canvas Kargo (5656)", "5656", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Flanela CO (5820)", "5820", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Veludo Premium (9200)", "9200", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Piquet Cotton (9008)", "9008", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Sarja Pesada (7166)", "7166", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Sarja Leve (6500)", "6500", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Cetim Cotton Stretch (6006)", "6006", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Tricoline 40 BR (5353)", "5353", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Tricoline 50 (5151)", "5151", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Cambraia (5400)", "5400", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Popeline / Cambraia Flamê CO (5480)", "5480", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Gaze Doble (5555)", "5555", "tecido_plano", "100% Algodão Orgânico", 15.0),
        ("Perkal Pima 400 (6895)", "6895", "tecido_plano", "100% Algodão Orgânico", 15.0),
        # Lonas
        ("Lona OC ECO (8500)", "8500", "lona", "100% Algodão Orgânico", 15.0),
        ("Lonita OC ECO (8001)", "8001", "lona", "100% Algodão Orgânico", 15.0),
        # Seda
        ("Crepe de Chine (1025)", "1025", "tecido_plano", "100% Seda Natural", 15.0),
        ("Organza (1013)", "1013", "tecido_plano", "100% Seda Natural", 15.0),
        ("Mousseline Voile (1001)", "1001", "tecido_plano", "100% Seda Natural", 15.0),
        # Linho
        ("Canvas LN (4050)", "4050", "tecido_plano", "100% Linho", 162.80),
        ("Cambraia LN (4010)", "4010", "tecido_plano", "100% Linho", 162.80),
    ]
    for nome, cod, tipo, comp, preco in produtos:
        add_produto(db, fornecedor_id, {
            "nome": nome,
            "codigo_fornecedor": cod,
            "tipo": tipo,
            "composicao": comp,
            "tingimento": "sem_tingimento",
            "preco_referencia": preco,
            "unidade_preco": "metro",
            "disponivel": "sim",
            "fonte": "manual",
            "observacoes": "Produto confirmado via pesquisa de mercado jun/2026.",
        })


# ---------------------------------------------------------------------------
# Scraper — Dalila Têxtil / Ilumiara
# ---------------------------------------------------------------------------

def scrape_dalila(db: Session):
    print("\n=== Dalila Têxtil / Ilumiara ===")
    url = "https://ecommerce.dalilatextil.com.br/sustentavel/algodao-organico"

    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
    except Exception as e:
        print(f"  [erro] {e}")
        _seed_dalila_manual(db)
        return

    soup = BeautifulSoup(r.text, "lxml")

    f = get_or_create_fornecedor(db, {
        "codigo": "FOR-004",
        "nome": "Dalila Têxtil / Ilumiara",
        "tipo": "industria",
        "estado": "SC",
        "cidade": "Santa Catarina",
        "elo_cadeia": json.dumps(["malha"]),
        "produto_principal": "Malhas 100% algodão orgânico (linha Ilumiara)",
        "escala": "medio_lote",
        "publico_alvo": "b2b",
        "status": "confirmado",
        "nota_confianca": 4,
        "site": "https://ecommerce.dalilatextil.com.br",
        "email_contato": "ecommerce@dalilatextil.com.br",
        "observacoes": (
            "Parceira do Projeto Ilumiara com Cataguases. "
            "60 famílias em Ingá-PB cultivam o algodão. "
            "Produção 100% orgânica sem agrotóxicos. "
            "Pedir certificado de lote antes de fechar pedido."
        ),
    })

    produtos_inseridos = 0
    cards = soup.find_all(["div", "li", "article"], class_=re.compile(r"product|card|item"))

    for card in cards:
        nome_tag = card.find(["h2", "h3", "h4", "span", "a"], string=re.compile(r"Ilumiara", re.I))
        if not nome_tag:
            # tenta qualquer título dentro do card
            nome_tag = card.find(["h2", "h3", "h4"])
        if not nome_tag:
            continue

        nome = nome_tag.get_text(strip=True)
        if not nome or "Ilumiara" not in nome:
            continue

        preco_tag = card.find(string=re.compile(r"R\$|\d+,\d{2}"))
        preco = None
        if preco_tag:
            match = re.search(r"(\d+)[,.](\d{2})", str(preco_tag))
            if match:
                preco = float(f"{match.group(1)}.{match.group(2)}")

        add_produto(db, f.id, {
            "nome": nome,
            "tipo": "malha",
            "composicao": "100% Algodão Orgânico",
            "tingimento": "sem_tingimento",
            "preco_referencia": preco,
            "unidade_preco": "kg",
            "uso_recomendado": "Camisetas, peças casuais, infantil",
            "disponivel": "sim",
            "fonte": "scraping",
        })
        produtos_inseridos += 1

    if produtos_inseridos == 0:
        print("  [aviso] Scraping sem resultado — inserindo via seed manual")
        _seed_dalila_manual_produtos(db, f.id)
    else:
        print(f"  [{produtos_inseridos} produtos via scraping]")

    add_cert(db, f.id, {
        "tipo": "A validar por lote",
        "apresentado": "pendente",
        "escopo": "malha",
        "nivel_confianca": "medio",
        "evidencia": "Projeto Ilumiara declara produção 100% orgânica. Pedir Transaction Certificate.",
    })

    db.commit()


def _seed_dalila_manual(db: Session):
    f = get_or_create_fornecedor(db, {
        "codigo": "FOR-004",
        "nome": "Dalila Têxtil / Ilumiara",
        "tipo": "industria",
        "estado": "SC",
        "cidade": "Santa Catarina",
        "elo_cadeia": json.dumps(["malha"]),
        "produto_principal": "Malhas 100% algodão orgânico (linha Ilumiara)",
        "escala": "medio_lote",
        "publico_alvo": "b2b",
        "status": "confirmado",
        "nota_confianca": 4,
        "site": "https://ecommerce.dalilatextil.com.br",
        "email_contato": "ecommerce@dalilatextil.com.br",
        "observacoes": "Parceira do Projeto Ilumiara. 60 famílias em Ingá-PB.",
    })
    _seed_dalila_manual_produtos(db, f.id)
    db.commit()


def _seed_dalila_manual_produtos(db: Session, fornecedor_id: int):
    malhas = [
        ("Texture Dona Maria Ilumiara", 88.15),
        ("Malha Seu Bio Ilumiara", 80.87),
        ("Malha Seu Severino Ilumiara", 82.96),
        ("Malha Ecológica Ilumiara", 81.94),
    ]
    for nome, preco in malhas:
        add_produto(db, fornecedor_id, {
            "nome": nome,
            "tipo": "malha",
            "composicao": "100% Algodão Orgânico",
            "tingimento": "sem_tingimento",
            "preco_referencia": preco,
            "unidade_preco": "kg",
            "uso_recomendado": "Camisetas, peças casuais, infantil",
            "disponivel": "sim",
            "fonte": "manual",
            "observacoes": "Confirmado via e-commerce Dalila, jun/2026.",
        })


# ---------------------------------------------------------------------------
# Seed manual — demais fornecedores
# ---------------------------------------------------------------------------

def seed_manual(db: Session):
    fornecedores = [
        # --- FOR-001 ITACOOP ---
        {
            "fornecedor": {
                "codigo": "FOR-001",
                "nome": "ITACOOP",
                "tipo": "cooperativa",
                "estado": "PB",
                "cidade": "Ingá",
                "elo_cadeia": json.dumps(["fibra"]),
                "produto_principal": "Pluma/lint cotton 100% algodão orgânico",
                "escala": "medio_lote",
                "publico_alvo": "b2b",
                "status": "confirmado",
                "nota_confianca": 5,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Cooperativa de Agricultores Familiares de Ingá e Região. "
                    "Certificação GOTS v7.0 para pluma 100% orgânica, licença nº 00266467, "
                    "válida até 11/03/2027. Contato via Prefeitura de Ingá ou Projeto Cooperar PB."
                ),
            },
            "produtos": [
                {
                    "nome": "Pluma / Lint Cotton 100% Algodão Orgânico Branco",
                    "tipo": "pluma",
                    "composicao": "100% Algodão Orgânico",
                    "cor": "branco",
                    "tingimento": "sem_tingimento",
                    "uso_recomendado": "Fiação, tecelagem, malharia",
                    "disponivel": "sim",
                    "fonte": "manual",
                    "observacoes": "Usina beneficia ~4.000 kg/h de algodão em rama gerando fardos de 190 kg de pluma.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "GOTS",
                    "apresentado": "sim",
                    "validade": "2027-03-11",
                    "escopo": "fibra",
                    "numero_licenca": "00266467",
                    "evidencia": "GOTS v7.0, licença pública. Exigir Transaction Certificate por lote comprado.",
                    "nivel_confianca": "alto",
                },
            ],
        },
        # --- FOR-003 Cataguases / Ilumiara ---
        {
            "fornecedor": {
                "codigo": "FOR-003",
                "nome": "Companhia Industrial Cataguases — Linha Ilumiara",
                "tipo": "industria",
                "estado": "MG",
                "cidade": "Cataguases",
                "elo_cadeia": json.dumps(["tecido_plano", "fio"]),
                "produto_principal": "Tecidos planos 100% algodão orgânico (Org.150N Cravo, Org.220N Uva)",
                "escala": "industrial",
                "publico_alvo": "b2b",
                "status": "confirmado",
                "nota_confianca": 4,
                "site": "https://cataguases.com.br",
                "email_contato": None,
                "observacoes": (
                    "Linha Ilumiara usa algodão de Ingá-PB. Persegue certificação GOTS. "
                    "Validar certificado por artigo e lote antes de comprar. "
                    "Boa para escala industrial de tecidos planos."
                ),
            },
            "produtos": [
                {
                    "nome": "Org.150N Cravo",
                    "tipo": "tecido_plano",
                    "composicao": "100% Algodão Orgânico",
                    "gramatura_gm2": 150.0,
                    "tingimento": "sem_tingimento",
                    "uso_recomendado": "Camisaria, peças leves",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
                {
                    "nome": "Org.220N Uva",
                    "tipo": "tecido_plano",
                    "composicao": "100% Algodão Orgânico",
                    "gramatura_gm2": 220.0,
                    "tingimento": "sem_tingimento",
                    "uso_recomendado": "Peças estruturadas, alfaiataria leve",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "GOTS",
                    "apresentado": "pendente",
                    "escopo": "tecido_plano",
                    "nivel_confianca": "medio",
                    "evidencia": "Empresa declara busca por certificação GOTS. Exigir Scope Certificate antes de fechar pedido.",
                },
            ],
        },
        # --- FOR-005 Natural Cotton Color ---
        {
            "fornecedor": {
                "codigo": "FOR-005",
                "nome": "Natural Cotton Color / NCC Ecobrands",
                "tipo": "marca",
                "estado": "PB",
                "cidade": "João Pessoa",
                "elo_cadeia": json.dumps(["fibra", "tecido_plano", "malha", "produto_acabado"]),
                "produto_principal": "Algodão colorido orgânico, tecidos, malhas, vestuário",
                "escala": "pequeno_lote",
                "publico_alvo": "b2b",
                "status": "confirmado",
                "nota_confianca": 4,
                "site": "https://nccecobrands.com.br",
                "email_contato": "vendas@naturalcottoncolor.com.br",
                "observacoes": (
                    "Algodão nasce colorido (beige, marrom, verde) dispensando tingimento. "
                    "MOQ: 100m (varejo) ou 200kg malha / 300m tecido plano (atacado). "
                    "Prazo de entrega: 30 dias úteis após pagamento. "
                    "Catálogo por e-mail — solicitar amostras com assunto: AMOSTRA TECIDOS."
                ),
            },
            "produtos": [
                {
                    "nome": "Malha Algodão Colorido Orgânico",
                    "tipo": "malha",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom natural / verde natural",
                    "tingimento": "natural",
                    "moq": "200kg",
                    "uso_recomendado": "Camisetas, vestuário premium, acessórios",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
                {
                    "nome": "Denim / Sarja Algodão Colorido Orgânico",
                    "tipo": "tecido_plano",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "marrom natural / verde natural",
                    "tingimento": "natural",
                    "moq": "300m",
                    "uso_recomendado": "Calças, jaquetas, peças de denim sustentável",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
                {
                    "nome": "Malha Moletom Algodão Colorido",
                    "tipo": "malha",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom natural",
                    "tingimento": "natural",
                    "moq": "200kg",
                    "uso_recomendado": "Moletom, peças de inverno premium",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "ECOCERT",
                    "apresentado": "pendente",
                    "escopo": "fibra",
                    "nivel_confianca": "medio",
                    "evidencia": "Site lista ECOCERT/NOP/FOE. Solicitar certificado atualizado por lote.",
                },
            ],
        },
        # --- FOR-006 Justa Trama ---
        {
            "fornecedor": {
                "codigo": "FOR-006",
                "nome": "Justa Trama",
                "tipo": "cooperativa",
                "estado": "RS",
                "cidade": "Porto Alegre (rede nacional)",
                "elo_cadeia": json.dumps(["fibra", "fio", "malha", "confeccao", "produto_acabado"]),
                "produto_principal": "Vestuário, cama, acessórios e eco-corporativos em algodão agroecológico",
                "escala": "pequeno_lote",
                "publico_alvo": "b2b",
                "status": "parceiro_estrategico",
                "nota_confianca": 3,
                "site": "https://justatrama.com.br",
                "email_contato": None,
                "observacoes": (
                    "Cadeia solidária com 600 cooperados em RS, MS, MG, CE, RO. "
                    "Agricultores de Tauá-CE (ADEC) fornecem o algodão orgânico. "
                    "Ideal para parceria de marca, produto acabado, uniformes e storytelling social."
                ),
            },
            "produtos": [
                {
                    "nome": "Camiseta Algodão Agroecológico",
                    "tipo": "produto_acabado",
                    "composicao": "100% Algodão Agroecológico",
                    "tingimento": "sem_tingimento",
                    "uso_recomendado": "Uniforme, cápsula solidária, eco-brinde corporativo",
                    "disponivel": "sim",
                    "fonte": "manual",
                },
                {
                    "nome": "Ecobag / Sacola Algodão Orgânico",
                    "tipo": "produto_acabado",
                    "composicao": "100% Algodão Orgânico",
                    "tingimento": "sem_tingimento",
                    "disponivel": "sim",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "IBD",
                    "apresentado": "pendente",
                    "escopo": "fibra",
                    "nivel_confianca": "medio",
                    "evidencia": "Histórico de certificação IBD via ADEC. Validar status atual.",
                },
            ],
        },
        # --- FOR-007 ADEC Tauá ---
        {
            "fornecedor": {
                "codigo": "FOR-007",
                "nome": "ADEC — Associação de Desenvolvimento Educacional e Cultural de Tauá",
                "tipo": "projeto_agroecologico",
                "estado": "CE",
                "cidade": "Tauá / Inhamuns",
                "elo_cadeia": json.dumps(["fibra"]),
                "produto_principal": "Algodão agroecológico/orgânico em sistema consorciado",
                "escala": "pequeno_lote",
                "publico_alvo": "cooperativas",
                "status": "lead_validar",
                "nota_confianca": 3,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Histórico forte — fornece para Justa Trama e Veja/Vert. "
                    "Certificação IBD e cultivo sem agrotóxicos/adubo químico. "
                    "Validar status atual da certificação antes de avançar."
                ),
            },
            "produtos": [
                {
                    "nome": "Algodão Agroecológico em Rama / Pluma",
                    "tipo": "pluma",
                    "composicao": "100% Algodão Agroecológico",
                    "cor": "branco",
                    "tingimento": "sem_tingimento",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "IBD",
                    "apresentado": "pendente",
                    "escopo": "fibra",
                    "nivel_confianca": "medio",
                    "evidencia": "Fonte antiga indica certificação IBD. Validar certificado e Transaction Certificate atual.",
                },
            ],
        },
        # --- FOR-008 EcoSimple ---
        {
            "fornecedor": {
                "codigo": "FOR-008",
                "nome": "EcoSimple",
                "tipo": "industria",
                "estado": "SP",
                "cidade": "São Paulo",
                "elo_cadeia": json.dumps(["tecido_plano", "malha"]),
                "produto_principal": "Tecidos sustentáveis — linha Green Cotton com fio orgânico da Paraíba",
                "escala": "medio_lote",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 3,
                "site": "https://ecosimple.com.br",
                "email_contato": "comercial@ecosimple.com.br",
                "telefone": "(19) 3469.9750",
                "observacoes": (
                    "Empresa B Certificada. Linha Green Cotton declara fio orgânico da PB. "
                    "Catálogo em PDF por cadastro — solicitar certificado por artigo e lote. "
                    "Validar escopo orgânico antes de comprar."
                ),
            },
            "produtos": [
                {
                    "nome": "Green Cotton — Tecido Plano Orgânico",
                    "tipo": "tecido_plano",
                    "composicao": "Algodão Orgânico (origem PB)",
                    "tingimento": "a_validar",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Solicitar ficha técnica, certificado de lote e composição exata.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "Empresa B",
                    "apresentado": "sim",
                    "escopo": "empresa",
                    "nivel_confianca": "medio",
                    "evidencia": "Certificada pelo Sistema B Brasil. Não confirma GOTS/OCS por produto.",
                },
            ],
        },
        # --- FOR-009 Texpar Malhas ---
        {
            "fornecedor": {
                "codigo": "FOR-009",
                "nome": "Texpar Malhas (Grupo Unitêxtil)",
                "tipo": "industria",
                "estado": "PB/PE",
                "cidade": "Paraíba / Pernambuco",
                "elo_cadeia": json.dumps(["malha"]),
                "produto_principal": "Malhas, ribanas e golas com algodão orgânico/colorido",
                "escala": "medio_lote",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": "https://www.texpar.com.br",
                "email_contato": None,
                "observacoes": (
                    "Maior comprador de algodão colorido na PB. "
                    "Site apenas institucional — catálogo em área restrita. "
                    "Tratar como lead: pedir composição, origem da fibra e certificado por artigo."
                ),
            },
            "produtos": [
                {
                    "nome": "Malha Algodão Colorido Orgânico",
                    "tipo": "malha",
                    "composicao": "A validar — declara algodão orgânico colorido",
                    "cor": "beige / marrom / verde natural",
                    "tingimento": "natural",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Pedir ficha técnica, certificado e composição exata antes de avançar.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "nao",
                    "nivel_confianca": "baixo",
                    "evidencia": "Nenhum certificado público encontrado. Exigir documentação.",
                },
            ],
        },
        # --- FOR-010 Diaconia / ACOPASA ---
        {
            "fornecedor": {
                "codigo": "FOR-010",
                "nome": "Diaconia / ACOPASA — Sertão do Apodi",
                "tipo": "projeto_agroecologico",
                "estado": "RN",
                "cidade": "Apodi",
                "elo_cadeia": json.dumps(["fibra"]),
                "produto_principal": "Pluma orgânica com certificação participativa",
                "escala": "amostra",
                "publico_alvo": "cooperativas",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Mais projeto em desenvolvimento do que fornecedor industrial consolidado. "
                    "Houve piloto de fio 12/1 com Senai. "
                    "Bom para cadeia de longo prazo e impacto social mensurável no RN."
                ),
            },
            "produtos": [
                {
                    "nome": "Pluma Orgânica com Certificação Participativa",
                    "tipo": "pluma",
                    "composicao": "100% Algodão Orgânico",
                    "tingimento": "sem_tingimento",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Escala ainda em desenvolvimento. Contato via Diaconia RN.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "Participativa",
                    "apresentado": "pendente",
                    "escopo": "fibra",
                    "nivel_confianca": "baixo",
                    "evidencia": "Certificação participativa em desenvolvimento. Validar status atual.",
                },
            ],
        },
    ]

    for item in fornecedores:
        f = get_or_create_fornecedor(db, item["fornecedor"])
        for p in item.get("produtos", []):
            add_produto(db, f.id, p)
        for c in item.get("certificacoes", []):
            add_cert(db, f.id, c)

    db.commit()
    print(f"\n  [seed manual] {len(fornecedores)} fornecedores processados.")


# ---------------------------------------------------------------------------
# Catálogo ampliado — pequenos e médios fornecedores
# Grupos:
#   G1 Fibra / Pluma
#   G2 Fios
#   G3 Tecidos / Malhas a metro
#   G4 Beneficiamento / Confecção / Artesanato
# ---------------------------------------------------------------------------

def _patch_fornecedor(db: Session, codigo: str, **kwargs):
    """Atualiza campos de um fornecedor existente."""
    f = db.query(Fornecedor).filter(Fornecedor.codigo == codigo).first()
    if not f:
        return
    for k, v in kwargs.items():
        setattr(f, k, v)


def seed_catalogo_ampliado(db: Session):
    print("\n=== Catálogo ampliado ===")

    # ── Atualiza entradas existentes com dados novos ──────────────────────

    # FOR-005 NCC: adiciona contexto Projeto Algodão Paraíba
    _patch_fornecedor(db, "FOR-005",
        nome="Natural Cotton Color / NCC Ecobrands / Projeto Algodão Paraíba",
        observacoes=(
            "Algodão nasce colorido (beige, marrom, verde) dispensando tingimento. "
            "Projeto Algodão Paraíba envolve ~300 famílias em 8 municípios. "
            "MOQ: 100m (varejo) ou 200kg malha / 300m tecido plano (atacado). "
            "Catálogo por e-mail — assunto: AMOSTRA TECIDOS. Validar certificado por lote."
        ),
    )

    # FOR-008 EcoSimple: adiciona produto Varanasi identificado na pesquisa
    _f008 = db.query(Fornecedor).filter(Fornecedor.codigo == "FOR-008").first()
    if _f008:
        add_produto(db, _f008.id, {
            "nome": "Varanasi 100% Algodão Orgânico Natural",
            "tipo": "tecido_plano",
            "composicao": "100% Algodão Orgânico",
            "cor": "natural (cru)",
            "tingimento": "sem_tingimento",
            "gramatura_gm2": 105.0,
            "largura_m": 1.45,
            "uso_recomendado": "Camisaria leve, vestidos, blusas, lingerie sustentável",
            "disponivel": "a_validar",
            "fonte": "manual",
            "observacoes": "Produto EcoSimple identificado na pesquisa. Validar estoque e certificado por lote.",
        })

    db.flush()

    # ── Novos fornecedores ────────────────────────────────────────────────

    novos = [

        # ── G3 Tecidos / Malhas a metro ──────────────────────────────────

        {
            "fornecedor": {
                "codigo": "FOR-011",
                "nome": "Aradefe Malhas",
                "tipo": "industria",
                "estado": "SC",
                "cidade": "Brusque / Criciúma",
                "elo_cadeia": json.dumps(["malha"]),
                "produto_principal": "Malha 100% algodão orgânico; misturas com PET reciclado e algodão desfibrado",
                "escala": "medio_lote",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 3,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "LaLuz cita Aradefe como fornecedora de malha 100% algodão orgânico. "
                    "LinkedIn da empresa menciona linha Eco com algodão 100% orgânico. "
                    "Lead forte para malha — validar certificado, escopo e disponibilidade de lote."
                ),
            },
            "produtos": [
                {
                    "nome": "Malha 100% Algodão Orgânico (linha Eco)",
                    "tipo": "malha",
                    "composicao": "100% Algodão Orgânico",
                    "tingimento": "sem_tingimento",
                    "uso_recomendado": "Camisetas, peças básicas, infantil",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Pedir Scope Certificate e Transaction Certificate. Confirmar linha Eco disponível.",
                },
                {
                    "nome": "Malha Eco PET Reciclado + Algodão Desfibrado",
                    "tipo": "malha",
                    "composicao": "PET reciclado + algodão desfibrado (pct a validar)",
                    "tingimento": "a_validar",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "risco": "Não classificar como orgânico. Pedir composição exata e laudo.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "nao",
                    "escopo": "malha",
                    "nivel_confianca": "medio",
                    "evidencia": "Evidência indireta via LaLuz. Exigir certificado antes de comprar.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-012",
                "nome": "Banco de Tecido",
                "tipo": "distribuidor",
                "estado": "SP",
                "cidade": "São Paulo (online)",
                "elo_cadeia": json.dumps(["tecido_plano"]),
                "produto_principal": "Algodão Orgânico Slub Cru — revenda circular a metro",
                "escala": "amostra",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Revenda circular de tecidos. Produto anunciado como algodão orgânico leve e macio. "
                    "Bom para desenvolvimento e amostras em baixa escala. "
                    "Validar origem, certificado e disponibilidade por lote."
                ),
            },
            "produtos": [
                {
                    "nome": "Algodão Orgânico Slub Cru",
                    "tipo": "tecido_plano",
                    "composicao": "100% Algodão Orgânico",
                    "cor": "cru",
                    "tingimento": "sem_tingimento",
                    "uso_recomendado": "Camisaria, vestidos, protótipos",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Revenda circular — estoque pode variar. Pedir certificado de origem.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "nao",
                    "nivel_confianca": "baixo",
                    "evidencia": "Declaração no anúncio. Exigir documentação de origem.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-013",
                "nome": "Arte Decor Prince",
                "tipo": "distribuidor",
                "estado": "SP",
                "cidade": "São Paulo (online)",
                "elo_cadeia": json.dumps(["tecido_plano"]),
                "produto_principal": "Tecido 100% algodão orgânico 150 cm — varejo/metro",
                "escala": "amostra",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Loja de varejo. Útil para amostras e desenvolvimento de pequenos lotes. "
                    "Validar origem da fibra e certificação antes de comprar para coleção."
                ),
            },
            "produtos": [
                {
                    "nome": "Tecido 100% Algodão Orgânico 150 cm",
                    "tipo": "tecido_plano",
                    "composicao": "100% Algodão Orgânico",
                    "largura_m": 1.50,
                    "tingimento": "a_validar",
                    "uso_recomendado": "Amostras, protótipos, desenvolvimentos pontuais",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "risco": "Varejo sem garantia de rastreabilidade. Tratar como amostra.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "nao",
                    "nivel_confianca": "baixo",
                    "evidencia": "Nenhum certificado público encontrado.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-016",
                "nome": "Santa Luzia Redes e Decoração",
                "tipo": "industria",
                "estado": "PB",
                "cidade": "São Bento / João Pessoa",
                "elo_cadeia": json.dumps(["malha", "tecido_plano", "produto_acabado"]),
                "produto_principal": "Redes, mantas, tapetes, fios e tecidos em algodão orgânico colorido",
                "escala": "pequeno_lote",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 3,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Usa algodão orgânico naturalmente colorido e algodão reciclado em linha especial. "
                    "Muito boa para casa/decor e cadeia artesanal. "
                    "Validar disponibilidade de tecido avulso e certificação por produto."
                ),
            },
            "produtos": [
                {
                    "nome": "Rede Algodão Colorido Orgânico",
                    "tipo": "produto_acabado",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom / verde natural",
                    "tingimento": "natural",
                    "uso_recomendado": "Decoração, casa, lifestyle sustentável",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
                {
                    "nome": "Fio Algodão Orgânico Colorido para Artesanato",
                    "tipo": "fio",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom natural",
                    "tingimento": "natural",
                    "uso_recomendado": "Crochê, tricô, malharia manual, artesanato",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "pendente",
                    "escopo": "fibra/produto",
                    "nivel_confianca": "medio",
                    "evidencia": "Usa algodão colorido orgânico. Pedir documentação de origem e certificado.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-023",
                "nome": "Menegotti Têxtil",
                "tipo": "industria",
                "estado": "SC",
                "cidade": "Santa Catarina",
                "elo_cadeia": json.dumps(["malha", "tecido_plano"]),
                "produto_principal": "Malhas BCI, pigmentação natural, linha sustentável",
                "escala": "medio_lote",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "ATENÇÃO: Sou de Algodão lista algodão BCI, não orgânico certificado. "
                    "Não classificar como orgânico sem prova documental. "
                    "BCI (Better Cotton Initiative) é padrão de responsabilidade, NÃO certificação orgânica. "
                    "Interessante para pigmentação natural e linha sustentável, mas escopo precisa ser validado."
                ),
            },
            "produtos": [
                {
                    "nome": "Malha Algodão BCI / Linha Sustentável",
                    "tipo": "malha",
                    "composicao": "Algodão BCI (não orgânico certificado)",
                    "tingimento": "a_validar",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "risco": "BCI ≠ orgânico. Não usar em comunicação orgânica sem certificado específico.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "BCI",
                    "apresentado": "nao",
                    "escopo": "fibra",
                    "nivel_confianca": "baixo",
                    "evidencia": "BCI é padrão socioambiental, não orgânico. Pedir evidência de linha específica.",
                },
            ],
        },

        # ── G2 Fios ──────────────────────────────────────────────────────

        {
            "fornecedor": {
                "codigo": "FOR-014",
                "nome": "Made by You",
                "tipo": "marca",
                "estado": "SP",
                "cidade": "São Paulo (online)",
                "elo_cadeia": json.dumps(["fio"]),
                "produto_principal": "Fios de algodão orgânico naturalmente colorido para crochê e tricô",
                "escala": "amostra",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 3,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Fio de algodão orgânico colorido da Paraíba apresentado em parceria com "
                    "Natural Cotton Color / Embrapa. "
                    "Boa para fio artesanal, collab e desenvolvimento de produto manual."
                ),
            },
            "produtos": [
                {
                    "nome": "Fio Algodão Orgânico Colorido Paraíba — Crochê / Tricô",
                    "tipo": "fio",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom / verde natural",
                    "tingimento": "natural",
                    "uso_recomendado": "Crochê, tricô, malharia manual, acessórios artesanais",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Parceria com NCC/Embrapa. Validar disponibilidade atual e certificado.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "pendente",
                    "escopo": "fio",
                    "nivel_confianca": "medio",
                    "evidencia": "Origem declarada em parceria com NCC (algodão orgânico colorido PB). Pedir certificado.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-015",
                "nome": "EuroFios / EuroRoma",
                "tipo": "industria",
                "estado": "SC",
                "cidade": "Blumenau",
                "elo_cadeia": json.dumps(["fio"]),
                "produto_principal": "Fio EcoYarn de algodão colorido orgânico da Paraíba",
                "escala": "pequeno_lote",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Lançou linha EcoYarn com algodão colorido orgânico da Paraíba em 2020. "
                    "Validar disponibilidade atual — pode ser linha descontinuada. "
                    "Lead interessante para fios de artesanato e malharia manual."
                ),
            },
            "produtos": [
                {
                    "nome": "EcoYarn Algodão Colorido Orgânico Paraíba",
                    "tipo": "fio",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom / verde natural",
                    "tingimento": "natural",
                    "uso_recomendado": "Crochê, tricô, malharia manual",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Lançamento 2020 — confirmar se linha ainda ativa e disponível.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "nao",
                    "escopo": "fio",
                    "nivel_confianca": "baixo",
                    "evidencia": "Nenhum certificado público encontrado. Validar junto à empresa.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-018",
                "nome": "Norfil",
                "tipo": "industria",
                "estado": "PB",
                "cidade": "João Pessoa",
                "elo_cadeia": json.dumps(["fio"]),
                "produto_principal": "Fios de algodão; parceira estratégica no ecossistema de algodão orgânico da Paraíba",
                "escala": "industrial",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Fiação industrial parceira do Projeto Algodão Orgânico PB junto a Embrapa e Empaer. "
                    "Site destaca BCI; nas fontes do projeto PB aparece como parceira comercial/logística. "
                    "Validar se há linha orgânica certificada disponível para compra. "
                    "Estratégica para escala industrial de fios com origem rastreada na PB."
                ),
            },
            "produtos": [
                {
                    "nome": "Fio Algodão (BCI / possível linha orgânica PB)",
                    "tipo": "fio",
                    "composicao": "A validar — declara BCI; parceira em projeto orgânico PB",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "risco": "BCI ≠ orgânico. Exigir Scope Certificate GOTS/OCS para compra orgânica.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "BCI",
                    "apresentado": "nao",
                    "escopo": "fio",
                    "nivel_confianca": "baixo",
                    "evidencia": "BCI listado no site. Pedir evidência de linha orgânica separada.",
                },
            ],
        },

        # ── G1 Fibra / Pluma ──────────────────────────────────────────────

        {
            "fornecedor": {
                "codigo": "FOR-017",
                "nome": "Coopnatural",
                "tipo": "cooperativa",
                "estado": "PB",
                "cidade": "Paraíba",
                "elo_cadeia": json.dumps(["fibra"]),
                "produto_principal": "Articulação comercial do algodão orgânico da Paraíba",
                "escala": "medio_lote",
                "publico_alvo": "cooperativas",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Aparece como parceira do Projeto Algodão Orgânico da Paraíba "
                    "junto à Norfil, Embrapa e Empaer. "
                    "Lead institucional relevante para articulação da cadeia; "
                    "não foi possível identificar canal de venda direta. Contato via projeto PB."
                ),
            },
            "produtos": [
                {
                    "nome": "Algodão Orgânico Paraíba (articulação de cadeia)",
                    "tipo": "pluma",
                    "composicao": "100% Algodão Orgânico",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Papel de articulação comercial — não necessariamente venda direta.",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "pendente",
                    "escopo": "fibra",
                    "nivel_confianca": "baixo",
                    "evidencia": "Aparece em projeto orgânico PB mas sem certificado público identificado.",
                },
            ],
        },

        # ── G4 Beneficiamento / Confecção / Artesanato ───────────────────

        {
            "fornecedor": {
                "codigo": "FOR-019",
                "nome": "Rendas Paraíba",
                "tipo": "artesanato",
                "estado": "PB",
                "cidade": "Paraíba / Rio de Janeiro",
                "elo_cadeia": json.dumps(["acabamento"]),
                "produto_principal": "Bicos, entremeios e aviamentos em algodão colorido orgânico",
                "escala": "amostra",
                "publico_alvo": "marcas",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Já produziu aviamentos em algodão colorido orgânico para Natural Cotton Color. "
                    "Boa para detalhe artesanal, diferenciação de peça e narrativa de impacto social. "
                    "Lead de aviamento — contato preferencialmente via NCC."
                ),
            },
            "produtos": [
                {
                    "nome": "Bicos e Aviamentos Algodão Colorido Orgânico",
                    "tipo": "acabamento",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom / verde natural",
                    "tingimento": "natural",
                    "uso_recomendado": "Detalhe de barra, cós, decote, acabamento artesanal",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "pendente",
                    "escopo": "acabamento",
                    "nivel_confianca": "baixo",
                    "evidencia": "Produção documentada em parceria NCC. Pedir ficha técnica e origem.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-020",
                "nome": "Associação Borda Viva",
                "tipo": "cooperativa",
                "estado": "PR",
                "cidade": "São José dos Pinhais",
                "elo_cadeia": json.dumps(["confeccao"]),
                "produto_principal": "Costura, bolsas, mochilas, reaproveitamento têxtil",
                "escala": "amostra",
                "publico_alvo": "marcas",
                "status": "lead_validar",
                "nota_confianca": 1,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Não é fornecedor de algodão orgânico — parceira de confecção e impacto social. "
                    "Pode ser interessante para produção de peças com reaproveitamento têxtil, "
                    "bolsas, acessórios e acabamentos com narrativa de impacto."
                ),
            },
            "produtos": [
                {
                    "nome": "Confecção sob encomenda — bolsas e acessórios",
                    "tipo": "produto_acabado",
                    "composicao": "A validar por encomenda",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Parceria de confecção social, não fornecedor de matéria-prima orgânica.",
                },
            ],
            "certificacoes": [],
        },

        {
            "fornecedor": {
                "codigo": "FOR-021",
                "nome": "Coopercostura Vila Verde",
                "tipo": "cooperativa",
                "estado": "PR",
                "cidade": "Curitiba",
                "elo_cadeia": json.dumps(["confeccao"]),
                "produto_principal": "Costura, confecção, possível estamparia",
                "escala": "amostra",
                "publico_alvo": "marcas",
                "status": "lead_validar",
                "nota_confianca": 1,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Cooperativa desde 2001. Não é fornecedor de matéria-prima orgânica, "
                    "mas pode ser parceira de confecção social. "
                    "Validar capacidade produtiva atual antes de avançar."
                ),
            },
            "produtos": [
                {
                    "nome": "Confecção sob encomenda",
                    "tipo": "produto_acabado",
                    "composicao": "A validar por encomenda",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                    "observacoes": "Parceira de confecção. Validar capacidade atual.",
                },
            ],
            "certificacoes": [],
        },

        {
            "fornecedor": {
                "codigo": "FOR-022",
                "nome": "Etnobotânica Pigmentos (corantes e tingimento natural)",
                "tipo": "industria",
                "estado": "MG/SP",
                "cidade": "Belo Horizonte / São Paulo",
                "elo_cadeia": json.dumps(["acabamento"]),
                "produto_principal": "Corantes vegetais, pigmentos naturais, bases para tingimento têxtil",
                "escala": "amostra",
                "publico_alvo": "b2b",
                "status": "lead_validar",
                "nota_confianca": 3,
                "site": "https://etnobotanica.com.br",
                "email_contato": None,
                "observacoes": (
                    "Mesma empresa da Etno Botânica (FOR-002), linha de pigmentos naturais. "
                    "Complementar ao algodão orgânico para tingimento vegetal. "
                    "Reduz impacto no acabamento e amplia narrativa de sustentabilidade da peça."
                ),
            },
            "produtos": [
                {
                    "nome": "Corante Vegetal para Tingimento Têxtil",
                    "tipo": "insumo",
                    "composicao": "Pigmento vegetal natural (sem metais pesados)",
                    "uso_recomendado": "Tingimento natural de algodão, linho, seda e fibras celulósicas",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "pendente",
                    "escopo": "insumo/acabamento",
                    "nivel_confianca": "medio",
                    "evidencia": "Produto natural declarado. Pedir ficha técnica e laudo de ausência de metais pesados.",
                },
            ],
        },

        {
            "fornecedor": {
                "codigo": "FOR-024",
                "nome": "Ateliê SÄL",
                "tipo": "marca",
                "estado": "SP",
                "cidade": "São Paulo",
                "elo_cadeia": json.dumps(["produto_acabado"]),
                "produto_principal": "Marca que usa algodão orgânico colorido e tecidos reciclados",
                "escala": "amostra",
                "publico_alvo": "marcas",
                "status": "lead_validar",
                "nota_confianca": 1,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Mais marca usuária do que fornecedora. "
                    "Pode indicar cadeia de fornecimento ou servir como benchmark de materiais e storytelling. "
                    "Útil como referência de posicionamento e parceria de collab."
                ),
            },
            "produtos": [],
            "certificacoes": [],
        },

        {
            "fornecedor": {
                "codigo": "FOR-025",
                "nome": "Artesãos do APL Algodão Colorido — Paraíba",
                "tipo": "artesanato",
                "estado": "PB",
                "cidade": "Paraíba (vários municípios)",
                "elo_cadeia": json.dumps(["produto_acabado", "acabamento"]),
                "produto_principal": "Roupas, acessórios, bolsas, bijuterias e artigos domésticos em algodão colorido",
                "escala": "amostra",
                "publico_alvo": "marcas",
                "status": "lead_validar",
                "nota_confianca": 2,
                "site": None,
                "email_contato": None,
                "observacoes": (
                    "Arranjo Produtivo Local do algodão colorido orgânico da Paraíba — "
                    "reúne microfornecedores e artesãos. "
                    "Interessante para collab, cápsulas artesanais e narrativa de origem. "
                    "Contato via Projeto Algodão Paraíba / NCC / Embrapa / Empaer."
                ),
            },
            "produtos": [
                {
                    "nome": "Artesanato em Algodão Colorido Orgânico (bonecas, bolsas, bijuterias)",
                    "tipo": "produto_acabado",
                    "composicao": "100% Algodão Orgânico Colorido",
                    "cor": "beige / marrom / verde natural",
                    "tingimento": "natural",
                    "uso_recomendado": "Collab, cápsulas artesanais, presentes institucionais",
                    "disponivel": "a_validar",
                    "fonte": "manual",
                },
            ],
            "certificacoes": [
                {
                    "tipo": "A validar",
                    "apresentado": "pendente",
                    "escopo": "fibra/produto",
                    "nivel_confianca": "medio",
                    "evidencia": "Usa algodão colorido orgânico via cadeia do APL-PB. Pedir rastreabilidade por peça.",
                },
            ],
        },

    ]

    for item in novos:
        f = get_or_create_fornecedor(db, item["fornecedor"])
        for p in item.get("produtos", []):
            add_produto(db, f.id, p)
        for c in item.get("certificacoes", []):
            add_cert(db, f.id, c)

    db.commit()
    print(f"  [{len(novos)} novos fornecedores processados]")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    with Session(engine) as db:
        print("Iniciando seed do catálogo de fornecedores...")

        print("\n=== Seed manual (base) ===")
        seed_manual(db)

        print("\n=== Catálogo ampliado (P&M) ===")
        seed_catalogo_ampliado(db)

        # Scraping Etno Botânica
        scrape_etno_botanica(db)
        time.sleep(2)

        # Scraping Dalila
        scrape_dalila(db)

        print("\nConcluído. Banco atualizado com sucesso.")

        total_f = db.query(Fornecedor).count()
        total_p = db.query(ProdutoFornecedor).count()
        total_c = db.query(CertificacaoFornecedor).count()
        print(f"\n  Fornecedores: {total_f}")
        print(f"  Produtos:     {total_p}")
        print(f"  Certificações: {total_c}")


if __name__ == "__main__":
    main()
