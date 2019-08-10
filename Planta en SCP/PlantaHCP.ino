
int i_bender = 13;
int i_boton = 12;
int i_b_reinicio = 11;
int i_presion = 10;
int o_visualizador = 9; //No requiere BJT directo a Micro 
int o_motor = 8;
int o_luz_cong = 7;
int o_bocina = 6;

int inprocess=7;
int produced=0;
int alerts=1;

int bandera = 0;

void setup() 
{ 
  pinMode(i_presion, INPUT);
  pinMode(i_bender , INPUT);
  pinMode(i_b_reinicio, INPUT);
  pinMode(i_boton, INPUT);
  
  pinMode(o_motor, OUTPUT);
  pinMode(o_luz_cong, OUTPUT);
  pinMode(o_visualizador, OUTPUT);
  pinMode(o_bocina, OUTPUT);

  Serial.begin(9600);
}

void loop() 
{ 

  if(digitalRead(i_b_reinicio) == HIGH)  
     {
     inprocess=7;
     produced=0;
     alerts=1; 
     hcp(inprocess, produced, alerts) ; 
     digitalWrite(o_bocina, LOW); 
     bandera = 0;
     }
  
  
  if(digitalRead(i_presion) == HIGH)
     {
     digitalWrite(o_bocina, LOW); 
     digitalWrite(o_motor, HIGH);
     delay(10000);
     digitalWrite(o_motor, LOW);
     inprocess = 9;
     hcp(inprocess, produced, alerts) ;
     }

  if(digitalRead(i_bender) == HIGH && bandera == 0)
     {
     alerts = 0;
     hcp(inprocess, produced, alerts);
     bandera = 1;  
     }
  
  if(digitalRead(i_bender) == HIGH && digitalRead(i_boton))
     {
     digitalWrite(o_luz_cong, HIGH); 
     for(int i=1; i<=10; i++)
       {
       if(digitalRead(i_bender) == HIGH)
          {
          digitalWrite(o_visualizador, HIGH);   
          delay(1000);
          digitalWrite(o_visualizador, LOW);  
          delay(20);
          if(i == 9)
             {
             produced = 9;
             inprocess = 0;
             digitalWrite(o_bocina, HIGH); 
             }
          }
        else
          {
          i=10;
          alerts = 1;
          }
        }
      digitalWrite(o_luz_cong, LOW);  
      hcp(inprocess, produced, alerts) ;       
     }
}

     
   
   



void hcp(int inprocess, int produced, int alerts) 
  {
  Serial.print(inprocess);
  Serial.print(" ");  
  Serial.print(produced);
  Serial.print(" ");  
  Serial.print(alerts);
  Serial.println(" ");  
  delay(1000);
  }

