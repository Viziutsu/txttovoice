from gtts import gTTS
import os
file = open("abc.txt", "r", encoding="utf-8").read()
speech = gTTS(text=file, lang='ru', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")