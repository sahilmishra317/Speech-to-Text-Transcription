import speech_recognition as sr
import urllib.request
import os

print("Downloading test audio file...")
urllib.request.urlretrieve("https://www2.cs.uic.edu/~i101/SoundFiles/preamble10.wav", "test.wav")

print("Initializing recognizer...")
r = sr.Recognizer()

try:
    with sr.AudioFile("test.wav") as source:
        audio = r.record(source)
    print("Sending audio to Google Speech API...")
    text = r.recognize_google(audio)
    print("---------------------------------")
    print("SUCCESS! Recognized text:")
    print(text)
    print("---------------------------------")
except Exception as e:
    print(f"ERROR: {e}")

if os.path.exists("test.wav"):
    os.remove("test.wav")
