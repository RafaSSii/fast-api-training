import os
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
from passlib.handlers import bcrypt

load_dotenv(verbose=True)
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Aqui estou importando as rotas dos respectivos arquivos
from auth_routes import auth_router
from order_routes import order_router

#Aqui estou chamando as rotas através de "inclusão"
app.include_router(auth_router)
app.include_router(order_router)
