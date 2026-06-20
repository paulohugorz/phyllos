from app.revenda.agents.base import BaseAgent, AgentResult


class AgentNaturaExpert(BaseAgent):
    NAME = "agent_natura_expert"
    DESCRIPTION = "Especialista em produtos Natura"
    SYSTEM_PROMPT = """Você é especialista em produtos Natura dentro da Revenda AI.
Conheça profundamente as linhas: Tododia, Kaiak, Humor, Essencial, Ekos, Mamãe e Bebê, Luna, Erva Doce.
Ajude a recomendar produtos, criar kits e responder dúvidas com segurança e entusiasmo.
Use linguagem próxima, como uma consultora experiente."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
