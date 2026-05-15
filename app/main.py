from fastapi import FastAPI

from app.database import engine, Base

from app.models.user import User

from app.routes import user

from app.models.student import Student

from app.routes import student

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user.router)

app.include_router(student.router)

@app.get("/")
def home():
    return {
        "message": "AI School Backend Running"
    }