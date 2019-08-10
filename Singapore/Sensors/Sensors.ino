#include <dht.h>
dht DHT;
int analogValue;
int digValue;

#define DHT11_PIN 11 //temperatura
int light  = A0;     //fotoresistencia
int mercury_tilt  = 12;
int boton = 10;

void setup() 
  {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT); 
  pinMode(A0, INPUT); 
  }

void loop() 
  {
  digital_sensor(10);  //boton  
  temperatura();      //temp 11
  digital_sensor(12); // mercurio tilt
  digital_sensor(13); // infrared
  analog_sensor(A0);  // light
  Serial.println("");
  }

int temperatura()
  {
  int chk = DHT.read11(DHT11_PIN); 
  Serial.print(DHT.temperature);
  Serial.print(" ");
  Serial.print(DHT.humidity);
  Serial.print(" ");
  }

int analog_sensor(char y)
 {
  analogValue = analogRead (y);
  Serial.print(analogValue);
  Serial.print(" ");
 }

int digital_sensor(int x)
{
  digValue = digitalRead(x); //Read the sensor
  Serial.print(digValue);
  Serial.print(" ");
}

