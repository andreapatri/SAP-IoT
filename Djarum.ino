#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

#include <dht.h>
dht DHT;
#define DHT11_PIN 7
 
MFRC522 rfid(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key key; 
// Init array that will store new NUID 
byte nuidPICC[3];
int x = 1;
int b;
int z;
int buttonState = 0; 
int peso;

//-------------PINES
int buttonPin = 8;
int PIN_PESO_0 = A0;

/* Signal     Pin              Pin               Pin
 *            Arduino Uno      Arduino Mega      MFRC522 board
 * ------------------------------------------------------------
 * Reset      9                5                 RST
 * SPI SS     10               53                SDA
 * SPI MOSI   11               51                MOSI
 * SPI MISO   12               50                MISO
 * SPI SCK    13               52                SCK */

bool estado = true; 

void setup() 
{ 
  Serial.begin(9600);
  pinMode(PIN_PESO_0, INPUT);
  SPI.begin();          // Init SPI bus
  rfid.PCD_Init();      // Init MFRC522
  pinMode(4, OUTPUT);
  pinMode(buttonPin, INPUT);  
  pinMode(5, OUTPUT);  
  pinMode(6, OUTPUT);  
  digitalWrite(5, LOW); 
  digitalWrite(6, HIGH); 
    
  for (byte i = 0; i < 6; i++) 
    {  key.keyByte[i] = 0xFF;
    }
    
  printHex(key.keyByte, MFRC522::MF_KEY_SIZE);
}


void imp()
  {
   Serial.print(x); //rfid
   Serial.print(" ");
   Serial.print(int(DHT.temperature));
   if(int(DHT.temperature) >= 26)
     digitalWrite(4, HIGH);
   else 
     digitalWrite(4, LOW);     
   Serial.print(" ");
   Serial.print(int(DHT.humidity)); //humedad
   Serial.print(" ");
   Serial.println(peso); 
   delay(1000);
  }

void boton()
  {
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) 
     estado = !estado;
  if (estado == true)
     b = 1;
  else 
     b = 0;
  imp();     
  }

void weight()
  {
  int sensorvalue = analogRead(PIN_PESO_0);
  peso = sensorvalue;
  imp();  
  }


void temperature()
  {
  int chk = DHT.read11(DHT11_PIN);
  imp();
  }


// ------------------------------------------------------------------
void printHex(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    //Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    //Serial.print(buffer[i], HEX);
  }
}
void printDec(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    //Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    //Serial.print(buffer[i], DEC);
  }
}
//------------------------------------------------------------------

void loop() {

  boton();
  weight();
  temperature();
//  temperature();
//  weight();

  // Buscamos tarjetas
  if ( ! rfid.PICC_IsNewCardPresent())
    return;

  // SI la encuentra la leemos
  if ( ! rfid.PICC_ReadCardSerial())
    return;

  //Serial.print(F("PICC type: "));
  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
  //Serial.println(rfid.PICC_GetTypeName(piccType));

  // Check is the PICC of Classic MIFARE type
  if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&  
    piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
    piccType != MFRC522::PICC_TYPE_MIFARE_4K) 
      {
        //Serial.println(F("Your tag is not of type MIFARE Classic."));
        return;
      }

  if (rfid.uid.uidByte[0] != nuidPICC[0] || 
    rfid.uid.uidByte[1] != nuidPICC[1] || 
    rfid.uid.uidByte[2] != nuidPICC[2] || 
    rfid.uid.uidByte[3] != nuidPICC[3] ) 
    {
        if ( rfid.uid.uidByte[2] == 27)
           {         
            x=1;
           } 
        if ( rfid.uid.uidByte[2] == 167)
           {
            x=4;
           }
        if ( rfid.uid.uidByte[2] == 246)
           {
            x=3;
           }
        if ( rfid.uid.uidByte[2] == 254)
           {
            x=2;
           }  
                
        rfid.PICC_HaltA();
        rfid.PCD_StopCrypto1();
    imp();

    }

}



