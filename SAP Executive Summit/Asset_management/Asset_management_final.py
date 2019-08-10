import datetime
import time
import urllib3
import serial #Import Serial Library
import linecache

arduinoSerialData = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout=1) 

try: 
	urllib3.disable_warnings()
except:
	print('urllib3.disable_warnings() failed - get a recentenough urllib3 version to avoid potential InsecureRequestWarning warnings! Can and will continue though.')

# use with or without proxy
http = urllib3.PoolManager()
url = 'https://iotmmssdctechmo.hana.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/'
deviceID = '7319efcb-da10-49e8-b707-8b707dbd422e'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'ff096c1b5306c622369d42bcc807d8b' 
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
	current_time = int (time.time() *100) 
	timestamp =str (current_time) 
	#sensores()
	if (arduinoSerialData.inWaiting()>0):
		myData = arduinoSerialData.readline()
		lista = myData.split(" ")
		Hit = lista[0]
		BrakeLiquid = lista[1]
                HardBreak = 45 #lista[2]		
		Revision = 1 #lista[3]
		
		stringHit = str (Hit) 
		stringBrakeLiquid = str(BrakeLiquid) 
		stringRevision = str(Revision)
		stringHardBreak = str(HardBreak)

		
		print (str (current_time))
		# send message body and the corresponding payload layout that you defined in the IoT Services Cockpit
		# replace messagetypeid with id from IOT cockpit
		#body='{"messageType":"91fb92c97a2fc19a9d10","mode":"sync","messages":[{"timestamp":'
                body='{"messageType":"3aac1a7fd860c970be0b","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        
		body = body +',"materiala":'+stringHit
		body = body +',"materialb":'+stringBrakeLiquid
		body = body +',"overheating":'+stringRevision 
		body = body +',"temperature":'+stringHardBreak +'}]}'
		print body

		print ("")
		print (body)
		r = http.urlopen('POST', url, body=body, headers=headers)
		print ("") 
		print(r.status) 
		print(r.data)
         






