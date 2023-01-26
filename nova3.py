import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wake_up():
    speak("Hello, I am Jarvis. How can I assist you?")

def play_music():
    speak("Playing some music for you.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

def open_chrome():
    speak("Opening chrome for you.")
    webbrowser.open("http://www.google.com")




while True:
    command = input("What would you like to do? ")
    if command.lower() == "wake up jarvis":
        wake_up()
    elif command.lower() == "play some music":
        play_music()
    elif command.lower() == "what's the time":
        current_time()
    elif command.lower() == "open chrome":
        open_chrome()
    else:
        speak("Sorry, I didn't understand that command.")
