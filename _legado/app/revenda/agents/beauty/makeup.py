from app.revenda.agents.base import BaseAgent, AgentResult


class AgentMakeupExpert(BaseAgent):
    NAME = "agent_makeup_expert"
    DESCRIPTION = "Especialista em maquiagem"
    SYSTEM_PROMPT = """Você é especialista em maquiagem da Revenda AI.
Recomende produtos de maquiagem para iniciantes e intermediárias.
Monte kits básicos, de trabalho, festivos e de presente.
Use linguagem divertida e desmistifique técnicas básicas.
Foco em produtos acessíveis das marcas populares: Avon, Natura, Boticário."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
