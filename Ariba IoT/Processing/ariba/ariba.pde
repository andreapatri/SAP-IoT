import processing.serial.*;
Serial mySerial;
PrintWriter output;
int[] list = new int[5];
int peso2 = 0; 
int flag = 0;
int parar = 0;

PImage img;  // Declare variable "a" of type PImage
PImage img2;
int cual = 0;

void setup() {
  mySerial = new Serial (this, "COM3", 9600);
  size(1600, 900);
  img = loadImage("a1.jpg");  // Load the image into the program  
  img.resize(1600, 830);
  img2 = loadImage("a2.jpg");
  img2.resize(1600, 830);
   
}
void draw() {
    if (mySerial.available() > 0 ) {
         String value = mySerial.readString();
         if ( value != null ) {
              if(value.length() > 6){
                String[] list = split(value, ' ');
                println(list[0]+" "+ list[1]);
                if(int(list[0]) == 0 && parar == 0)
                  imagen1();
                else
                  {
                  imagen2();
                  parar = 1;
                  }
              }
         }
    }
}

void imagen1() 
{
  // Displays the image at its actual size at point (0,0)
  image(img, 0, 0);
  // Displays the image at point (0, height/2) at half of its size
  image(img, 0, height, img.width, img.height);
}

void imagen2() 
{
  // Displays the image at its actual size at point (0,0)
  image(img2, 0, 0);
  // Displays the image at point (0, height/2) at half of its size
  image(img2, 0, height, img2.width, img2.height);
}