import datetime
import time
import urllib3
import serial #Import Serial Library


try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

http = urllib3.PoolManager()
url = 'https://iotmmsp1942747344trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '7a604597-bcfb-41ce-b37f-0dc8d71c44ba' #Este es el id que se encuentra en "Devices"
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'ed121e414099d0384d2efc34399b71ab' #Numero de seguridad que aparece cuando se genera
headers['Content-Type'] = 'application/json;charset=utf-8'

current_time = int (time.time() *100) 
timestamp =str (current_time)

body ='{"messageType":"cff8651e719b7a52ee80","mode":"async","messages":[{"timestamp":'
body=body+timestamp
body = body +',"sensor":'+str (1) 
body = body +',"value":'+ str (2) 
body = body +',"timestamp":'+ str (3)  +'}]}'
print body

print ("")
print body
r = http.urlopen('POST', url, body=body, headers=headers)
print ("")
print (r.status)
print (r.data)
