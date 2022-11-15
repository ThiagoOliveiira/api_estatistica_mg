from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..models.models_base import Base


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cpf = Column(String)
    telefone = Column(String)
    endereco = relationship('Endereco', backref='cliente', lazy='subquery')
    pedidos = relationship("Pedido", back_populates="clientes")
