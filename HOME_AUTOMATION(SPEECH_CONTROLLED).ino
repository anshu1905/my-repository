/*
  Physical Pixel

  An example of using the Arduino board to receive data from the computer. In
  this case, the Arduino boards turns on an LED when it receives the character
  'H', and turns off the LED when it receives the character 'L'.

  The data can be sent from the Arduino Serial Monitor, or another program like
  Processing (see code below), Flash (via a serial-net proxy), PD, or Max/MSP.

  The circuit:
  - LED connected from digital pin 13 to ground

  created 2006
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe and Scott Fitzgerald

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/PhysicalPixel
*/


int incomingByte;
int Green=8;
int Red=10;
int Yellow=12;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(Green,OUTPUT);
pinMode(Red,OUTPUT);
pinMode(Yellow,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available()>0){
  incomingByte=Serial.read();
  if(incomingByte=='G'){
    digitalWrite(Green,HIGH);
    delay(2000);
    digitalWrite(Green,LOW);
  }
  if(incomingByte=='R'){
    digitalWrite(Red,HIGH);
    delay(2000);
    digitalWrite(Red,LOW);
  }
  if(incomingByte=='Y'){
    digitalWrite(Yellow,HIGH);
    delay(2000);
    digitalWrite(Yellow,LOW);
  }
}
}
