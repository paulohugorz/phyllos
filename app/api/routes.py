from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.models import Colecao, Peca, FichaTecnica
from app.schemas.schemas import (
    ColecaoCreate, ColecaoOut,
    PecaCreate, PecaUpdate, PecaOut,
    FichaTecnicaCreate, FichaTecnicaOut,
)

router = APIRouter()


# ---------- Coleções ----------

@router.get("/colecoes", response_model=List[ColecaoOut], tags=["Coleções"])
def listar_colecoes(db: Session = Depends(get_db)):
    return db.query(Colecao).all()


@router.post("/colecoes", response_model=ColecaoOut, status_code=201, tags=["Coleções"])
def criar_colecao(data: ColecaoCreate, db: Session = Depends(get_db)):
    colecao = Colecao(**data.model_dump())
    db.add(colecao)
    db.commit()
    db.refresh(colecao)
    return colecao


@router.get("/colecoes/{colecao_id}", response_model=ColecaoOut, tags=["Coleções"])
def obter_colecao(colecao_id: int, db: Session = Depends(get_db)):
    colecao = db.query(Colecao).filter(Colecao.id == colecao_id).first()
    if not colecao:
        raise HTTPException(status_code=404, detail="Coleção não encontrada")
    return colecao


# ---------- Peças ----------

@router.get("/pecas", response_model=List[PecaOut], tags=["Peças"])
def listar_pecas(db: Session = Depends(get_db)):
    return db.query(Peca).all()


@router.post("/pecas", response_model=PecaOut, status_code=201, tags=["Peças"])
def criar_peca(data: PecaCreate, db: Session = Depends(get_db)):
    if db.query(Peca).filter(Peca.codigo == data.codigo).first():
        raise HTTPException(status_code=400, detail="Código já existe")
    peca = Peca(**data.model_dump())
    db.add(peca)
    db.commit()
    db.refresh(peca)
    return peca


@router.get("/pecas/{codigo}", response_model=PecaOut, tags=["Peças"])
def obter_peca(codigo: str, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    return peca


@router.patch("/pecas/{codigo}", response_model=PecaOut, tags=["Peças"])
def atualizar_peca(codigo: str, data: PecaUpdate, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(peca, field, value)
    db.commit()
    db.refresh(peca)
    return peca


# ---------- Fichas Técnicas ----------

@router.get("/fichas-tecnicas", response_model=List[FichaTecnicaOut], tags=["Fichas Técnicas"])
def listar_fichas(db: Session = Depends(get_db)):
    return db.query(FichaTecnica).all()


@router.post("/fichas-tecnicas", response_model=FichaTecnicaOut, status_code=201, tags=["Fichas Técnicas"])
def criar_ficha(data: FichaTecnicaCreate, db: Session = Depends(get_db)):
    if db.query(FichaTecnica).filter(FichaTecnica.peca_id == data.peca_id).first():
        raise HTTPException(status_code=400, detail="Ficha técnica já existe para esta peça")
    ficha = FichaTecnica(**data.model_dump())
    db.add(ficha)
    db.commit()
    db.refresh(ficha)
    return ficha


@router.get("/fichas-tecnicas/{peca_id}", response_model=FichaTecnicaOut, tags=["Fichas Técnicas"])
def obter_ficha(peca_id: int, db: Session = Depends(get_db)):
    ficha = db.query(FichaTecnica).filter(FichaTecnica.peca_id == peca_id).first()
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha técnica não encontrada")
    return ficha


# ---------- Health ----------

@router.get("/api/status", tags=["Status"])
def root():
    return {"status": "ok", "sistema": "Fashion OS v1"}
