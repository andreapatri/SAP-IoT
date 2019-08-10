#include <dht.h>
dht DHT;
#define DHT11_PIN 11


void setup() 
  {
  Serial.begin(9600);
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  }

void loop() 
  {
  digitalWrite(13, LOW); 
  digitalWrite(10, HIGH); 
  temperatura(); //digital 11
//  Serial.print("1 1 ");
  Serial.println(" ");
  delay(500);
  }

void temperatura()
  {
  int chk = DHT.read11(DHT11_PIN);
//  if(DHT.temperature >= 24)
//      Serial.print("1");
//  else
//      Serial.print("0");    
  Serial.print(DHT.temperature);
  Serial.print(" ");
  //delay(1000);
  }

