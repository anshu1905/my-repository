#define S0 4
#define S1 5
#define S2 6
#define S3 7
#define sensorOut 8

int frequency = 0;
int frequency1 = 0;
int frequency2 = 0;
int frequency3 = 0;
int redled=9;
int greenled=10;
int blueled=11;

void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  
  // Setting frequency-scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);

  pinMode(redled,OUTPUT);
  pinMode(greenled,OUTPUT);
  pinMode(blueled,OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  // Setting red filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  // Reading the output frequency
   frequency = pulseIn(sensorOut, LOW);
  //Remaping the value of the frequency to the RGB Model of 0 to 255
  frequency1 = map(frequency, 25,72,255,0);
  // Printing the value on the serial monitor
  Serial.print("R= ");//printing name
  Serial.print(frequency1);//printing RED color frequency
  Serial.print("  ");
  delay(1000);

  // Setting Green filtered photodiodes to be read
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  // Reading the output frequency
  frequency = pulseIn(sensorOut, LOW);
  //Remaping the value of the frequency to the RGB Model of 0 to 255
  frequency2 = map(frequency, 30,90,255,0);
  // Printing the value on the serial monitor
  Serial.print("G= ");//printing name
  Serial.print(frequency2);//printing GREEN color frequency
  Serial.print("  ");
  delay(1000);

  // Setting Blue filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  // Reading the output frequency
  frequency = pulseIn(sensorOut, LOW);
  //Remaping the value of the frequency to the RGB Model of 0 to 255
  frequency3 = map(frequency, 25,70,255,0);
  // Printing the value on the serial monitor
  Serial.print("B= ");//printing name
  Serial.print(frequency3);//printing BLUE color frequency
  Serial.println("  ");
  delay(1000);

  
 int value[3]={frequency1,frequency2,frequency3};
 int i;
  for (i = 1; i < 3; ++i) {
    if (value[0] < value[i])
      value[0] = value[i];
    }

    Serial.print("Largest element = ");
    Serial.print(value[0]);
    Serial.println("\n");
    delay(100);
    
  if (frequency1 >= frequency2 && frequency1 >= frequency3)
        digitalWrite(redled,HIGH);
        delay(1000);
        digitalWrite(redled,LOW);

    // if n2 is greater than both n1 and n3, n2 is the largest
  if (frequency2 >= frequency1 && frequency2 >= frequency3)
        digitalWrite(greenled,HIGH);
        delay(1000);
        digitalWrite(greenled,LOW);
    // if n3 is greater than both n1 and n2, n3 is the largest
  if (frequency3 >= frequency1 && frequency3 >= frequency2)
        digitalWrite(blueled,HIGH);
        delay(1000);
        digitalWrite(blueled,LOW);

}
