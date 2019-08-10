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

# http = urllib3.proxy_from_url('http://proxy_host:proxy_port')

# interaction for a specific Device instance - replace 1 with your specific Device ID

# url = 'https://iotmms_on_your_trial_system.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/1'

url = 'https://iotmmsi843568trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'

deviceID = 'b7e75e6a-0364-494b-a6c4-7a25af775ea9'

url = url +deviceID
headers = urllib3.util.make_headers()
# use with authentication
# please insert correct OAuth token 
headers['Authorization'] = 'Bearer ' + '64a33a2048da5ed80a854b6789084da' 
headers['Content-Type'] = 'application/json;charset=utf-8'

#I just started with random numbers, you can choose what ever you like
temperature =1
humidity =50
brightness=100
#just put in 3 rows into the DB 

for x in range(0, 10):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	brightness= brightness+1 
	humidity=humidity+1 
	temperature=temperature+1 
	stringBrightness = str (brightness) 
	stringHumidity = str(humidity) 
	stringTemperature = str(temperature)
	print (str (current_time))
	# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
	# replace messagetypeid with id from IOT cockpit
	body='{"messageType":"2d5275e0437f7199dfb2","mode":"sync","messages":[{"timestamp":'
	body=body+timestamp
	body = body +',"Humidity":'+stringHumidity 
	body = body +',"Brightness":'+stringBrightness 
	body = body +',"Temperature":'+stringTemperature+'}]}'

	print ("")
	print (body)
	r = http.urlopen('POST', url, body=body, headers=headers)
	print ("") 
	print(r.status) 
	print(r.data)










