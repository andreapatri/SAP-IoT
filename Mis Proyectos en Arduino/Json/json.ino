int x=1;
int y=2;
int z=3;
int a=1;

String jsonString;

void setup() {
  // put your setup code here, to run once:
  // form a JSON-formatted string:
  
    jsonString = "{\"x\":\"";
    jsonString += x;
    jsonString +="\",\"y\":\"";
    jsonString += y;
    jsonString +="\",\"z\":\"";
    jsonString += z;
    jsonString +="\"}";

    // print it:

}

void loop() {
      //if(a==1)
        Serial.println(jsonString + a);
      a=a+1;
      
}
