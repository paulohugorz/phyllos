from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import Produto, RevendedoraProfile


class AgentPromotions(BaseAgent):
    NAME = "agent_promotions"
    DESCRIPTION = "Cria promoções inteligentes com base no estoque"
    SYSTEM_PROMPT = """Você é o agente de promoções da Revenda AI.
Crie sugestões de promoções, kits e ofertas criativas para revendedoras de cosméticos.
Use linguagem animada e vendedora. Foque em aumentar o ticket médio e girar o estoque parado.
Seja específica com nomes de produtos, preços sugeridos e argumentos de venda."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False)

        products = self.db.query(Produto).filter(
            Produto.seller_id == seller.id
        ).all()

        parados = [p for p in products if p.quantity and p.quantity > 3]
        estoque_info = "\n".join(
            f"- {p.name} ({p.brand or 'sem marca'}): {p.quantity} unidades, preço R${p.sale_price or '?'}"
            for p in products[:20]
        )

        prompt = f"""Solicitação da revendedora: {message}

Estoque disponível:
{estoque_info or 'Sem dados de estoque.'}

Produtos com mais unidades (possível estoque parado):
{', '.join(p.name for p in parados) or 'nenhum identificado'}

Crie 2-3 sugestões de promoções ou kits usando os produtos disponíveis.
Seja criativa, inclua preço sugerido e argumento de venda."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")

        return AgentResult(
            agent=self.NAME,
            content=response,
            data={"parados": [p.name for p in parados]},
        )
