from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List
import json
import uuid
import io

from app.core.database import get_db
from app.models.models import Colecao, Peca, FichaTecnica, VisualReference, PecaVisualReference, EtapaProducao
from app.schemas.schemas import (
    ColecaoCreate, ColecaoOut,
    PecaCreate, PecaUpdate, PecaOut,
    FichaTecnicaBase, FichaTecnicaCreate, FichaTecnicaOut,
    VisualReferenceCreate, VisualReferenceOut,
    PecaVisualReferenceCreate, PecaVisualReferenceOut,
    EtapaProducaoCreate, EtapaProducaoOut,
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


@router.patch("/fichas-tecnicas/{peca_id}", response_model=FichaTecnicaOut, tags=["Fichas Técnicas"])
def atualizar_ficha(peca_id: int, data: FichaTecnicaBase, db: Session = Depends(get_db)):
    ficha = db.query(FichaTecnica).filter(FichaTecnica.peca_id == peca_id).first()
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha técnica não encontrada")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(ficha, field, value)
    db.commit()
    db.refresh(ficha)
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


# ---------- Etapas de Produção ----------

@router.post("/pecas/{codigo}/etapas-producao", response_model=EtapaProducaoOut, status_code=201, tags=["DPP"])
def adicionar_etapa(codigo: str, data: EtapaProducaoCreate, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    etapa = EtapaProducao(peca_id=peca.id, **data.model_dump(exclude={"peca_id"}))
    db.add(etapa)
    db.commit()
    db.refresh(etapa)
    return etapa


@router.get("/pecas/{codigo}/etapas-producao", response_model=List[EtapaProducaoOut], tags=["DPP"])
def listar_etapas(codigo: str, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    return db.query(EtapaProducao).filter(EtapaProducao.peca_id == peca.id).all()


# ---------- Digital Product Passport ----------

@router.post("/pecas/{codigo}/dpp/publicar", response_model=PecaOut, tags=["DPP"])
def publicar_dpp(codigo: str, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.codigo == codigo).first()
    if not peca:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    if not peca.ficha_tecnica or not peca.ficha_tecnica.composicao_fibras:
        raise HTTPException(status_code=400, detail="Ficha técnica incompleta: composicao_fibras obrigatória para publicar DPP")
    if not peca.gtin:
        raise HTTPException(status_code=400, detail="GTIN obrigatório para publicar DPP")
    if not peca.dpp_uuid:
        peca.dpp_uuid = str(uuid.uuid4())
    peca.dpp_status = "publicado"
    db.commit()
    db.refresh(peca)
    return peca


@router.get("/dpp/{gtin}", tags=["DPP"])
def obter_dpp(gtin: str, db: Session = Depends(get_db)):
    peca = db.query(Peca).filter(Peca.gtin == gtin).first()
    if not peca or peca.dpp_status != "publicado":
        raise HTTPException(status_code=404, detail="DPP não encontrado ou não publicado")
    ficha = peca.ficha_tecnica
    etapas = db.query(EtapaProducao).filter(EtapaProducao.peca_id == peca.id).all()
    return {
        "@context": ["https://schema.org/", "https://gs1.org/voc/"],
        "@type": "Product",
        "gtin": peca.gtin,
        "identifier": peca.dpp_uuid,
        "name": peca.nome,
        "description": ficha.descricao_tecnica if ficha else None,
        "material": json.loads(ficha.composicao_fibras) if ficha and ficha.composicao_fibras else [],
        "recycledContent": ficha.conteudo_reciclado_pct if ficha else None,
        "carbonFootprint": {"value": ficha.pegada_carbono_kgco2e, "unitCode": "KGM"} if ficha and ficha.pegada_carbono_kgco2e else None,
        "certifications": json.loads(ficha.certificacoes) if ficha and ficha.certificacoes else [],
        "repairInstructions": ficha.instrucoes_reparo if ficha else None,
        "endOfLifeInstructions": ficha.instrucoes_fim_de_vida if ficha else None,
        "durability": {"washCycles": ficha.durabilidade_ciclos_lavagem} if ficha and ficha.durabilidade_ciclos_lavagem else None,
        "productionChain": [
            {"stage": e.etapa, "country": e.pais, "facility": e.instalacao_nome, "gln": e.instalacao_gln}
            for e in etapas
        ],
    }


@router.get("/dpp/{gtin}/qr", tags=["DPP"])
def obter_qr_dpp(gtin: str, db: Session = Depends(get_db)):
    try:
        import qrcode
    except ImportError:
        raise HTTPException(status_code=501, detail="qrcode não instalado. Execute: pip install qrcode[pil]")
    peca = db.query(Peca).filter(Peca.gtin == gtin).first()
    if not peca or peca.dpp_status != "publicado":
        raise HTTPException(status_code=404, detail="DPP não encontrado ou não publicado")
    # GS1 Digital Link URI format
    url = f"https://phyllos-production.up.railway.app/dpp/{gtin}"
    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


# ---------- Health ----------

@router.get("/api/status", tags=["Status"])
def root():
    return {"status": "ok", "sistema": "Fashion OS v1"}
