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

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmssdctechmo.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '3c8c1ccf-f2bd-49de-bd8b-386072d9fb27'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '8e18a0e245d8c6a199f9248ad2694a' 
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
        current_time = int (time.time() *100) 
	timestamp =str (current_time) 

        light = 12
	temperature = 22.1
	pressure = 799.3
	accelerationX = 0.17
	accelerationY = 0.00
	accelerationZ = 0.01
		
	stringlight = str (light) 
	stringtemperature = str(temperature) 
	stringpressure = str(pressure)
	stringaccelerationX= str(accelerationX)
	stringaccelerationY= str(accelerationY)
	stringaccelerationZ= str(accelerationZ)

		
	print (str (current_time))
	body='{"messageType":"52a85d6caea96b5d7384","mode":"async","messages":[{"timestamp":'
        body=body+timestamp                        
	body = body +',"light":'+stringlight
	body = body +',"temperature":'+stringtemperature
	body = body +',"pressure":'+stringpressure
	body = body +',"accelerationX":'+stringaccelerationX 
	body = body +',"accelerationY":'+stringaccelerationY 
	body = body +',"accelerationZ":'+stringaccelerationZ +'}]}'
	print body

	print ("")
	print (body)
	r = http.urlopen('POST', url, body=body, headers=headers)
	print ("") 
	print(r.status) 
	print(r.data)
         






