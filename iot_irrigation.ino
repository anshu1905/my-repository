#include <ESP8266WiFi.h>;

#include <WiFiClient.h>;

#include <ThingSpeak.h>;

const char* ssid = "DESKTOP-BH29T2M 1472"; //Your Network SSID

const char* password = "T74j91@2"; //Your Network Password

WiFiClient client;

unsigned long myChannelNumber = 1232491; //Your Channel Number (Without Brackets)

const char * myWriteAPIKey = "1CANT2O8PSUXSR5O"; //Your Write API Key

#include <dht.h>
#define dht_apin D1 // Analog Pin sensor is connected to
dht DHT;
int h;
int t;

int  sensorPin=A0;
int sensorValue;  
int limit = 300; 
 
void setup() {
  // put your setup code here, to run once:
 Serial.begin(115200);
 delay(10);
 WiFi.begin(ssid, password);
 ThingSpeak.begin(client);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensor1();
  sensor2();
  ThingSpeak.writeField(myChannelNumber,1,sensorValue, myWriteAPIKey);
  ThingSpeak.writeField(myChannelNumber,2,t, myWriteAPIKey);
  ThingSpeak.writeField(myChannelNumber,3,h, myWriteAPIKey);
  //Update in ThingSpeak
}

void sensor1()
{
    DHT.read11(dht_apin);
    Serial.print("Current humidity = ");
    h=DHT.humidity;
    Serial.print(h); 
    Serial.print("%  ");
    Serial.print("temperature = ");
    t=DHT.temperature;
    Serial.print(t); 
    Serial.println("C  ");
    delay(1000);
}

void sensor2(){
   sensorValue = analogRead(sensorPin); 
   Serial.println("Analog Value : ");
   Serial.println(sensorValue);
 
   if (sensorValue<limit) {
      digitalWrite(13, HIGH); 
      Serial.println("--------PLEASE WATER THE PLANTS--------");
   }
   else {
      digitalWrite(13, LOW); 
   }
   delay(1000);   
}
