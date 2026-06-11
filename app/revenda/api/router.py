from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.revenda.schemas import ChatRequest, ChatResponse
from app.revenda.agents.orchestrator import AgentOrchestrator
from app.revenda.agents.memory import AgentMemory
from app.revenda.agents.inventory import AgentInventory
from app.revenda.agents.crm import AgentCRM
from app.revenda.agents.dashboard import AgentDashboard
from app.revenda.agents.onboarding import AgentOnboarding
from app.revenda.models import (
    RevendedoraProfile, Cliente, Produto, Venda, AgendaItem, Conversa, Mensagem
)

router = APIRouter(prefix="/revenda", tags=["revenda"])
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def chat_ui(request: Request):
    return templates.TemplateResponse("revenda/chat.html", {"request": request})


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    orchestrator = AgentOrchestrator(db=db)
    result = orchestrator.process(
        user_id=req.user_id,
        message=req.message,
        conversa_id=req.conversa_id,
    )
    return ChatResponse(**result)


@router.get("/onboarding-status/{user_id}")
def onboarding_status(user_id: str, db: Session = Depends(get_db)):
    orchestrator = AgentOrchestrator(db=db)
    return orchestrator.get_onboarding_status(user_id)


@router.post("/upload-stock")
async def upload_stock(
    user_id: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    allowed = {"image/jpeg", "image/png", "image/webp", "image/gif"}
    if file.content_type not in allowed:
        raise HTTPException(status_code=400, detail="Formato de imagem não suportado")

    contents = await file.read()
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Imagem muito grande (máx 5MB)")

    agent = AgentOnboarding(db=db)
    result = agent.analyze_stock_photo(user_id, contents, file.content_type)

    added = result.get("added", [])
    if added:
        msg = f"Analisei sua foto e encontrei {len(added)} produto(s):\n" + "\n".join(f"• {p}" for p in added)
    else:
        msg = "Não consegui identificar produtos cosméticos na foto. Pode me mandar a lista por texto?"

    return {"message": msg, "products": result.get("products", []), "added": added}


@router.get("/dashboard/{user_id}")
def dashboard(user_id: str, db: Session = Depends(get_db)):
    agent = AgentDashboard(db=db)
    result = agent.process({"user_id": user_id, "message": "resumo do dia"}, {})
    return {"summary": result.content, "data": result.data}


@router.get("/inventory/{user_id}")
def inventory(user_id: str, db: Session = Depends(get_db)):
    profile = db.query(RevendedoraProfile).filter(
        RevendedoraProfile.user_id == user_id
    ).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    products = db.query(Produto).filter(Produto.seller_id == profile.id).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "brand": p.brand,
            "quantity": p.quantity,
            "sale_price": p.sale_price,
            "purchase_price": p.purchase_price,
        }
        for p in products
    ]


@router.get("/clients/{user_id}")
def clients(user_id: str, db: Session = Depends(get_db)):
    profile = db.query(RevendedoraProfile).filter(
        RevendedoraProfile.user_id == user_id
    ).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    clients = db.query(Cliente).filter(
        Cliente.seller_id == profile.id,
        Cliente.is_active == True,
    ).all()
    return [
        {
            "id": c.id,
            "name": c.name,
            "phone": c.phone,
            "last_purchase_date": str(c.last_purchase_date) if c.last_purchase_date else None,
            "average_ticket": c.average_ticket,
            "favorite_products": c.favorite_products or [],
            "notes": c.notes,
        }
        for c in clients
    ]


@router.get("/sales/{user_id}")
def sales(user_id: str, db: Session = Depends(get_db)):
    profile = db.query(RevendedoraProfile).filter(
        RevendedoraProfile.user_id == user_id
    ).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    vendas = db.query(Venda).filter(
        Venda.seller_id == profile.id
    ).order_by(Venda.criado_em.desc()).limit(50).all()
    return [
        {
            "id": v.id,
            "total_amount": v.total_amount,
            "payment_method": v.payment_method,
            "delivery_status": v.delivery_status,
            "sale_date": str(v.sale_date),
            "client": v.cliente.name if v.cliente else None,
            "items": [
                {"product": i.product_name, "qty": i.quantity, "price": i.unit_price}
                for i in v.itens
            ],
        }
        for v in vendas
    ]


@router.get("/agenda/{user_id}")
def agenda(user_id: str, db: Session = Depends(get_db)):
    profile = db.query(RevendedoraProfile).filter(
        RevendedoraProfile.user_id == user_id
    ).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    items = db.query(AgendaItem).filter(
        AgendaItem.seller_id == profile.id,
        AgendaItem.is_done == False,
    ).order_by(AgendaItem.due_date).all()
    return [
        {
            "id": i.id,
            "tipo": i.tipo,
            "titulo": i.titulo,
            "descricao": i.descricao,
            "due_date": str(i.due_date) if i.due_date else None,
        }
        for i in items
    ]


@router.patch("/agenda/{item_id}/done")
def mark_done(item_id: int, db: Session = Depends(get_db)):
    item = db.query(AgendaItem).filter(AgendaItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    item.is_done = True
    db.commit()
    return {"ok": True}


@router.get("/history/{user_id}")
def history(user_id: str, conversa_id: int = None, db: Session = Depends(get_db)):
    profile = db.query(RevendedoraProfile).filter(
        RevendedoraProfile.user_id == user_id
    ).first()
    if not profile:
        return {"messages": []}
    query = db.query(Conversa).filter(Conversa.seller_id == profile.id)
    if conversa_id:
        query = query.filter(Conversa.id == conversa_id)
    conversa = query.order_by(Conversa.criado_em.desc()).first()
    if not conversa:
        return {"messages": [], "conversa_id": None}
    msgs = db.query(Mensagem).filter(
        Mensagem.conversa_id == conversa.id
    ).order_by(Mensagem.criado_em).all()
    return {
        "conversa_id": conversa.id,
        "messages": [{"role": m.role, "content": m.content} for m in msgs],
    }
