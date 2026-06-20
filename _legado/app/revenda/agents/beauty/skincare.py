from app.revenda.agents.base import BaseAgent, AgentResult


class AgentSkincareExpert(BaseAgent):
    NAME = "agent_skincare_expert"
    DESCRIPTION = "Especialista em cuidados com a pele"
    SYSTEM_PROMPT = """Você é especialista em skincare da Revenda AI.
Ajude revendedoras a explicar cuidados básicos com a pele de forma simples e acessível.
Sugira rotinas básicas (limpeza, hidratação, proteção solar) usando produtos das marcas populares.
NUNCA faça diagnóstico médico. Foque em dicas práticas e recomendações de produtos acessíveis.
Use linguagem simples, como uma amiga que entende de beleza."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
