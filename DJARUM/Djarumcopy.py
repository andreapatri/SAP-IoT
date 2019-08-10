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
deviceID = '45bd4983-33ce-40ef-bbb3-36cc1cc99ae8'
url = url +deviceID
headers = urllib3.util.make_headers()
headers['Authorization'] = 'Bearer ' + 'ed47179cbaa3ba12e86b768d43f5e5f' 
headers['Content-Type'] = 'application/json;charset=utf-8'


while (1==1):
                current_time = int (time.time() *100) 
                timestamp =str (current_time)
          
 #         if (arduinoSerialData.inWaiting()>0):
          
#                myData = arduinoSerialData.readline()
#                lista = myData.split(" ")

                Rfid = 3
		Temp = 29
		Alert = 0
		Weight = 66
                      
                stringRfid = str(Rfid) 
                stringTemp = str(Temp)
                stringAlert = str(Alert)
                stringWeight = str(Weight) 
                                
                print (str (current_time))

                body='{"messageType":"b325a06fb18e2aa8d1c3","mode":"async","messages":[{"timestamp":'
                body=body+timestamp                        

                body = body +',"Rfid":'+stringRfid
                body = body +',"Temp":'+ stringTemp
                body = body +',"Alert":'+stringAlert
                body = body +',"Weight":'+stringWeight +'}]}'
                print body

                print ("")
                print (body)
                r = http.urlopen('POST', url, body=body, headers=headers)
                print ("") 
                print(r.status) 
                print(r.data)
                 






