from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import take_session
from main import bcrypt_context
from sqlalchemy.orm import Session
from schemas import UserSchema

#Criação do roteador de rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do sistema
    """
    return {"Message": "Você acessou o login", "Autenticado": False}

@auth_router.post("/create_account")
async def create_account(user_schema: UserSchema, session: Session = Depends(take_session)):
    user = session.query(User).filter(User.email == user_schema.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email de usuário já cadastrado")
    else:
        encrypted_password = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email, encrypted_password, user_schema.active, user_schema.admin)
        session.add(new_user)
        session.commit()
        return {f"mensagem: Usuário cadastrado com sucesso {user_schema.email}"}
