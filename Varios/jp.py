import datetime
import time
import urllib3
import serial 
import linecache

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

http = urllib3.PoolManager()
url = 'https://iotmmsa1305c29f.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '3cd5e96e-09b4-4331-878f-491b2c0a24bd'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '15ce7eb28eb59eb029f1e1ecf8434b1' 
headers['Content-Type'] = 'application/json;charset=utf-8'

x=y=z=1

while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	Sensor1 = x
	Sensor2 = y
	Sensor3 = z
		
	stringSensor1 = str (Sensor1) 
        stringSensor2 = str(Sensor2) 
	stringSensor3 = str(Sensor3) 
		
	print (str (current_time))

        body='{"messageType":"7acaddab5ad5173d0561","mode":"async","messages":[{"timestamp":'
        body=body+timestamp                        
	
	body = body +',"Sensor1":'+stringSensor1
	body = body +',"Sensor2":'+stringSensor2
	body = body +',"Sensor3":'+ stringSensor3 +'}]}'
	print body

	print ("")
	print (body)
	r = http.urlopen('POST', url, body=body, headers=headers)
	print ("") 
	print(r.status) 
	print(r.data)
	time.sleep(3)
	x=x+1
	y=y+2
	z=x+y
	
	
         






