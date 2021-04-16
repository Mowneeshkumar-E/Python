import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wp
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def mic_input():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print('listening...')
        r.pause_threshold = 0.8
        record = r.listen(mic)
    try:
        print('wait few more seconds')
        mic_output = r.recognize_google(record, language='en-in')
        mic_output = mic_output.lower()
        return mic_output
    except:
        print('sorry something went wrong')
        return 'None'



def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak('good morning mownish')
    elif hour >= 12 and hour < 18:
        speak('good afternoon mownish')
    else:
        speak('good evening mownish')


wishme()
while True:
    str = mic_input()
    if 'help' in str:
        speak('how can i help you')
    elif 'wikipedia' in str:
        speak('searching in wikipedia')
        result = wp.summary(str, sentences=2)
        speak('with the help of wikipedia')
        speak(result)
    elif 'time' in str:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        speak('the time is  {} '.format(time))
    elif 'date' in str:
        date = datetime.datetime.now().date()
        speak('today date is  {} '.format(date))
    elif 'website' in str:
        speak('opening your website')
        webbrowser.open('http://investyourtime.000webhostapp.com')
    elif 'game' in str:
        speak('opening your game')
        os.startfile('flycycle.exe')
    elif 'miv' in str:
        speak('opening your multimedia software')
        os.startfile('MIV.exe')
    elif 'colab' in str:
        speak('colab is ready to use')
        webbrowser.open('https://colab.research.google.com')
    elif 'music' in str:
        speak('playing music for you')
        musicdir = 'music file path'
        songs = os.listdir(musicdir)
        os.startfile(os.path.join(musicdir, random.choice(songs)))
    elif 'photo' in str:
        os.startfile('image file path')
    elif 'video' in str:
        os.startfile('video file path')
    elif 'notepad' in str:
        os.startfile("notepad++.exe")
    elif 'thank' in str:
        speak('thank you')

