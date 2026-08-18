from typing import Any

from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, values
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType


#Cria a conexão com banco de dados
db = create_engine('sqlite:///sqlite3.db')

#Cria a base do banco
Base = declarative_base()

#Cria as tabelas/classes do banco
class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, nullable=False ,primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

#Pedido
class Order(Base):
    __tablename__ = "orders"

    #ORDERS_STATUS = (
    #("PENDENTE", "Pendente"),
    #("CANCELADO", "Cancelado"),
    #("FINALIZADO", "Finalizado")
    #)

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, cancelado, finalizado
    user_id = Column("user_id", Integer, ForeignKey('users.id'))
    price = Column("price", Float)
    quantity = Column("quantity", Integer)

    def __init__(self, user, status="PENDENTE", price=0):
        self.user = user
        self.status = status
        self.price = price


#ItensPedido

class OrderItem(Base):
    __tablename__ = "order_itens"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unit_price = Column("unit_price", Float)
    user_id = Column("user_id", Integer, ForeignKey('users.id'))
    order_id = Column("order_id", Integer, ForeignKey('orders.id'))

    def __init__(self, quantity, flavor, size, unit_price, order_id):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price
        self.order_id = order_id

#Executa a criação dos metadados do banco (criação do banco efetivamente)