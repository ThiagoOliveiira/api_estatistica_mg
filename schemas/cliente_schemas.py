from pydantic import BaseModel


class ClientePost(BaseModel):
    nome: str
    cpf: str
    telefone: str


class ClienteUpdate(BaseModel):

    nome: str
    cpf: str
    telefone: str


class ClienteListOutput(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
