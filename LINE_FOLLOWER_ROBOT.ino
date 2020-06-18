int leftSensorPin=A0;
int rightSensorPin=A1;

int leftSensorVal=0;
int rightSensorVal=0;

int leftMotorFront=2;
int leftMotorBack=3;
int rightMotorFront=4;
int rightMotorBack=5;


void setup() {
  // put your setup code here, to run once:
pinMode(leftSensorPin,INPUT);
pinMode(rightSensorPin,INPUT);
pinMode(leftMotorFront,OUTPUT);
pinMode(leftMotorBack,OUTPUT);
pinMode(rightMotorFront,OUTPUT);
pinMode(rightMotorBack,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
leftSensorVal=analogRead(leftSensorPin);
rightSensorVal=analogRead(rightSensorPin);

Serial.print("The left sensor value is:  ");
Serial.println(leftSensorVal);
delay(100);
Serial.print("The right sensor value is:  ");
Serial.println(rightSensorVal);
delay(100);

if (leftSensorVal<=500 and rightSensorVal<=500)
{
  Serial.print("FORWARD");
  digitalWrite(leftMotorFront,HIGH);
  digitalWrite(rightMotorFront,HIGH);
  digitalWrite(leftMotorBack,LOW);
  digitalWrite(rightMotorBack,LOW);
  
}
else if(leftSensorVal>=500 and rightSensorVal<=500)
{
  Serial.print("LEFT");
  digitalWrite(leftMotorFront,HIGH);
  digitalWrite(rightMotorBack,HIGH);
  digitalWrite(leftMotorBack,LOW);
  digitalWrite(rightMotorFront,LOW);
}
else if(leftSensorVal<=500 and rightSensorVal>=500)
{
  Serial.print("RIGHT");
  digitalWrite(rightMotorFront,HIGH);
  digitalWrite(leftMotorBack,HIGH);
  digitalWrite(leftMotorFront,LOW);
  digitalWrite(rightMotorBack,LOW);
}
else if(leftSensorVal>=500 and rightSensorVal>=500)
{
  Serial.print("STOP");
  digitalWrite(leftMotorFront,LOW);
  digitalWrite(rightMotorFront,LOW);
  digitalWrite(leftMotorBack,LOW);
  digitalWrite(rightMotorBack,LOW);
}
}
