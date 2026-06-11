import json
from datetime import datetime, date, timedelta
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import AgendaItem, RevendedoraProfile


class AgentCalendar(BaseAgent):
    NAME = "agent_calendar"
    DESCRIPTION = "Organiza rotina da revendedora com lembretes e tarefas"
    SYSTEM_PROMPT = """Você é o agente de agenda da Revenda AI.
Extraia tarefas e lembretes da mensagem e retorne JSON:

{
  "tasks": [
    {
      "tipo": "entrega" | "cobranca" | "postagem" | "reposicao" | "pos_venda" | "outro",
      "titulo": "...",
      "descricao": "...",
      "due_date": "YYYY-MM-DD HH:MM" | null
    }
  ]
}

"amanhã" = amanhã. "semana que vem" = em 7 dias. Interprete datas relativas à data de hoje.
Responda APENAS com JSON válido."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def get_pending(self, seller_id: int) -> list[AgendaItem]:
        return self.db.query(AgendaItem).filter(
            AgendaItem.seller_id == seller_id,
            AgendaItem.is_done == False,
        ).order_by(AgendaItem.due_date).limit(10).all()

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")
        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False)

        try:
            raw = self.call_llm(message)
            data = json.loads(raw)
        except Exception:
            data = {"tasks": []}

        created = []
        for task in data.get("tasks", []):
            titulo = task.get("titulo", "")
            if not titulo:
                continue
            due = None
            if task.get("due_date"):
                try:
                    due = datetime.fromisoformat(task["due_date"])
                except Exception:
                    pass

            item = AgendaItem(
                seller_id=seller.id,
                tipo=task.get("tipo", "outro"),
                titulo=titulo,
                descricao=task.get("descricao"),
                due_date=due,
            )
            self.db.add(item)
            created.append(titulo)

        if created:
            self.db.commit()

        content = ""
        if created:
            content = "Lembrete criado: " + "; ".join(created) + "."

        return AgentResult(
            agent=self.NAME,
            content=content,
            actions=[{"action": "calendar_created", "tasks": created}],
            data={"created": created},
        )
