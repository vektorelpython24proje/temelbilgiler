from playsound import playsound
from gtts import gTTS,gTTSError

def playaudio(audio):
    playsound(audio)

def convert_to_audio(text):
    audio =gTTS(text)
    audio.save("textaud.mp3")
    playaudio("textaud.mp3")

convert_to_audio("my name is joe")