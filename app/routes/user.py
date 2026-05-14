from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/users")

def create_user(user: UserCreate):
    db: Session  = SessionLocal()
    
    new_user = User(
        name = user.name,
        email = user.email,
        password = user.password
        )
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return{
        "message": "User created successfully"
        }
