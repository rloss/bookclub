from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import SignupRequest
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, data: SignupRequest) -> User:
    hashed_pw = pwd_context.hash(data.password)
    user = User(
        email=data.email,
        username=data.username,
        password_hash=hashed_pw
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
