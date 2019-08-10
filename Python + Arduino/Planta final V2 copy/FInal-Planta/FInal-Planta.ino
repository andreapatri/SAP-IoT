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
int x=41;
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
interfaz(); 
if(digitalRead(i_b_reinicio) == HIGH)
   {
   x=701;
   termino = 0;
   digitalWrite(o_bocina, LOW);
   }

//--------------------- ESCENARIO BANDA ---------------------//
if(digitalRead(i_presion) == HIGH ) 
  {
  if(parar == 0)  
      parar = 1;
  digitalWrite(o_motor, HIGH);
  x=901;
  interfaz();
  delay(10000);
  }
else
  { 
  if(parar == 1)  
      parar = 0;
  digitalWrite(o_motor, LOW);     
  }
  
//------------------ ESCENARIO CONGELADOR ------------------//
if(digitalRead(i_bender) == HIGH && termino == 0) 
  {
  //alertas = 0;
  x=900;
  interfaz();  
  if(digitalRead(i_boton) == HIGH) 
    {
    if(parar2 == 0)
      {
      parar2 = 1;
      interfaz();
      }
    digitalWrite(o_luz, HIGH);
    for(int i=1; i<=10; i++)
      {
      if(digitalRead(i_bender) == HIGH)
          {
          digitalWrite(o_visualizador, HIGH);   
          delay(1000);
          digitalWrite(o_visualizador, LOW);  
          delay(20);
          }
       else
          {
          i=10;
          x=901;
          //alertas = 1;
          interfaz();
          }
        }       
    digitalWrite(o_luz, LOW);
    digitalWrite(o_bocina, HIGH);
    x=990;
    interfaz();
    termino = 1;
    }
  else
    if(parar2 == 1)
      {
      parar2 = 0;
      }
  }
else
 {
 alertas = 1;
 interfaz();  
 }
}

//------------------ FUNCION INTERFAZ ------------------//

void interfaz()
  {
  if(x != nuevo )
      {
      Serial.print(x);
      }
   nuevo = x; 
  }
