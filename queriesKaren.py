import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import *
from bs4 import BeautifulSoup
import requests
import sys
import time
import multiprocessing
import InputOutput
import functionsKaren
import pyautogui
import random
from cv2 import cv2
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def commandsViaVoice():
    WAKE = "karen"
    readylist=["I am ready sir","shoot","hello sir"]
    while True:
        print("\nSay Hey Karen...")
        text = InputOutput.takeCommand().lower()

        if text.count(WAKE) > 0:
            InputOutput.speak(random.choice(readylist))
            query = InputOutput.takeCommand().lower()
            AllQuerise(query)

def commandsViaKeyboard():
    while True:
        query=InputOutput.takeCommandViaKeyborad().lower()
        AllQuerise(query)

def commandsViaAndroid():
    while True:
        query=InputOutput.takeCommandViaAndroid().lower()
        AllQuerise(query)

def start():
    flag = int(input("\n Press 1 for speech\n Press 2 For Text\n Press 3 For android\n"))
    if flag == 1:
        InputOutput.speakPrint("Taking Command from Voice\n")
        commandsViaVoice()
    elif flag == 2:
        InputOutput.speakPrint("Taking Command from Keyboard\n")
        commandsViaKeyboard()
    elif flag == 3:
        InputOutput.speakPrint("Taking Command From your phone sir\n")
        commandsViaAndroid()
    else:
        print("Invalid Input")

def AllQuerise(query):
            if 'wikipedia' in query:
                InputOutput.speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                InputOutput.speak("wikipedia says,")
                print(results)
                InputOutput.speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                InputOutput.speak("Opening Youtube.com...")

            elif 'open google' in query:
                webbrowser.open("google.com")
                InputOutput.speak("Opening Google.com...")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open spotify' in query:
                webbrowser.open("https://open.spotify.com/collection/tracks")
                InputOutput.speak("Opening spotify...")

            elif 'play music' in query:
                music_dir = 'C:/Users/Utkarsh/Music/music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                InputOutput.speak("Playing music for you sir...")

            elif "time" in query:
                x = datetime.datetime.now()
                InputOutput.speakPrint(x.strftime("it's %I:%M %p, sir\n"))

            elif "open code" in query:
                codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                InputOutput.speak("opening code....")

            elif 'email' in query:
                functionsKaren.mailSender()

            elif 'shutdown' in query or 'shut down' in query:
                InputOutput.speak("shutting down sir, see you soon...")
                os.startfile(
                    "C:/Users/Utkarsh/Documents/Programs/Python/Karen/shutdown.lnk")

            elif 'restart' in query or 'reboot' in query:
                InputOutput.speak("Rebooting laptop...")
                os.startfile(
                    "C:/Users/Utkarsh/Documents/Programs/Python/Karen/Restart.lnk")

            elif 'log out' in query or 'lock screen' in query:
                InputOutput.speak("logging out sir, see you soon...")
                os.startfile(
                    "C:/Users/Utkarsh/Documents/Programs/Python/Karen/logout.lnk")

            elif 'google' in query:
                query = query.replace("google", "")
                chrome_path = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                    webbrowser.open("https://google.com/search?q=%s" % query)
                    InputOutput.speak("Here is what i found on google sir...")

            elif 'corona count' in query or 'COVID-19' in query:
                functionsKaren.coronaCount()

            elif 'date' in query:
                x = datetime.datetime.now()
                InputOutput.speakPrint(x.strftime("it's %A, %B %d %Y \n"))

            elif 'old' in query or 'age' in query:
                functionsKaren.ageCalculate()

            elif 'click photo' in query or 'take photo' in query:
                stream = cv2.VideoCapture(0)
                InputOutput.speak('ok sir')
                grabbed, frame = stream.read()

                if grabbed:
                    cv2.imshow('window', frame)
                    cv2.imwrite('me.png', frame)
                    InputOutput.speak('Done, pic take a succefully')
                stream.release()

            elif 'take screenshot' in query:
                screenshot = pyautogui.screenshot()
                screenshot.save('ss.jpg')
                InputOutput.speak('screenshot taken succesfully')

            elif 'weather' in query:
                functionsKaren.weather(query)

            elif 'take attendance' in query or 'attendance' in query:
                lst=[]
                for i in range(1, 5):
                    i = str(i)
                    InputOutput.speak('roll number' + i)
                    ans = InputOutput.takeCommand().lower()
                    if 'pressent sir ' in ans or 'present' in ans or 'yes sir' in ans:
                        InputOutput.speak(f'ok, roll number {i} is present')
                    else:
                        InputOutput.speak(f'roll number {i} is absent')
                        lst.append(i)
                InputOutput.speak(f"absent student's roll numbers are,")
                for m in lst:
                    InputOutput.speak(f"roll number {m}")

            elif 'keyboard input' in query:
                InputOutput.speakPrint("Taking Command from keyboard\n")
                commandsViaKeyboard()

            elif 'voice input' in query:
                InputOutput.speakPrint("Taking Command from Voice\n")
                commandsViaVoice()

            elif 'phone input' in query:
                InputOutput.speakPrint("Taking Command from your phone sir\n")
                commandsViaAndroid()
            else:
                if 'stop' in query or 'abort' in query or 'quit' in query:
                    InputOutput.speak("Good Bye sir, have a nice day")
                    sys.exit()
                elif '' in query:
                    InputOutput.speak("Invalid input sir, please try again")
                else:
                    InputOutput.speak(
                        "didnt find any command for this, should i google it?")
                    yesorno = InputOutput.takeCommand().lower()
                    if 'yes' in yesorno:
                        chrome_path = r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                            webbrowser.open(
                                "https://google.com/search?q=%s" % query)
                            InputOutput.speak("Here is what i found on google sir...")

                    else:
                        InputOutput.speak("No problem sir, I am Ready for the next command...\n")

