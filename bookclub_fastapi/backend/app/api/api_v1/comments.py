from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.comment import CommentCreate, CommentOut
from app.crud import comment as comment_crud

router = APIRouter()

@router.post("/", response_model=CommentOut)
def write_comment(
    comment_in: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return comment_crud.create_comment(db, current_user.id, comment_in)

@router.get("/post/{post_id}", response_model=list[CommentOut])
def list_comments(post_id: int, db: Session = Depends(get_db)):
    return comment_crud.get_comments_by_post(db, post_id)
