from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql.functions import user

from models import User
from dependencies import take_session
from main import bcrypt_context
from sqlalchemy.orm import Session
from schemas import UserSchema, LoginSchema

#Criação do roteador de rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user_id):
    token = f"ajshdgfsoiv{user_id}"
    return token

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

@auth_router.post("/login")
async def login(login_schema: LoginSchema ,session: Session = Depends(take_session)):
    users = session.query(User).filter(User.email == login_schema.email).first()
    if not users:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    else:
        access_token = create_token(users.id)
        return {"access_token": access_token, "token_type": "bearer"}
