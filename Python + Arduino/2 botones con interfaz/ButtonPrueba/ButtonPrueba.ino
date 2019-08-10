
const int buttonPin = 2;
const int buttonPin2 = 3;     
const int ledPin =  13;      
boolean cambio = false;
int buttonState = 0;  
int buttonState2 = 0;   
int x; 
int nuevo = 3;    

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(buttonPin2, INPUT);
  Serial.begin(9600) ;
}

void loop() {
  
  buttonState = digitalRead(buttonPin);
  buttonState2 = digitalRead(buttonPin2);
  if (buttonState == HIGH && buttonState2 == HIGH) 
    x = 11;
  if (buttonState == HIGH && buttonState2 == LOW) 
    x = 10;  
  if (buttonState == LOW && buttonState2 == HIGH) 
    x = 31;  
  if (buttonState == LOW && buttonState2 == LOW) 
    x = 33;
  interfaz();  
  
}

void interfaz()
  {
  if(x != nuevo )
      {
      //Serial.print(" ");
      Serial.print(x);
      }
   nuevo = x; 
  }
