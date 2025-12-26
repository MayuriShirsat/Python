# A PERSONAL ASSISTANT Sandhya

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
import music
import requests
from openai import OpenAI
#  pip install openai (paid)
from gtts import gTTS
import pygame
import os
from gpt4all import GPT4All

# Set API key securely as enviroment veriable (to protect the API KEY) (recommended)
# Windows PowerShell:
# setx OPENAI_API_KEY "your_new_api_key_here"


r= sr.Recognizer() # for simplicity (audio to text)
engine= pyttsx3.init() # for initilisation (text to speach)
rate=engine.getProperty('rate')
engine.setProperty('rate', 230)  # faster
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change to female voice (for male voice use "0' insted of "1")


gnewsapi="1e29147acb4546043eb39b9161774f90"
url = f"https://gnews.io/api/v4/search?q=Google&lang=en&max=5&apikey={gnewsapi}"


# jarvis response
def speak_old(text):
    engine.say(text) # (text to speach)
    engine.runAndWait() # otherwise program will exit before reading the text

################ 
# note--> this fun may not run in future in that case use above "speak_old" fun everywhere or change it name to "speak" 
###############
def speak(text):               
    tts=gTTS(text,slow=False,tld="co.in") #tld="co.in" for indian accent
    tts.save('temp.mp3')
    #  to run the mp3 audio
    # initilize the pygame mixer
    pygame.mixer.init()
    # load the mp3 file
    pygame.mixer.music.load('temp.mp3')
    # play the mp3 file
    pygame.mixer.music.play()
    # keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    #  to take the next speak argument we havw to unload the first one
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

####################################
# this is optional to using openai
# model = GPT4All(
#     "orca-mini-3b-gguf2-q4_0.gguf",
#     n_threads=8,   # or number of CPU cores
#     allow_download=True
# )
# def AIresponce(command): # using gpt4all
#     try:
#         response = model.generate(command,max_tokens=200,temp=0.7)
#         return(response)
#     except Exception as e:
#         print(e)
#         return("I am not able to answer this")
#####################################

def AIresponce(command): #  using OpenAI
    try:
        client=OpenAI()
        response = client.responses.create(
            model="gpt-5-nano",
            input=[
                {"role":"system","content":"You are a virtual assistant named Sandhya skilled in general tasks like Alexa and Google Cloud."},
                {"role": "user","content": "what is coding."}
                ]
        )
        return(response.output_text)
    except:
        return("This is a mock response until API credits are enabled")

def processCommand(c):
    print(c)
    if "open" in c.lower():
        site = c.split(" ")[1]
        webbrowser.open(f"https://www.{site}.com")
    elif "open youtube" in c.lower() or "open you tube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        s=c.lower().split(" ")[1]
        link=music.song[s]
        webbrowser.open(link)
    elif "news" in c.lower():
        n=requests.get(url)
        if n.status_code==200:
            # parse the JSON response
            data=n.json()
            # Extract the articles
            articles=data.get('articles',[])
            speak("Here are the top news headlines")
            # print the headlines
            for article in articles:
                title = article.get("title")
                if title:
                    print(title)
                    speak(title)
        else:
            speak("Sorry, I am unable to fetch the news right now.")
    else:
        # let OpenAi handel this
        output=AIresponce(c)
        print(output)
        speak(output)


if __name__=="__main__":
    speak("Hey Mayuri!! how may I help you.")
    while True:
        # lisition for the word "Jarvis" and then only respond
        try:
            r = sr.Recognizer() # fresh recognizer each loop so it not overflow
            # obtain audio from the microphone 
            with sr.Microphone() as source: # take audio from microphone
                print("listening....")
                audio= r.listen(source,timeout=5,phrase_time_limit=2)
                # timeout-->starting timeout(before speaking)
                # phrase_time_limit-->time space between words

            # recognize speech using google recognizer    
            word=r.recognize_google(audio) # speech_recognition-->Recognizer() class -->recognize_google() subclass
            print(word)
            if "sandhya" in word.lower():
                speak("Yes Mayuri!!")
                # Listen for command
                with sr.Microphone() as source: 
                    print("Sandhya Active....")
                    audio= r.listen(source, timeout=5)
                    command=r.recognize_google(audio) 
                    processCommand(command)
            # if "exit" in command.lower() or "bye" in command.lower():
            #     break
        except Exception as e:
            print("Error; {0}".format(e))

