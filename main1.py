import cv2
import numpy as np

systemType = input("1. Kamera\n2. Video\nSecim: ")
if systemType == "1":
    cap = cv2.VideoCapture(0)
elif systemType == "2":
    cap = cv2.VideoCapture('video.mp4')
else:
    print("Hatali Giris Yaptiniz")
    exit()

face_cascade = cv2.CascadeClassifier('lib.xml')

def updatePeopleCount(l):
    cv2.setWindowTitle("frame", f"Kisi Sayisi: {str(l)}")
    cv2.putText(frame, f"Kisi Sayisi: {str(l)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 127, 255), 2, cv2.LINE_AA)
     

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    updatePeopleCount(len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (28, 42, 231), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break