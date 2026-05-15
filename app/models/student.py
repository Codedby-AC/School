from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key = True, index = True)
    
    name = Column(String(100))
    
    student_class = Column(String(100))
    
    section = Column(String(100))
    
    roll_number = Column(Integer)
    
    maths_marks = Column(Float)
    
    science_marks = Column(Float)
    
    english_marks = Column(Float)