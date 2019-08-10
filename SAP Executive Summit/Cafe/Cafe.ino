
int PIN_PESO_0 = A0;
int PIN_PESO_1 = A1;
int buttonState = 0;  

void setup() 
  {
  Serial.begin(9600);
  pinMode(PIN_PESO_0, INPUT);
  pinMode(PIN_PESO_1, INPUT);
  }

void loop() 
  {
  peso1(); 
  peso2(); 
  delay(200);
  }

void peso1()
  {
  int sensorvalue = analogRead(PIN_PESO_0);
  //Serial.print(sensorvalue);
  if(sensorvalue > 500)
    Serial.print("1 "); 
  else
    Serial.print("0 "); 
  }

void peso2()
  {
  int sensorvalue = analogRead(PIN_PESO_1);
  //Serial.print(sensorvalue);
  if(sensorvalue > 500)
    Serial.print("1 "); 
  else
    Serial.print("0 "); 
  }  
  
