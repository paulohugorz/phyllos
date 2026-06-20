from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from app.core.database import engine, Base
from app.revenda import models as revenda_models  # noqa: F401 — registers tables
from app.revenda.api.router import router as revenda_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Revenda AI",
    description="Chatbot com múltiplos agentes para revendedoras de cosméticos",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(revenda_router)

if os.path.isdir("app/static"):
    app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/health")
def health():
    return {"status": "ok", "service": "revenda-ai"}
