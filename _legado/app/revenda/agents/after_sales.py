from datetime import date, timedelta
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import Cliente, Venda, RevendedoraProfile


class AgentAfterSales(BaseAgent):
    NAME = "agent_after_sales"
    DESCRIPTION = "Gera recompra com sugestões de pós-venda"
    SYSTEM_PROMPT = """Você é o agente de pós-venda da Revenda AI.
Crie mensagens de reativação e sugestões de recompra para clientes.
Linguagem calorosa, pessoal e natural — como uma amiga que vende cosméticos.
Sempre sugira produtos específicos quando possível. Use emojis com moderação."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def get_clients_for_followup(self, seller_id: int, days: int = 28) -> list[dict]:
        cutoff = date.today() - timedelta(days=days)
        clients = self.db.query(Cliente).filter(
            Cliente.seller_id == seller_id,
            Cliente.last_purchase_date <= cutoff,
            Cliente.is_active == True,
        ).all()
        return [
            {
                "name": c.name,
                "last_purchase": str(c.last_purchase_date),
                "favorite_products": c.favorite_products or [],
                "days_ago": (date.today() - c.last_purchase_date).days if c.last_purchase_date else None,
            }
            for c in clients[:10]
        ]

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False)

        followups = self.get_clients_for_followup(seller.id)
        followup_info = "\n".join(
            f"- {c['name']}: última compra há {c['days_ago']} dias, prefere {', '.join(c['favorite_products']) or 'produtos variados'}"
            for c in followups
        ) if followups else "Nenhum cliente para reativar no momento."

        prompt = f"""Pedido: {message}

Clientes que podem precisar de reativação:
{followup_info}

Crie sugestões de mensagens de pós-venda e reativação personalizadas."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")

        return AgentResult(
            agent=self.NAME,
            content=response,
            data={"clients_for_followup": followups},
        )
