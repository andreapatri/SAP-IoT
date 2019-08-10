//---------------------- SENSORES ----------------------//

int i_presion = 13; 
int o_motor = 9;
int o_bocina = 8;
int i_bender = 12;
int o_luz = 6;
int o_visualizador = 7; //No requiere BJT directo a Micro
int i_boton = 10;
int i_b_reinicio = 11;

//---------------------- OTRAS VARIABLES ----------------------//

int buttonState = 0;
int parar =1;
int parar2 =0;
int cant_producida = 4;
int alertas = 1;


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
   cant_producida = 4;

//--------------------- ESCENARIO BANDA ---------------------//
if(digitalRead(i_presion) == HIGH ) 
  {
  if(parar == 0)  
      parar = 1;
  digitalWrite(o_motor, HIGH);
  delay(10000);
  cant_producida = 9;
  interfaz();
  }
else
  { 
  if(parar == 1)  
      parar = 0;
  digitalWrite(o_motor, LOW);     
  }
  
//------------------ ESCENARIO CONGELADOR ------------------//
if(digitalRead(i_bender) == HIGH) 
  {
  alertas = 0;
  interfaz();  
  if(digitalRead(i_boton) == HIGH) 
    {
    if(parar2 == 0)
      {
      parar2 = 1;
      alertas = 0;
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
          alertas = 1;
          interfaz();
          }
        }       
    digitalWrite(o_luz, LOW);
    }
  else
    if(parar2 == 1)
      {
      alertas = 1;//REVISAR SI ES NECESARIO
      parar2 = 0;
      interfaz(); //REVISAR SI ES NECESARIO 
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
  Serial.print(" ");
  Serial.print(cant_producida);
  Serial.print(" ");
  Serial.print(alertas);
  //Serial.print(" ");
  }
