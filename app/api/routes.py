from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.models import Colecao, Peca, FichaTecnica, VisualReference, PecaVisualReference
from app.schemas.schemas import (
    ColecaoCreate, ColecaoOut,
    PecaCreate, PecaUpdate, PecaOut,
    FichaTecnicaCreate, FichaTecnicaOut,
    VisualReferenceCreate, VisualReferenceOut,
    PecaVisualReferenceCreate, PecaVisualReferenceOut,
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


# ---------- Referências Visuais ----------

@router.get("/referencias-visuais", response_model=List[VisualReferenceOut], tags=["Referências Visuais"])
def listar_referencias_visuais(
    contexto: str | None = None,
    categoria: str | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(VisualReference)
    if contexto:
        query = query.filter(VisualReference.contexto_uso.contains(contexto))
    if categoria:
        query = query.filter(VisualReference.categoria == categoria)
    if status:
        query = query.filter(VisualReference.status == status)
    return query.order_by(VisualReference.prioridade.desc(), VisualReference.titulo.asc()).all()


@router.post("/referencias-visuais", response_model=VisualReferenceOut, status_code=201, tags=["Referências Visuais"])
def criar_referencia_visual(data: VisualReferenceCreate, db: Session = Depends(get_db)):
    if db.query(VisualReference).filter(VisualReference.slug == data.slug).first():
        raise HTTPException(status_code=400, detail="Referência visual já existe")
    referencia = VisualReference(**data.model_dump())
    db.add(referencia)
    db.commit()
    db.refresh(referencia)
    return referencia


@router.get("/referencias-visuais/{slug}", response_model=VisualReferenceOut, tags=["Referências Visuais"])
def obter_referencia_visual(slug: str, db: Session = Depends(get_db)):
    referencia = db.query(VisualReference).filter(VisualReference.slug == slug).first()
    if not referencia:
        raise HTTPException(status_code=404, detail="Referência visual não encontrada")
    return referencia


@router.post("/pecas/{codigo}/referencias-visuais", response_model=PecaVisualReferenceOut, status_code=201, tags=["Referências Visuais"])
def vincular_referencia_visual(
    codigo: str,
    data: PecaVisualReferenceCreate,
    db: Session = Depends(get_db),
):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    if not db.query(VisualReference).filter(VisualReference.id == data.visual_reference_id).first():
        raise HTTPException(status_code=404, detail="Referência visual não encontrada")
    vinculo = PecaVisualReference(peca_id=peca.id, **data.model_dump())
    db.add(vinculo)
    db.commit()
    db.refresh(vinculo)
    return vinculo


@router.get("/pecas/{codigo}/referencias-visuais", response_model=List[VisualReferenceOut], tags=["Referências Visuais"])
def listar_referencias_da_peca(codigo: str, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    return (
        db.query(VisualReference)
        .join(PecaVisualReference)
        .filter(PecaVisualReference.peca_id == peca.id)
        .order_by(VisualReference.prioridade.desc(), VisualReference.titulo.asc())
        .all()
    )


# ---------- Health ----------

@router.get("/api/status", tags=["Status"])
def root():
    return {"status": "ok", "sistema": "Fashion OS v1"}
