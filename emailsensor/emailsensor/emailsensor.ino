
// constants won't change. They're used here to set pin numbers:
const int buttonPin = 13;     // the number of the pushbutton pin
const int ledPin =  2;      // the number of the LED pin
const int power = 12;
// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int x=0;
int ant;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(power, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(power, HIGH);
  
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  delay(1000);
  ant = x;

  if (buttonState == HIGH) {
    
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    x = 0;
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
    x = 1;
  }
  if(ant != x)
    Serial.println(x);
}
