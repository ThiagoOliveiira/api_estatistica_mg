from ..models.models_base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Entrega(Base):
    __tablename__ = 'entrega'
    id = Column(primary_key=True, autoincrement=True)
    status = Column(String)
    fk_pedido = Column(Integer, ForeignKey('pedido.id'))