from fastapi import APIRouter, Depends
from app.schemas.user import User as UserOut
from app.models.user import User
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user
