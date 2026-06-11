import json
import base64
from app.revenda.agents.base import BaseAgent, AgentResult, get_claude_client
from app.revenda.models import RevendedoraProfile, Produto

EXTRACTOR_PROMPT = """Extraia informações de perfil de revendedora da mensagem abaixo.

Retorne APENAS JSON válido:
{
  "seller_name": "..." | null,
  "city": "..." | null,
  "brands": ["Natura", "Avon"] | null,
  "monthly_goal": 2000 | null,
  "wants_to_skip": true | false
}

Inclua apenas campos claramente mencionados. "pular", "depois", "não sei" → wants_to_skip: true."""

NEXT_STEP_PROMPT = """Você é a Revenda AI, conduzindo o cadastro inicial de uma nova revendedora.

Tom: acolhedor, paciente, como uma amiga que entende de negócio. Emojis com propósito.
Frases curtas. Valide sempre o que a usuária disse antes de pedir mais informações.

Perfil até agora:
{profile_summary}

Próximo campo a coletar: {next_field}
Descrição: {field_desc}

Gere a próxima mensagem natural do onboarding. Máximo 4 linhas."""

STEP_FIELDS = {
    1: ("seller_name",  "Nome da revendedora"),
    2: ("city",         "Cidade onde mora/vende"),
    3: ("brands",       "Marcas que trabalha (Natura, Avon, Boticário...)"),
    4: ("stock",        "Produtos em estoque — texto ou foto"),
    5: ("monthly_goal", "Meta de faturamento mensal (pode pular)"),
}

STOCK_VISION_PROMPT = """Analise esta foto de estoque de cosméticos/produtos de beleza.
Liste todos os produtos visíveis com quantidade estimada e marca quando identificável.

Retorne APENAS JSON válido:
[
  {"name": "Hidratante Tododia", "brand": "Natura", "quantity": 3},
  {"name": "Malbec Gold", "brand": "Boticário", "quantity": 1}
]

Se não houver produtos cosméticos visíveis, retorne [].
Seja conservador nas quantidades — prefira subestimar."""


class AgentOnboarding(BaseAgent):
    NAME = "agent_onboarding"
    DESCRIPTION = "Guia o cadastro inicial da revendedora"

    def _get_profile(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def _profile_summary(self, profile: RevendedoraProfile) -> str:
        parts = []
        if profile.seller_name: parts.append(f"Nome: {profile.seller_name}")
        if profile.city:         parts.append(f"Cidade: {profile.city}")
        if profile.brands:       parts.append(f"Marcas: {', '.join(profile.brands)}")
        if profile.monthly_goal: parts.append(f"Meta: R${profile.monthly_goal:.0f}/mês")
        return "\n".join(parts) if parts else "Nenhuma informação ainda"

    def _missing_step(self, profile: RevendedoraProfile) -> int:
        if not profile.seller_name: return 1
        if not profile.city:        return 2
        if not profile.brands:      return 3
        count = self.db.query(Produto).filter(Produto.seller_id == profile.id).count()
        if count == 0:              return 4
        return 5

    def _extract_profile(self, message: str) -> dict:
        client = get_claude_client()
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=256,
            system=EXTRACTOR_PROMPT,
            messages=[{"role": "user", "content": message}],
        )
        try:
            return json.loads(resp.content[0].text)
        except Exception:
            return {}

    def _apply_extracted(self, profile: RevendedoraProfile, data: dict) -> list[str]:
        updated = []
        if data.get("seller_name") and not profile.seller_name:
            profile.seller_name = data["seller_name"].strip().title()
            updated.append("nome")
        if data.get("city") and not profile.city:
            profile.city = data["city"].strip().title()
            updated.append("cidade")
        if data.get("brands"):
            existing = profile.brands or []
            new = [b for b in data["brands"] if b not in existing]
            if new:
                profile.brands = existing + new
                updated.append("marcas")
        if data.get("monthly_goal") and not profile.monthly_goal:
            profile.monthly_goal = data["monthly_goal"]
            updated.append("meta")
        return updated

    def _next_question(self, profile: RevendedoraProfile, next_step: int) -> str:
        if next_step > 5:
            name = profile.seller_name or "você"
            brands = ", ".join(profile.brands or []) or "suas marcas"
            count = self.db.query(Produto).filter(Produto.seller_id == profile.id).count()
            return (
                f"Perfeito, {name}! Tudo anotado \U0001f389\n\n"
                f"\U0001f4cd {profile.city or 'Cidade'}\n"
                f"\U0001f6cd️ {brands}\n"
                f"\U0001f4e6 {count} produto(s) no estoque\n"
                f"\U0001f3af Meta: R${profile.monthly_goal:.0f}/mês" if profile.monthly_goal else
                f"Perfeito, {name}! Tudo anotado \U0001f389\n\n"
                f"\U0001f4cd {profile.city or 'Cidade'}\n"
                f"\U0001f6cd️ {brands}\n"
                f"\U0001f4e6 {count} produto(s) no estoque\n\n"
                "Agora é só me mandar mensagem quando quiser registrar uma venda, "
                "pedir um post ou checar seu estoque. Pode começar! \U0001f680"
            )

        field_name, field_desc = STEP_FIELDS[next_step]
        summary = self._profile_summary(profile)

        client = get_claude_client()
        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system=NEXT_STEP_PROMPT.format(
                profile_summary=summary,
                next_field=field_name,
                field_desc=field_desc,
            ),
            messages=[{"role": "user", "content": "Gere a próxima mensagem."}],
        )
        return resp.content[0].text.strip()

    def analyze_stock_photo(self, user_id: str, image_data: bytes, media_type: str) -> dict:
        profile = self._get_profile(user_id)
        if not profile:
            return {"products": [], "message": "Perfil não encontrado"}

        b64 = base64.standard_b64encode(image_data).decode()
        client = get_claude_client()

        resp = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {"type": "base64", "media_type": media_type, "data": b64},
                    },
                    {"type": "text", "text": STOCK_VISION_PROMPT},
                ],
            }],
        )

        try:
            products = json.loads(resp.content[0].text)
        except Exception:
            products = []

        added = []
        for p in products:
            name = p.get("name", "")
            if not name:
                continue
            existing = self.db.query(Produto).filter(
                Produto.seller_id == profile.id,
                Produto.name == name,
            ).first()
            if existing:
                existing.quantity += p.get("quantity", 1)
            else:
                novo = Produto(
                    seller_id=profile.id,
                    name=name,
                    brand=p.get("brand"),
                    quantity=p.get("quantity", 1),
                )
                self.db.add(novo)
            added.append(f"{p.get('quantity', 1)}x {name}")

        if added:
            if profile.onboarding_step == 4:
                profile.onboarding_step = 5
            self.db.commit()

        return {"products": products, "added": added}

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")

        profile = self._get_profile(user_id)
        if not profile:
            return AgentResult(agent=self.NAME, content="", success=False)

        extracted = self._extract_profile(message)
        updated_fields = self._apply_extracted(profile, extracted)

        stock_mentioned = any(w in message.lower() for w in [
            "tenho", "estoque", "produto", "unidade", "caixa", "peça",
            "natura", "avon", "boticário", "boticario", "kaiak", "malbec",
            "tododia", "lily", "egeo", "ekos"
        ])
        if stock_mentioned and profile.onboarding_step == 4:
            from app.revenda.agents.inventory import AgentInventory
            inv = AgentInventory(db=self.db)
            inv.process(payload, context)
            count = self.db.query(Produto).filter(Produto.seller_id == profile.id).count()
            if count > 0 and profile.onboarding_step < 5:
                profile.onboarding_step = 5

        next_step = self._missing_step(profile)

        if updated_fields:
            profile.onboarding_step = max(profile.onboarding_step, min(next_step, 5))
            self.db.commit()

        is_complete = (
            bool(profile.seller_name)
            and bool(profile.brands)
            and next_step >= 5
        )
        if is_complete and profile.onboarding_step != 99:
            profile.onboarding_step = 99

        self.db.commit()
        self.db.refresh(profile)

        final_step = self._missing_step(profile)
        response_text = self._next_question(profile, final_step if not is_complete else 99)

        return AgentResult(
            agent=self.NAME,
            content=response_text,
            data={
                "onboarding_step": profile.onboarding_step,
                "onboarding_complete": profile.onboarding_step == 99,
                "updated_fields": updated_fields,
            },
        )
