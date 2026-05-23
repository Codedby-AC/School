from pydantic import BaseModel

class ProgressCreate(BaseModel):
    student_name: str
    
    raisedhands: int
    visited_resources: int
    announcements: int
    discussion: int