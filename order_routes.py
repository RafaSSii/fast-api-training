from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import take_session
from models import Order
from schemas import OrderSchema

order_router = APIRouter(prefix="/order", tags=["order"])

#@ cria um decorator, ele atribui uma funcionalidade nova, além da padrão
@order_router.get("/")
async def orders():
    """
    Essa é a rota padrão de pedidos do sistema
    """
    return {"message": "Você acessou a rota de pedidos"}

@order_router.post("/order")
async def create_order(order_schema: OrderSchema, session: Session = Depends(take_session)):
    new_order = Order(user=order_schema.user)
    session.add(new_order)
    session.commit()
    return {"menssagem": f"Pedido criado com sucesso{new_order.id}"}