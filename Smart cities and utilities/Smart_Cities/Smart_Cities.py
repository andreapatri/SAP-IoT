import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache

#arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

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
	#if (arduinoSerialData.inWaiting()>0):
	#	myData = arduinoSerialData.readline()
	#	lista = myData.split(" ")
		sensor1 = 1
		sensor2 = 1
		sensor3 = 1
		sensor4 = 1
		sensor5 = 1
		sensor6 = 1
		sensor7 = 1
                sensor8 = 1
		sensor9 = 1
		sensor10 = 1
		
		stringsensor1 = str(sensor1) 
		stringsensor2 = str(sensor2)
		stringsensor3 = str(sensor3) 
		stringsensor4 = str(sensor4)
		stringsensor5 = str(sensor5) 
		stringsensor6 = str(sensor6)
		stringsensor7 = str(sensor7) 
		stringsensor8 = str(sensor8)
		stringsensor9 = str(sensor9) 
		stringsensor10 = str(sensor10)

		print (str (current_time))
                body='{"messageType":"5f11658ee8ec18d6973c","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
		body = body +',"sensor1":'+stringsensor1
		body = body +',"sensor2":'+stringsensor2
		body = body +',"sensor3":'+stringsensor3
		body = body +',"sensor4":'+stringsensor4
		body = body +',"sensor5":'+stringsensor5
		body = body +',"sensor6":'+stringsensor6
		body = body +',"sensor7":'+stringsensor7
		body = body +',"sensor8":'+stringsensor8
		body = body +',"sensor9":'+stringsensor9
		body = body +',"sensor10":'+stringsensor10+'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






