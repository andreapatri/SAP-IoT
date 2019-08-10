import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache

#arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) #Esta linea cambia en windows COM3,4,5

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
#	if (arduinoSerialData.inWaiting()>0):
	#	myData = arduinoSerialData.readline()
	#	lista = myData.split(" ")
		materiala = 7 # lista[0]
		materialb = 7 # lista[1]
		overheating = 7
		temperature = 7
		
		stringmateriala = str(materiala) 
		stringmaterialb = str(materialb)
		stringoverheating= str(overheating)
		stringtemperature = str(temperature)
		

		print (str (current_time))
                body='{"messageType":"3aac1a7fd860c970be0b","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
		body = body +',"materiala":'+stringmateriala
		body = body +',"materialb":'+stringmateriala
		body = body +',"overheating":'+stringmateriala
		body = body +',"temperature":'+stringmaterialb+'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






