from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import RevendedoraProfile


class AgentContent(BaseAgent):
    NAME = "agent_content"
    DESCRIPTION = "Cria posts, stories e mensagens de WhatsApp"
    SYSTEM_PROMPT = """Você é o agente de conteúdo da Revenda AI.
Crie conteúdos para Instagram, TikTok e WhatsApp para revendedoras brasileiras de cosméticos.
Linguagem próxima, animada, popular e autêntica. Evite parecer corporativo.
Adapte o formato ao pedido: legenda, story, Reels, carrossel ou mensagem de WhatsApp.
Use emojis com moderação. Inclua call-to-action."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        seller = self._get_seller(user_id)

        tone = (seller.tone if seller else None) or "simpático e popular"
        name = (seller.seller_name if seller else None) or "revendedora"

        prompt = f"""Solicitação: {message}

Perfil da revendedora: {name}, tom de comunicação: {tone}.

Crie o conteúdo solicitado. Se não for especificado o formato, crie legenda para Instagram + mensagem de WhatsApp."""

        response = self.call_llm(prompt, model="claude-haiku-4-5-20251001")

        return AgentResult(
            agent=self.NAME,
            content=response,
        )
