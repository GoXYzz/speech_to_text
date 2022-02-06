# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=10) # Duration in seconds
    print("Recognizing...")
    # convert speech to text
    # For additional languages, check the link https://developers.google.com/admin-sdk/directory/v1/languages
    text = r.recognize_google(audio_data, language="sr-SR")
    print(text)