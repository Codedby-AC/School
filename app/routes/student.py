from fastapi import APIRouter

router = APIRouter()

@router.get("/students")
def get_students():
    return {
        "students": []
    }