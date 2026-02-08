from pydantic import BaseModel, EmailStr
from typing import Optional

# aqui a API recebe os dados vindos do usuário do jeito que ele escreveu
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    is_superuser: bool = False

class UserResponse(BaseModel):
    id_usuario: int
    nome: str
    email: EmailStr
    is_superuser: bool

class UserUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    is_superuser: Optional[bool]