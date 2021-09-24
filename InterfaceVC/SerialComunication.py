

import serial
import time
# alterar a porta para a do ESP
esp = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_serial(x):
    esp.write(bytes(x, "utf-8"))
    time.sleep(0.01)


def cordenadas(cord):

    x, y = cord
    msg = "c" + format(x, '03d')+","+format(y, '03d')
    print(msg)
    write_serial(msg)
