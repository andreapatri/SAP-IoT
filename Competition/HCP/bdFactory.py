import datetime
import time
import urllib3
try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
#url = 'https://iotmmsb7af91ae6.us1.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
url = 'https://iotmmsi843568trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = 'dac00507-e0d4-4ea5-98f1-9346ac71f90c'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'd19954b4b51d8c3f5df3ab21845aca9' 
headers['Content-Type'] = 'application/json;charset=utf-8'

#I just started with random numbers, you can choose what ever you like

InProcessQty = 0
ProducedQty = 9
ProductAlerts = 0

#just put in 3 rows into the DB 

for x in range(0, 10):

	current_time = int (time.time() *100) 
	timestamp =str (current_time)

	stringInProcessQty =  str (InProcessQty)
	stringProducedQty = str (ProducedQty) 
	stringProductAlerts = str (ProductAlerts) 

	print (str (current_time))
	# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
	# replace messagetypeid with id from IOT cockpit
	body='{"messageType":"1b462f382c29ddc2d24c","mode":"sync","messages":[{"timestamp":'
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









