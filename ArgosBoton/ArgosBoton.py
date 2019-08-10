import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) #Esta linea cambia en windows COM3,4,5

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

http = urllib3.PoolManager()
url = 'https://iotmmsp1942166068trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '58a10e8a-0231-463f-b052-e165c6487f5e' #Este es el id que se encuentra en "Devices"
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'd4a8b16532962267d1f25999b71cb5' #Numero de seguridad que aparece cuando se genera
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		boton1 = lista[0]
		boton2 = lista[1]
		
		stringboton1 = str (boton1) 
		stringboton2 = str(boton2) 

		print (str (current_time))
                body='{"messageType":"633be6f0143c5537eee2","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
		body = body +',"boton1":'+stringboton1
		body = body +',"boton2":'+stringboton2+'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






