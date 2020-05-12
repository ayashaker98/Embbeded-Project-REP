import serial
import tkinter as tk
import time
COM = input("Enter Com port: ")
br = input("Enter BaudRate: ")
ser = serial.Serial(COM ,baudrate = br,timeout = 1)
ser.flushInput()
ser.flushOutput()


while True:
    line = ser.read(ser.in_waiting)
    if line == b'':
        time.sleep(1)  # be sure we don't try too often to request data
        continue
    else:
        line = line.decode('ascii')
        print(line)


