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
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
import InputOutput
import functionsKaren
import queriesKaren


if __name__ == "__main__":
    if functionsKaren.checkInternetConnection() == True:
        functionsKaren.wishMe()
        queriesKaren.start()

