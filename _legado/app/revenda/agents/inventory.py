import json
from app.revenda.agents.base import BaseAgent, AgentResult
from app.revenda.models import Produto, RevendedoraProfile


LOW_STOCK_THRESHOLD = 2


class AgentInventory(BaseAgent):
    NAME = "agent_inventory"
    DESCRIPTION = "Controla produtos e estoque"
    SYSTEM_PROMPT = """Você é o agente de estoque da Revenda AI.
Extraia operações de estoque da mensagem e retorne JSON:

{
  "operations": [
    {
      "action": "add" | "remove" | "query",
      "product_name": "...",
      "brand": "...",
      "quantity": number,
      "purchase_price": number,
      "sale_price": number
    }
  ]
}

Interprete "chegaram X" como add, "vendi X" como remove.
Responda APENAS com JSON válido."""

    def _get_seller(self, user_id: str) -> RevendedoraProfile:
        return self.db.query(RevendedoraProfile).filter(
            RevendedoraProfile.user_id == user_id
        ).first()

    def _find_or_create_product(self, seller_id: int, name: str, brand: str = None) -> Produto:
        name_lower = name.strip().lower()
        products = self.db.query(Produto).filter(Produto.seller_id == seller_id).all()
        for p in products:
            if p.name.lower() == name_lower:
                return p
        produto = Produto(
            seller_id=seller_id,
            name=name.strip().title(),
            brand=brand,
            quantity=0,
        )
        self.db.add(produto)
        self.db.commit()
        self.db.refresh(produto)
        return produto

    def get_low_stock(self, seller_id: int) -> list[Produto]:
        return self.db.query(Produto).filter(
            Produto.seller_id == seller_id,
            Produto.quantity <= LOW_STOCK_THRESHOLD,
            Produto.quantity > 0,
        ).all()

    def get_zero_stock(self, seller_id: int) -> list[Produto]:
        return self.db.query(Produto).filter(
            Produto.seller_id == seller_id,
            Produto.quantity == 0,
        ).all()

    def deduct(self, seller_id: int, product_name: str, quantity: int) -> bool:
        produto = self._find_or_create_product(seller_id, product_name)
        if produto.quantity >= quantity:
            produto.quantity -= quantity
            self.db.commit()
            return True
        return False

    def process(self, payload: dict, context: dict) -> AgentResult:
        user_id = payload.get("user_id")
        message = payload.get("message", "")

        seller = self._get_seller(user_id)
        if not seller:
            return AgentResult(agent=self.NAME, content="", success=False, error="Perfil não encontrado")

        try:
            raw = self.call_llm(message)
            data = json.loads(raw)
        except Exception:
            data = {"operations": []}

        results = []
        alerts = []

        for op in data.get("operations", []):
            name = op.get("product_name", "")
            if not name:
                continue
            qty = int(op.get("quantity", 1))
            produto = self._find_or_create_product(seller.id, name, op.get("brand"))

            if op["action"] == "add":
                if op.get("purchase_price"):
                    produto.purchase_price = op["purchase_price"]
                if op.get("sale_price"):
                    produto.sale_price = op["sale_price"]
                produto.quantity += qty
                self.db.commit()
                results.append(f"+{qty} {produto.name}")

            elif op["action"] == "remove":
                if produto.quantity >= qty:
                    produto.quantity -= qty
                    self.db.commit()
                    results.append(f"-{qty} {produto.name}")
                else:
                    alerts.append(f"Estoque insuficiente de {produto.name} (tem {produto.quantity})")

            if produto.quantity <= LOW_STOCK_THRESHOLD:
                alerts.append(f"Estoque baixo: {produto.name} — apenas {produto.quantity} unidade(s)")

        content = ""
        if results:
            content = "Estoque atualizado: " + ", ".join(results) + "."
        if alerts:
            content += " ⚠️ " + " ".join(alerts)

        return AgentResult(
            agent=self.NAME,
            content=content,
            actions=[{"action": "inventory_update", "operations": data.get("operations", [])}],
            data={"operations": data.get("operations", []), "alerts": alerts},
        )
