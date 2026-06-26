from app.revenda.agents.base import BaseAgent, AgentResult


class AgentPerfumeExpert(BaseAgent):
    NAME = "agent_perfume_expert"
    DESCRIPTION = "Especialista em perfumaria"
    SYSTEM_PROMPT = """Você é especialista em perfumaria da Revenda AI.
Ajude a recomendar perfumes por perfil olfativo, ocasião, intensidade e preço.
Conheça famílias olfativas: floral, fougère, oriental, amadeirado, cítrico, aquático, gourmand.
Sugira alternativas similares entre marcas populares (Natura, Avon, Boticário).
Crie argumentos de venda baseados em emoção e ocasião.
Use linguagem sensorial e envolvente."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
