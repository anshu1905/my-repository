#include <LedControl.h>
int DIN = 12;
int CS =  11;
int CLK = 10;
int incomingByte=0;
LedControl lc=LedControl(DIN,CLK,CS,0);

void setup(){
Serial.begin(9600);
 lc.shutdown(0,false);       
 lc.setIntensity(0,15);      //Adjust the brightness maximum is 15
 lc.clearDisplay(0);    
}
void loop(){ 
   
    if(Serial.available()>0){
    incomingByte=Serial.read();
    //Facial Expression
    if (incomingByte='Happy')
    {
    byte smile[8]=   {0x3C,0x42,0xA5,0x81,0xA5,0x99,0x42,0x3C};
    printByte(smile);
    delay(100);
    }
    else if(incomingByte='Neutral')
    {
    byte neutral[8]= {0x3C,0x42,0xA5,0x81,0xBD,0x81,0x42,0x3C};
    printByte(neutral);
    delay(100);
    }
    else if(incomingByte='Sad')
    {
    byte sad[8]=   {0x3C,0x42,0xA5,0x81,0x99,0xA5,0x42,0x3C};
    printByte(sad);    
    delay(100);
    }  
    }
}

void printByte(byte character [])
{
  int i = 0;
  for(i=0;i<8;i++)
  {
    lc.setRow(0,i,character[i]);
  }
}
