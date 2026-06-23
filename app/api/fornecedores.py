from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.models.models import Fornecedor, ProdutoFornecedor, CertificacaoFornecedor
from app.schemas.schemas import (
    FornecedorCreate, FornecedorUpdate, FornecedorOut,
    ProdutoFornecedorCreate, ProdutoFornecedorOut,
    CertificacaoFornecedorCreate, CertificacaoFornecedorOut,
    MateriaPrimaOut,
)

router = APIRouter(prefix="/fornecedores", tags=["Fornecedores"])


@router.get("", response_model=List[FornecedorOut])
def listar_fornecedores(
    status: str = None,
    elo: str = None,
    nota_min: int = None,
    db: Session = Depends(get_db),
):
    q = db.query(Fornecedor)
    if status:
        q = q.filter(Fornecedor.status == status)
    if elo:
        q = q.filter(Fornecedor.elo_cadeia.contains(elo))
    if nota_min is not None:
        q = q.filter(Fornecedor.nota_confianca >= nota_min)
    return q.order_by(Fornecedor.nota_confianca.desc().nulls_last(), Fornecedor.codigo).all()


@router.post("", response_model=FornecedorOut, status_code=201)
def criar_fornecedor(data: FornecedorCreate, db: Session = Depends(get_db)):
    if db.query(Fornecedor).filter(Fornecedor.codigo == data.codigo).first():
        raise HTTPException(status_code=400, detail="Código já existe")
    f = Fornecedor(**data.model_dump())
    db.add(f)
    db.commit()
    db.refresh(f)
    return f


@router.get("/{fornecedor_id}", response_model=FornecedorOut)
def obter_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    f = db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
    if not f:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return f


@router.patch("/{fornecedor_id}", response_model=FornecedorOut)
def atualizar_fornecedor(fornecedor_id: int, data: FornecedorUpdate, db: Session = Depends(get_db)):
    f = db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
    if not f:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(f, field, value)
    db.commit()
    db.refresh(f)
    return f


@router.delete("/{fornecedor_id}", status_code=204)
def remover_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    f = db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first()
    if not f:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    db.delete(f)
    db.commit()


# ---------- Produtos ----------

@router.get("/{fornecedor_id}/produtos", response_model=List[ProdutoFornecedorOut])
def listar_produtos(fornecedor_id: int, db: Session = Depends(get_db)):
    _check_fornecedor(fornecedor_id, db)
    return db.query(ProdutoFornecedor).filter(ProdutoFornecedor.fornecedor_id == fornecedor_id).all()


@router.post("/{fornecedor_id}/produtos", response_model=ProdutoFornecedorOut, status_code=201)
def adicionar_produto(
    fornecedor_id: int, data: ProdutoFornecedorCreate, db: Session = Depends(get_db)
):
    _check_fornecedor(fornecedor_id, db)
    p = ProdutoFornecedor(fornecedor_id=fornecedor_id, **data.model_dump())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@router.delete("/{fornecedor_id}/produtos/{produto_id}", status_code=204)
def remover_produto(fornecedor_id: int, produto_id: int, db: Session = Depends(get_db)):
    p = db.query(ProdutoFornecedor).filter(
        ProdutoFornecedor.id == produto_id,
        ProdutoFornecedor.fornecedor_id == fornecedor_id,
    ).first()
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(p)
    db.commit()


# ---------- Certificações ----------

@router.get("/{fornecedor_id}/certificacoes", response_model=List[CertificacaoFornecedorOut])
def listar_certificacoes(fornecedor_id: int, db: Session = Depends(get_db)):
    _check_fornecedor(fornecedor_id, db)
    return db.query(CertificacaoFornecedor).filter(
        CertificacaoFornecedor.fornecedor_id == fornecedor_id
    ).all()


@router.post("/{fornecedor_id}/certificacoes", response_model=CertificacaoFornecedorOut, status_code=201)
def adicionar_certificacao(
    fornecedor_id: int, data: CertificacaoFornecedorCreate, db: Session = Depends(get_db)
):
    _check_fornecedor(fornecedor_id, db)
    c = CertificacaoFornecedor(fornecedor_id=fornecedor_id, **data.model_dump())
    db.add(c)
    db.commit()
    db.refresh(c)
    return c


@router.delete("/{fornecedor_id}/certificacoes/{cert_id}", status_code=204)
def remover_certificacao(fornecedor_id: int, cert_id: int, db: Session = Depends(get_db)):
    c = db.query(CertificacaoFornecedor).filter(
        CertificacaoFornecedor.id == cert_id,
        CertificacaoFornecedor.fornecedor_id == fornecedor_id,
    ).first()
    if not c:
        raise HTTPException(status_code=404, detail="Certificação não encontrada")
    db.delete(c)
    db.commit()


# ---------- Busca de matérias-primas (catálogo unificado) ----------

@router.get("/materias-primas", response_model=List[MateriaPrimaOut], tags=["Catálogo"])
def buscar_materias_primas(
    q: Optional[str] = Query(None, description="Busca livre por nome ou composição"),
    tipo: Optional[str] = Query(None, description="malha | tecido_plano | fio | pluma | lona"),
    nota_min: Optional[int] = Query(None, description="Nota mínima de confiança do fornecedor (1–5)"),
    disponivel: Optional[str] = Query(None, description="sim | nao | a_validar"),
    db: Session = Depends(get_db),
):
    produtos = db.query(ProdutoFornecedor).join(Fornecedor)

    if q:
        termo = f"%{q.lower()}%"
        produtos = produtos.filter(
            ProdutoFornecedor.nome.ilike(termo) |
            ProdutoFornecedor.composicao.ilike(termo) |
            ProdutoFornecedor.tipo.ilike(termo)
        )
    if tipo:
        produtos = produtos.filter(ProdutoFornecedor.tipo == tipo)
    if nota_min is not None:
        produtos = produtos.filter(Fornecedor.nota_confianca >= nota_min)
    if disponivel:
        produtos = produtos.filter(ProdutoFornecedor.disponivel == disponivel)

    produtos = produtos.order_by(
        Fornecedor.nota_confianca.desc().nulls_last(),
        ProdutoFornecedor.nome,
    ).limit(60).all()

    return [_produto_para_materia_prima(p) for p in produtos]


def _produto_para_materia_prima(p: ProdutoFornecedor) -> dict:
    f = p.fornecedor
    return {
        "id": p.id,
        "nome": p.nome,
        "codigo_fornecedor": p.codigo_fornecedor,
        "tipo": p.tipo,
        "composicao": p.composicao,
        "tingimento": p.tingimento,
        "gramatura_gm2": p.gramatura_gm2,
        "largura_m": p.largura_m,
        "moq": p.moq,
        "preco_referencia": p.preco_referencia,
        "unidade_preco": p.unidade_preco,
        "uso_recomendado": p.uso_recomendado,
        "disponivel": p.disponivel,
        "fornecedor_id": f.id,
        "fornecedor_nome": f.nome,
        "fornecedor_cidade": f.cidade,
        "nota_confianca": f.nota_confianca,
        "certificacoes_fornecedor": f.certificacoes,
    }


# ---------- helpers ----------

def _check_fornecedor(fornecedor_id: int, db: Session):
    if not db.query(Fornecedor).filter(Fornecedor.id == fornecedor_id).first():
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
