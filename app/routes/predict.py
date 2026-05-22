from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
import joblib

router = APIRouter()

model = joblib.load("ml_models/student_cluster_model.pkl")

scaler= joblib.load("ml_models/scaler.pkl")

class StudentData(BaseModel):
    
    raisedhands: int
    VisITedResources: int
    AnnouncementsView: int
    Discussion: int
    
@router.post("/predict-engagement")
def predict_engagement(data: StudentData):
    
    features = np.array([[
        data.raisedhands,
        data.VisITedResources,
        data.AnnouncementsView,
        data.Discussion
    ]])
    
    scaled_data = scaler.transform(features)
    
    cluster = model.predict(scaled_data)[0]
    
    cluster_names = {
        0: "Medium Engagement",
        1: "High Engagement",
        2: "Low Engagement"
    }
    
    engagement = cluster_names.get(cluster)
    
    return {
        "cluster": int(cluster),
        "engagement_level": engagement
        }