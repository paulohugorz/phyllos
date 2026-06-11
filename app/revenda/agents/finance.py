from datetime import datetime, date, timedelta
from sqlalchemy import func
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import Venda, VendaItem, RevendedoraProfile


class AgentFinance(BaseAgent):
    NAME = "agent_finance"
    DESCRIPTION = "Acompanha saúde financeira da revendedora"
    SYSTEM_PROMPT = """Você é o agente financeiro da Revenda AI.
Com base nos dados financeiros fornecidos, gere um resumo simples, direto e motivador para a revendedora.
Use linguagem informal e amigável. Inclua faturamento, lucro estimado e ticket médio."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def get_monthly_stats(self, seller_id: int, year: int = None, month: int = None) -> dict:
        today = date.today()
        year = year or today.year
        month = month or today.month
        start = datetime(year, month, 1)
        if month == 12:
            end = datetime(year + 1, 1, 1)
        else:
            end = datetime(year, month + 1, 1)

        vendas = self.db.query(Venda).filter(
            Venda.seller_id == seller_id,
            Venda.sale_date >= start,
            Venda.sale_date < end,
        ).all()

        total = sum(v.total_amount for v in vendas)
        count = len(vendas)
        ticket_medio = total / count if count else 0

        lucro = 0.0
        for v in vendas:
            for item in v.itens:
                if item.unit_cost:
                    lucro += (item.unit_price - item.unit_cost) * item.quantity

        return {
            "total_vendas": total,
            "num_vendas": count,
            "ticket_medio": ticket_medio,
            "lucro_estimado": lucro,
            "mes": f"{month:02d}/{year}",
        }

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False)

        stats = self.get_monthly_stats(seller.id)
        margin = seller.default_margin or 0.35
        lucro = stats["lucro_estimado"] or stats["total_vendas"] * margin

        prompt = f"""Dados financeiros da revendedora:
- Mês: {stats['mes']}
- Faturamento: R${stats['total_vendas']:.2f}
- Número de vendas: {stats['num_vendas']}
- Ticket médio: R${stats['ticket_medio']:.2f}
- Lucro estimado: R${lucro:.2f}
- Meta mensal: R${seller.monthly_goal or 0:.2f}

Gere um resumo motivador e prático."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")

        return AgentResult(
            agent=self.NAME,
            content=response,
            data=stats,
        )
