import serial
from Tkinter import *

ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

def update():
	while 1: 
		e = ser.readline()
		sensor1= e [0:1]
		sensor2= e [1:2]
		sensor3= e [2:3]
		readingsensor1.set(sensor1)
		readingsensor2.set(sensor2)
		readingsensor3.set(sensor3)
		root.update()
		sleep(1)

root = Tk()

canvas = Canvas(root, width=1024, height=574)
canvas.pack()
photo = PhotoImage(file= r"rsz_fiori.gif")
label=Label(root, image=photo)
photo = PhotoImage(file= r"rsz_fiori.gif")
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, image=photo, anchor='nw')
	
readingsensor1 = StringVar()
readingsensor2 = StringVar()
readingsensor3 = StringVar()

s1=canvas.create_text(190, 150, text=readingsensor1, fill="gray", font="Helvetica 45 bold",tag="T1")
s2=canvas.create_text(333, 150, text=readingsensor2, fill="gray", font="Helvetica 45 bold",tag="T2")
s3=canvas.create_text(533, 150, text=readingsensor3, fill="gray", font="Helvetica 45 bold",tag="T3")

canvas.delete("T3")	
canvas.delete("T2")
#canvas.delete("T1")


mainloop()

