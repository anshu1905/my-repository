#define BLYNK_PRINT Serial


#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include "DHT.h"           // including the library of DHT11 temperature and humidity sensor
#define DHTTYPE DHT11      // DHT 11

#define dht_dpin D2
DHT dht(dht_dpin, DHTTYPE); 
char auth[] = "c7tOfzkHH7earHV6p8eo6s_McbuFWaVZ";            // You should get Auth Token in the Blynk App.
                                           // Go to the Project Settings (nut icon).

char ssid[] = "DESKTOP-BH29T2M 1472";    // Your WiFi credentials.
char pass[] = "T74j91@2";  // Set password to "" for open networks.
float t;                                   // Declare the variables 
float h;



void setup()
{
    Serial.begin(115200);// Debug console
    Blynk.begin(auth, ssid, pass);
    dht.begin();
    
}

void sensor()
{
  
  float h = dht.readHumidity();
  float t = dht.readTemperature(); 
  Serial.println("Humidity and temperature\n\n");
  Serial.print("Current humidity = ");
  Serial.print(h);
  Serial.print("%  ");
  Serial.print("temperature = ");
  Serial.print(t); 
  Blynk.virtualWrite(V0, t);
  Blynk.virtualWrite(V1, h);
  
}

void loop()
{
  sensor();
  Blynk.run();
  delay(100);
}
