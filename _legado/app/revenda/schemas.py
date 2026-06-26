from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime


class ChatRequest(BaseModel):
    user_id: str
    message: str
    conversa_id: Optional[int] = None


class AgentAction(BaseModel):
    agent: str
    action: str
    data: dict = {}


class ChatResponse(BaseModel):
    message: str
    agents_used: List[str] = []
    actions: List[AgentAction] = []
    conversa_id: int


class ProfileCreate(BaseModel):
    user_id: str
    seller_name: Optional[str] = None
    city: Optional[str] = None
    brands: Optional[List[str]] = []
    default_margin: Optional[float] = 0.35
    tone: Optional[str] = "simpático e popular"
    monthly_goal: Optional[float] = None


class ClienteCreate(BaseModel):
    name: str
    phone: Optional[str] = None
    city: Optional[str] = None
    notes: Optional[str] = None


class ProdutoCreate(BaseModel):
    name: str
    brand: Optional[str] = None
    category: Optional[str] = None
    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    quantity: Optional[int] = 0


class VendaCreate(BaseModel):
    customer_name: Optional[str] = None
    total_amount: float
    payment_method: Optional[str] = None
    items: List[dict] = []
    delivery_date: Optional[str] = None


class AgendaItemCreate(BaseModel):
    tipo: str
    titulo: str
    descricao: Optional[str] = None
    due_date: Optional[str] = None


class DashboardResponse(BaseModel):
    total_vendas_mes: float
    lucro_estimado: float
    ticket_medio: float
    clientes_ativos: int
    alertas: List[str] = []
    prioridades: List[str] = []
