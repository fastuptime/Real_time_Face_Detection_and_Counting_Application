import cv2
import numpy as np
import os

cascades = [
    'haarcascade_frontalface_default.xml',
    'haarcascade_frontalface_alt.xml',
    'haarcascade_frontalface_alt2.xml',
    'haarcascade_frontalface_alt_tree.xml',
    'haarcascade_profileface.xml'
]

scaleFactor = 1.1
minNeighbors = 5
minSize = (30, 30)

source = input("1. Kamera\n2. Video\nSecim: ")
if source == "1":
    cap = cv2.VideoCapture(0)
elif source == "2":
    if not os.path.exists('video.mp4'):
        print("video.mp4 bulunamadi")
        exit()
    cap = cv2.VideoCapture('video.mp4')
else:
    print("Hatali Giris Yaptiniz")
    exit()

buffer_size = 5
detections_buffer = []
resize_factor = 0.5
frame_skip = 5
frame_count = 0

gray_frame = cv2.cvtColor(cv2.resize(cap.read()[1], (0, 0), fx=resize_factor, fy=resize_factor), cv2.COLOR_BGR2GRAY)
cascade_performance = []

for cascade in cascades:
    classifier = cv2.CascadeClassifier(f"data/{cascade}")
    faces = classifier.detectMultiScale(gray_frame, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    cascade_performance.append((len(faces), cascade))

best_cascade = max(cascade_performance, key=lambda x: x[0])[1]
classifier = cv2.CascadeClassifier(f"data/{best_cascade}")

def updatePeopleCount(l):
    cv2.putText(frame, f"Kisi Sayisi: {str(l)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 127, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, f"Kullanilan lib: {best_cascade}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 127, 255), 2, cv2.LINE_AA)
    cv2.setWindowTitle("facesx", f"Kisi Sayisi: {str(l)}")

tracked_faces = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % frame_skip != 0:
        cv2.imshow('facesx', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    small_frame = cv2.resize(frame, (0, 0), fx=resize_factor, fy=resize_factor)
    gray_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    for (x, y, w, h) in tracked_faces:
        cv2.rectangle(frame, (int(x / resize_factor), int(y / resize_factor)), 
                      (int((x + w) / resize_factor), int((y + h) / resize_factor)), 
                      (0, 255, 0), 2)

    faces = classifier.detectMultiScale(gray_frame, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    
    current_faces = []

    for (x, y, w, h) in faces:
        x, y, w, h = int(x / resize_factor), int(y / resize_factor), int(w / resize_factor), int(h / resize_factor)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        current_faces.append((x, y, w, h))

    tracked_faces = []

    for face in current_faces:
        if len(tracked_faces) == 0:
            tracked_faces.append(face)
        else:
            matched = False
            for (tx, ty, tw, th) in tracked_faces:
                if abs(face[0] - tx) < tw and abs(face[1] - ty) < th:
                    matched = True
                    break
            if not matched:
                tracked_faces.append(face)

    detections_buffer.append(len(tracked_faces))
    if len(detections_buffer) > buffer_size:
        detections_buffer.pop(0)

    avg_faces = int(np.mean(detections_buffer))

    updatePeopleCount(avg_faces)

    cv2.imshow('facesx', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
