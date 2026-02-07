from fastapi import APIRouter, status
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user, list_users
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create(user: UserCreate):
    return create_user(user)

@router.get(
    "/",
    response_model=List[UserResponse]
)
def get_all():
    return list_users()
