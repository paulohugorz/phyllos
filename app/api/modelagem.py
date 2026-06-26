from __future__ import annotations

from datetime import datetime, timezone
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, or_, distinct
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.models import ModelagemSpec, Peca, MoldeBase, MoldeVariacao
from app.schemas.schemas import (
    ModelagemSpecCreate,
    ModelagemSpecOut,
    ModelagemSpecRevisao,
    ModelagemSpecUpdate,
)
from app.services.modelagem_matcher import (
    build_molde_intent_spec,
    measurement_strategy,
    rank_variations,
    resolve_semantic_profile,
    select_representative_recommendations,
)

router = APIRouter(prefix="/modelagem-specs", tags=["MIE — Modelagem"])
router_banco = APIRouter(prefix="/modelagem", tags=["Banco de Modelagens"])


def _serializar_variacao(v: MoldeVariacao, match=None):
    payload = {
        "id": v.id,
        "codigo": v.codigo,
        "molde_nome": v.molde_base.nome,
        "molde_categoria": v.molde_base.categoria,
        "molde_subcategoria": v.molde_base.subcategoria,
        "tamanho": v.tamanho,
        "tipo_tecido": v.tipo_tecido,
        "elasticidade": v.elasticidade,
        "grau_ajuste": v.grau_ajuste,
        "genero": v.genero,
        "comprimento": v.comprimento,
        "decote": v.decote,
        "manga": v.manga,
        "fechamento": v.fechamento,
        "cos": v.cos,
        "descricao_natural": v.descricao_natural,
        "tags": v.tags,
        "medidas": {
            "busto": v.busto_molde,
            "cintura": v.cintura_molde,
            "quadril": v.quadril_molde,
            "ombro": v.ombro_molde,
            "costas": v.costas_molde,
            "comprimento_total": v.comprimento_total_molde,
            "gancho": v.gancho_molde,
            "joelho": v.largura_joelho_molde,
            "tornozelo": v.largura_tornozelo_molde,
        },
    }
    if match:
        payload["match"] = {
            "score": match.score,
            "papel_referencia": match.papel_referencia,
            "motivos": list(match.motivos),
        }
    return payload


def _query_variacoes_filtradas(
    db: Session,
    categoria: Optional[str] = None,
    genero: Optional[str] = None,
    tamanho: Optional[str] = None,
    grau_ajuste: Optional[str] = None,
    tipo_tecido: Optional[str] = None,
):
    q_obj = db.query(MoldeVariacao).join(MoldeBase)
    if categoria:
        q_obj = q_obj.filter(MoldeBase.categoria == categoria)
    if genero:
        q_obj = q_obj.filter(MoldeVariacao.genero == genero)
    if tamanho:
        q_obj = q_obj.filter(MoldeVariacao.tamanho == tamanho)
    if grau_ajuste:
        q_obj = q_obj.filter(MoldeVariacao.grau_ajuste == grau_ajuste)
    if tipo_tecido:
        q_obj = q_obj.filter(MoldeVariacao.tipo_tecido == tipo_tecido)
    return q_obj


@router_banco.get("/variacoes/buscar")
def buscar_variacoes(
    q: Optional[str] = Query(None),
    categoria: Optional[str] = Query(None),
    genero: Optional[str] = Query(None),
    tamanho: Optional[str] = Query(None),
    grau_ajuste: Optional[str] = Query(None),
    tipo_tecido: Optional[str] = Query(None),
    limit: int = Query(12, le=50),
    db: Session = Depends(get_db),
):
    """Busca variações do banco de modelagens por texto e filtros."""
    q_obj = _query_variacoes_filtradas(db, categoria, genero, tamanho, grau_ajuste, tipo_tecido)
    if q:
        variacoes = q_obj.all()
        ranking_limit = len(variacoes)
        perfil, ranked = rank_variations(q, variacoes, ranking_limit)
        ranked = select_representative_recommendations(perfil, ranked, limit)
        has_semantic_signal = bool(perfil.categoria_input or perfil.grau_ajuste or perfil.tipo_tecido)
        if ranked and (has_semantic_signal or ranked[0].score > 0):
            return [_serializar_variacao(item.variacao, item) for item in ranked if item.score > -10]

        for word in q.lower().split():
            pattern = f"%{word}%"
            q_obj = q_obj.filter(
                or_(
                    func.lower(MoldeVariacao.descricao_natural).like(pattern),
                    func.lower(MoldeVariacao.tags).like(pattern),
                    func.lower(MoldeBase.nome).like(pattern),
                    func.lower(MoldeBase.categoria).like(pattern),
                )
            )

    variacoes = q_obj.limit(limit).all()
    return [_serializar_variacao(v) for v in variacoes]


@router_banco.get("/referencias/recomendar")
def recomendar_referencias_modelagem(
    q: str = Query(..., min_length=2),
    categoria: Optional[str] = Query(None),
    genero: Optional[str] = Query(None),
    tamanho: Optional[str] = Query(None),
    grau_ajuste: Optional[str] = Query(None),
    tipo_tecido: Optional[str] = Query(None),
    limit: int = Query(8, le=50),
    db: Session = Depends(get_db),
):
    """Recomenda referências de modelagem para uma descrição natural.

    Diferente da busca textual simples, este endpoint explicita a interpretação:
    categoria aproximada, grau de folga, preferência de tecido/construção e a
    estratégia de medidas quando a peça pede uma base composta, como macacão.
    """
    perfil = resolve_semantic_profile(q)
    q_obj = _query_variacoes_filtradas(
        db,
        categoria=categoria,
        genero=genero,
        tamanho=tamanho,
        grau_ajuste=grau_ajuste,
        tipo_tecido=tipo_tecido or perfil.tipo_tecido,
    )
    variacoes = q_obj.all()
    ranking_limit = len(variacoes)
    perfil, ranked = rank_variations(q, variacoes, ranking_limit)
    ranked = select_representative_recommendations(perfil, ranked, limit)

    return {
        "query": q,
        "perfil": perfil.as_dict(),
        "especificacao_texto_molde": build_molde_intent_spec(q),
        "estrategia_medidas": measurement_strategy(perfil),
        "recomendacoes": [
            _serializar_variacao(item.variacao, item)
            for item in ranked
            if item.score > -10
        ],
    }


@router_banco.get("/bases/categorias")
def listar_categorias(db: Session = Depends(get_db)):
    """Lista categorias distintas de moldes base disponíveis."""
    cats = db.query(distinct(MoldeBase.categoria)).all()
    return [c[0] for c in cats if c[0]]


def _get_spec_or_404(peca_id: int, db: Session) -> ModelagemSpec:
    spec = db.query(ModelagemSpec).filter(ModelagemSpec.peca_id == peca_id).first()
    if not spec:
        raise HTTPException(status_code=404, detail="Spec de modelagem não encontrada para esta peça")
    return spec


@router.post("", response_model=ModelagemSpecOut, status_code=201)
def criar_spec(data: ModelagemSpecCreate, db: Session = Depends(get_db)):
    """Cria a spec de modelagem de uma peça. Ponto de entrada do MIE."""
    if not db.query(Peca).filter(Peca.id == data.peca_id).first():
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    if db.query(ModelagemSpec).filter(ModelagemSpec.peca_id == data.peca_id).first():
        raise HTTPException(status_code=400, detail="Spec já existe para esta peça — use PATCH para atualizar")
    spec = ModelagemSpec(**data.model_dump())
    db.add(spec)
    db.commit()
    db.refresh(spec)
    return spec


@router.get("", response_model=List[ModelagemSpecOut])
def listar_specs(
    status_revisao: Optional[str] = Query(None, description="gerado | em_revisao | aprovado | reprovado"),
    categoria_peca: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    """Lista specs de modelagem. Filtrável por status de revisão e categoria."""
    q = db.query(ModelagemSpec)
    if status_revisao:
        q = q.filter(ModelagemSpec.status_revisao == status_revisao)
    if categoria_peca:
        q = q.filter(ModelagemSpec.categoria_peca == categoria_peca)
    return q.all()


@router.get("/{peca_id}", response_model=ModelagemSpecOut)
def obter_spec(peca_id: int, db: Session = Depends(get_db)):
    """Retorna a spec de modelagem de uma peça."""
    return _get_spec_or_404(peca_id, db)


@router.patch("/{peca_id}", response_model=ModelagemSpecOut)
def atualizar_spec(peca_id: int, data: ModelagemSpecUpdate, db: Session = Depends(get_db)):
    """Atualiza campos técnicos da spec. Não altera status_revisao — use /revisao para isso."""
    spec = _get_spec_or_404(peca_id, db)
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(spec, field, value)
    spec.atualizado_em = datetime.now(timezone.utc)
    db.commit()
    db.refresh(spec)
    return spec


@router.patch("/{peca_id}/revisao", response_model=ModelagemSpecOut)
def revisar_spec(peca_id: int, data: ModelagemSpecRevisao, db: Session = Depends(get_db)):
    """Registra revisão humana — o feedback loop que alimenta o data moat.

    notas_revisao deve descrever o que o modelista corrigiu: cada nota é um
    ponto de dado que refina as regras de modelagem ao longo do tempo.
    """
    status_validos = {"gerado", "em_revisao", "aprovado", "reprovado"}
    if data.status_revisao not in status_validos:
        raise HTTPException(
            status_code=400,
            detail=f"status_revisao inválido. Use: {sorted(status_validos)}",
        )
    spec = _get_spec_or_404(peca_id, db)
    spec.status_revisao = data.status_revisao
    if data.revisado_por is not None:
        spec.revisado_por = data.revisado_por
    if data.notas_revisao is not None:
        spec.notas_revisao = data.notas_revisao
    spec.revisado_em = datetime.now(timezone.utc)
    spec.atualizado_em = datetime.now(timezone.utc)
    db.commit()
    db.refresh(spec)
    return spec


@router.delete("/{peca_id}", status_code=204)
def deletar_spec(peca_id: int, db: Session = Depends(get_db)):
    """Remove a spec de modelagem. Não remove a peça."""
    spec = _get_spec_or_404(peca_id, db)
    db.delete(spec)
    db.commit()
