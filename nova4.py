import tkinter as tk
from tkinter import ttk
import pyttsx3
import datetime
import webbrowser
import os
import smtplib

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

def on_time():
    time()

def on_browser():
    open_browser()

def on_music():
    play_music()

def on_email():
    content = input("What should I say? ")
    to = input("To whom should I send this email? ")
    send_email(to, content)

root = tk.Tk()
root.title("Nova - Personal Assistant")
root.geometry("250x200")

time_button = ttk.Button(root, text="Time", command=on_time)
time_button.pack()

browser_button = ttk.Button(root, text="Open Browser", command=on_browser)
browser_button.pack()

music_button = ttk.Button(root, text="Play Music", command=on_music)
music_button.pack()

email_button = ttk.Button(root, text="Send Email", command=on_email)
email_button.pack()

wake_up()
root.mainloop()
