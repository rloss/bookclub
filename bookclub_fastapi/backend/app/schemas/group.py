from pydantic import BaseModel
from datetime import datetime

class GroupBase(BaseModel):
    name: str
    description: str = ""
    is_public: bool = True

class GroupCreate(GroupBase):
    pass

class GroupOut(GroupBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True
