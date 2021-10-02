

import serial
import time
import tkinter as tk


def motion(event):
    x, y = event.x, event.y
    return(x, y)


def mouseMov():
    root = tk.Tk()
    root.geometry('500x500')
    root.bind('<Motion>', motion)
    root.mainloop()


'''while True:
    msg = input("cxxx,yyy")
    write_read(msg)
    print(str(arduino.readline()))'''
