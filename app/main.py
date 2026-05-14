from fastapi import FastAPI

from app.database import engine, Base

from app.models.user import User

from app.routes import user

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def home():
    return {
        "message": "AI School Backend Running"
    }