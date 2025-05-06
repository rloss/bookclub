from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    type: str = "common"  # "common" or "personal"

class PostCreate(PostBase):
    group_id: int

class PostOut(PostBase):
    id: int
    author_id: int
    group_id: int
    created_at: datetime

    class Config:
        orm_mode = True
