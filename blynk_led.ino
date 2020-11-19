
#define BLYNK_PRINT Serial
#include <WiFiClient.h>;
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "";
char pass[] = "";

#define LEDpin D6

void setup() {
  // put your setup code here, to run once:
// Connect Blynk
  Blynk.begin(auth, ssid, pass);
  Serial.begin(115200);
  pinMode(LEDpin,OUTPUT);
}

BLYNK_WRITE(V0) {
  float button = param.asInt(); // read button
  Serial.println(button);
  analogWrite(LEDpin, button);
 
}
void loop() {
  // put your main code here, to run repeatedly:
Blynk.run();
}
