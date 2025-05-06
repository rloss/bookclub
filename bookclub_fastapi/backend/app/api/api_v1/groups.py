from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.group import GroupCreate, GroupOut
from app.models.user import User
from app.crud import group as group_crud

router = APIRouter()

@router.post("/", response_model=GroupOut)
def create_group(
    group_in: GroupCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return group_crud.create_group(db, current_user.id, group_in)

@router.get("/", response_model=list[GroupOut])
def list_public_groups(db: Session = Depends(get_db)):
    return group_crud.get_public_groups(db)

@router.get("/{group_id}", response_model=GroupOut)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = group_crud.get_group_by_id(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group
