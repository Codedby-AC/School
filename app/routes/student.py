from fastapi import APIRouter

router = APIRouter()

students = []

@router.get("/students")
def get_students():
    return students
    