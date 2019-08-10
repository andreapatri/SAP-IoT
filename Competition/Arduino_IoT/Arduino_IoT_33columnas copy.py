import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

http = urllib3.PoolManager()
url = 'https://iotmmsi843568trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = 'b7e75e6a-0364-494b-a6c4-7a25af775ea9'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '64a33a2048da5ed80a854b6789084da' 
headers['Content-Type'] = 'application/json;charset=utf-8'

while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		Temperatura = lista[0]
		Distancia = lista[1]
		Peso1 = lista[2]
		Peso2 = lista[3]
		Peso3 = lista[4]
		Pasos = lista[5]
		stringTemperature = str (Temperatura) 
		stringDistance = str(Distancia) 
		stringWeight1 = str(Peso1)
		stringWeight2 = str (Peso2) 
		stringWeight3 = str(Peso3) 
		stringSteps = str(Pasos)
		print (str (current_time))
		# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
		# replace messagetypeid with id from IOT cockpit
		body='{"messageType":"91fb92c97a2fc19a9d10","mode":"sync","messages":[{"timestamp":'
		body=body+timestamp
		body = body +',"Temperature":'+stringTemperature
		body = body +',"ActivePause":'+stringDistance 
		body = body +',"Weight1":'+stringWeight1 +'}]}'

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)

		#EntradasArduinoYun2
		print (str (current_time))
		body='{"messageType":"d6ff6fa25ece28281037","mode":"sync","messages":[{"timestamp":'
		body=body+timestamp
		body = body +',"Weight2":'+stringWeight2
		body = body +',"Weight3":'+stringWeight3
		body = body +',"Steps":'+stringSteps +'}]}'

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






