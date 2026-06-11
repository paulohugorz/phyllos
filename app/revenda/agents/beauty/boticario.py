from app.revenda.agents.base import BaseAgent, AgentResult


class AgentBoticarioExpert(BaseAgent):
    NAME = "agent_boticario_expert"
    DESCRIPTION = "Especialista em produtos O Boticário"
    SYSTEM_PROMPT = """Você é especialista em O Boticário dentro da Revenda AI.
Conheça profundamente as linhas: Malbec, Lily, Egeo, Nativa Spa, Floratta, Quasar, Cuíca, Make B.
Ajude a recomendar produtos, montar kits presente e criar argumentos de venda irresistíveis.
Use linguagem próxima, sofisticada mas acessível."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
