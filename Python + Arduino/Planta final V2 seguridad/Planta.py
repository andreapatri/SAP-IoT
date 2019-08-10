import serial
import time
from Tkinter import *
root = Tk()
ser = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1)
flagCharacter = 'k'
			
#--------------------- DECLARACION DE VARIABLES ------------------------------#		

canvas = Canvas(root, width=1024, height=574)
canvas.pack()
photo = PhotoImage(file= r"rsz_fiori.gif")
label=Label(root, image=photo)
photo = PhotoImage(file= r"rsz_fiori.gif")
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, image=photo, anchor='nw')

#-------------------------------- FUNCIONES ----------------------------------#			
	
def sensores(x,y,z):
	#canvas.create_rectangle(140, 100, 210, 175, fill="white", outline = "white")
	borrar()
	canvas.create_text(330, 150, text=x, fill="gray", font="Helvetica 45 bold",tag="T2")
	canvas.create_text(465, 150, text=y, fill="gray", font="Helvetica 45 bold",tag="T3")
	canvas.create_text(595, 150, text=z, fill="gray", font="Helvetica 45 bold",tag="T4")

def borrar():
	canvas.delete("T2")
	canvas.delete("T3")
	canvas.delete("T4")

def do_update():
    ser.write(flagCharacter)
    allitems=ser.readline(3)
    print allitems
    if(allitems == "701"):
		sensores(7,0,1)
    if(allitems == "900"):
		sensores(9,0,0)
    if(allitems == "901"):
		sensores(9,0,1)
    if(allitems == "990"):
		sensores(0,9,0)
    root.after(300, do_update)
    
#------------------------------------ MAIN -------------------------------------#  
try:
	canvas.create_text(190, 150, text="9", fill="gray", font="Helvetica 45 bold",tag="T1")
	canvas.create_text(330, 150, text="7", fill="gray", font="Helvetica 45 bold",tag="T2")
	canvas.create_text(465, 150, text="0", fill="gray", font="Helvetica 45 bold",tag="T3")
	canvas.create_text(595, 150, text="1", fill="gray", font="Helvetica 45 bold",tag="T4")
	do_update()
	root.mainloop()

except:

	pass  	