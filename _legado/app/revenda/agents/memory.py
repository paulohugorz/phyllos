import json
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import RevendedoraProfile


class AgentMemory(BaseAgent):
    NAME = "agent_memory"
    DESCRIPTION = "Mantém contexto permanente da revendedora"
    SYSTEM_PROMPT = """Você é o agente de memória da Revenda AI.
Sua função é extrair e atualizar informações permanentes sobre a revendedora a partir de mensagens.

Extraia apenas dados explicitamente mencionados como:
- nome, cidade, marcas que vende, margem padrão, metas, estilo preferido

Retorne um JSON com os campos identificados para atualização.
Se nenhum dado de perfil for mencionado, retorne {}.

Responda APENAS com JSON válido, sem texto adicional."""

    def get_or_create_profile(self, user_id: str) -> RevendedoraProfile:
        profile = self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()
        if not profile:
            profile = RevendedoraProfile(user_id=user_id)
            self.db.add(profile)
            self.db.commit()
            self.db.refresh(profile)
        return profile

    def get_context(self, user_id: str) -> dict:
        profile = self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()
        if not profile:
            return {}
        return {
            "seller_name": profile.seller_name,
            "city": profile.city,
            "brands": profile.brands or [],
            "default_margin": profile.default_margin,
            "tone": profile.tone,
            "monthly_goal": profile.monthly_goal,
        }

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")

        profile = self.get_or_create_profile(user_id)

        try:
            raw = self.call_llm(message)
            updates = json.loads(raw)
        except Exception:
            updates = {}

        updated_fields = []
        if updates.get("seller_name"):
            profile.seller_name = updates["seller_name"]
            updated_fields.append("nome")
        if updates.get("city"):
            profile.city = updates["city"]
            updated_fields.append("cidade")
        if updates.get("brands"):
            existing = profile.brands or []
            new_brands = [b for b in updates["brands"] if b not in existing]
            profile.brands = existing + new_brands
            updated_fields.append("marcas")
        if updates.get("default_margin"):
            profile.default_margin = updates["default_margin"]
            updated_fields.append("margem")
        if updates.get("monthly_goal"):
            profile.monthly_goal = updates["monthly_goal"]
            updated_fields.append("meta mensal")
        if updates.get("tone"):
            profile.tone = updates["tone"]

        if updated_fields:
            self.db.commit()

        return AgentResult(
            agent=self.NAME,
            content=f"Perfil atualizado: {', '.join(updated_fields)}" if updated_fields else "",
            data=updates,
        )
