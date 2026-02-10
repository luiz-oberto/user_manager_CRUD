from fastapi import Depends, HTTPException, status
from app.services.dependencies import get_current_user

def require_superuser(current_user=Depends(get_current_user)):
    if not current_user.get("is_superuser"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permissão insuficiente"
        )
    return current_user
