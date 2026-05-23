from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import joblib
import numpy as np

from app.database import get_db
from app.models.progress import Progress
from app.schemas.progress import ProgressCreate

router = APIRouter()

model = joblib.load("ml_models/student_cluster_model.pkl")
scaler = joblib.load("ml_models/scaler.pkl")

cluster_map = {
    0: "Medium Engagement",
    1: "High Engagement",
    2: "Low Engagement"
}

@router.post("/predict_engagement")
def predict_engagement(data: ProgressCreate, db: Session = Depends(get_db)):

    features = np.array([[
        data.raisedhands,
        data.visited_resources,
        data.announcements,
        data.discussion
    ]])

    scaled = scaler.transform(features)

    cluster = model.predict(scaled)[0]

    engagement = cluster_map[int(cluster)]

    new_progress = Progress(
        student_name=data.student_name,

        raisedhands=data.raisedhands,
        visited_resources=data.visited_resources,
        announcements=data.announcements,
        discussion=data.discussion,

        engagement_level=engagement
    )

    db.add(new_progress)
    db.commit()

    return {
        "engagement_level": engagement
    }