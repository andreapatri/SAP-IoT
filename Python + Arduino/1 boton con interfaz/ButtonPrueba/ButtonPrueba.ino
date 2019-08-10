
const int buttonPin = 2;     
const int ledPin =  13;      
boolean cambio = false;
int buttonState = 0;   
int x; 
int nuevo = 3;    

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600) ;
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) 
    {
    digitalWrite(ledPin, HIGH);
    x = 1;
    interfaz();  

    }
  else 
    {
    digitalWrite(ledPin, LOW);
    x = 0;
    interfaz(); 

    } 
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
