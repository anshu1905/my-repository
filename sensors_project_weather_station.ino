//Sensors Project-Weather Station For Farmers !

#include <SoftwareSerial.h>`  
  
#define rxPin 0                     // define SoftwareSerial rx data pin  
#define txPin 1                     // define SoftwareSerial tx data pin  
  
SoftwareSerial blueTooth(txPin, rxPin);  // create instance of SoftwareSerial  


int ledPin1=13;
int ledPin2=12;

int soilPin = A0; 
int sensorValue;  
int limit = 750; 

#include <dht.h>
#define dht_apin A1 // Analog Pin sensor is connected to
 dht DHT;

const int trigPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor
long duration;
int distance;

const int ldrPin = A2;

int smokePin = A3;
// Your threshold value
int sensorThres = 400;



const int capteur_D = 4;
int val_analogique;

#define pirPin 10
int calibrationTime = 30;
long unsigned int lowIn;
long unsigned int pause = 5000;
boolean lockLow = true;
boolean takeLowTime;
int PIRValue = 0;//Initializing the PIR Motion Sensor Value

void setup() {
  // put your setup code here, to run once:
  
   Serial.begin(9600);
   blueTooth.begin(9600); 
   pinMode(pirPin,INPUT);
   pinMode(soilPin, INPUT);
   pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
   pinMode(echoPin, INPUT); // Sets the echoPin as an Input
   pinMode(ldrPin,INPUT);
   pinMode(smokePin, INPUT);
   pinMode(capteur_D, INPUT);
   pinMode(ledPin1,OUTPUT);
   pinMode(ledPin2,OUTPUT);
  Serial.println("\t\t\t  WELCOME TO OUR WEATHER  STATION!!  \t\t\t" );
}

void loop() {
  // put your main code here, to run repeatedly:
    
    if(Serial.available()) 
   {  
    delay(1000);
    sensor2();
    delay(1000);
    sensor3();
    delay(1000);
    sensor5();
    delay(1000);
    sensor7();
    delay(1000);
    sensor1();
    delay(1000);
    Serial.println("Motion Detected!");
    sensor6();
    delay(1000);
     Serial.println("-------------------------------------------------------------------------------");
     Serial.println("\n");
    }
}


void sensor1(){
    if(digitalRead(pirPin) == HIGH) {
      if(lockLow) {
         PIRValue = 1;
         lockLow = false;
         Serial.println("      Motion detected    ");
         delay(100);
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
          blueTooth.write("Motion ended.");
         delay(100);
      }
   }
}


void sensor2(){
  sensorValue = analogRead(soilPin); //Reads the soil mositure values
   Serial.print("Soil Moisture Value Is: ");
   Serial.println(sensorValue);

 
  if (sensorValue>limit) {
  Serial.println("   Watering Needed!!  (GREEN LED) ");
  digitalWrite(ledPin1, HIGH); 
  }
  else {
  digitalWrite(ledPin1, LOW); 
  }
 
  delay(1000);     
 }


 void sensor3(){
  DHT.read11(dht_apin);
    //Reads The Humidity Of The Surrounding
     Serial.print("Current Humidity = ");
     Serial.print(DHT.humidity);
     Serial.println("%  ");
    //Reads The Temperature Of The Surrounding
    Serial.print("Temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("oC  ");
 }



void sensor5(){
int ldrStatus = analogRead(ldrPin);
//To Detect The Amount Of Sunlight
  if (ldrStatus >=300) {

  Serial.print("Its BRIGHT !");
  Serial.println(ldrStatus);

} else {

     Serial.println("Its DARK ! ");
     Serial.println(ldrStatus);
} 
}


void sensor6(){
  //To detect any kind of hazardous gas
  int analogSensor = analogRead(smokePin);
  // Checks if it has reached the threshold value
  if (analogSensor > sensorThres)
  {
    digitalWrite(ledPin2,HIGH);
   
  }
  else
  {
    digitalWrite(ledPin2, LOW);
  
  }
  delay(100);
}


void sensor7()
{
if(digitalRead(capteur_D) == LOW) 
  {
    Serial.println("Digital value : wet"); 
    delay(100); 
  }
else
  {
    Serial.println("Digital value : dry");
    delay(100); 
  }

}
