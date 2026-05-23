from sqlalchemy import Column, Integer, String
from app.database import Base

class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(Integer, primary_key = True, index = True)
    
    student_name = Column(String(100))
    
    raisedhands = Column(Integer)
    visited_resources = Column(Integer)
    announcements = Column(Integer)
    discussion = Column(Integer)
    
    engagement_level = Column(String(50))