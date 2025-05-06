from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.post import PostCreate, PostOut
from app.crud import post as post_crud

router = APIRouter()

@router.post("/", response_model=PostOut)
def create_post(
    post_in: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return post_crud.create_post(db, current_user.id, post_in)

@router.get("/group/{group_id}", response_model=list[PostOut])
def get_group_posts(group_id: int, db: Session = Depends(get_db)):
    return post_crud.get_posts_by_group(db, group_id)

@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = post_crud.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
