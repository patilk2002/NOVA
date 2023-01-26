from gtts import gTTS
import os

text = "Hello, I am Jarvis. How can I assist you?"
tts = gTTS(text, slow=False, lang='en')
tts.save("hello.mp3")
os.system("start hello.mp3")
