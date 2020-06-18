//OBSTACLE AVOIDING ROBOT
#define echopin  8 // echo pin
#define trigpin 9 // Trigger pin


int maximumRange = 30;
long duration, distance;

void setup() {
  Serial.begin (9600);
  pinMode (trigpin, OUTPUT);
  pinMode (echopin, INPUT );
  pinMode (4, OUTPUT);// FRONT RIGHT MOTOR
  pinMode (5, OUTPUT);// BACK RIGHT MOTOR
  pinMode (3, OUTPUT);// BACK LEFT MOTOR
  pinMode (2, OUTPUT);// FRONT LEFT MOTOR
}

void loop ()
{

  {
    //ULTRASONIC SENSOR 
    digitalWrite(trigpin,LOW);
    delayMicroseconds(2);
    
    digitalWrite(trigpin,HIGH);
    delayMicroseconds(10);
    
    duration=pulseIn (echopin,HIGH);
    
    distance= duration/58.2;
    delay (50);
    Serial.println(distance);
  }
  
  if (distance >= 30 ){
    //MOVE FORWARD
    digitalWrite(2,HIGH);
    digitalWrite(5,LOW); 
    digitalWrite(3,LOW);
    digitalWrite(4,HIGH);
    delay (200);
  }
  
  else if (distance >=15 && distance <= 25) {
    //MOVE RIGHT
    digitalWrite (4,LOW);
    digitalWrite (5,HIGH);
    digitalWrite (3,LOW);
    digitalWrite (2,HIGH);
    delay (2000);
    //MOVE FORWARD
    digitalWrite(2,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(5,LOW);
  }
 else if (distance < 15){
  //MOVE BACKWARD
   digitalWrite (2, LOW);
   digitalWrite (4, LOW);
   digitalWrite (3,HIGH);
   digitalWrite (5,HIGH);
   delay (2000);
   //MOVE LEFT
   digitalWrite (2,LOW);
   digitalWrite (5,LOW);
   digitalWrite (3,HIGH);
   digitalWrite (4,HIGH);
   delay (2000);
   //MOVE FORWARD
    digitalWrite(2,HIGH);
    digitalWrite(4,HIGH);
    digitalWrite(3,LOW);
    digitalWrite(5,LOW);
   
   }

}
