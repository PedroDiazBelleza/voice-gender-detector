from features import extract_feature
from .model_loader import load_model
import numpy as np

# Cargar el modelo al inicio (solo una vez)
model = load_model()

def predict_gender_service(audio_path):
    features = extract_feature(audio_path, mel=True).reshape(1, -1)
    male_prob = model.predict(features)[0][0]
    female_prob = 1 - male_prob
    gender = "Male" if male_prob > female_prob else "Female"

    return {
        "gender": gender,
        "male_prob": round(male_prob * 100, 2),
        "female_prob": round(female_prob * 100, 2)
    }
