from pydantic import BaseModel

class ProdutoPost(BaseModel):
    descricao: str
    preco: float

class ProdutoUpdate(BaseModel):
    descricao: str
    preco: float


class ProdutoListOutput(BaseModel):
    id: int
    descricao: str
    preco: float

    class Config:
        orm_mode = True