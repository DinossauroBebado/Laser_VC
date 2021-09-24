import sys

import cv2 as cv

import imutils

from identificar import bola, pessoa

pessoas = ['Dinossauro Bebado']

#video = r"src\VisualRec\midia\MalabBruto1.mp4"
video = ""

salvar = False

if video == "":
    video_capture = cv.VideoCapture(0)
else:
    video_capture = cv.VideoCapture(video)
if(salvar):
    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    out = cv.VideoWriter('MalabCodeM.avi', fourcc, 29.0, (720,  404))


while True:
    # captura os frame tudo
    ret, frame = video_capture.read()
    frame = cv.resize(frame, (500, 500))
    if ret == True:
        # chama a função para usar o reconhecimento facial
        #pessoa(frame, pessoas)
        frame, cord = bola(frame)
        # mostra

        if(salvar):
            out.write(frame)
            cv.imshow('Video', frame)
        else:
            cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Fecha
if(salvar):
    out.release()
video_capture.release()
cv.destroyAllWindows()
print("-----------------DONE----------------")
