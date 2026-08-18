from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    active: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_atributes = True

class OrderSchema(BaseModel):
    user: int

    class Config:
        from_atributes = True