import datetime
import time
import urllib3
# disable InsecureRequestWarning if your are working without certificate verification
# see https://urllib3.readthedocs.org/en/latest/security.html # be sure to use a recent enough urllib3 version if this fails
try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmsb7af91ae6.us1.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
#url = 'https://iotmmsi843568trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
#deviceID = 'b7e75e6a-0364-494b-a6c4-7a25af775ea9'
deviceID = '34d074e3-ad45-42b7-bc9f-d3ee28765424'
url = url +deviceID
headers = urllib3.util.make_headers()
#headers['Authorization'] = 'Bearer ' + '64a33a2048da5ed80a854b6789084da' 
headers['Authorization'] = 'Bearer ' + 'ecde36ac5bf57a96943c3bc34c338a6b' 
headers['Content-Type'] = 'application/json;charset=utf-8'

#I just started with random numbers, you can choose what ever you like

MM_water =1
MM_pages =2
MM_car=3
MM_bike = 4
LN_water = 5
LN_pauses = 6 
LN_bike = 7
LN_walk = 8
LN_pages = 9
LN_car = 10

#just put in 3 rows into the DB 

for x in range(0, 10):

	current_time = int (time.time() *100) 
	timestamp =str (current_time) 

	inumber = 1843568
	MM_water = MM_water + 1
	MM_pages = MM_pages + 2
	MM_car= MM_car + 3
	MM_bike = MM_bike + 4
	LN_water = LN_water + 5
	LN_pauses = LN_pauses + 6 
	LN_bike = LN_bike + 7
	LN_walk = LN_walk + 8
	LN_pages = LN_pages + 9
	LN_car = LN_car + 10

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









