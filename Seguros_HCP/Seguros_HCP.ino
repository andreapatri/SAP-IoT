#include <dht.h>
dht DHT;
#define DHT11_PIN 11
int trigPin=13; //Sensor Trig pin connected to Arduino pin 13 para distancia
int echoPin=12;  //Sensor Echo pin connected to Arduino pin 12 para distancia
float pingTime;  //time for ping to travel from sensor to target and return
float targetDistance; //Distance to Target in inches
float speedOfSound=776.5; //Speed of sound in miles per hour when temp is 77 degrees.
const int buttonPin = 10;     
int buttonState = 0;   
int cont = 0;
int flag = 0;
//A1 presion1
//A2 presion2 
//D11 temp    
int frenos[490];
int brusco = 0;
int x =0;

void setup() 
  {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT);
  }

void loop() 
  {
  temperatura(); //digital 11
  agua(); //A2
  peso1(); // A1
  //peso3();
  //boton1();
  Serial.println(" ");
  delay(500);
  }

void temperatura()
  {
  int chk = DHT.read11(DHT11_PIN);
  //Serial.print("Temperature = ");
  if(DHT.temperature >= 24)
      Serial.print("1");
  else
      Serial.print("0");    
  //Serial.print(DHT.temperature);
  Serial.print(" ");
  //delay(1000);
  }

void distancia()
  {
  digitalWrite(trigPin, LOW); //Set trigger pin low
  delayMicroseconds(2000); //Let signal settle
  digitalWrite(trigPin, HIGH); //Set trigPin high
  delayMicroseconds(15); //Delay in high state
  digitalWrite(trigPin, LOW); //ping has now been sent
  delayMicroseconds(10); //Delay in low state
  pingTime = pulseIn(echoPin, HIGH);  //pingTime is presented in microceconds
  pingTime=pingTime/1000000; //convert pingTime to seconds by dividing by 1000000 (microseconds in a second)
  pingTime=pingTime/3600; //convert pingtime to hourse by dividing by 3600 (seconds in an hour)
  targetDistance= speedOfSound * pingTime;  //This will be in miles, since speed of sound was miles per hour
  targetDistance=targetDistance/2; //Remember ping travels to target and back from target, so you must divide by 2 for actual target distance.
  targetDistance= targetDistance*63360;    //Convert miles to inches by multipling by 63360 (inches per mile)
  //Serial.print("Distancia = ");
  Serial.print(targetDistance);
  Serial.print(" ");
  delay(100); //delay tenth of a  second to slow things down a little.
  }

void peso1()
  {  
  int sensorValue = analogRead(A1);
  //Serial.print("Sensor0 = ");
  float voltage = sensorValue; //* (5.0 / 1023.0);
  if(voltage >= 100)
     x = x + 1;
  Serial.print(x);
  Serial.print(" ");
  }

void agua()
  {
  int sensorValue = analogRead(A2);
  //Serial.print("Sensor2 = ");
  float voltage = sensorValue; //* (5.0 / 1023.0);
  if(voltage >= 300)
      Serial.print("0");
  else
      Serial.print("1");    
  Serial.print(" ");
  }

void peso3()
  {
  int sensorValue = analogRead(A0);
  //Serial.print("Sensor0 = ");
  float voltage = sensorValue; //* (5.0 / 1023.0);
  Serial.print(voltage);
  Serial.print(" ");
  }

void boton1()
  {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH && flag == 0) 
    {
    cont++;
    flag = 1;
    }
  else  
    flag = 0;
  Serial.print(cont);
  //Serial.print(" ");
  delay(100);
  }


