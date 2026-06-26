from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/database/fashion_os.db")
DATABASE_URL = f"sqlite:///{os.path.abspath(DB_PATH)}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def _migrate(conn):
    """Adiciona colunas novas sem Alembic. SQLite não suporta DROP/RENAME via ALTER."""

    def cols(table):
        return {r[1] for r in conn.execute(text(f"PRAGMA table_info({table})")).fetchall()}

    def add_if_missing(table, col, typedef):
        if _table_exists(conn, table) and col not in cols(table):
            conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {col} {typedef}"))

    # pecas — colunas DPP (UNIQUE não pode ir no ALTER; index criado separado)
    add_if_missing("pecas", "gtin",       "VARCHAR")
    add_if_missing("pecas", "dpp_uuid",   "VARCHAR")
    add_if_missing("pecas", "dpp_status", "VARCHAR DEFAULT 'rascunho'")

    if _table_exists(conn, "pecas"):
        conn.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS ix_pecas_gtin     ON pecas(gtin)"))
        conn.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS ix_pecas_dpp_uuid ON pecas(dpp_uuid)"))

    # fichas_tecnicas — colunas DPP adicionadas depois da criação inicial
    add_if_missing("fichas_tecnicas", "composicao_fibras",          "TEXT")
    add_if_missing("fichas_tecnicas", "instrucoes_reparo",          "TEXT")
    add_if_missing("fichas_tecnicas", "instrucoes_fim_de_vida",     "TEXT")
    add_if_missing("fichas_tecnicas", "certificacoes",              "TEXT")
    add_if_missing("fichas_tecnicas", "conteudo_reciclado_pct",     "FLOAT")
    add_if_missing("fichas_tecnicas", "pegada_carbono_kgco2e",      "FLOAT")
    add_if_missing("fichas_tecnicas", "durabilidade_ciclos_lavagem","INTEGER")

    # etapas_producao — coluna GLN adicionada depois
    add_if_missing("etapas_producao", "instalacao_gln", "VARCHAR")

    # peca_materiais — criada inteiramente via create_all (tabela nova)

    # fornecedores — colunas adicionadas após criação inicial
    add_if_missing("fornecedores", "conformidade_social", "VARCHAR DEFAULT 'nao_verificado'")
    add_if_missing("fornecedores", "site",                "VARCHAR")
    add_if_missing("fornecedores", "email_contato",       "VARCHAR")
    add_if_missing("fornecedores", "telefone",            "VARCHAR")
    add_if_missing("fornecedores", "observacoes",         "TEXT")

    # produtos_fornecedor — colunas extras e ISCM
    add_if_missing("produtos_fornecedor", "consumo_agua_litros_kg", "FLOAT")
    add_if_missing("produtos_fornecedor", "risco",                  "TEXT")
    add_if_missing("produtos_fornecedor", "uso_recomendado",        "TEXT")
    add_if_missing("produtos_fornecedor", "disponivel",             "VARCHAR DEFAULT 'a_validar'")
    add_if_missing("produtos_fornecedor", "fonte",                  "VARCHAR DEFAULT 'manual'")
    add_if_missing("produtos_fornecedor", "observacoes",            "TEXT")

    # peca_materiais — quantidade e peso para ponderação mássica no ISCM
    add_if_missing("peca_materiais", "quantidade_m", "FLOAT")
    add_if_missing("peca_materiais", "peso_kg",      "FLOAT")


def _table_exists(conn, name: str) -> bool:
    row = conn.execute(
        text("SELECT name FROM sqlite_master WHERE type='table' AND name=:n"),
        {"n": name},
    ).first()
    return row is not None


def run_migrations():
    with engine.begin() as conn:
        _migrate(conn)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
