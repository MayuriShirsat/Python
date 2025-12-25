# PyAudio ❌ does NOT support Python 3.14
# PyAudio ✅ works with Python 3.11

# first need to install python version 3.11
''' 
1️⃣ Installing new Python version does NOT delete old versions
On Windows:
Each Python version installs into its own folder
They coexist safely
2️⃣ A virtual environment does NOT install Python.
It only copies/links an existing Python version
3️⃣ Which version runs when you type python
This is controlled by:Python Launcher (py)
ex.,
py -3.11 -m venv audioenv
py -3.14 -m venv venv

audioenv → Python 3.11
venv → Python 3.14
'''
# py -3.11 -m venv venv
# py -3.11 -m venv --> “Use Python 3.11 to create a virtual environment”
# venv(name of virtual environment)

# cd c:\Python\Megha_Project1-Jarvis(to make the current directry in the forlder we are working on)
# .\venv\Scripts\activate.ps1
#                                       OR
# go to interpreter and select venv-->python 3.11(this automatically created venv)

# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
'''
PyAudio:A Python library used to capture audio from the microphone.
SpeechRecognition:A Python library used to convert spoken language into text.
Setuptools:A utility library used for building and installing Python packages.
pyttsx3:Convert text to speech
'''

import speech_recognition as sr
import webbrowser # builtin module-->It allows Python to open URLs in a web browser automatically.
import pyttsx3

r= sr.Recognizer() # for simplicity (audio to text)
engine= pyttsx3.init() # for initilisation (text to speach)

# jarvis response
def speak(text):
    engine.say(text) # (text to speach)
    engine.runAndWait() # otherwise program will exit before reading the text

if __name__=="__main__":
    speak("Hey Mayuri!! how may I help you.")
    while True:
        # lisition for the word "Jarvis" and then only respond
        try:
            # obtain audio from the microphone 
            with sr.Microphone() as source: # take audio from microphone
                print("listening....")
                audio= r.listen(source,timeout=3,phrase_time_limit=2)
                # timeout-->starting timeout(before speaking)
                # phrase_time_limit-->time space between words

            # recognize speech using google recognizer    
            command=r.recognize_google(audio) # speech_recognition-->Recognizer() class -->recognize_google() subclass
            print(command)
            
        except Exception as e:
            print("Error; {0}".format(e))

