from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class Colecao(Base):
    __tablename__ = "colecoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(Text)
    status = Column(String, default="planejamento")
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    pecas = relationship("Peca", back_populates="colecao")


class Peca(Base):
    __tablename__ = "pecas"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, nullable=False, index=True)
    nome = Column(String, nullable=False)
    colecao_id = Column(Integer, ForeignKey("colecoes.id"))
    status = Column(String, default="ideia")
    prioridade = Column(String, default="media")
    tecido = Column(String)
    custo_estimado = Column(Float)
    preco_sugerido = Column(Float)
    observacoes = Column(Text)
    prompt_croqui = Column(Text)
    prompt_foto = Column(Text)
    # DPP — Digital Product Passport
    gtin = Column(String, unique=True, nullable=True, index=True)
    dpp_uuid = Column(String, unique=True, nullable=True)
    dpp_status = Column(String, default="rascunho")  # rascunho | publicado | revogado
    area_peca_m2 = Column(Float)
    perda_corte_pct = Column(Float)
    lote_quantidade = Column(Integer)
    pais_fabricacao = Column(String)
    dpp_version = Column(String, default="1.0")
    data_publicacao = Column(DateTime(timezone=True))
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    colecao = relationship("Colecao", back_populates="pecas")
    ficha_tecnica = relationship("FichaTecnica", back_populates="peca", uselist=False)
    referencias_visuais = relationship("PecaVisualReference", back_populates="peca")
    etapas_producao = relationship("EtapaProducao", back_populates="peca")
    materiais = relationship("PecaMaterial", back_populates="peca", cascade="all, delete-orphan")


class FichaTecnica(Base):
    __tablename__ = "fichas_tecnicas"

    id = Column(Integer, primary_key=True, index=True)
    peca_id = Column(Integer, ForeignKey("pecas.id"), unique=True)
    descricao_tecnica = Column(Text)
    materiais = Column(Text)
    construcao = Column(Text)
    medidas = Column(Text)
    qualidade = Column(Text)
    # DPP — campos estruturados para Digital Product Passport
    # JSON: [{"fibra": "poliester_reciclado", "pct": 78}, {"fibra": "elastano", "pct": 22}]
    composicao_fibras = Column(Text)
    instrucoes_reparo = Column(Text)
    instrucoes_fim_de_vida = Column(Text)
    # JSON: [{"nome": "OEKO-TEX", "numero": "XX-XXXXX", "validade": "2027-06-01"}]
    certificacoes = Column(Text)
    conteudo_reciclado_pct = Column(Float)
    pegada_carbono_kgco2e = Column(Float)
    gramatura_g_m2 = Column(Float)
    agua_litros_kg = Column(Float)
    energia_kwh_kg = Column(Float)
    carbono_kgco2e_kg = Column(Float)
    fonte_agua_litros_kg = Column(Text)
    fonte_energia_kwh_kg = Column(Text)
    fonte_carbono_kgco2e_kg = Column(Text)
    metodologia_fatores_impacto = Column(Text)
    area_total_requerida_m2 = Column(Float)
    area_perdida_m2 = Column(Float)
    peso_peca_kg = Column(Float)
    agua_peca_litros = Column(Float)
    energia_peca_kwh = Column(Float)
    evidencia_statuses = Column(Text)
    durabilidade_ciclos_lavagem = Column(Integer)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    peca = relationship("Peca", back_populates="ficha_tecnica")


class EtapaProducao(Base):
    """Rastreabilidade por etapa da cadeia produtiva (Tier 1+)."""
    __tablename__ = "etapas_producao"

    id = Column(Integer, primary_key=True, index=True)
    peca_id = Column(Integer, ForeignKey("pecas.id"), nullable=False)
    # fiacao | tecelagem | corte | costura | tingimento | acabamento | lavanderia
    etapa = Column(String, nullable=False)
    pais = Column(String)
    instalacao_nome = Column(String)
    instalacao_gln = Column(String)  # Global Location Number (GS1)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    peca = relationship("Peca", back_populates="etapas_producao")


class VisualReference(Base):
    __tablename__ = "visual_references"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)
    titulo = Column(String, nullable=False)
    fonte = Column(String, nullable=False)
    source_url = Column(Text, nullable=False)
    image_url = Column(Text)
    categoria = Column(String, default="athleisure")
    contexto_uso = Column(Text, nullable=False)
    cenario = Column(Text, nullable=False)
    pecas_chave = Column(Text)
    paleta = Column(Text)
    styling_notes = Column(Text)
    atributos_visuais = Column(Text)
    prompt_tokens = Column(Text)
    prompt_negativo = Column(Text)
    direitos_uso = Column(Text, default="Referencia externa para curadoria. Nao copiar imagem para campanha ou produto final.")
    status = Column(String, default="prospectado")
    prioridade = Column(Integer, default=3)
    curador = Column(String, default="Codex")
    revisado_em = Column(String, nullable=False, server_default=func.current_date())
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    pecas = relationship("PecaVisualReference", back_populates="referencia_visual")


class PecaVisualReference(Base):
    __tablename__ = "peca_visual_references"
    __table_args__ = (
        UniqueConstraint("peca_id", "visual_reference_id", "tipo_vinculo"),
    )

    id = Column(Integer, primary_key=True, index=True)
    peca_id = Column(Integer, ForeignKey("pecas.id"), nullable=False)
    visual_reference_id = Column(Integer, ForeignKey("visual_references.id"), nullable=False)
    tipo_vinculo = Column(String, default="moodboard")
    observacoes = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    peca = relationship("Peca", back_populates="referencias_visuais")
    referencia_visual = relationship("VisualReference", back_populates="pecas")


# ---------------------------------------------------------------------------
# Catálogo de Fornecedores de Matérias-Primas
# ---------------------------------------------------------------------------

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, index=True)
    # FOR-001, FOR-002 …
    codigo = Column(String, unique=True, nullable=False, index=True)
    nome = Column(String, nullable=False)
    # cooperativa | industria | marca | distribuidor | projeto_agroecologico
    tipo = Column(String)
    estado = Column(String)
    cidade = Column(String)
    # JSON array: ["fibra","fiacao","tecido","malha","confeccao","produto_acabado"]
    elo_cadeia = Column(Text)
    produto_principal = Column(String)
    # amostra | pequeno_lote | medio_lote | industrial
    escala = Column(String)
    # b2b | b2c | cooperativas | marcas | exportacao (pode ser lista JSON)
    publico_alvo = Column(String)
    # confirmado | lead_validar | parceiro_estrategico
    status = Column(String, default="lead_validar")
    # 1–5 (ver critério no catálogo)
    nota_confianca = Column(Integer)
    # ISCM — conformidade trabalhista declarada/verificada
    # nao_verificado | em_processo | certificado_abvtex | certificado_sa8000
    conformidade_social = Column(String, default="nao_verificado")
    site = Column(String)
    email_contato = Column(String)
    telefone = Column(String)
    observacoes = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    produtos = relationship("ProdutoFornecedor", back_populates="fornecedor", cascade="all, delete-orphan")
    certificacoes = relationship("CertificacaoFornecedor", back_populates="fornecedor", cascade="all, delete-orphan")


class ProdutoFornecedor(Base):
    __tablename__ = "produtos_fornecedor"

    id = Column(Integer, primary_key=True, index=True)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"), nullable=False)
    nome = Column(String, nullable=False)
    codigo_fornecedor = Column(String)
    # pluma | fio | malha | tecido_plano | lona | produto_acabado
    tipo = Column(String)
    composicao = Column(String)
    cor = Column(String)
    # sem_tingimento | vegetal | convencional | natural
    tingimento = Column(String, default="sem_tingimento")
    gramatura_gm2 = Column(Float)
    largura_m = Column(Float)
    # pedido mínimo — string flexível: "100m", "200kg", "1 rolo"
    moq = Column(String)
    preco_referencia = Column(Float)
    # metro | kg | rolo | unidade
    unidade_preco = Column(String)
    uso_recomendado = Column(Text)
    risco = Column(Text)
    # sim | nao | a_validar
    disponivel = Column(String, default="a_validar")
    # scraping | manual | email | catalogo_pdf
    fonte = Column(String, default="manual")
    # ISCM — dado primário de consumo hídrico; L de água por kg de material produzido
    consumo_agua_litros_kg = Column(Float, nullable=True)
    observacoes = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    fornecedor = relationship("Fornecedor", back_populates="produtos")
    usos_em_pecas = relationship("PecaMaterial", back_populates="produto")


class CertificacaoFornecedor(Base):
    __tablename__ = "certificacoes_fornecedor"

    id = Column(Integer, primary_key=True, index=True)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"), nullable=False)
    # GOTS | OCS | IBD | ECOCERT | SisOrg | Participativa | USDA | EU_Organic
    tipo = Column(String, nullable=False)
    # sim | nao | pendente
    apresentado = Column(String, default="pendente")
    validade = Column(String)
    # fibra | fio | tecido | confeccao | produto_final
    escopo = Column(String)
    numero_licenca = Column(String)
    # URL, caminho de PDF, nota fiscal
    evidencia = Column(Text)
    # alto | medio | baixo
    nivel_confianca = Column(String)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    fornecedor = relationship("Fornecedor", back_populates="certificacoes")


class PecaMaterial(Base):
    """Vínculo entre uma peça e uma matéria-prima do catálogo de fornecedores."""
    __tablename__ = "peca_materiais"

    id = Column(Integer, primary_key=True, index=True)
    peca_id = Column(Integer, ForeignKey("pecas.id"), nullable=False)
    produto_fornecedor_id = Column(Integer, ForeignKey("produtos_fornecedor.id"), nullable=False)
    # principal | forro | ribana | aviamento | entretela | elastico
    funcao = Column(String, default="principal")
    # metros de tecido usados nesta peça (opcional — para cálculo de peso)
    quantidade_m = Column(Float, nullable=True)
    # peso em kg deste material na peça final (calculado ou informado)
    peso_kg = Column(Float, nullable=True)
    observacoes = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    peca = relationship("Peca", back_populates="materiais")
    produto = relationship("ProdutoFornecedor", back_populates="usos_em_pecas")
