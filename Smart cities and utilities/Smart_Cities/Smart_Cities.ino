int luces_1 = 13;     
int luces_2 = 12;  
int panel = 11;  
int rueda = 10;
int reserva = 9;
int mov = 8;
int volt = 7;
int volt2 = 6;
int state_panel = 0;
int state_mov = 0;

void setup() 
  {
  Serial.begin(9600);
  pinMode(luces_1, OUTPUT);
  pinMode(luces_2, OUTPUT);
  pinMode(panel, INPUT);
  pinMode(rueda, OUTPUT);
  pinMode(reserva, OUTPUT);
  pinMode(mov, INPUT);
  pinMode(volt, OUTPUT);
  pinMode(volt2, OUTPUT);
  }

void loop() 
  {
  digitalWrite(volt, HIGH);
  digitalWrite(volt2, HIGH);  
  state_panel = digitalRead(panel);
  state_mov = digitalRead(mov);
  if (state_panel == HIGH && state_mov == LOW) 
    {
    Serial.println("1 0");
    digitalWrite(luces_1, HIGH);
    digitalWrite(luces_2, LOW);
    digitalWrite(rueda, LOW);
    digitalWrite(reserva, LOW);
    } 
  if (state_panel == LOW && state_mov == HIGH) 
    {
    Serial.println("0 1");
    digitalWrite(luces_2, HIGH);
    digitalWrite(luces_1, LOW);
    digitalWrite(rueda, LOW);
    digitalWrite(reserva, LOW);
    }
  if (state_panel == HIGH && state_mov == HIGH) 
    {
    Serial.println("1 1");
    digitalWrite(luces_1, HIGH);
    digitalWrite(luces_2, HIGH);
    digitalWrite(rueda, HIGH);
    digitalWrite(reserva, LOW);
    delay(5000);
    }
  if (state_panel == LOW && state_mov == LOW) 
    {
    Serial.println("0 0");
    digitalWrite(luces_1, LOW);
    digitalWrite(luces_2, LOW);
    digitalWrite(rueda, LOW);
    digitalWrite(reserva, HIGH);
    }
  delay(1000);
  }




  
