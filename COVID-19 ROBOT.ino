#define pirPin 10
int red=8;
int green=9;
int calibrationTime = 30;
long unsigned int lowIn;
long unsigned int pause = 5000;
boolean lockLow = true;
boolean takeLowTime;
int PIRValue = 0;
#include <dht.h>
#define dht_apin A0 // Analog Pin sensor is connected to
dht DHT;
int LeftMotorFront=2;
int LeftMotorBack=3;
int RightMotorFront=4;
int RightMotorBack=5;

int ln=0;
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   pinMode(pirPin, INPUT);
   pinMode(red,OUTPUT);
   pinMode(green,OUTPUT);
   
  pinMode(LeftMotorFront,OUTPUT);
  pinMode(LeftMotorBack,OUTPUT);
  pinMode(RightMotorFront,OUTPUT);
  pinMode(RightMotorBack,OUTPUT);
 }

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0)
{
   ln=Serial.read();
   Serial.println(ln);
   Serial.print("\n");
   if (ln==49)
  {
    digitalWrite(LeftMotorFront,HIGH);
    digitalWrite(RightMotorFront,HIGH);
    digitalWrite(LeftMotorBack,LOW);
    digitalWrite(RightMotorBack,LOW);
  }
  else if(ln==51)
  {
    digitalWrite(LeftMotorFront,LOW);
    digitalWrite(RightMotorFront,LOW);
    digitalWrite(LeftMotorBack,HIGH);
    digitalWrite(RightMotorBack,HIGH);
  }
  else if(ln==50)
  {
    digitalWrite(LeftMotorFront,HIGH);
    digitalWrite(RightMotorFront,LOW);
    digitalWrite(LeftMotorBack,LOW);
    digitalWrite(RightMotorBack,HIGH);
  }
  else if(ln==52)
  {
    digitalWrite(LeftMotorFront,LOW);
    digitalWrite(RightMotorFront,HIGH);
    digitalWrite(LeftMotorBack,HIGH);
    digitalWrite(RightMotorBack,LOW);
  }
}
sensor2();
}

void sense1(){
      DHT.read11(dht_apin);
      int h=int(DHT.temperature);
      Serial.print("The body temperature is:");
      Serial.println(h); 
}
void sensor2(){
  if(digitalRead(pirPin) == HIGH) {
      if(lockLow) {
         PIRValue = 1;
         lockLow = false;
         Serial.println("Motion detected.");
         digitalWrite(green,HIGH);
         digitalWrite(red,LOW);
         sense1();
         delay(50);
      }
      takeLowTime = true;
   }
   if(digitalRead(pirPin) == LOW) {
      if(takeLowTime){
         lowIn = millis();takeLowTime = false;
      }
      if(!lockLow && millis() - lowIn > pause) {
         PIRValue = 0;
         lockLow = true;
         Serial.println("Motion ended.");
         digitalWrite(red,HIGH);
         digitalWrite(green,LOW);
         delay(50);
      }
   }
}
