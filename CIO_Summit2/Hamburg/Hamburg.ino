#include <dht.h>
dht DHT;
#define DHT6_PIN 6

#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9
 
MFRC522 rfid(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key key; 
// Init array that will store new NUID 
byte nuidPICC[3];
int x = 0;
int y = 0;
int z = 0;

const int buttonPin = 3;     // the number of the pushbutton pin
const int buttonPin1 = 4;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;         // variable for reading the pushbutton status
int buttonState1 = 0; 
int puente=0;
int n_x=0;
int n_p=0;
int prim=1;

void setup() 
{ 
  
  Serial.begin(9600);
  SPI.begin();          // Init SPI bus

  pinMode(buttonPin, INPUT);
  pinMode(buttonPin1, INPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  
  rfid.PCD_Init();      // Init MFRC522
  
  for (byte i = 0; i < 6; i++) 
    {  key.keyByte[i] = 0xFF;
    }

  //Serial.println(F("This code scan the MIFARE Classsic NUID."));
  //Serial.print(F("Using the following key:"));
  printHex(key.keyByte, MFRC522::MF_KEY_SIZE);

  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
}
// ------------------------------------------------------------------


void imp()
  {

     {
     Serial.print(x);
     Serial.print(" ");
     Serial.println(puente);
     }
     
  delay(600);
  }
  
void boton()
  {
  buttonState1 = digitalRead(buttonPin1);
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) 
     puente = 1;
  if (buttonState1 == HIGH) 
     puente = 0;
  imp();    
  }

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
  if ( ! rfid.PICC_IsNewCardPresent())
    return;

  if ( ! rfid.PICC_ReadCardSerial())
    return;

  MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);


  // Check is the PICC of Classic MIFARE type
  if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&  
    piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
    piccType != MFRC522::PICC_TYPE_MIFARE_4K) 
      {
   
        return;
      }

  if (rfid.uid.uidByte[0] != nuidPICC[0] || 
    rfid.uid.uidByte[1] != nuidPICC[1] || 
    rfid.uid.uidByte[2] != nuidPICC[2] || 
    rfid.uid.uidByte[3] != nuidPICC[3] ) 
    {

        printHex(rfid.uid.uidByte, rfid.uid.size);

        printDec(rfid.uid.uidByte, rfid.uid.size);

        if ( rfid.uid.uidByte[2] == 27)
           {
            x=1;
           } 
        if ( rfid.uid.uidByte[2] == 167)
           {
            x=0;
           }
   
        rfid.PICC_HaltA();
        rfid.PCD_StopCrypto1();
        
        imp();


    }
}






