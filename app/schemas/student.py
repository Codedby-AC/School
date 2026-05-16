from pydantic import BaseModel

class StudentCreate(BaseModel):
    
    
    name: str
    
    student_class: str
    
    section: str
    
    roll_number: int
    
    maths_marks: float
    
    science_marks: float
    
    english_marks: float
    