from fastapi import FastAPI
from app.routes import student

app = FastAPI()

app.include_router(student.router)

@app.get("/")
def home():
    return {
        "message": "AI School Backend Running"
    }