#include <Process.h> 
String jsonString;

int x=1;
int y=2;
int z=3;
int a=1;

String url = "https://iotmmsi843568trial.hanatrial.ondemand.com/com.sap.iotservices.mms/v1/api/http/data/cb653061-f79b-41ba-8676-7ec61cd15268"; 
String token = "Authorization: Bearer 1ebb9fc6ab25479a495261da0297e28"; // 65dfd57b9f52cb3e8b2d024f1d196dd"; 
//String data = "{"mode":"sync","messageType":"m0t0y0p0e1","messages":[{"sensor":"sensor1","value":20,"timestamp":1413191650}]}";
//local body = "{\"mode\":\"sync\", \"messageType\":\"c5b17a4be2d56c9b0eca\", \"messages\":[{\"light\":" + light + "}]}";

Process p; 

const int buttonPin = 2;     
const int ledPin =  13;      
int buttonState = 0;         

void setup() {
  
 // jsonString +="\"messages\":[{\"light\":" + x + "}]}" ;

  Serial.begin(9600) ;
  Bridge.begin();


    jsonString = "{\"mode\":\"sync";
    jsonString +="\",\"messageType\":\"82f5c15c1e7ab5b34a33\",";
  
//  jsonString = "{\"x\":\"";
//  jsonString += x;
//  jsonString +="\",\"y\":\"";
//  jsonString += y;
//  jsonString +="\",\"z\":\"";
//  jsonString += z;
//  jsonString +="\"}";
 
}

void loop() {


  p.begin ("curl"); 
  p.addParameter ("-H"); 
  p.addParameter (token); 
  p.addParameter ("-d"); 
  p.addParameter (jsonString); 
  p.addParameter (url); 
  p.addParameter ("-k"); 
  p.run();
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600) ;
  Bridge.begin();
  
  Serial.println(jsonString);  
  
  buttonState = digitalRead(buttonPin);
  
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.print("Exit  "); 
    Serial.println(p.exitValue()); 
  }
  
  else {
    digitalWrite(ledPin, LOW);
    //Serial.print("abajo");
  }
  

}


 
 

 
