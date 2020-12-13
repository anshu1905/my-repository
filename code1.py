import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

mixer.init()
sound1 = mixer.Sound('beep-02.wav')

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
            print("Please Don't Talk During The Exam")
            sound1.play()
        except Exception as e:
            print()
    return said
while True:
    text=get_audio()


