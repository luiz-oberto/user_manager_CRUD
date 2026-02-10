from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_service import authenticate_user
from app.services.security import create_access_token

router = APIRouter(tags=["Auth"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(
        data={
            "sub": str(user["id_usuario"]),
            "email": user["email"],
            "is_superuser": user["is_superuser"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
