ßimport serial
import time
from Tkinter import *
root = Tk()
ser = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=None)
flagCharacter = 'k'
			
canvas = Canvas(root, width=1343, height=1278)
canvas.pack()

photo = PhotoImage(file= r"ANDREA-3.gif")
label=Label(root, image=photo)
photo = PhotoImage(file= r"ANDREA-3.gif")
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, image=photo, anchor='nw')


	
def sensores(planeado, producido, alertas):

	canvas.create_text(390, 430, text=planeado, fill="gray", font="Helvetica 100 bold",tag="T1")
	canvas.create_text(650, 430, text=producido, fill="gray", font="Helvetica 100 bold",tag="T2")		
	canvas.create_text(900, 430, text=alertas, fill="gray", font="Helvetica 100 bold",tag="T3")

def borrar():
	canvas.delete("T1")
	canvas.delete("T2")
	canvas.delete("T3")

def do_update():
    ser.write(flagCharacter)
    borrar()
    allitems=ser.readline(4)
    print allitems
    x, y = allitems.split()
    if(y>x):
        f=x
    	x=y
    	y=f
    sensores(9, x, y)
    root.after(1000, do_update)

do_update()
root.mainloop()




