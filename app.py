# app.py
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Serve the HTML file
    return send_from_directory('static', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({"error": "No files part in the request"}), 400

    files = request.files.getlist('files')
    uploaded_files = []

    for file in files:
        if file and file.filename:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            uploaded_files.append(file.filename)

    return jsonify({"uploaded_files": uploaded_files}), 200

if __name__ == "__main__":
    app.run(debug=True)
