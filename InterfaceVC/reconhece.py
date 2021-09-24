import numpy as np
import cv2 as cv


def scale(frame, scale):
    altura = int(frame.shape[0]*scale)
    largura = int(frame.shape[1]*scale)
    dimensoes = (largura, altura)
    return cv.resize(frame, dimensoes, interpolation=cv.INTER_AREA)


haar_cascade = cv.CascadeClassifier(r'haar_face.xml')

TOLERANCIA = 100

people = ['Dinossauro Bebado']


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'treinado_DINO.yml')

img = cv.imread(r'_GPS1495.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 7)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    if confidence > TOLERANCIA:
        continue
    cv.putText(img, str(people[label]), (x, y),
               cv.FONT_HERSHEY_COMPLEX, 5.0, (255, 0, 0), thickness=4)
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=5)

cv.imshow('Detected Face', scale(img, 0.4))

cv.waitKey(0)
