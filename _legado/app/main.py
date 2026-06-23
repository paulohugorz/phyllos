from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.core.database import Base, engine, run_migrations, SessionLocal
from app.api.routes import router
from app.api.fornecedores import router as router_fornecedores
import os, json

run_migrations()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fashion OS v1",
    description="Sistema operacional para criação, gestão, produção e lançamento de moda com IA, agentes Claude e stack gratuita.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

images_dir = os.path.join(os.path.dirname(__file__), "../data/images")
os.makedirs(images_dir, exist_ok=True)
app.mount("/static/images", StaticFiles(directory=images_dir), name="images")

app.include_router(router)
app.include_router(router_fornecedores)


@app.get("/", response_class=HTMLResponse)
async def frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def _dpp_context(peca, request):
    """Monta o contexto compartilhado entre /p/{uuid} e /etiqueta."""
    from app.models.models import EtapaProducao
    ficha    = peca.ficha_tecnica
    materiais = peca.materiais

    composicao = json.loads(ficha.composicao_fibras) if ficha and ficha.composicao_fibras else []
    certs      = json.loads(ficha.certificacoes)     if ficha and ficha.certificacoes      else []

    fornecedores_info = []
    seen = set()
    for m in materiais:
        f = m.produto.fornecedor
        if f.id not in seen:
            seen.add(f.id)
            fornecedores_info.append({
                "nome": f.nome, "cidade": f.cidade,
                "estado": f.estado, "nota": f.nota_confianca,
            })

    instrucoes_reparo   = ficha.instrucoes_reparo       if ficha else None
    instrucoes_fim_vida = ficha.instrucoes_fim_de_vida  if ficha else None
    total_cards = 3 + (1 if composicao else 0) + (1 if instrucoes_reparo or instrucoes_fim_vida else 0)

    return {
        "request": request,
        "peca_nome":         peca.nome,
        "peca_codigo":       peca.codigo,
        "peca_gtin":         peca.gtin,
        "peca_uuid":         peca.dpp_uuid,
        "peca_status":       peca.dpp_status,
        "composicao":        composicao,
        "certificacoes":     certs,
        "carbono_kgco2e":    ficha.pegada_carbono_kgco2e      if ficha else None,
        "durabilidade_ciclos": ficha.durabilidade_ciclos_lavagem if ficha else None,
        "instrucoes_reparo":  instrucoes_reparo,
        "instrucoes_fim_vida": instrucoes_fim_vida,
        "fornecedores":      fornecedores_info,
        "total_cards":       total_cards,
    }


@app.get("/p/{uuid}", response_class=HTMLResponse)
async def consumer_dpp(request: Request, uuid: str):
    from app.models.models import Peca
    db: Session = SessionLocal()
    try:
        peca = db.query(Peca).filter(Peca.dpp_uuid == uuid).first()
        if not peca:
            return HTMLResponse(
                "<html><body style='font-family:sans-serif;padding:40px'>"
                "<h2>Passaporte não encontrado</h2>"
                "<p>O QR code pode estar desatualizado.</p></body></html>",
                status_code=404,
            )
        ctx = _dpp_context(peca, request)
    finally:
        db.close()
    return templates.TemplateResponse("dpp_consumer.html", ctx)


@app.get("/pecas/{codigo}/etiqueta", response_class=HTMLResponse)
async def etiqueta_peca(request: Request, codigo: str):
    from app.models.models import Peca
    from app.api.routes import _gerar_qr_base64
    db: Session = SessionLocal()
    try:
        peca = db.query(Peca).filter(Peca.codigo == codigo).first()
        if not peca:
            return HTMLResponse("<h2>Peça não encontrada</h2>", status_code=404)
        if not peca.dpp_uuid:
            return HTMLResponse("<h2>Peça sem UUID — crie a peça novamente para gerar etiqueta</h2>", status_code=400)

        ctx = _dpp_context(peca, request)
        passport_url = f"https://phyllos-production.up.railway.app/p/{peca.dpp_uuid}"
        ctx["qr_b64"]       = _gerar_qr_base64(passport_url)
        ctx["passport_url"] = passport_url
    finally:
        db.close()
    return templates.TemplateResponse("etiqueta.html", ctx)
