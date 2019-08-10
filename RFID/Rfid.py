import serial
import time
from Tkinter import *
root = Tk()
ser = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1)
flagCharacter = 'k'
			
#-------------------------------- FUNCIONES ----------------------------------#			
	
def do_update():

    ser.write(flagCharacter)
    allitems=ser.readline()
    if(len(allitems)> 6):
        print allitems
        file = open("/Users/andreapatri/Dropbox/IoT/RFID/Lumira.txt", "w")
        file.write("Material Cantidad Ubicacion" + "\n")
        file.write("Decorativo " + allitems[0] + " Bogota" + "\n")
        file.write("Decorativo 4 Cota" + "\n")
        file.write("Decorativo 3 Chia" + "\n")
        file.write("FiltroUV " + allitems[2] + " Bogota" + "\n")
        file.write("FiltroUV 1 Cota" + "\n")
        file.write("FiltroUV 2 Chia" + "\n")
        file.close()    

    root.after(300, do_update)

#------------------------------------ MAIN -------------------------------------#  
try:
	do_update()
	root.mainloop()

except:

	pass  	
