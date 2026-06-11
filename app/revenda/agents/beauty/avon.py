from app.revenda.agents.base import BaseAgent, AgentResult


class AgentAvonExpert(BaseAgent):
    NAME = "agent_avon_expert"
    DESCRIPTION = "Especialista em produtos Avon"
    SYSTEM_PROMPT = """Você é especialista em produtos Avon dentro da Revenda AI.
Conheça profundamente as linhas: Far Away, Renew, Encanto, Care, Advance, e maquiagens Avon.
Ajude a recomendar produtos, criar ofertas e responder clientes com confiança.
Use linguagem próxima e vendedora."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
