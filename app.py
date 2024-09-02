from flask import Flask, render_template, Response, request, jsonify
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import time
import base64

app = Flask(__name__)

# Load pre-trained models for age and gender prediction
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

age_model = load_model('models/age_model.keras')
gender_model = load_model('models/gender_model.keras')

# Variables for prediction timing and control
last_prediction_time = 0
prediction_interval = 5
start_prediction = False
stop_prediction = False

last_age = None
last_gender = None

# Process the image from the frontend and return predictions
def process_image(image_data):
    global last_prediction_time, start_prediction, stop_prediction, last_age, last_gender

    # Decode the image data from base64
    nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    predictions = []

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (w + x, h + y), (60, 60, 163), 2)

        face = frame[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (128, 128))
        face_array = np.expand_dims(face_resized, axis=0) / 255.0

        current_time = time.time()

        # For a more stable output, an operation should be performed every 5 seconds.
        if start_prediction and (current_time - last_prediction_time) > prediction_interval:
            last_prediction_time = current_time

            last_age = int(age_model.predict(face_array)[0])
            last_gender_prob = gender_model.predict(face_array)[0]
            last_gender = "Male" if last_gender_prob < 0.5 else "Female"

        # Append the prediction results
        predictions.append({
            'age': last_age,
            'gender': last_gender,
            'box': [int(x), int(y), int(w), int(h)]
        })

    return predictions

# Route to handle image processing
@app.route('/process_image', methods=['POST'])
def process_image_route():
    image_data = request.json['image']
    predictions = process_image(image_data)
    return jsonify(predictions)

# Route to start prediction
@app.route('/start_prediction', methods=['POST'])
def start_prediction_route():
    global start_prediction
    start_prediction = True
    return ('', 204)

# Route to stop prediction
@app.route('/stop_prediction', methods=['POST'])
def stop_prediction_route():
    global stop_prediction
    stop_prediction = True
    return ('', 204)

# Main page route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
