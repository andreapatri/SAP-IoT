import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache
from random import randint
import smtplib

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 



while (1==1):
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		data = int(myData) 
		print data
                if data == 1:
                        print "OK"
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login("demoinventorysap@gmail.com", "SAPSAP2017")
                        msg = "We have created a new order, to add something else to your basket go to www.goo.gl/FcKv8N "
                        server.sendmail("demoinventorysap@gmail.com", "demoinventorysap@gmail.com", msg)
                        server.quit()






