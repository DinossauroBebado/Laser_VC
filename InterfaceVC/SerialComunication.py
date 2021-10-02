

import serial
import time
# alterar a porta para a do ESP
esp = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_serial(x):
    esp.write(bytes(x, "utf-8"))
    time.sleep(0.01)


def cordenadas(cord):

    x, y = correcion(cord)
    msg = "c" + format(x, '03d')+","+format(y, '03d')
    print(msg)
    write_serial(msg)


def correcion(cord):
    correcion_x = -100
    correcion_y = 70
    neo_cordenadas = (cord[0] + correcion_x, cord[1]+correcion_y)
    return neo_cordenadas
