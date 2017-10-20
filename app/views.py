from PIL import Image
from io import BytesIO

from flask import render_template
from flask import request
from flask import jsonify

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/predict", methods=['POST'])
def prediction():
    # Send JSON to the client
    return jsonify(status='success',
                   probabilities=0.5,
                   predicted_class=3)

