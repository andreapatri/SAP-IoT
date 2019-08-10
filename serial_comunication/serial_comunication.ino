
int a = 0;
int b= 0;
int c=0;
int i_presion = 2; 

void setup() {
  Serial.begin (9600);
  pinMode(i_presion, INPUT);
}

void loop() 
{
 if(digitalRead(i_presion) == HIGH ) 
  { 
  Serial.print(1);
  Serial.print(" ");
  Serial.print(1);
  Serial.print(" ");
  Serial.print(1);
  Serial.print(" "); 
  delay(1000);
  }
 else 
 { 
  Serial.print(random(3,8));
  Serial.print(" ");
  Serial.print(2);
  Serial.print(" ");
  Serial.print(2);
  Serial.print(" "); 
  }
}

