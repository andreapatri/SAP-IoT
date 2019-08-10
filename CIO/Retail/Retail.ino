#include <dht.h>
dht DHT;
#define DHT11_PIN 11
int PIN_PESO = A0;
int PIN_DOOR = 7;
int PIN_5V_1 = 12;
int PIN_5V_2 = 13;
int buttonState = 0; 

void setup() 
  {
  Serial.begin(9600);
  pinMode(PIN_PESO, INPUT);
  pinMode(PIN_DOOR, INPUT);
  pinMode(PIN_5V_1, OUTPUT);
  pinMode(PIN_5V_2, OUTPUT);
  }

void loop() 
  {
  digitalWrite(PIN_5V_1, HIGH);
  digitalWrite(PIN_5V_2, HIGH);  
  temperatura(); //digital 11
  peso(); // A0 - con 5V en 12
  door();
  delay(1500);
  }

void peso()
  {
  int sensorvalue = analogRead(PIN_PESO);
  //Serial.print(sensorvalue);
  if(sensorvalue > 500)
    Serial.print("1 "); 
  else
    Serial.print("0 "); 
  }
  
void temperatura()
  {
  int chk = DHT.read11(DHT11_PIN);
  Serial.print(int (DHT.temperature));
  Serial.print(" ");
  }
  
void door()
  {
  buttonState = digitalRead(PIN_DOOR);
  if(buttonState == HIGH)
    Serial.println("1 "); 
  else
    Serial.println("0 "); 
  }  
