import tkinter as tk
from tkinter import ttk
import pyttsx3
import datetime
import webbrowser
import os
import smtplib
import requests
import json

engine = pyttsx3.init()

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

def weather(city):
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(f"Temperature: {current_temperature} Kelvin \n")

    
root = tk.Tk()
root.title("Nova - Personal Assistant")

frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)

time_button = ttk.Button(frame, text="wake_up", command=wake_up)
time_button.grid(column=0, row=0)

time_button = ttk.Button(frame, text="What's the time?", command=time)
time_button.grid(column=1, row=0)

browser_button = ttk.Button(frame, text="Open browser", command=open_browser)
browser_button.grid(column=2, row=0)

music_button = ttk.Button(frame, text="Play music", command=play_music)
music_button.grid(column=3, row=0)

email_button = ttk.Button(frame, text="Send email", command=send_email)
email_button.grid(column=4, row=0)

weather_button = ttk.Button(frame, text="Weather", command=lambda: weather(city_entry.get()))
weather_button.grid(column=5, row=0)

city_label = ttk.Label(frame, text="City:")
city_label.grid(column=6, row=0)

city_entry = ttk.Entry(frame)
city_entry.grid(column=6, row=0)

root.mainloop()
