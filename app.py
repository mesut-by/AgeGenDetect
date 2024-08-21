from flask import Flask, render_template, Response, request
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import time

app = Flask(__name__)

# Load pre-trained models for age and gender prediction
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

age_model = load_model('models/age_model.keras')
gender_model = load_model('models/gender_model.keras')

#  Variables for prediction timing and control
last_prediction_time = 0
prediction_interval = 5
start_prediction = False
stop_prediction = False

last_age = None
last_gender = None

# Generate video frames from webcam with face detection and age/gender prediction
def gen_frames():
    global last_prediction_time, start_prediction, stop_prediction, last_age, last_gender

    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()  
        if not success or stop_prediction:
            break
        else:
            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detecting
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
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
                
                # Choose text color based on predicted gender
                text_color = (235, 52, 201) if last_gender == "Female" else  (235, 204, 52) 

                # Display age and gender on the frame
                if last_age is not None and last_gender is not None:
                    cv2.putText(frame, f"Age: {last_age}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
                    cv2.putText(frame, f"Gender: {last_gender}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

# Route for video feed
@app.route('/video_feed')
def video_feed():
    global stop_prediction
    stop_prediction = False  
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

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
    app.run(debug=True)
