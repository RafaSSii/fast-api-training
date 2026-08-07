from fastapi import APIRouter

#Criação do roteador de rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def login():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"Message": "Você acessou o login", "Autenticado": False}