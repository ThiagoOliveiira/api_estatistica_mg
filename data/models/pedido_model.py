from ..models.models_base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship


class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    total = Column(Float)
    data_pedido = Column(Date)
    fk_cliente = Column(Integer, ForeignKey('cliente.id'))
    fk_endereco = Column(Integer, ForeignKey('endereco.id'))
    fk_produto = Column(Integer, ForeignKey('produto.id'))
    clientes = relationship("Cliente", back_populates="pedidos")
