//---------------------- SENSORES ----------------------//
int i_bender = 13;
int i_boton = 12;
int i_b_reinicio = 11;
int i_presion = 10;
int o_visualizador = 9; //No requiere BJT directo a Micro 
int o_motor = 8;
int o_luz = 7;
int o_bocina = 6;



//---------------------- OTRAS VARIABLES ----------------------//

int buttonState = 0;
int parar =1;
int parar2 =0;
int cant_producida = 4;
int alertas = 1;
int x = 7;
int y = 0;
int z ;
int nuevo = 27;
int termino = 0;


void setup() 
{
  //--------------------- ESCENARIO BANDA ---------------------//
  pinMode(i_presion, INPUT);
  pinMode(o_motor, OUTPUT);

  //------------------ ESCENARIO CONGELADOR ------------------//
  pinMode(i_bender , INPUT);
  pinMode(o_luz, OUTPUT);
  pinMode(o_visualizador, OUTPUT);
  
  //------------------------ BOTONES ------------------------//
  pinMode(i_b_reinicio, INPUT);
  pinMode(i_boton, INPUT);

  //--------------- ESCENARIO FIN PRODUCCION ---------------//
  pinMode(o_bocina, OUTPUT);

  Serial.begin(9600);
}

void loop() 
{ 

//------------------------ REINICIO ------------------------//

cerrado();
interfaz(); 

if(digitalRead(i_b_reinicio) == HIGH)
   {
   x=7;
   y=0; 
   cerrado();
   digitalWrite(o_bocina, LOW);
   interfaz();
   }

//--------------------- ESCENARIO BANDA ---------------------//
if(digitalRead(i_presion) == HIGH ) 
  {
  digitalWrite(o_motor, HIGH);
  x = 9;
  y = 0;
  cerrado();
  interfaz();
  delay(10000);
  }
else
  { 
  digitalWrite(o_motor, LOW);     
  }
  
//------------------ ESCENARIO CONGELADOR ------------------//
if(digitalRead(i_bender) == HIGH && digitalRead(i_boton) == HIGH) 
  {
  x = 9;
  y = 0;
  cerrado();
  interfaz();  
  digitalWrite(o_luz, HIGH);
  for(int i=1; i<=10; i++)
       {      
       digitalWrite(o_visualizador, HIGH);   
       delay(1000);
       digitalWrite(o_visualizador, LOW);  
       delay(20);
       }
  digitalWrite(o_luz, LOW);
  digitalWrite(o_bocina, HIGH);
  x=0;
  y=9;
  cerrado();
  interfaz();
  }

}
//------------------ FUNCION INTERFAZ ------------------//

void cerrado()
  {
  if(digitalRead(i_bender) == HIGH)
    z=0;
  else
    z=1;
  }

void interfaz()
   {
      //Serial.print(x);
      //Serial.print(y);
      //Serial.println(z);
      if(x == 7 && y == 0 && z == 1)
        Serial.print("701");
      if(x == 7 && y == 0 && z == 0)
        Serial.print("700");
      if(x == 9 && y == 0 && z == 0)
        Serial.print("900");
      if(x == 0 && y == 9 && z == 0)
        Serial.print("090");
      
   }  
