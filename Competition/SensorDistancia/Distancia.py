import serial #Import Serial Library

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print myData
