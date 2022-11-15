from sqlalchemy import Column, Integer, String, Float
from ..models.models_base import Base

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String)
    preco = Column(Float)
