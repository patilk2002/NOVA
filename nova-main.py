import pyttsx3
import webbrowser
import smtplib
import subprocess
import os


engine = pyttsx3.init()
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

# engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wake_up():
    speak("I'm Nova, your personal assistant. How can I help you?")

def play_music():
    speak("Playing some music for you.")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def current_time():
    import datetime
    now = datetime.datetime.now()
    speak(f"The current time is {now.hour}:{now.minute}")

def open_browser():
    url = 'https://www.google.com'
    webbrowser.get(using=None).open(url)

def search_web(query):
    speak(f"Searching for {query}")
    query = query.replace(" ", "+")
    webbrowser.get(using=None).open(f"https://www.google.com/search?q={query}")

def send_email(to, subject, body):
    speak(f"Sending email to {to} with subject {subject}")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("youremail@gmail.com", "yourpassword")
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail("youremail@gmail.com", to, message)
    server.quit()

while True:
    command = input("What would you like to do? ")
    if command.lower() == "wake up nova":
        wake_up()
    elif command.lower() == "play some music":
        play_music()
    elif command.lower() == "what's the time":
        current_time()
    elif command.lower() == "open browser":
        open_browser()
    elif command.lower() == "search web":
        query = input("What would you like to search for? ")
        search_web(query)
    elif command.lower() == "send email":
        to = input("To: ")
        subject = input("Subject: ")
        body = input("Body: ")
        send_email(to,subject,body)
