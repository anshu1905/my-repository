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

//MOTOR DRIVER 
//lmf->LEFT MOTOR FRONT
//rmf->RIGHT MOTOR FRONT
//lmb->LEFT MOTOR BACK
//rmb->RIGHT MOTOR BACK

#define lmf_0 D0
#define lmf_1 D1
#define rmf_2 D2
#define rmf_3 D3
#define lmb_4 D4
#define lmb_5 D5
#define rmb_6 D6
#define rmb_7 D7

// SETUP
void setup()
{
  pinMode(lmf_0, OUTPUT);
  pinMode(lmf_1, OUTPUT);
  pinMode(rmf_2, OUTPUT);
  pinMode(rmf_3, OUTPUT);
  pinMode(lmb_4, OUTPUT);
  pinMode(lmb_5, OUTPUT);
  pinMode(rmb_6, OUTPUT);
  pinMode(rmb_7, OUTPUT);
  
  // Start serial communication
  Serial.begin(115200);

  // Connect Blynk
  Blynk.begin(auth, ssid, pass);
}


// FORWARD
BLYNK_WRITE(V0) {
  int button = param.asInt(); // read button
  if (button == 1) {
    Serial.println("------MOVING FORWARD------ ");

    digitalWrite(lmf_0, HIGH);
    digitalWrite(lmf_1, LOW);
    digitalWrite(rmf_2, HIGH);
    digitalWrite(rmf_3, LOW);
    digitalWrite(lmb_4, HIGH);
    digitalWrite(lmb_5, LOW);
    digitalWrite(rmb_6, HIGH);
    digitalWrite(rmb_7, LOW);
    
  }
  else {
    Serial.println("------STOP------");
    
    digitalWrite(lmf_0, LOW);
    digitalWrite(lmf_1, LOW);
    digitalWrite(rmf_2, LOW);
    digitalWrite(rmf_3, LOW);
    digitalWrite(lmb_4, LOW);
    digitalWrite(lmb_5, LOW);
    digitalWrite(rmb_6, LOW);
    digitalWrite(rmb_7, LOW);
  }
}

// LEFT
BLYNK_WRITE(V1) {
  int button = param.asInt(); // read button
  if (button == 1) {
    Serial.println("------MOVING LEFT------ ");

    digitalWrite(lmf_0, LOW);
    digitalWrite(lmf_1, HIGH);
    digitalWrite(rmf_2, HIGH);
    digitalWrite(rmf_3, LOW);
    digitalWrite(lmb_4, LOW);
    digitalWrite(lmb_5, HIGH);
    digitalWrite(rmb_6, HIGH);
    digitalWrite(rmb_7, LOW);
    
  }
  else {
    Serial.println("------STOP------");
    
    digitalWrite(lmf_0, LOW);
    digitalWrite(lmf_1, LOW);
    digitalWrite(rmf_2, LOW);
    digitalWrite(rmf_3, LOW);
    digitalWrite(lmb_4, LOW);
    digitalWrite(lmb_5, LOW);
    digitalWrite(rmb_6, LOW);
    digitalWrite(rmb_7, LOW);
  }
}


// RIGHT
BLYNK_WRITE(V2) {
  int button = param.asInt(); // read button
  if (button == 1) {
    Serial.println("------MOVING RIGHT------ ");

    digitalWrite(lmf_0, HIGH);
    digitalWrite(lmf_1, LOW);
    digitalWrite(rmf_2, LOW);
    digitalWrite(rmf_3, HIGH);
    digitalWrite(lmb_4, HIGH);
    digitalWrite(lmb_5, LOW);
    digitalWrite(rmb_6, LOW);
    digitalWrite(rmb_7, HIGH);
    
  }
  else {
    Serial.println("------STOP------");
    
    digitalWrite(lmf_0, LOW);
    digitalWrite(lmf_1, LOW);
    digitalWrite(rmf_2, LOW);
    digitalWrite(rmf_3, LOW);
    digitalWrite(lmb_4, LOW);
    digitalWrite(lmb_5, LOW);
    digitalWrite(rmb_6, LOW);
    digitalWrite(rmb_7, LOW);
  }
}

// BACKWARD
BLYNK_WRITE(V3) {
  int button = param.asInt(); // read button
  if (button == 1) {
    Serial.println("Moving backward");

    digitalWrite(lmf_0, LOW);
    digitalWrite(lmf_1, HIGH);
    digitalWrite(rmf_2, LOW);
    digitalWrite(rmf_3, HIGH);
    digitalWrite(lmb_4, LOW);
    digitalWrite(lmb_5, HIGH);
    digitalWrite(rmb_6, LOW);
    digitalWrite(rmb_7, HIGH);
  }
  else {
    Serial.println("Stop");

    digitalWrite(lmf_0, LOW);
    digitalWrite(lmf_1, LOW);
    digitalWrite(rmf_2, LOW);
    digitalWrite(rmf_3, LOW);
    digitalWrite(lmb_4, LOW);
    digitalWrite(lmb_5, LOW);
    digitalWrite(rmb_6, LOW);
    digitalWrite(rmb_7, LOW);
  }
}

// MAIN CODE
void loop()
{
  Blynk.run();
}
