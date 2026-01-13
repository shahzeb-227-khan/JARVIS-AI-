import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning shahzeb ")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon shahzeb")
    else:
        speak("Good evening shahzeb" )
    speak(" I am Jarvis , How may i help u sir")

def takecommand():
    #it takes microphone input from user and returns a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please speak up I am listening")
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-PK')
        print(f"You said : {query}\n")

    except Exception as e:
        speak("Please say that again... I could not hear")
        print("Please say that again...")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search on google' in query:
            speak("What would you like to search on google?")
            google_query = takecommand().lower()
            speak(f"Searching on google for {google_query}")
            webbrowser.open(f"https://www.google.com/search?q={google_query}")

        elif 'search on youtube' in query:
            speak("What would you like to search on youtube")
            youtube_query = takecommand().lower()
            if youtube_query != 'none':
                speak(f"Searching on youtube for {youtube_query}")
                webbrowser.open(f"https://www.youtube.com/results?search_query={youtube_query}")

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open('google.com')

        elif 'open leet code' in query:
            speak("Opening leetcode")
            webbrowser.open('leetcode.com')

        elif 'open LinkedIn' in query:
            speak("Opening LinkedIn")
            webbrowser.open('linkedin.com')

        elif 'open stack overflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open('stackoverflow.com')

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is {strtime}")

        elif 'open code' in query:
            speak("Opening visual studio code")
            visualcode = "C:\\Users\\shahz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualcode)

        elif 'open word' in query:
            speak("Opening word")
            word = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(word)

        elif 'play music'  in query:
            speak("playing a random music from your playlist")
            music_dir = "C:\\Users\\shahz\\OneDrive\\Desktop\\mymusic"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'stop' in query:
            print("It was a pleasure talking to you shahzeb\nBye !")
            speak("It was a pleasure talking to you shahzeb\nBye")
            exit()


