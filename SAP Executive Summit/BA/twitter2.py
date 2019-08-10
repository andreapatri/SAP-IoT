 
from twython import TwythonStreamer

import RPi.GPIO as GPIO  
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11,GPIO.LOW)
flag = 0

C_Key = "4bZr0NRQvpDX6CIwpMFC3FG4v"
C_Secret = "7EZovvSr3fwFLWI2MYWgnlWaGeKQE7CHx94oPgc1GaoL5W1yaQ"
A_Token = "790965576432746496-jlQLqfkp3tG0uqJN6oAV0iclo0QQuOT"
A_Secret = "F942r9Gcy1PJYlUCoT2617DfYOZZGnMkYt5pezbWjfG6E"

count = 0

def action():
  global count
  global flag
  count = count + 1
  if count >= 5:
    if flag== 0:
  	print("OK")
  	GPIO.output(11,GPIO.HIGH)
  	time.sleep(10)
  	GPIO.output(11,GPIO.LOW)
  	flag = 1

  
      
class MyStreamer (TwythonStreamer):
        def on_success (self, data):
                if 'text' in data:
                        action()
                        

stream= MyStreamer (C_Key, C_Secret, A_Token, A_Secret)

stream.statuses.filter(track = "aaa123")
         
GPIO.cleanup()   
