from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.login import LoginSchema

from app.auth.auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()

# ---------------- CREATE USER ---------------- #

@router.post("/users")

def create_user(user: UserCreate):
    
    
    print(user)

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        return {
            "message": "Email already registered"
        }

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

# ---------------- GET USERS ---------------- #

@router.get("/users")

def get_users():

    db: Session = SessionLocal()

    users = db.query(User).all()

    return users

# ---------------- UPDATE USER ---------------- #

@router.put("/users/{user_id}")

def update_user(
    user_id: int,
    updated_user: UserCreate
):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        return {
            "message": "User not found"
        }

    user.name = updated_user.name

    user.email = updated_user.email

    user.password = hash_password(
        updated_user.password
    )

    db.commit()

    return {
        "message": "User updated successfully"
    }

# ---------------- DELETE USER ---------------- #

@router.delete("/users/{user_id}")

def delete_user(user_id: int):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        return {
            "message": "User not found"
        }

    db.delete(user)

    db.commit()

    return {
        "message": "User deleted successfully"
    }

# ---------------- LOGIN ---------------- #

@router.post("/login")

def login(login_data: LoginSchema):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    # USER NOT FOUND
    if not user:

        raise HTTPException(

            status_code=404,

            detail="No user found. Please signup first."
        )

    # WRONG PASSWORD
    if not verify_password(
        login_data.password,
        user.password
    ):

        raise HTTPException(

            status_code=401,

            detail="Incorrect password"
        )

    # CREATE TOKEN
    access_token = create_access_token(

        data={
            "sub": user.email
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"
    }