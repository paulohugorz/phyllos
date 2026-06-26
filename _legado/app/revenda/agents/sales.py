import json
from datetime import date
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import Venda, VendaItem, Cliente, Produto, RevendedoraProfile


class AgentSales(BaseAgent):
    NAME = "agent_sales"
    DESCRIPTION = "Registra vendas"
    SYSTEM_PROMPT = """Você é o agente de vendas da Revenda AI.
Extraia dados de venda da mensagem e retorne JSON:

{
  "items": [
    {"product_name": "...", "brand": "...", "quantity": 1, "unit_price": 0.0}
  ],
  "client_name": "...",
  "total_amount": 0.0,
  "payment_method": "pix" | "dinheiro" | "cartao" | "fiado" | null,
  "delivery_date": "YYYY-MM-DD" | null,
  "notes": "..."
}

Se o total não for mencionado, some os itens.
Interprete "amanhã" como amanhã em relação à data atual.
Responda APENAS com JSON válido."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def _find_client(self, seller_id: int, name: str) -> Cliente | None:
        if not name:
            return None
        name_lower = name.strip().lower()
        clients = self.db.query(Cliente).filter(Cliente.seller_id == seller_id).all()
        for c in clients:
            if c.name.lower() == name_lower:
                return c
        client = Cliente(seller_id=seller_id, name=name.strip().title())
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")

        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False, error="Perfil não encontrado")

        try:
            raw = self.call_llm(message)
            data = json.loads(raw)
        except Exception:
            return AgentResult(agent=self.NAME, content="Não consegui identificar a venda.", success=False)

        items = data.get("items", [])
        if not items and not data.get("total_amount"):
            return AgentResult(agent=self.NAME, content="", data={})

        total = data.get("total_amount") or sum(
            i.get("unit_price", 0) * i.get("quantity", 1) for i in items
        )
        client = self._find_client(seller.id, data.get("client_name"))

        venda = Venda(
            seller_id=seller.id,
            customer_id=client.id if client else None,
            total_amount=total,
            payment_method=data.get("payment_method"),
            delivery_status="pendente" if data.get("delivery_date") else "entregue",
            notes=data.get("notes"),
        )
        self.db.add(venda)
        self.db.flush()

        for item in items:
            vi = VendaItem(
                sale_id=venda.id,
                product_name=item.get("product_name", "Produto"),
                quantity=item.get("quantity", 1),
                unit_price=item.get("unit_price", total),
            )
            self.db.add(vi)

        if client:
            client.last_purchase_date = date.today()

        self.db.commit()

        client_desc = f" para {client.name}" if client else ""
        payment_desc = f" via {data['payment_method']}" if data.get("payment_method") else ""
        items_desc = ", ".join(
            f"{i.get('quantity', 1)} {i.get('product_name', '')}" for i in items
        ) if items else "produto"

        return AgentResult(
            agent=self.NAME,
            content=f"Venda registrada: {items_desc}{client_desc} — R${total:.2f}{payment_desc}.",
            actions=[{"action": "sale_registered", "sale_id": venda.id, "total": total}],
            data={"sale_id": venda.id, "total": total, "client_name": data.get("client_name")},
        )
