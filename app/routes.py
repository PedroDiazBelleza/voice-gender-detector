from flask import Blueprint, request, jsonify, current_app
from .utils import allowed_file
from werkzeug.utils import secure_filename
from .services import predict_gender_service

main = Blueprint("main", __name__)

@main.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = f"{current_app.config['UPLOAD_FOLDER']}/{filename}"
        file.save(filepath)

        result = predict_gender_service(filepath)
        return jsonify(result)

    return jsonify({"error": "Invalid file format"}), 400
