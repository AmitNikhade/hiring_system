from flask import render_template
from flask import Response
from flask import jsonify
import cv2
from deepface import DeepFace
import numpy as np

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def generate_frames():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
            for x, y, w, h in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)

            try:
                result = DeepFace.analyze(frame, actions=['emotion'])
                c = list(result[0]['emotion'].values()).index(max(result[0]['emotion'].values()))
                if c == 6:
                    emotion = "Neutral"
                elif c == 5:
                    emotion = "Surprise"
                elif c == 4:
                    emotion = "Sad"
                elif c == 3:
                    emotion = "Happy"
                elif c == 2:
                    emotion = "Fear"
                elif c == 1:
                    emotion = "Disgust"
                elif c == 0:
                    emotion = "Angry"
                else:
                    emotion = "Unknown"

                cv2.putText(frame, f"Emotion: {emotion}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            except:
                pass

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
