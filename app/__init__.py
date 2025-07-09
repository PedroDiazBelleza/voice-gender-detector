from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configuraciones
    basedir = os.path.abspath(os.path.dirname(__file__))
    upload_path = os.path.join(basedir, "..", "uploads")
    os.makedirs(upload_path, exist_ok=True)
    app.config["UPLOAD_FOLDER"] = upload_path
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app
