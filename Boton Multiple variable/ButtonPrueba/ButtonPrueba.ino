
const int buttonPin = 2;     
const int buttonPin2 = 3;   
const int ledPin =  13;      
boolean cambio = false;
int buttonState = 0;   
int buttonState2 = 0; 
int x, y; 
int nuevo = 3;    
int nuevo2 = 6; 

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(buttonPin2, INPUT);
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

    
  buttonState2 = digitalRead(buttonPin2);
  if (buttonState2 == HIGH) 
    {
    digitalWrite(ledPin, HIGH);
    y = 2;
    interfaz();  
    }
  else 
    {
    digitalWrite(ledPin, LOW);
    y = 3;
    interfaz(); 
    } 


    
}

void interfaz()
  {
   
//  if(x != nuevo )
//      {
//      //Serial.print(" ");
//      Serial.print(x);
//      }
//   nuevo = x; 
//
//   if(y != nuevo2 )
//      {
//      //Serial.print(" ");
//      Serial.print(y);
//      }
//   nuevo2 = y; 
    
  if(x != nuevo || y != nuevo2  )
      {
      Serial.print(x);
      Serial.print(y);
      }
   nuevo = x; 
   nuevo2 = y; 
   
  }
