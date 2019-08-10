import datetime
import time
import urllib3
try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmssdctechmo.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = 'f85bc05a-1340-4382-8a36-2843fe09007c'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + '9a44efa9ea1ea9a7c27156a99cb9b97' 
headers['Content-Type'] = 'application/json;charset=utf-8'

#I just started with random numbers, you can choose what ever you like

InProcessQty = 2
ProducedQty = 2
ProductAlerts = 2

#just put in 3 rows into the DB 

for x in range(0, 10):

        ProductAlerts = ProductAlerts + 1
	current_time = int (time.time() *100) 
	timestamp =str (current_time)

	stringInProcessQty =  str (InProcessQty)
	stringProducedQty = str (ProducedQty) 
	stringProductAlerts = str (ProductAlerts) 

	print (str (current_time))
	# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
	# replace messagetypeid with id from IOT cockpit
	body='{"messageType":"36b95c76915d3aad10d7","mode":"sync","messages":[{"timestamp":'
	body=body+timestamp
	
	body = body +',"InProcessQty":'+ stringInProcessQty
	body = body +',"ProducedQty":'+stringProducedQty 
	body = body +',"ProductAlerts":'+stringProductAlerts+'}]}'

	print ("")
	print (body)
	r = http.urlopen('POST', url, body=body, headers=headers)
	print ("") 
	print(r.status) 
	print(r.data)









