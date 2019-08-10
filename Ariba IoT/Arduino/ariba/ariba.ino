int buttonState1 = 0;
int buttonState2 = 0;
const int buttonPin1 = 2;
const int buttonPin2 = 3;
int flag = 1;
int a=0;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
}

void loop() 
  {
  boton1();
  boton2();
  Serial.print(" ");
  Serial.println("1");
  delay(1000);
  }

void boton1()
  {
  buttonState1 = digitalRead(buttonPin1);
  if(buttonState1 == LOW && flag == 1)
    {
    Serial.print("0");
    a = 0;
    }
  else 
    {
    flag = 0;
    Serial.print("1");
    a=1;
    } 
  Serial.print(" ");
  }

void boton2()
  {
  buttonState2 = digitalRead(buttonPin2);
  if(buttonState2 == HIGH)
    flag = 1;
  Serial.print(a);
  Serial.print(" ");
  }
