from fastapi import APIRouter, status, HTTPException, Depends
from app.services.dependencies import get_current_user
from app.services.permissions import require_superuser
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate, LoginRequest
from app.services.user_service import create_user, list_users, get_user_by_id, update_user, delete_user, authenticate_user
from typing import List

# Defini as rotas explicitamente
router = APIRouter(
    prefix="/users", 
    tags=["Users"]
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, current_user=Depends(require_superuser)):
    '''
    Apenas super usuários podem criar novos usuários
    '''
    return create_user(user)


@router.get("/", response_model=List[UserResponse])
def get_all(current_user=Depends(require_superuser)): # vai analisar se o token do usuário é valido antes de listar os usuários.
    return list_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id: int, current_user=Depends(get_current_user)):
    # usuário comum só pode ver a si mesmo
    if not current_user["is_superuser"]:
        if int(current_user["sub"]) != user_id: # evita de um usuário acessar dados sem permissão
            raise HTTPException(
                status_code=403,
                detail="Você não tem permissão para acessar este recurso"
            )

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserUpdate, current_user=Depends(require_superuser)):
    updated = update_user(user_id, user)

    if not updated:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return updated


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(user_id: int, current_user=Depends(require_superuser)):
    deleted = delete_user(user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return


@router.post("/login")
def login(data: LoginRequest):
    user = authenticate_user(data.email, data.senha)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    return {
        "message": "Login realizado com sucesso",
        "user": user
    }

