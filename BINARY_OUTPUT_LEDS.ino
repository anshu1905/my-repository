const int LedPins[]={2,3,4,5,6,7,8,9};
byte led=0b00001111;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
int i;
for (i=0;i<=7;i++)
{
  pinMode(LedPins[i],OUTPUT);
}
Serial.println("Enter a number between 0 and 255 : ");
}

void loop() {
  // put your main code here, to run repeatedly:

if(Serial.available())
{
  int Val=Serial.parseInt();
  
  
  if (Val>255)
  {
    Serial.print("Not possible");
    Serial.print("Please try again");
    Serial.print("\n");
    Serial.println("Enter a number between 0 and 255:  ");
    return;
  }
  Serial.print("The decimal number is: ");
  Serial.println(Val);
  Serial.print("\n\n");
  Serial.print("The binary number is:  ");
  Serial.println(Val,BIN);
  Serial.print("\n\n");
  delay(5000);

  Serial.print("THE AND RESULT IS:  ");
  byte r1=(led & Val);
  Serial.println(r1);
  char c1[8];
  itoa(r1,c1,2);
  Serial.println(c1);
  int a;
  for(a==0;a<strlen(c1);a++)
  {
    if(c1[a]=='1')
    {
      digitalWrite(LedPins[a],HIGH);
    }
    else if(c1[a]=='0')
    {
      digitalWrite(LedPins[a],LOW);
    }
  }
  delay(5000);
  int b;
  for (b==0;b<=7;b++)
  {
    digitalWrite(LedPins[b],LOW);
  }
  delay(2000);
  Serial.print("\n\n");


  
  
  Serial.print("THE OR RESULT IS: ");
  byte r2=(led | Val);
  Serial.println(r2);
  char c2[8];
  itoa(r2,c2,2);
  Serial.println(c2);
  int c;
  for(c==0;c<strlen(c2);c++)
  {
    if(c2[c]=='1')
    {
      digitalWrite(LedPins[c],HIGH);
    }
    else if(c2[c]=='0')
    {
      digitalWrite(LedPins[c],LOW);
    }
    
  }
  delay(5000);
  int d;
  for (d==0;d<=7;d++)
  {
    digitalWrite(LedPins[d],LOW);
  }
  delay(2000);
  Serial.print("\n\n");



  Serial.print("THE XOR RESULT IS: ");
  byte r3=(led ^ Val);
  Serial.println(r3);
  char c3[8];
  itoa(r3,c3,2);
  Serial.println(c3);
  int e;
  for(e==0;e<strlen(c3);e++)
  {
    if (c3[e]=='1')
    {
      digitalWrite(LedPins[e],HIGH);
    }
    else if(c3[e]=='0')
    {
      digitalWrite(LedPins[e],LOW);
    }
  }
  delay(5000);
  int f;
  for (f==0;f<=7;f++)
  {
    digitalWrite(LedPins[f],LOW);
  }
  delay(2000);
  Serial.print("\n\n");
  
  Serial.print("ONE CYCLE IS FINISHED!!!");
  
}
}
