from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def create_post(db: Session, user_id: int, post_in: PostCreate) -> Post:
    post = Post(
        title=post_in.title,
        content=post_in.content,
        type=post_in.type,
        group_id=post_in.group_id,
        author_id=user_id
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts_by_group(db: Session, group_id: int):
    return db.query(Post).filter(Post.group_id == group_id).order_by(Post.created_at.desc()).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()
