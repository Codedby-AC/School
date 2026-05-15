from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):

    db: Session = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }


@router.get("/users")
def get_users():

    db: Session = SessionLocal()

    users = db.query(User).all()

    return users


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UserCreate):

    db: Session = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {
            "message": "User not found"
        }

    user.name = updated_user.name
    user.email = updated_user.email
    user.password = updated_user.password

    db.commit()

    return {
        "message": "User updated successfully"
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: int):

    db: Session = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {
            "message": "User not found"
        }

    db.delete(user)

    db.commit()

    return {
        "message": "User deleted successfully"
    }