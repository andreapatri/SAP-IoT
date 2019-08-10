const int ledPin =  13;   

const int buttonPin1 = 12;    
const int buttonPin2 = 11;    
const int buttonPin3 = 10;    
const int buttonPin4 = 9;    

int buttonState1 = 0; 
int buttonState2 = 0; 
int buttonState3 = 0; 
int buttonState4 = 0;    

int sensorPin1 = A8; 
int sensorPin2 = A9; 
int sensorPin3 = A10; 
int sensorPin4 = A11; 
int sensorPin5 = A12;
int sensorPin6 = A13;
     
int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
int sensorValue5 = 0;
int sensorValue6 = 0;

void setup() {
  Serial.begin(9600); 
  pinMode(ledPin, OUTPUT);
  pinMode(buttonState1, INPUT);
  pinMode(buttonState2, INPUT);
  pinMode(buttonState3, INPUT);
  pinMode(buttonState4, INPUT);
}

void loop() {
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  buttonState4 = digitalRead(buttonPin4);
  
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);
  sensorValue3 = analogRead(sensorPin3);
  sensorValue4 = analogRead(sensorPin4);
  sensorValue5 = analogRead(sensorPin5);
  sensorValue6 = analogRead(sensorPin6);
  
  Serial.print(sensorValue1); //line chart
  Serial.print(" ");
  Serial.print(sensorValue2); //line chart
  Serial.print(" ");
  Serial.print(sensorValue3); //waterfall 
  Serial.print(" ");

  Serial.print(buttonState1); //bullet micro chart 
  Serial.print(" ");
  Serial.print(buttonState2);// column chart
  Serial.print(" ");
  Serial.print(buttonState3); // double column chart  
  Serial.print(" ");
  Serial.print(buttonState4); //double column chart 
  Serial.print(" ");

  Serial.print(sensorValue4/10); //radial micro chart 1
  Serial.print(" ");
  Serial.print(sensorValue5/10);  //radial micro chart 2
  Serial.print(" ");  
  Serial.println(sensorValue6);  //geomap


  delay(3000);
  
}
