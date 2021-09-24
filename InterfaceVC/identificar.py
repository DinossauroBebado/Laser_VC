import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier(r'InterfaceVC\haar_face.xml')
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r"InterfaceVC\treinado_DINO.yml")
TOLERANCIA = 100

verdeClaro = (21, 45, 102)  # modificar para um ajuste
verdeEscuro = (70, 255, 255)


def pessoa(frame, pessoas):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),

    )

    for (x, y, w, h) in faces:

        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        #print(f'Label = {pessoas[label]} with a confidence of {confidence}')
        if confidence > TOLERANCIA:
            continue
        cv.putText(frame, str(pessoas[label]), (x, y),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=1)
        cv.putText(frame, str(confidence)[:2], (x, y+h),
                   cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 0), thickness=1)

        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=1)

    return frame


def bola(frame):

    # aplica mascara das cores
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, verdeClaro, verdeEscuro)
    # filtra a imagem
    mascE = cv.erode(mask, None, iterations=2)
    mascD = cv.dilate(mascE, None, iterations=2)

   # acha os contornos
    cnts = cv.findContours(mascD.copy(), cv.RETR_EXTERNAL,
                           cv.CHAIN_APPROX_SIMPLE)[-2]
    # se tiver achado alguma coisa
    if len(cnts) > 0:

        c = max(cnts, key=cv.contourArea)
        for i in cnts:
            ((x, y), radius) = cv.minEnclosingCircle(c)

            if (radius < 300) & (radius > 10):

                cv.circle(frame, (int(x), int(y)), int(
                    radius), (255, 255, 255), 2)

                # X
                cv.line(frame, (int(x), 0), (int(x), 500),
                        (255, 255, 255), thickness=1)
                # Y
                cv.line(frame, (0, int(y)), (700, int(y)),
                        (255, 255, 255), thickness=1)

                cv.putText(frame, "X: " + str(int(x))+" Y: "+str(int(y)), (50, 375),
                           cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), thickness=1)
                cord = ((int(x), int(y)))

    return frame, cord
