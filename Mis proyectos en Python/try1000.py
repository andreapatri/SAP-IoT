import serial
import time
from Tkinter import *
root = Tk()

ser = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1)

line=ser.readline()
line=valor.strip('\n')
x, y, z = line.split()
print x,y,z