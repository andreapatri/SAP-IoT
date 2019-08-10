
const int buttonPin1 = 3;  
const int buttonPin2 = 4;     
int buttonState = 0;   

void setup() 
  {
  Serial.begin(9600);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  }

void loop() 
  {
  //boton1();
  Serial.println("14 1 23");
  delay(300);
  }

void boton1()
  {
  buttonState = digitalRead(buttonPin1);
  if (buttonState == HIGH) 
    Serial.print("1");
  else 
    Serial.print("0");  
  }

void boton2()
  {
  buttonState = digitalRead(buttonPin2);
  if (buttonState == HIGH) 
    Serial.println("1");
  else 
    Serial.println("0");  
  }


