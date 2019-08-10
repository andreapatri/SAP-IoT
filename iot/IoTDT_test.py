import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache
from random import randint

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmsa1305c29f.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '3cd5e96e-09b4-4331-878f-491b2c0a24bd'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '15ce7eb28eb59eb029f1e1ecf8434b1' 
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 

	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
        	lista = myData.split(" ")

        Sensor1 = randint(0, 9) # lista[0] line chart 
        Sensor2 = randint(10, 20) #lista[1] line chart
        Sensor3 = 1000 #lista[2] waterfall
        Sensor4 = 150 #bullet micro chart
        Sensor5 = 200 #column chart 
        Sensor6A = 300 #double column chart 1
        Sensor6B = 10 # double column chart 2
        Sensor7A = 500 #radial micro chart 1
        Sensor7B = 13 #radial micro chart 2
        Sensor8 = 300 #geomap
        Sensor9 = 0
        Sensor10 = 0
        Sensor11 = 0
        Sensor12 = 0
        Sensor13 = 0
	
	stringSensor1 = str (Sensor1)
	stringSensor2 = str (Sensor2)
	stringSensor3 = str (Sensor3)
	stringSensor4 = str (Sensor4)
	stringSensor5 = str (Sensor5)
	stringSensor6A = str (Sensor6A)
	stringSensor6B = str (Sensor6B)
	stringSensor7A = str (Sensor7A)
	stringSensor7B = str (Sensor7B)
	stringSensor8 = str (Sensor8)
	stringSensor9 = str (Sensor9)
	stringSensor10 = str (Sensor10)
	stringSensor11 = str (Sensor11)
	stringSensor12 = str (Sensor12)
	stringSensor13 = str (Sensor13) 
		
	print (str (current_time))

        body='{"messageType":"07afa34044c1e7fec6d3","mode":"async","messages":[{"timestamp":'
        body=body+timestamp                        
	
	body = body +',"Sensor1":'+stringSensor1
	body = body +',"Sensor2":'+stringSensor2
	body = body +',"Sensor3":'+stringSensor3
	body = body +',"Sensor4":'+stringSensor4
        body = body +',"Sensor5":'+stringSensor5
	body = body +',"Sensor6A":'+stringSensor6A
	body = body +',"Sensor6B":'+stringSensor6B
	body = body +',"Sensor7A":'+stringSensor7A
	body = body +',"Sensor7B":'+stringSensor7B
	body = body +',"Sensor8":'+stringSensor8
	body = body +',"Sensor9":'+stringSensor9
	body = body +',"Sensor10":'+stringSensor10
	body = body +',"Sensor11":'+stringSensor11
	body = body +',"Sensor12":'+stringSensor12
	body = body +',"Sensor13":'+ stringSensor13+'}]}'
	print body

	print ("")
	print (body)
	r = http.urlopen('POST', url, body=body, headers=headers)
	print ("") 
	print(r.status) 
	print(r.data)

         






