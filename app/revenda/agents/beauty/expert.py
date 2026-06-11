from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.agents.beauty.natura import AgentNaturaExpert
from app.revenda.agents.beauty.avon import AgentAvonExpert
from app.revenda.agents.beauty.boticario import AgentBoticarioExpert
from app.revenda.agents.beauty.perfume import AgentPerfumeExpert
from app.revenda.agents.beauty.skincare import AgentSkincareExpert
from app.revenda.agents.beauty.makeup import AgentMakeupExpert


BRAND_MAP = {
    "natura": AgentNaturaExpert,
    "avon": AgentAvonExpert,
    "boticário": AgentBoticarioExpert,
    "boticario": AgentBoticarioExpert,
    "o boticário": AgentBoticarioExpert,
    "perfume": AgentPerfumeExpert,
    "skincare": AgentSkincareExpert,
    "pele": AgentSkincareExpert,
    "maquiagem": AgentMakeupExpert,
    "makeup": AgentMakeupExpert,
}


class AgentBeautyExpert(BaseAgent):
    NAME = "agent_beauty_expert"
    DESCRIPTION = "Especialista geral em beleza — cosméticos, perfumes, marcas"
    SYSTEM_PROMPT = """Você é especialista em beleza da Revenda AI.
Responda dúvidas sobre cosméticos, perfumes, skincare e maquiagem de forma simples e prática.
Ajude a revendedora a recomendar produtos, criar argumentos de venda e responder clientes com confiança."""

    def process(self, payload: dict, context: dict) -> AgentResult:
        message = payload.get("message", "").lower()

        for keyword, AgentClass in BRAND_MAP.items():
            if keyword in message:
                agent = AgentClass(db=self.db)
                return agent.process(payload, context)

        response = self.call_llm(payload.get("message", ""), model="claude-haiku-4-5-20251001")
        return AgentResult(agent=self.NAME, content=response)
