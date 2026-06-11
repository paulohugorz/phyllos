from sqlalchemy import (
    Column, Integer, String, Float, Text, DateTime, Date,
    ForeignKey, Boolean, JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class RevendedoraProfile(Base):
    __tablename__ = "revenda_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, nullable=False, index=True)
    seller_name = Column(String)
    city = Column(String)
    brands = Column(JSON, default=list)
    default_margin = Column(Float, default=0.35)
    tone = Column(String, default="simpático e popular")
    monthly_goal = Column(Float)
    extra_data = Column(JSON, default=dict)
    onboarding_step = Column(Integer, default=0)  # 0=novo 1-5=em andamento 99=completo
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

    clientes = relationship("Cliente", back_populates="vendedora")
    produtos = relationship("Produto", back_populates="vendedora")
    vendas = relationship("Venda", back_populates="vendedora")
    agenda_itens = relationship("AgendaItem", back_populates="vendedora")
    conversas = relationship("Conversa", back_populates="vendedora")


class Cliente(Base):
    __tablename__ = "revenda_clientes"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("revenda_profiles.id"), nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String)
    birthday = Column(Date)
    city = Column(String)
    preferred_brands = Column(JSON, default=list)
    favorite_products = Column(JSON, default=list)
    average_ticket = Column(Float)
    last_purchase_date = Column(Date)
    notes = Column(Text)
    is_active = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

    vendedora = relationship("RevendedoraProfile", back_populates="clientes")
    compras = relationship("Venda", back_populates="cliente")


class Produto(Base):
    __tablename__ = "revenda_produtos"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("revenda_profiles.id"), nullable=False)
    name = Column(String, nullable=False)
    brand = Column(String)
    category = Column(String)
    purchase_price = Column(Float)
    sale_price = Column(Float)
    quantity = Column(Integer, default=0)
    expiration_date = Column(Date)
    sku = Column(String)
    notes = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

    vendedora = relationship("RevendedoraProfile", back_populates="produtos")
    itens_venda = relationship("VendaItem", back_populates="produto")


class Venda(Base):
    __tablename__ = "revenda_vendas"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("revenda_profiles.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("revenda_clientes.id"), nullable=True)
    sale_date = Column(DateTime(timezone=True), server_default=func.now())
    total_amount = Column(Float, nullable=False)
    payment_method = Column(String)
    delivery_status = Column(String, default="pendente")
    delivery_date = Column(Date)
    notes = Column(Text)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    vendedora = relationship("RevendedoraProfile", back_populates="vendas")
    cliente = relationship("Cliente", back_populates="compras")
    itens = relationship("VendaItem", back_populates="venda")


class VendaItem(Base):
    __tablename__ = "revenda_venda_itens"

    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("revenda_vendas.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("revenda_produtos.id"), nullable=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, nullable=False)
    unit_cost = Column(Float)

    venda = relationship("Venda", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_venda")


class AgendaItem(Base):
    __tablename__ = "revenda_agenda"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("revenda_profiles.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("revenda_clientes.id"), nullable=True)
    tipo = Column(String, nullable=False)  # entrega, cobranca, postagem, reposicao, pos_venda
    titulo = Column(String, nullable=False)
    descricao = Column(Text)
    due_date = Column(DateTime(timezone=True))
    is_done = Column(Boolean, default=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    vendedora = relationship("RevendedoraProfile", back_populates="agenda_itens")


class Conversa(Base):
    __tablename__ = "revenda_conversas"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("revenda_profiles.id"), nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    vendedora = relationship("RevendedoraProfile", back_populates="conversas")
    mensagens = relationship("Mensagem", back_populates="conversa", order_by="Mensagem.criado_em")


class Mensagem(Base):
    __tablename__ = "revenda_mensagens"

    id = Column(Integer, primary_key=True, index=True)
    conversa_id = Column(Integer, ForeignKey("revenda_conversas.id"), nullable=False)
    role = Column(String, nullable=False)  # user | assistant
    content = Column(Text, nullable=False)
    agents_used = Column(JSON, default=list)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    conversa = relationship("Conversa", back_populates="mensagens")
