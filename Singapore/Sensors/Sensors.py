import datetime
import time
import urllib3
import serial 
import linecache

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmssdctechmo.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = 'f905e20c-c6b5-4914-90f2-ed5759eee530'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '95e61ccaef41fbf1f4cd9788d429df' 
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		
		button = 1 #lista[0]
		temperature = 2 #lista[1]
		humidity = 3 #lista[2]
		tilt = 4 #lista[3]
		infrared = 5 #lista[4]
		light = 6 #lista[5]

		stringbutton = str (button) 
                stringtemperature = str(temperature) 
		stringhumidity= str(humidity) 
                stringtilt = str (tilt) 
                stringinfrared = str(infrared) 
		stringlight= str(light) 
		
		print (str (current_time))

                body='{"messageType":"ac6310d95a95df9a14ea","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
	
		body = body +',"button":'+stringbutton
		body = body +',"temperature":'+stringtemperature
                body = body +',"humidity":'+stringhumidity
		body = body +',"tilt":'+stringtilt
		body = body +',"infrared":'+stringinfrared
		body = body +',"light":'+ stringlight+'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






