from datetime import datetime
from pydantic import BaseModel, EmailStr

# 응답용 스키마
class User(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime

    class Config:
        orm_mode = True  # SQLAlchemy 연동
