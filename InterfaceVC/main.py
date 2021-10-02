

import cv2 as cv

from identificar import bola, pessoa

import SerialComunication

import SerialComMouse

import threading
pessoas = ['Dinossauro Bebado']

config = {"salvar": False, "mouse": False,
          "simulation": False}  # mouse feature not working

# TO DO
# fix mouse function

# se quiser passar um video para o programa descomentar essa linha
#video = r"src\VisualRec\midia\MalabBruto1.mp4"

# para usar a webcam deixar essa linha
video = ""

# para salvar o video modificado em AVi mudar essa bol
# Testado no windons
salvar = config["salvar"]
simulation = config["simulation"]

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
        # função para o reconhecimento da bola retorna as  cordenadas da bola tupla
        if (config["mouse"]):
            y = threading.Thread(target=SerialComMouse.mouseMov)
            y.start()

        frame, cord = bola(frame)

        if(cord != None):
            x = threading.Thread(
                target=lambda: SerialComunication.cordenadas(cord))
            x.start()

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
