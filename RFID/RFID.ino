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

void setup() 
{ 
  Serial.begin(9600);
  SPI.begin();          // Init SPI bus
  rfid.PCD_Init();      // Init MFRC522
  
  Serial.print(x);
  Serial.print(" ");
  Serial.print(y);
  Serial.print(" ");
  Serial.println(z);
  
  for (byte i = 0; i < 6; i++) 
    {  key.keyByte[i] = 0xFF;
    }

  //Serial.println(F("This code scan the MIFARE Classsic NUID."));
  //Serial.print(F("Using the following key:"));
  printHex(key.keyByte, MFRC522::MF_KEY_SIZE);
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
        //Serial.println(F("A new card has been detected."));
    
        //Serial.println(F("The NUID tag is:"));
        //Serial.print(F("In hex: "));
        printHex(rfid.uid.uidByte, rfid.uid.size);
        //Serial.println();
        //Serial.print(F("In dec: "));
        printDec(rfid.uid.uidByte, rfid.uid.size);
        //Serial.println();
        ////Serial.println(rfid.uid.uidByte[2]);
        if ( rfid.uid.uidByte[2] == 27)
           {
            ////Serial.println("Llavero");  
            x++;
           } 
        if ( rfid.uid.uidByte[2] == 185)
           {
            ////Serial.println("Tarjeta");
            y++;
           }
        if ( rfid.uid.uidByte[2] == 76)
           {
            ////Serial.println("Cositos de impresora");  
            z++;
           }     
        rfid.PICC_HaltA();
        rfid.PCD_StopCrypto1();
        //Serial.println(" ");
        //Serial.println(" "p);
        //Serial.print("Llavero: ");
        Serial.print(x);
        Serial.print(" ");
        //Serial.print("Tarjeta: ");
        Serial.print(y);
        Serial.print(" ");
        //Serial.print("Impresora: ");
        Serial.println(z);
    }
    delay(600);
}



