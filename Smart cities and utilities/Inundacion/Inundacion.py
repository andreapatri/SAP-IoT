import serial
import time
from Tkinter import *
root = Tk()
ser = serial.Serial("/dev/cu.usbmodem1421", 9600, timeout=1)
flagCharacter = 'k'
			
#-------------------------------- FUNCIONES ----------------------------------#			
	
def do_update():

    ser.write(flagCharacter)
    allitems=ser.readline()
    if(len(allitems)> 4):
        print allitems
        file = open("/Users/andreapatri/Dropbox/IoT/BA_sensors.txt", "w")
        file.write("Circunstancia,Intensidad,Ubicacion"+ "\n")
        file.write("Lluvia," + allitems[0] + ",Buenos Aires" + "\n")
        file.write("Innundacion," + (allitems[2]) + ",Buenos Aires" + "\n")
        file.write("Lluvia,0,Rio Cuarto"+ "\n")
        file.write("Lluvia,0,Tandil"+ "\n")
        file.write("Innundacion,0,Rio Cuarto"+ "\n")
        file.write("Innundacion,0,Tandil"+ "\n")
        file.write("Basuras,0,Buenos Aires"+ "\n")
        file.write("Basuras,0,Rio Cuarto"+ "\n")
        file.write("Basuras,0,Tandil"+ "\n")
        file.close()    

    root.after(300, do_update)

#------------------------------------ MAIN -------------------------------------#  
try:
	do_update()
	root.mainloop()

except:

	pass  	
