# Assistant with voice recognition 

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
# engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
engine.say("Hello, I am Jarvis. How can I assist you?")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wake_up():
    speak("I'm Nova, your personal assistant. How can I help you?")

def time():
    current_time = datetime.datetime.now().time()
    speak(f"The current time is {current_time.hour}:{current_time.minute}")

def open_browser():
    speak("Opening browser")
    webbrowser.open("https://www.google.com/")

def play_music():
    speak("Playing music")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "yourpassword")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()
    speak("Email sent!")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        if "time" in command:
            time()
        elif "browser" in command:
            open_browser()
        elif "music" in command:
            play_music()
        elif "email" in command:
            send_email()
        else:
            speak("Sorry, I didn't understand that.")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        speak("Sorry, my speech service is down")
while True:
    listen()