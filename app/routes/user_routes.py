from fastapi import APIRouter, status, HTTPException
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services.user_service import create_user, list_users, get_user_by_id, update_user
from typing import List

# Defini as rotas explicitamente
router = APIRouter(
    prefix="/users", 
    tags=["Users"]
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate):
    return create_user(user)


@router.get("/", response_model=List[UserResponse])
def get_all():
    return list_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(user_id: int):
    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserUpdate):
    updated = update_user(user_id, user)

    if not updated:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return updated

from fastapi import status
from app.services.user_service import delete_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(user_id: int):
    deleted = delete_user(user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return
