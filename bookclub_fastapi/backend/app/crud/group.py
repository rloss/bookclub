from sqlalchemy.orm import Session
from app.models.group import Group
from app.schemas.group import GroupCreate

def create_group(db: Session, owner_id: int, group_in: GroupCreate) -> Group:
    group = Group(
        name=group_in.name,
        description=group_in.description,
        is_public=group_in.is_public,
        owner_id=owner_id
    )
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

def get_public_groups(db: Session):
    return db.query(Group).filter(Group.is_public == True).order_by(Group.created_at.desc()).all()

def get_group_by_id(db: Session, group_id: int):
    return db.query(Group).filter(Group.id == group_id).first()
