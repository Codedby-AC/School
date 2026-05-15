from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.student import Student
from app.schemas.student import StudentCreate

router = APIRouter()

@router.post("/students")

def create_student(student: StudentCreate):
    db: Session = SessionLocal()
    
    new_student = Student(
        name = student.name,
        
        student_class = student.student_class,
        
        section = student.section,
        
        roll_number = student.roll_number,
        
        maths_marks = student.maths_marks,
        
        science_marks = student.science_marks,
        
        english_marks = student.english_marks
        )
    
    db.add(new_student)
    
    db.commit()
    
    db.refresh(new_student)
    
    return {
        "message": "Student created successfully"
        }

@router.get("/students")

def get_students():
    
    db: Session = SessionLocal()
    
    students = db.query(Student).all()
    
    return students
    