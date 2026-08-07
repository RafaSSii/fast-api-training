from fastapi import FastAPI

app = FastAPI()

#Aqui estou importando as rotas dos respectivos arquivos
from auth_routes import auth_router
from order_routes import order_router

#Aqui estou chamando as rotas através de "inclusão"
app.include_router(auth_router)
app.include_router(order_router)
