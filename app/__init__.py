from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configuraciones
    app.config["UPLOAD_FOLDER"] = "uploads"
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app
