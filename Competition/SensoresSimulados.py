import datetime
import time
import urllib3
import random

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmsb7af91ae6.us1.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '34d074e3-ad45-42b7-bc9f-d3ee28765424'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'ecde36ac5bf57a96943c3bc34c338a6b' 
headers['Content-Type'] = 'application/json;charset=utf-8'

for x in range(0, 10):

	current_time = int (time.time() *100) 
	timestamp =str (current_time) 

	inumber = 1843568
	MM_water = (random.randint(0,1))
	MM_pages = (random.randint(0,1))
	MM_car= (random.randint(0,1))
	MM_bike = (random.randint(0,1))
	LN_water = (random.randint(0,6))
	LN_pauses = (random.randint(0,2))
	LN_bike = (random.randint(0,1))
	LN_walk = (random.randint(0,10))
	LN_pages = (random.randint(0,15))
	LN_car = (random.randint(0,1))

	stringID =  str (inumber)
	stringMM_water = str (MM_water) 
	stringMM_pages = str (MM_pages) 
	stringMM_car = str (MM_car) 
	stringMM_bike = str (MM_bike) 
	stringLN_water = str (LN_water) 
	stringLN_pauses = str (LN_pauses) 
	stringLN_bike = str (LN_bike) 
	stringLN_walk = str (LN_walk) 
	stringLN_pages = str (LN_pages) 
	stringLN_car = str (LN_car) 

	print (str (current_time))
	# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
	# replace messagetypeid with id from IOT cockpit
	body='{"messageType":"90565350a776a483b8b9","mode":"sync","messages":[{"timestamp":'
	body=body+timestamp
	
	body = body +',"ID":'+ stringID
	body = body +',"MMwater":'+stringMM_water 
	body = body +',"MMpages":'+stringMM_pages 
	body = body +',"MMcar":'+stringMM_car 
	body = body +',"MMbike":'+stringMM_bike
	body = body +',"LNwater":'+stringLN_water 
	body = body +',"LNpauses":'+stringLN_pauses
	body = body +',"LNbike":'+stringLN_bike 
	body = body +',"LNwalk":'+stringLN_walk
	body = body +',"LNpages":'+stringLN_pages 
	body = body +',"LNcar":'+stringLN_car+'}]}'

	print ("")
	print (body)
	r = http.urlopen('POST', url, body=body, headers=headers)
	print ("") 
	print(r.status) 
	print(r.data)









