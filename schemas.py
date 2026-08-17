from fastapi.openapi.models import Schema
from pydantic import BaseModel
from typing import Optional


class UserSchema(Schema):
    name: str
    email: str
    password: str
    active: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_atributes = True