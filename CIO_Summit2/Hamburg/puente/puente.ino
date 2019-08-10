
const int buttonPin1 = 3;  
const int buttonPin2 = 4;
int buttonState2 = 0;         // variable for reading the pushbutton status
int buttonState1 = 0; 
int puente=0;  

void setup() 
  {
  Serial.begin(9600);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  
  }

void loop() 
  {
  boton();
  delay(1000);
  }

void boton()
  {
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  if (buttonState2 == HIGH) 
     puente = 1;
  if (buttonState1 == HIGH) 
     puente = 0; 
  Serial.print("0 ");
  Serial.println(puente);
  } 



