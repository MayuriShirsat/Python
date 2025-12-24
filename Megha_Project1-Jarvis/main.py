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

# .\venv\Scripts\activate.ps1

# pip install speechrecognition pyaudio
# pip install setuptools
'''
PyAudio:A Python library used to capture audio from the microphone.
SpeechRecognition:A Python library used to convert spoken language into text.
Setuptools:A utility library used for building and installing Python packages.
'''
