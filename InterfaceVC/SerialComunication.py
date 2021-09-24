

import serial
import time


arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_serial(x):
    arduino.write(bytes(x, "utf-8"))
    time.sleep(0.01)


def cordenadas(event, cord):
    x, y = cord
    msg = "c" + format(x, '03d')+","+format(y, '03d')
    write_serial(msg)
