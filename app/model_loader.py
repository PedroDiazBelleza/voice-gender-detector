from utils import create_model
import os
from .download_model import download_model_from_gdrive

MODEL_PATH = "results/model.h5"
GDRIVE_FILE_ID = "1FjgapbOy45NBQ4lBAACD0MXj05LGRRG1"  # Reemplaza por el ID real

def load_model(weights_path=MODEL_PATH):
    if not os.path.exists(weights_path):
        print("🔽 Modelo no encontrado, descargando desde Google Drive...")
        download_model_from_gdrive(GDRIVE_FILE_ID, weights_path)

    model = create_model()
    model.load_weights(weights_path)
    return model



