

import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, "utf-8"))
    time.sleep(0.01)


while True:
    msg = input("cxxx,yyy")
    write_read(msg)
    print(str(arduino.readline()))
