#include<Servo.h>
Servo myservo;
int SensorPin=A0;
int ledPin1=2;
int ledPin2=3;
int ledPin3=4;
int ledPin4=5;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ledPin1,OUTPUT);
pinMode(ledPin2,OUTPUT);
pinMode(ledPin3,OUTPUT);
pinMode(ledPin4,OUTPUT);
pinMode(SensorPin,INPUT);
myservo.attach(8);
}

void loop() {
  // put your main code here, to run repeatedly:
int SensorVal=analogRead(SensorPin);
delay(500);
if (SensorVal<=500)
{
  Serial.print("Sensor Value says that the object detected is WHITE  ");
  Serial.println(SensorVal);
  Serial.print("\n");
  delay(500);
  
  digitalWrite(ledPin1,LOW);
  digitalWrite(ledPin2,LOW);
  myservo.write(100);
  delay(1000);
  
  digitalWrite(ledPin1,HIGH);
  digitalWrite(ledPin2,HIGH);
  myservo.write(0);
  delay(1000);
  
  digitalWrite(ledPin1,LOW);
  digitalWrite(ledPin2,LOW);
  myservo.write(100);
  delay(1000);
}
else if(SensorVal>500)
{
  Serial.print("Sensor Value says that the object detected is BLACK   ");
  Serial.println(SensorVal);
  Serial.print("\n");
  delay(500);

  digitalWrite(ledPin3,LOW);
  digitalWrite(ledPin4,LOW);
  myservo.write(100);
  delay(1000);

  digitalWrite(ledPin3,HIGH);
  digitalWrite(ledPin4,HIGH);
  myservo.write(180);
  delay(1000);

  digitalWrite(ledPin3,LOW);
  digitalWrite(ledPin4,LOW);
  myservo.write(100);
  delay(1000);
 }
}
