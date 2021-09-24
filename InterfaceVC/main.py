

import cv2 as cv

from identificar import bola, pessoa

from SerialComunication import cordenadas

pessoas = ['Dinossauro Bebado']

# se quiser passar um video para o programa descomentar essa linha
#video = r"src\VisualRec\midia\MalabBruto1.mp4"

# para usar a webcam deixar essa linha
video = ""

# para salvar o video modificado em AVi modar essa bol
# Testado no windons
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
        # função para o reconhecimento da bola retorna as  cordenadas da bola tupla
        frame, cord = bola(frame)

        if(cord != None):
            cordenadas(cord)
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
