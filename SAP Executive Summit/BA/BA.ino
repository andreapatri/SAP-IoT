int p_lluvia=A0;
int p_agua=A1;
int power_1=2;
int power_2=3;


void setup() {
  Serial.begin(9600);
  pinMode(p_lluvia, INPUT);
  pinMode(p_agua, INPUT);
  pinMode(power_1, OUTPUT);
  pinMode(power_2, OUTPUT);
}

void loop() 
  {
  digitalWrite(power_1, HIGH);
  digitalWrite(power_2, HIGH);
  lluvia();
  agua();
  delay(1000);
  }

void lluvia()
 {
 Serial.print((-9216+(9*(analogRead(p_lluvia))))/-1024); //lectura analógica
 Serial.print(" ");
 }

void agua()
  {   
  Serial.println(((9*(analogRead(p_agua)))/1024)*3);   
  }

