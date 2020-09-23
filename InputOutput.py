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
import socket
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def PrintStr(strslow, ts):
    for l in strslow:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(ts)


def speakPrint(spstr):
    p1 = multiprocessing.Process(target=PrintStr, args=(spstr, 0.031))
    p2 = multiprocessing.Process(target=speak, args=(spstr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()




def takeCommand():
    '''
    it takes microphone input from user and returns string output!
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def takeCommandViaKeyborad():
    ip = input("karen: ")   #it takes input via keyboard
    return ip.lower()


def takeCommandViaAndroid(): #socket programming
    listensocket = socket.socket()
    port = 7800
    maxConnections = 999
    IP = socket.gethostname()
    listensocket.bind(('', port))
    listensocket.listen(maxConnections)
    try:
        while True:
            (clientsocket, address) = listensocket.accept()
            message = clientsocket.recv(1024).decode()
            print(message)
            return message
    except IOError:
        print("Error: can \t find file or read data")
