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

@router.get("/students/{student_id}/analysis")



def analyze_student(student_id: int):

    db: Session = SessionLocal()

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return {
            "message": "Student not found"
        }

    marks = {

        "Maths": student.maths_marks,

        "Science": student.science_marks,

        "English": student.english_marks
    }

    weak_subject = min(marks, key=marks.get)

    average_marks = (

        student.maths_marks +

        student.science_marks +

        student.english_marks

    ) / 3

    recommendations = {

        "Maths": "Spend extra 2 hours daily solving Maths problems",

        "Science": "Revise Science concepts and practice diagrams daily",

        "English": "Spend extra time on English grammar and writing practice"
    }

    recommendation = recommendations.get(

        weak_subject,

        "No recommendation available"
    )

    return {

        "student_name": student.name,

        "weak_subject": weak_subject,

        "average_marks": average_marks,

        "recommendation": recommendation
    }
    
    


    
    
    
    