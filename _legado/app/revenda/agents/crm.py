import json
from datetime import date
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import Cliente, RevendedoraProfile


class AgentCRM(BaseAgent):
    NAME = "agent_crm"
    DESCRIPTION = "Organiza clientes e histórico de relacionamento"
    SYSTEM_PROMPT = """Você é o agente de CRM da Revenda AI.
Extraia informações de clientes da mensagem e retorne JSON:

{
  "action": "create" | "update" | "query",
  "client_name": "...",
  "phone": "...",
  "city": "...",
  "notes": "...",
  "preferred_brands": [...],
  "favorite_products": [...],
  "average_ticket": number,
  "birthday": "YYYY-MM-DD"
}

Inclua apenas campos mencionados. Responda APENAS com JSON válido."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def _find_or_create_client(self, seller_id: int, name: str) -> Cliente:
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

    def get_inactive_clients(self, seller_id: int, days: int = 30) -> list[Cliente]:
        from datetime import datetime, timedelta
        cutoff = date.today() - timedelta(days=days)
        return self.db.query(Cliente).filter(
            Cliente.seller_id == seller_id,
            Cliente.last_purchase_date <= cutoff,
            Cliente.is_active == True,
        ).all()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        client_name = payload.get("client_name")

        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False, error="Perfil não encontrado")

        try:
            raw = self.call_llm(message)
            data = json.loads(raw)
        except Exception:
            data = {}

        name = client_name or data.get("client_name")
        if not name:
            return AgentResult(agent=self.NAME, content="", data={})

        client = self._find_or_create_client(seller.id, name)
        updated = []

        if data.get("phone"):
            client.phone = data["phone"]
            updated.append("telefone")
        if data.get("city"):
            client.city = data["city"]
            updated.append("cidade")
        if data.get("notes"):
            client.notes = (client.notes or "") + " " + data["notes"]
            updated.append("observações")
        if data.get("preferred_brands"):
            client.preferred_brands = data["preferred_brands"]
            updated.append("marcas preferidas")
        if data.get("favorite_products"):
            client.favorite_products = data["favorite_products"]
            updated.append("produtos favoritos")
        if data.get("average_ticket"):
            client.average_ticket = data["average_ticket"]
            updated.append("ticket médio")

        if updated:
            self.db.commit()

        desc = f"Cliente {client.name} atualizado: {', '.join(updated)}." if updated else f"Cliente {client.name} encontrado."
        return AgentResult(
            agent=self.NAME,
            content=desc,
            actions=[{"action": "crm_update", "client_id": client.id, "client_name": client.name}],
            data={"client_id": client.id, "client_name": client.name},
        )
