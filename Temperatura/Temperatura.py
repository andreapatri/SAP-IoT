import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1421", 9600, timeout=1) #Esta linea cambia en windows COM3,4,5

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

http = urllib3.PoolManager()
url = 'https://iotmmsp1942253730trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = 'e6c09550-3148-4344-9a55-6c92a030833c' #Este es el id que se encuentra en "Devices"
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'e1126f7ed4b02974ae89d16329c23dc' #Numero de seguridad que aparece cuando se genera
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		temp = lista[0]
		humed = lista[1]
		
		stringtemp = str (temp) 
		stringhumed = str(humed) 

		print (str (current_time))
                body='{"messageType":"ddd4889d84442a894452","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
		body = body +',"temp":'+stringtemp
		body = body +',"humed":'+stringhumed+'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






