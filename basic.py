import sys
from wit import Wit
import speech_recognition as sr
from gtts import gTTS



access_token = 'UZWI6PSAHCZLFBI6G37DHVVQZ5IN5HIW'
client = Wit(access_token=access_token)
mes = ''
r = sr.Recognizer()
with sr.Microphone() as source :
  print("Speak:..")
  r.adjust_for_ambient_noise(source,duration = 5)
  audio = r.listen(source)
try :
  mes =  r.recognize_google(audio)
  print(mes)
except sr.UnknownValueError :
  print("Couldn't procdess audio")

response = client.message(mes)
task = response["entities"]["intent"][0]["value"]
print(task)


if(task == "Lights") :
  print("Turning on the lights








