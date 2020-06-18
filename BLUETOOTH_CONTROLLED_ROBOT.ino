int LeftMotorFront=2;
int LeftMotorBack=3;
int RightMotorFront=4;
int RightMotorBack=5;

int ln=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
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
}
