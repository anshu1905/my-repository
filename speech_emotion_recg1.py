import nltk
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts=gTTS(text=text,lang="en")
    filename="myvoice3.mp3"
    tts.save(filename)
    playsound.playsound(filename)
speak("How was your experience!")
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

text=get_audio()


print("Starting TextBlob Sentiment Analysis")
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
score =  TextBlob(text,analyzer=NaiveBayesAnalyzer()).sentiment
print(score)
if score[1]>score[2]:
    print("Happy Experience")
else:
    print("Sad Experience")

