from fastapi import FastAPI, APIRouter
from views.pedido_view import pedido_router
app = FastAPI()
router = APIRouter()

app.include_router(pedido_router)
