import json
from app.revenda.agents.base import BaseAgent, AgentResult, get_claude_client
from app.revenda.agents.memory import AgentMemory
from app.revenda.agents.crm import AgentCRM
from app.revenda.agents.inventory import AgentInventory
from app.revenda.agents.sales import AgentSales
from app.revenda.agents.finance import AgentFinance
from app.revenda.agents.promotions import AgentPromotions
from app.revenda.agents.content import AgentContent
from app.revenda.agents.customer_service import AgentCustomerService
from app.revenda.agents.after_sales import AgentAfterSales
from app.revenda.agents.calendar import AgentCalendar
from app.revenda.agents.beauty.expert import AgentBeautyExpert
from app.revenda.agents.growth import AgentGrowth
from app.revenda.agents.dashboard import AgentDashboard
from app.revenda.agents.onboarding import AgentOnboarding
from app.revenda.models import RevendedoraProfile, Conversa, Mensagem


ROUTING_SYSTEM = """Você é o agente orquestrador da Revenda AI.
Analise a mensagem de uma revendedora de cosméticos e identifique quais agentes especialistas devem ser acionados.

Agentes disponíveis:
- agent_memory: Atualizar perfil (nome, cidade, marcas, metas)
- agent_crm: Cadastro/atualização de cliente
- agent_inventory: Entrada ou baixa de estoque
- agent_sales: Registrar venda
- agent_finance: Relatório financeiro, faturamento, lucro
- agent_promotions: Criar promoções, kits, ofertas
- agent_content: Criar posts, stories, mensagens WhatsApp
- agent_customer_service: Responder perguntas de clientes
- agent_after_sales: Pós-venda, reativação de clientes
- agent_calendar: Lembretes, tarefas, entregas
- agent_beauty_expert: Dúvidas sobre produtos, marcas, recomendações
- agent_growth: Sugestões de crescimento, estratégia
- agent_dashboard: Resumo do dia, visão geral

Retorne um JSON com:
{
  "agents": ["agent_sales", "agent_inventory", ...],
  "client_name": "Ana" | null,
  "summary": "Breve descrição do que foi pedido"
}

Regras:
- Mensagem de venda → agent_sales + agent_inventory + agent_crm
- Entrada de produto → agent_inventory
- Pergunta de cliente repassada → agent_customer_service
- Pedido de post/conteúdo → agent_content
- Promoção/kit → agent_promotions
- Pergunta sobre produto → agent_beauty_expert
- Resumo do dia → agent_dashboard
- Cobrar ou entregar → agent_calendar
- Pergunta financeira → agent_finance
- Pós-venda → agent_after_sales
- Crescer/estratégia → agent_growth

Responda APENAS com JSON válido."""

SYNTHESIS_SYSTEM = """Você é a Revenda AI — assistente pessoal e parceira de negócio da revendedora.

ESTRUTURA obrigatória de cada resposta:
1. Validação imediata (obrigatória, 1 linha): confirme que entendeu antes de qualquer coisa.
   Use variações naturais: "Anotado! ✓" / "Entendi perfeitamente!" / "Com certeza!" / "Que ótimo, obrigada por me contar!"
2. Ação confirmada: diga claramente o que foi registrado ou feito, de forma breve.
3. Informação útil ou alerta, se houver (estoque baixo, data de entrega, etc.)
4. Próximo passo sugerido (opcional) — se houver oportunidade de venda, mencione com leveza e naturalidade.

REGRAS DE TOM (inegociáveis):
• Paciência total — nunca demonstre pressa, nunca seja seca
• Valide SEMPRE o que a revendedora disse antes de qualquer resposta
• Se a mensagem tiver ambiguidade, pergunte com gentileza antes de assumir
• Nunca deixe uma oportunidade de venda escapar — percebeu chance? Sugira com delicadeza
• Linguagem de parceira próxima que entende do negócio dela
• Emojis: 1 a 2 por mensagem, com propósito — nunca decorativos demais
• Frases curtas e escanáveis — ela está no celular
• Nunca seja robótica, nunca seja fria — cada mensagem deve parecer humana
• Não mencione "agentes" nem detalhes técnicos internos
• Se ela errou algo ou o dado está incompleto, corrija com gentileza e pergunte"""

AGENT_REGISTRY = {
    "agent_memory": AgentMemory,
    "agent_crm": AgentCRM,
    "agent_inventory": AgentInventory,
    "agent_sales": AgentSales,
    "agent_finance": AgentFinance,
    "agent_promotions": AgentPromotions,
    "agent_content": AgentContent,
    "agent_customer_service": AgentCustomerService,
    "agent_after_sales": AgentAfterSales,
    "agent_calendar": AgentCalendar,
    "agent_beauty_expert": AgentBeautyExpert,
    "agent_growth": AgentGrowth,
    "agent_dashboard": AgentDashboard,
}


class AgentOrchestrator:
    def __init__(self, db):
        self.db = db
        self.client = get_claude_client()

    def _get_or_create_profile(self, user_id: str) -> RevendedoraProfile:
        profile = self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()
        if not profile:
            profile = RevendedoraProfile(user_id=user_id)
            self.db.add(profile)
            self.db.commit()
            self.db.refresh(profile)
        return profile

    def _get_or_create_conversa(self, seller_id: int, conversa_id: int | None) -> Conversa:
        if conversa_id:
            conversa = self.db.query(Conversa).filter(
                Conversa.id == conversa_id,
                Conversa.seller_id == seller_id,
            ).first()
            if conversa:
                return conversa
        conversa = Conversa(seller_id=seller_id)
        self.db.add(conversa)
        self.db.commit()
        self.db.refresh(conversa)
        return conversa

    def _recent_history(self, conversa_id: int, limit: int = 6) -> list[dict]:
        msgs = self.db.query(Mensagem).filter(
            Mensagem.conversa_id == conversa_id
        ).order_by(Mensagem.criado_em.desc()).limit(limit).all()
        return [{"role": m.role, "content": m.content} for m in reversed(msgs)]

    def _route(self, message: str, context: dict) -> dict:
        ctx_str = ""
        if context.get("seller_name"):
            ctx_str = f"Revendedora: {context['seller_name']}, cidade: {context.get('city', '?')}"
        routing_message = f"{ctx_str}\n\nMensagem: {message}" if ctx_str else message
        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            system=ROUTING_SYSTEM,
            messages=[{"role": "user", "content": routing_message}],
        )
        raw = response.content[0].text
        try:
            return json.loads(raw)
        except Exception:
            return {"agents": ["agent_beauty_expert"], "client_name": None, "summary": message}

    def _synthesize(self, message: str, results: list[AgentResult], history: list[dict]) -> str:
        agent_outputs = "\n\n".join(
            f"[{r.agent}]: {r.content}"
            for r in results
            if r.content and r.success
        )
        if not agent_outputs:
            agent_outputs = "Nenhuma informação adicional dos agentes."
        messages = history + [
            {
                "role": "user",
                "content": f"Mensagem da revendedora: {message}\n\nInformações dos agentes:\n{agent_outputs}",
            }
        ]
        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=SYNTHESIS_SYSTEM,
            messages=messages,
        )
        return response.content[0].text

    def get_onboarding_status(self, user_id: str) -> dict:
        profile = self._get_or_create_profile(user_id)
        return {
            "onboarding_step": profile.onboarding_step,
            "onboarding_complete": profile.onboarding_step == 99,
            "seller_name": profile.seller_name,
        }

    def process(self, user_id: str, message: str, conversa_id: int | None = None) -> dict:
        profile = self._get_or_create_profile(user_id)
        conversa = self._get_or_create_conversa(profile.id, conversa_id)

        memory_agent = AgentMemory(db=self.db)
        context = memory_agent.get_context(user_id)
        history = self._recent_history(conversa.id)

        payload = {"user_id": user_id, "message": message, "client_name": None}
        results: list[AgentResult] = []
        agents_used = []

        # ── Onboarding mode ──────────────────────────────────────────────────
        if profile.onboarding_step != 99:
            onboarding = AgentOnboarding(db=self.db)
            result = onboarding.process(payload, context)
            results.append(result)
            agents_used = ["agent_onboarding"]

            final_message = result.content or "Como posso te ajudar?"
            onboarding_complete = result.data.get("onboarding_complete", False)

        # ── Normal mode ──────────────────────────────────────────────────────
        else:
            routing = self._route(message, context)
            agents_to_call = routing.get("agents", [])
            agents_used = agents_to_call
            payload["client_name"] = routing.get("client_name")

            # Always run memory silently
            if "agent_memory" not in agents_to_call:
                mem_result = memory_agent.process(payload, context)
                if mem_result.data:
                    results.append(mem_result)

            for agent_name in agents_to_call:
                AgentClass = AGENT_REGISTRY.get(agent_name)
                if not AgentClass:
                    continue
                agent = AgentClass(db=self.db)
                try:
                    result = agent.process(payload, context)
                    results.append(result)
                except Exception as e:
                    results.append(AgentResult(agent=agent_name, content="", success=False, error=str(e)))

            final_message = self._synthesize(message, results, history)
            onboarding_complete = True

        # Persist conversation
        user_msg = Mensagem(conversa_id=conversa.id, role="user", content=message)
        assistant_msg = Mensagem(
            conversa_id=conversa.id,
            role="assistant",
            content=final_message,
            agents_used=agents_used,
        )
        self.db.add(user_msg)
        self.db.add(assistant_msg)
        self.db.commit()

        all_actions = [a for r in results for a in r.actions]

        # Refresh profile to get latest onboarding_step
        self.db.refresh(profile)

        return {
            "message": final_message,
            "agents_used": agents_used,
            "actions": all_actions,
            "conversa_id": conversa.id,
            "onboarding_step": profile.onboarding_step,
            "onboarding_complete": profile.onboarding_step == 99,
        }
