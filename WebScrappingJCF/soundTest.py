import pyttsx3
import winsound

engine = pyttsx3.init()
engine.say("Hello!")
engine.runAndWait()

winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
