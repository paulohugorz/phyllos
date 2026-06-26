from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import RevendedoraProfile


class AgentCustomerService(BaseAgent):
    NAME = "agent_customer_service"
    DESCRIPTION = "Ajuda a responder clientes com simpatia e foco em conversão"
    SYSTEM_PROMPT = """Você é o agente de atendimento da Revenda AI.
Ajude a revendedora a responder clientes de forma simpática, consultiva e vendedora.
Evite respostas frias, robóticas ou genéricas.
Sugira uma resposta pronta para enviar via WhatsApp.
Quando pertinente, faça pergunta qualificadora para entender melhor o que o cliente quer.
Use emojis com naturalidade."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        seller = self._get_seller(user_id)
        tone = (seller.tone if seller else None) or "simpático e popular"

        prompt = f"""Situação: {message}
Tom da revendedora: {tone}

Sugira uma resposta para enviar ao cliente no WhatsApp. Seja breve, amigável e focada em ajudar."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")

        return AgentResult(
            agent=self.NAME,
            content=response,
        )
