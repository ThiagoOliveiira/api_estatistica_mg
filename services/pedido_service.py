import datetime

from utils.conexao_banco import async_session
from data.models.pedido_model import Pedido
from sqlalchemy.future import select
from sqlalchemy import delete


class PedidoService:
    
    @staticmethod
    async def order_details_by_status():
        async with async_session() as session:
        #     result = await session.execute("select p.id, p2.descricao, p.quantidade, p.total, p.data_pedido,  c.nome, c.cpf from pedido p" +
	    # "inner join produto p2" +
		# "on p2.id = p.fk_produto " +
	    # "inner join cliente c" +
		# "on c.id = p.fk_cliente" +
	    # "inner join entrega e" +
		# "on p.id = e.fk_pedido where e.status = 'finalizado'")

            result = await session.execute(f"select * from pedido p where p.id=2")

            print(f"PEDIDO ${result}")
            await session.commit()

    
    
    @staticmethod
    async def create_pedido(quantidade: int, total: float, data: datetime.date, fk_cliente, fk_produto, fk_endereco):
        async with async_session() as session:
            session.add(Pedido(quantidade=quantidade, total=total, data=data, fk_cliente=fk_cliente, fk_produto=fk_produto, fk_endereco=fk_endereco))
            await session.commit()



    @staticmethod
    async def delete_pedido(pedido_id: int):
        async with async_session() as session:
            await session.execute(delete(Pedido).where(Pedido.id == pedido_id))
            await session.commit()

    @staticmethod
    async def list_pedido():
        async with async_session() as session:
            result = await session.execute(select(Pedido))
            return result.scalars().all()

    @staticmethod
    async def get_by_id(pedido_id):
        async with async_session() as session:
            result = await session.execute(select(Pedido).where(Pedido.id == pedido_id))
            return result.scalar()

    @staticmethod
    async def atualizar_pedido(id : int, quantidade : int, total : float, data: datetime.date):
        async with async_session() as session:
            session.execute(f"update pedido set quantidade='{quantidade}', total='{total}', data='{data}' where id={id};")
            await session.commit()