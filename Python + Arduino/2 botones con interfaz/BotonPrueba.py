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
	
def sensores(x,y):
	#canvas.create_rectangle(140, 100, 210, 175, fill="white", outline = "white")
	borrar()
	canvas.create_text(190, 150, text=x, fill="gray", font="Helvetica 45 bold",tag="T1")
	canvas.create_text(590, 150, text=y, fill="gray", font="Helvetica 45 bold",tag="T2")

def borrar():
	canvas.delete("T1")
	canvas.delete("T2")

def do_update():
    ser.write(flagCharacter)
    allitems=ser.readline(2)
    if(allitems == "11"):
		sensores(1,1)
    if(allitems == "10"):
    	sensores(1,0)
    if(allitems == "31"):
		sensores(3,1)
    if(allitems == "33"):
    	sensores(3,3)	
    root.after(300, do_update)
    
#------------------------------------ MAIN -------------------------------------#  
try:
	canvas.create_text(190, 150, text="3", fill="gray", font="Helvetica 45 bold",tag="T1")
	canvas.create_text(590, 150, text="3", fill="gray", font="Helvetica 45 bold",tag="T2")
	do_update()
	root.mainloop()

except:

	pass  	