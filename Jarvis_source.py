import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Engine voice change
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


def speak(audio):
    """
    This is speak function
    :param audio:
    :return:
    """
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    This is wish function in this function perform to according to time
    :return: wish the user like: good morning sir, good afternoon, etc.
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak(" I am Jarvis sir. Please tell me how may I help you")


def takeCommand():
    """
    This is take_Command function.
    In this function give the input from the Microphone.

    :return: It's return the string object.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
            continue
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            continue
        elif "open google" in query:
            webbrowser.open("google.com")
            continue
        elif "play music" in query:
            music_dir = r"F:\Songs"
            songs = os.listdir(music_dir)
            speak("sir which song i have to play please give the index of the song")
            for i, song in enumerate(songs):
                engine.setProperty('rate', 300)
                print(f'{i+1} {song}')
                speak(f'{i+1} {song}')
            song_index = int(input("Enter Here:"))
            os.startfile(os.path.join(music_dir, songs[song_index-1]))
            continue
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is now {strTime}")
            continue
        elif "open code" in query:
            code_path = r"C:\Users\visha\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
            continue
        elif "open pycharm" in query:
            pycharm_path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2020.3.4\bin\pycharm64.exe"
            os.startfile(pycharm_path)
            continue
        elif 'open chrome' in query:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)
            continue
        elif 'your language' in query:
            speak("Sir my language is english")
        elif 'speak rate' in query:
            rate = engine.getProperty('rate')
            speak(f"sir my speak rate is {rate}")
        elif "jarvis stop" in query:
            speak("ok sir have a good day sir!")
            exit()


