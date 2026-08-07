from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

#@ cria um decorator, ele atribui uma funcionalidade nova, além da padrão
@order_router.get("/")
async def orders():
    """
    Essa é a rota padrão de pedidos do sistema
    """
    return {"message": "Você acessou a rota de pedidos"}