from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate

def create_comment(db: Session, user_id: int, comment_in: CommentCreate) -> Comment:
    comment = Comment(
        content=comment_in.content,
        post_id=comment_in.post_id,
        author_id=user_id
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comments_by_post(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).order_by(Comment.created_at.asc()).all()
