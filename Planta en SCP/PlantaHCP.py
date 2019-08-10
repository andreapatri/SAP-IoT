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
deviceID = 'e4d91c3d-f25f-4318-9ac5-34128062c1fd'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '89b8e7ff72d6e8ff92e608bcf12763d' 
headers['Content-Type'] = 'application/json;charset=utf-8'

while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		
		InProcessQty = lista[0]
		ProducedQty = lista[1]
                ProductAlerts = lista[2]		

                stringInProcessQty =  str (InProcessQty)
        	stringProducedQty = str (ProducedQty) 
                stringProductAlerts = str (ProductAlerts) 
		
		print (str (current_time))
		# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
		# replace messagetypeid with id from IOT cockpit
		#body='{"messageType":"91fb92c97a2fc19a9d10","mode":"sync","messages":[{"timestamp":'
                body='{"messageType":"36b95c76915d3aad10d7","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
                body = body +',"InProcessQty":'+ stringInProcessQty
                body = body +',"ProducedQty":'+stringProducedQty 
        	body = body +',"ProductAlerts":'+stringProductAlerts+'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






