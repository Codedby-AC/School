from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate

from app.auth.auth import hash_password
from app.schemas.login import LoginSchema

from app.auth.auth import(
    verify_password,
    create_access_token
    )
router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):

    db: Session = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
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

@router.post("/login")

def login(user: LoginSchema):
    
    db: Session = SessionLocal()
    
    existing_user = db.query(User).filter(
        User.email == user.email
        ).first()
    
    if not existing_user:
        return {
            "message": "Invalid email"
            }
    
    if not verify_password(
        user.password,
        existing_user.password
        ):
        return {
            "message": "Invalid password"
            }
    
    token = create_access_token(
        data = {
            "sub": existing_user.email
            }
        )
    
    return {
        "access_token": token,
        "token_type": "bearer"
        }