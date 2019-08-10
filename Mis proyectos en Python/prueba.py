import serial
import time
from Tkinter import *
root = Tk()
ser = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1)
flagCharacter = 'k'
			
canvas = Canvas(root, width=1024, height=574)
canvas.pack()

photo = PhotoImage(file= r"rsz_fiori.gif")
label=Label(root, image=photo)
photo = PhotoImage(file= r"rsz_fiori.gif")
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, image=photo, anchor='nw')
	
def sensores(planeado, producido, alertas):
	canvas.create_text(190, 150, text=planeado, fill="gray", font="Helvetica 45 bold",tag="T1")
	canvas.create_text(333, 150, text=producido, fill="gray", font="Helvetica 45 bold",tag="T2")
	canvas.create_text(463, 150, text=alertas, fill="gray", font="Helvetica 45 bold",tag="T3")
	#root.after(1000,sensores)

def borrar():
	canvas.delete("T1")
	canvas.delete("T2")
	canvas.delete("T3")

# while True:
# 	ser.write(flagCharacter)
# 	allitems=ser.readline(6)
# 	x, y, z = allitems.split()
# 	sensores(x, y, z)
# 	root.mainloop()

def do_update():
    ser.write(flagCharacter)
    borrar()
    allitems=ser.readline(6)
    x, y, z = allitems.split()
    sensores(x, y, z)
    root.after(1000, do_update)

do_update()
root.mainloop()




