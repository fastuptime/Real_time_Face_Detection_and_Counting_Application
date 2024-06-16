from deepface import DeepFace
import cv2
import numpy as np

frame = cv2.VideoCapture('video.mp4')

def updatePeopleCount(l):
    cv2.setWindowTitle("img", f"Kisi Sayisi: {str(l)}")
    cv2.putText(img, f"Kisi Sayisi: {str(l)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 127, 255), 2, cv2.LINE_AA)

while True:
    ret, img = frame.read()
    result = DeepFace.analyze(img, actions =['gender'], enforce_detection = False)
    for i in result:
        if i['region'] == {}: continue
        cv2.rectangle(img, (i['region']['x'], i['region']['y']), (i['region']['x']+i['region']['w'], i['region']['y']+i['region']['h']), (28, 42, 231), 2)
        cv2.putText(img, i['dominant_gender'], (i['region']['x'], i['region']['y']-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    updatePeopleCount(len(result))
    cv2.imshow('img', img)


    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame.release()
cv2.destroyAllWindows()