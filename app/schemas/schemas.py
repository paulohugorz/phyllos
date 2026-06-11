from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ColecaoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    status: Optional[str] = "planejamento"


class ColecaoCreate(ColecaoBase):
    pass


class ColecaoOut(ColecaoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class PecaBase(BaseModel):
    codigo: str
    nome: str
    colecao_id: Optional[int] = None
    status: Optional[str] = "ideia"
    prioridade: Optional[str] = "media"
    tecido: Optional[str] = None
    custo_estimado: Optional[float] = None
    preco_sugerido: Optional[float] = None
    observacoes: Optional[str] = None
    prompt_croqui: Optional[str] = None
    prompt_foto: Optional[str] = None


class PecaCreate(PecaBase):
    pass


class PecaUpdate(BaseModel):
    nome: Optional[str] = None
    status: Optional[str] = None
    prioridade: Optional[str] = None
    tecido: Optional[str] = None
    custo_estimado: Optional[float] = None
    preco_sugerido: Optional[float] = None
    observacoes: Optional[str] = None
    prompt_croqui: Optional[str] = None
    prompt_foto: Optional[str] = None


class PecaOut(PecaBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class FichaTecnicaBase(BaseModel):
    descricao_tecnica: Optional[str] = None
    materiais: Optional[str] = None
    construcao: Optional[str] = None
    medidas: Optional[str] = None
    qualidade: Optional[str] = None


class FichaTecnicaCreate(FichaTecnicaBase):
    peca_id: int


class FichaTecnicaOut(FichaTecnicaBase):
    id: int
    peca_id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class VisualReferenceBase(BaseModel):
    slug: str
    titulo: str
    fonte: str
    source_url: str
    image_url: Optional[str] = None
    categoria: Optional[str] = "athleisure"
    contexto_uso: str
    cenario: str
    pecas_chave: Optional[str] = None
    paleta: Optional[str] = None
    styling_notes: Optional[str] = None
    atributos_visuais: Optional[str] = None
    prompt_tokens: Optional[str] = None
    prompt_negativo: Optional[str] = None
    direitos_uso: Optional[str] = "Referencia externa para curadoria. Nao copiar imagem para campanha ou produto final."
    status: Optional[str] = "prospectado"
    prioridade: Optional[int] = 3
    curador: Optional[str] = "Codex"
    revisado_em: Optional[str] = None


class VisualReferenceCreate(VisualReferenceBase):
    pass


class VisualReferenceOut(VisualReferenceBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True


class PecaVisualReferenceCreate(BaseModel):
    visual_reference_id: int
    tipo_vinculo: Optional[str] = "moodboard"
    observacoes: Optional[str] = None


class PecaVisualReferenceOut(PecaVisualReferenceCreate):
    id: int
    peca_id: int
    criado_em: datetime

    class Config:
        from_attributes = True
