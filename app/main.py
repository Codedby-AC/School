from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models.user import User
from app.models.student import Student

from app.routes import user
from app.routes import student
from app.routes import predict

app = FastAPI()


# DATABASE TABLES CREATE
Base.metadata.create_all(bind=engine)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# TEST ROUTE
@app.get("/")
async def home():
    return {
        "message": "FastAPI Backend Running Successfully"
    }


# ROUTERS
app.include_router(user.router)
app.include_router(student.router)
app.include_router(predict.router)