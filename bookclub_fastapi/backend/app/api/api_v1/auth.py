from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import SignupRequest, LoginRequest, TokenResponse
from app.schemas.user import User as UserOut
from app.db.database import SessionLocal
from app.crud import user as user_crud
from app.core.security import create_access_token

router = APIRouter()

# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=UserOut)
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    existing = user_crud.get_user_by_email(db, data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db, data)

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, data.email)
    if not user or not user_crud.verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
