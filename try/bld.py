import cv2
from deepface import DeepFace

# Load the pre-trained DeepFace model for emotion analysis
model = DeepFace.build_model("Emotion")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Start capturing video from the default webcam (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    face = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    # Perform emotion analysis on the frame
    for x, y, w, h in face:
        image = cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 1)
# #       
        try:
            result = DeepFace.analyze(frame, actions=['emotion'])
            # print(result)
            c = list(result[0]['emotion'].values()).index(max(result[0]['emotion'].values()))
            # print(list(result[0]['emotion'].values()).index(max(result[0]['emotion'].values())))
            if c == 6:
                print("Neutral")
            if c == 5:
                print("Surprise")
            if c == 4:
                print("Sad")
            if c == 3:
                print("Happy")
            if c == 2:
                print("fear")
            if c == 1:
                print("disgust")
            if c == 0:
                print("angry")

            
            # Draw bounding box and label for the face
            # if result['success']:
            #     # Get the dominant emotion detected
            # dominant_emotion = result[0]['emotion']['neutral']

            #     # Display the emotion label on the frame
            cv2.putText(frame, "Axona.ai", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # # Display the resulting frame
            cv2.imshow('Real-time Emotion Analysis', frame)
        except:
            pass
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
