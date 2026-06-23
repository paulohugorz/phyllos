from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.api.routes import router
import os

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


@app.get("/", response_class=HTMLResponse)
async def frontend(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
