from fastapi import APIRouter, HTTPException
from typing import List

from services.pedido_service import PedidoService
from schemas.pedido_schema import (PedidoPost, PedidoListOutput, PedidoUpdate)
from schemas.base_shema import (StandardOutput, ErrorOutput)

pedido_router = APIRouter(prefix='/api/pedido')


@pedido_router.post('', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def criar_pedido(pedidoPost: PedidoPost):
    try:
        await PedidoService.create_pedido(
            quantidade=pedidoPost.quantidade,
            total=pedidoPost.total,
            data=pedidoPost.data,
            fk_cliente=pedidoPost.fk_cliente,
            fk_produto=pedidoPost.fk_produto,
            fk_endereco=pedidoPost.fk_endereco,
        )
        return StandardOutput(message='Criado com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


# @pedido_router.delete('/{pedido_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
# async def pedido_delete(pedido_id: int):
#     try:
#         await PedidoService.delete_pedido(pedido_id)
#         return StandardOutput(message='Ok')
#     except Exception as error:
#         raise HTTPException(400, detail=str(error))

@pedido_router.put('/{pedido_id}', response_model=StandardOutput, responses={'400': {'model': ErrorOutput}})
async def atualizar_estoque(pedido: int, pedidoUpdate: PedidoUpdate):
    try:
        await PedidoService.atualizar_pedido(id=pedido, quantidade=pedidoUpdate.quantidade, total=pedidoUpdate.total, data=pedidoUpdate.data)
        return StandardOutput(message='Atualizado com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@pedido_router.get('/all', response_model=List[PedidoListOutput], responses={400: {'model': ErrorOutput}})
async def pedido_all():
    try:
        return await PedidoService.list_pedido()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@pedido_router.get('/id/{pedido_id}', response_model=PedidoListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary(pedido_id: int):
    try:
        return await PedidoService.get_by_id(pedido_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@pedido_router.get('/finalizado', response_model=PedidoListOutput, responses={400: {'model': ErrorOutput}})
async def day_summary():
    try:
        return await PedidoService.order_details_by_status()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

