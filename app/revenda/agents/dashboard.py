from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.agents.finance import AgentFinance
from app.revenda.agents.inventory import AgentInventory
from app.revenda.agents.after_sales import AgentAfterSales
from app.revenda.agents.calendar import AgentCalendar
from app.revenda.models import RevendedoraProfile


class AgentDashboard(BaseAgent):
    NAME = "agent_dashboard"
    DESCRIPTION = "Gera resumo diário executivo da revendedora"
    SYSTEM_PROMPT = """Você é o agente de dashboard da Revenda AI.
Transforme os dados da revendedora em um resumo diário simples e acionável.
Estruture como: o que aconteceu, o que precisa de atenção, e o que fazer agora.
Seja concisa, clara e prática."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="Nenhum perfil encontrado. Diga seu nome para começar!")

        finance = AgentFinance(db=self.db)
        inventory = AgentInventory(db=self.db)
        after_sales = AgentAfterSales(db=self.db)
        calendar = AgentCalendar(db=self.db)

        stats = finance.get_monthly_stats(seller.id)
        low_stock = inventory.get_low_stock(seller.id)
        followups = after_sales.get_clients_for_followup(seller.id)
        pending = calendar.get_pending(seller.id)

        prompt = f"""Dados da revendedora {seller.seller_name or ''}:

Financeiro este mês:
- Faturamento: R${stats['total_vendas']:.2f}
- Vendas: {stats['num_vendas']}
- Ticket médio: R${stats['ticket_medio']:.2f}

Alertas de estoque:
{', '.join(p.name for p in low_stock) or 'Nenhum'}

Clientes para reativar:
{', '.join(c['name'] for c in followups) or 'Nenhum'}

Tarefas pendentes:
{', '.join(t.titulo for t in pending) or 'Nenhuma'}

Gere um resumo diário curto e acionável."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")
        return AgentResult(
            agent=self.NAME,
            content=response,
            data={
                "stats": stats,
                "alerts": [p.name for p in low_stock],
                "followups": [c["name"] for c in followups],
            },
        )
