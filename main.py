# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# Find short word on https://cloud.google.com/speech-to-text/docs/languages
lang = input("Shortword for speaking language (blank for english):   ")
dur = input("Duration in seconds:   ")
file_name = input("File name:   ")

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=int(dur)) 
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data, language=lang)
    print(text)

filename = file_name + '.txt'
# writting speech into file 
with open(filename, 'a') as thought:
    thought.write('\n' + text.capitalize() + '.')

