from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    type = Column(String, default="common")  # "common" or "personal"

    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # 관계
    author = relationship("User", backref="posts")
    group = relationship("Group", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
