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
url = 'https://iotmmsp1942958052trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = 'ef658d01-c5c0-4cab-9801-2970e2125e11'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'ae60d9da54bb4b86fcc9e67a581e4487' 
headers['Content-Type'] = 'application/json;charset=utf-8'

x=y=z=1

while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	sensor1 = x
	sensor2 = y
	sensor3 = z
		
	stringsensor1 = str(sensor1) 
        stringsensor2 = str(sensor2) 
	stringsensor3 = str(sensor3) 
		
	print (str (current_time))

        body='{"messageType":"82de92985dfc82644651","mode":"async","messages":[{"timestamp":'
        body=body+timestamp                        
	
	body = body +',"sensor1":'+stringsensor1
	body = body +',"sensor2":'+stringsensor2
	body = body +',"sensor3":'+ stringsensor3 +'}]}'
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
	
	
         






