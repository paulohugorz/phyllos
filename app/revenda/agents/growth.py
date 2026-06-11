from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.agents.finance import AgentFinance
from app.revenda.models import RevendedoraProfile


class AgentGrowth(BaseAgent):
    NAME = "agent_growth"
    DESCRIPTION = "Sugere ações para aumentar vendas e crescimento do negócio"
    SYSTEM_PROMPT = """Você é o agente de crescimento da Revenda AI.
Analise os dados da revendedora e sugira ações práticas e realizáveis para aumentar o faturamento.
Seja específica, com passos concretos para a semana atual. Linguagem motivadora e direta."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        seller = self._get_seller(user_id)

        finance_agent = AgentFinance(db=self.db)
        stats = {}
        if seller:
            stats = finance_agent.get_monthly_stats(seller.id)

        prompt = f"""Pedido da revendedora: {message}

Dados do negócio:
- Faturamento este mês: R${stats.get('total_vendas', 0):.2f}
- Vendas realizadas: {stats.get('num_vendas', 0)}
- Ticket médio: R${stats.get('ticket_medio', 0):.2f}
- Meta mensal: R${(seller.monthly_goal or 0):.2f}

Sugira 3-5 ações práticas para esta semana focadas em aumentar vendas e fidelizar clientes."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response, data=stats)
