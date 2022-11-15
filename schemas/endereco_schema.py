from pydantic import BaseModel
from schemas.cliente_schemas import (ClienteListOutput)


class EnderecoPost(BaseModel):
    rua:str
    numero:int
    bairro: str
    cep: str
    complemento:str
    fk_cliente:int

class EnderecoUpdate(BaseModel):
    rua: str
    numero: int
    bairro: str
    cep: str
    complemento: str


class EnderecoListOutput(BaseModel):
    id: int
    rua:str
    numero:int
    bairro: str
    cep: str
    complemento:str
    fk_cliente: int

    class Config:
        orm_mode = True