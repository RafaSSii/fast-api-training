from fastapi import APIRouter
from models import User
from dependencies import sessionmaker, take_session
from main import bcrypt_context

#Criação do roteador de rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"Message": "Você acessou o login", "Autenticado": False}

@auth_router.post("/create_account")
async def create_account(email: str, password: str, name: str, session = take_session()):
    user = session.query(User).filter(User.email == email).first()
    if user:
        return {"mensagem: Já existe um usuário com esse email"}
    else:
        encrypted_password = bcrypt_context.hash(password)
        new_user = User(name=name, email=email, encrypted_password=encrypted_password)
        session.add(new_user)
        session.commit()
        return {"mensagem: Usuário cadastrado com sucesso"}
