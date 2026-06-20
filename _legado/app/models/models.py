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
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    colecao = relationship("Colecao", back_populates="pecas")
    ficha_tecnica = relationship("FichaTecnica", back_populates="peca", uselist=False)
    referencias_visuais = relationship("PecaVisualReference", back_populates="peca")


class FichaTecnica(Base):
    __tablename__ = "fichas_tecnicas"

    id = Column(Integer, primary_key=True, index=True)
    peca_id = Column(Integer, ForeignKey("pecas.id"), unique=True)
    descricao_tecnica = Column(Text)
    materiais = Column(Text)
    construcao = Column(Text)
    medidas = Column(Text)
    qualidade = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    peca = relationship("Peca", back_populates="ficha_tecnica")


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
