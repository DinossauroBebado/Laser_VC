

import serial
import time
import tkinter as tk


arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
root = tk.Tk()
root.geometry('500x500')


def write_read(x):
    arduino.write(bytes(x, "utf-8"))
    time.sleep(0.01)


def motion(event):
    x, y = event.x, event.y
    msg = "c" + format(x, '03d')+","+format(y, '03d')
    write_read(msg)


root.bind('<Motion>', motion)
root.mainloop()


'''while True:
    msg = input("cxxx,yyy")
    write_read(msg)
    print(str(arduino.readline()))'''
