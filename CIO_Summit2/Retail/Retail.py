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

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmssdctechmo.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '7319efcb-da10-49e8-b707-8b707dbd422e'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'ff096c1b5306c622369d42bcc807d8b' 
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		Weight = lista[1]
		Door = lista[2]
		Temp1 = lista[0]

		
		stringWeight = str (Weight) 
                stringDoor = str(Door) 
		stringTemp1 = str(Temp1) 
		
		print (str (current_time))

                body='{"messageType":"1e06cf11f29d6c13c8e3","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
	
		body = body +',"Weight":'+stringWeight
		body = body +',"Door":'+stringDoor
		body = body +',"Temp1":'+ stringTemp1 +'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






