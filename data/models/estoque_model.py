from ..models.models_base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Estoque(Base):
    __tablename__ = 'estoque'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    fk_produto = Column(Integer, ForeignKey('produto.id'))