import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import serial
import time

ser = serial.Serial('COM4', 9600)
text=input("Enter which led should be turned on GREEN /RED /YELLOW:")
def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try :
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception"+str(e))
    return said

def led_on_off():
    text=get_audio()
    if (text=="green"):
        print('LED GREEN IS ON')
        time.sleep(0.1)
        ser.write(b'G')
        led_on_off()

    elif(text=="red"):
        print('LED RED IS ON')
        time.sleep(0.1)
        ser.write(b'R')
        led_on_off()

    elif(text=="yellow"):
        print('LED YELLOW IS ON')
        time.sleep(0.1)
        ser.write(b'Y')
        led_on_off()

    else:
        print('ALL LEDS ARE OFF')
        led_on_off()
time.sleep(2) # wait for the serial connection to initialize
led_on_off()

        
