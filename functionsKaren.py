from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pytz
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
from os import system, name
from time import sleep
import json
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def sendEmail(to, content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('thekarenofficial@gmail.com', 'thekarenofficial@4')
    server.sendmail('thekarenofficial@gmail.com', to, content)
    server.quit()


def mailSender():
    try:
        InputOutput.speak("Sure sir, What's the subject of the email?")
        subject = InputOutput.takeCommand()
        InputOutput.speak("and what should i say in email?")
        body = InputOutput.takeCommand()
        content = f"Subject: {subject}\n\n{body}"
        to = "upkharche@gmail.com"  # revievers mail address
        sendEmail(to, content)
        InputOutput.speak("Email has been send")
    except Exception as e:
        print(e)
        InputOutput.speak("Sorry sir, I am not able to send this email...")


def checkInternetConnection():
    url = "http://www.google.com"
    timeout = 5
    InputOutput.speak("connecting to the servers...")
    try:
        request = requests.get(url, timeout=timeout)
        InputOutput.speakPrint("connected to the servers sucessfully")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        InputOutput.PrintStr("Fail to connect to the servers.", 0.005)
        InputOutput.speak("Fail to connect to the servers.")
        return False


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        InputOutput.speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        InputOutput.speak("Good Afternoon Sir")
    else:
        InputOutput.speak("Good Evening sir")
    InputOutput.speak("I am karen, how may I help you Sir\n")


def coronaCount():
    wiki_link = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India"
    link = requests.get(wiki_link).text
    soup = BeautifulSoup(link, 'lxml')

    right_table = soup.find('table', class_='infobox')
    country = []
    for TR in right_table.find_all('tr'):
        for TH in TR.find_all('th'):
            if TH.get('scope') == 'row':
                country.append(TH.get_text())
                for TD in TR.find_all('td'):
                    a = TD.get_text()
                    country.append(a[:10])
    res_dct = {country[i]: country[i + 1]
               for i in range(0, len(country), 2)}
    print("India: ")
    InputOutput.speak("In India, ")
    InputOutput.PrintStr(f"Deaths: {res_dct['Deaths'][:7]}\n", 0.008)
    InputOutput.speak(
        f" the total number of deaths are {res_dct['Deaths'][:7]}")
    InputOutput.PrintStr(
        f"Confirmed cases: {res_dct['Confirmed cases']}\n", 0.008)
    InputOutput.speak(f" the Confirmed cases are {res_dct['Confirmed cases']}")
    InputOutput.PrintStr(
        f"Active cases: {res_dct['Active cases'][:8]}\n", 0.008)
    InputOutput.speak(f" Active cases are {res_dct['Active cases'][:8]}")
    InputOutput.PrintStr(f"Recovered: {res_dct['Recovered']}\n", 0.008)
    InputOutput.speak(f" Total patients Recovered are{res_dct['Recovered']}")
    print("--------------------------------------------------------------------")
    State_table = soup.find(
        'table', class_='wikitable plainrowheaders sortable')
    states = []
    for TRR in State_table.find_all('tr'):
        for THH in TRR.find_all('th'):
            if THH.get('scope') == 'row':
                states.append(THH.get_text())
                for TDD in TRR.find_all('td'):
                    b = TDD.get_text()
                    states.append(b)

    print("Maharashtra: ")
    InputOutput.speak("In Maharashtra, ")
    InputOutput.PrintStr(f"Deaths: {states[102]}", 0.008)
    InputOutput.speak(f" the total number of deaths are {states[102]}")
    InputOutput.PrintStr(f"Confirmed cases: {states[101]}", 0.008)
    InputOutput.speak(f" the Confirmed cases are {states[101]}")
    InputOutput.PrintStr(f"Active cases: {states[104]}", 0.008)
    InputOutput.speak(f" Active cases are {states[104]}")
    InputOutput.PrintStr(f"Recovered: {states[103]}", 0.008)
    InputOutput.speak(f" Total patients Recovered are {states[103]}")


def wikipediaSearch(query):
    InputOutput.speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    InputOutput.speak("wikipedia says,")
    InputOutput.speakPrint(results)
    InputOutput.speak(results)


def ageCalculate():
    currentDate = datetime.datetime.now()
    deadline = '11/03/2000'  # date of birth
    deadlineDate = datetime.datetime.strptime(deadline, '%m/%d/%Y')
    daysLeft = deadlineDate - currentDate
    years = ((daysLeft.total_seconds())/(365.242*24*3600))
    yearsInt = int(years)
    yearsStr = str(yearsInt).replace("-", "")
    months = (years-yearsInt)*12
    monthsInt = int(months)
    monthsStr = str(monthsInt).replace("-", "")
    days = (months-monthsInt)*(365.242/12)
    daysInt = int(days)
    daysStr = str(daysInt).replace("-", "")
    hours = (days-daysInt)*24
    hoursInt = int(hours)
    hoursStr = str(hoursInt).replace("-", "")
    minutes = (hours-hoursInt)*60
    minutesInt = int(minutes)
    minutesStr = str(minutesInt).replace("-", "")
    seconds = (minutes-minutesInt)*60
    secondsInt = int(seconds)
    secondsStr = str(secondsInt).replace("-", "")
    TotalDays = str(daysLeft).replace("-", "")
    InputOutput.speakPrint(
        f"You are {yearsStr} years {monthsStr} months {daysStr} days {hoursStr} hours {minutesStr} minutes {secondsStr} seconds old, sir. and Total Days Lived {TotalDays[:4]}")


def weather(query):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    URL = "https://google.com/search?q=%s" % query
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'lxml')
        results = []
        for g in soup.find_all('table'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                results.append(link)
    w_link = results[0]
    link = requests.get(w_link).text
    soup = BeautifulSoup(link, 'lxml')
    temprature = soup.find('span', class_='_3KcTQ').text
    Location = soup.find('h1', class_='_1Ayv3').text
    Today = soup.find('div', class_='_2xXSr').text
    hl = soup.find('div', class_='A4RQE').text
    fl = soup.find('span', class_='_2aogo').text
    wind = soup.find('span', class_='_1Va1P undefined').text
    sunrise = soup.find('p', class_='_2nwgx').text
    sunset = soup.find('div', class_='_2_gJb _2ATeV').text
    aqi = soup.find('text', class_='k2Z7I').text
    aqistatus = soup.find('span', class_='_1VMr2').text
    UHumidity = soup.find(
        'span', attrs={'data-testid': 'PercentageValue'}).text
    VisibilityValue = soup.find(
        'span', attrs={'data-testid': 'VisibilityValue'}).text
    uvindex = soup.find('span', attrs={'data-testid': 'UVIndexValue'}).text
    PressureValue = soup.find(
        'span', attrs={'data-testid': 'PressureValue'}).text
    Precipitation = None
    print("temprature       :", temprature)
    print("Location         :", Location)
    try:
        Precipitation = soup.find(
            'div', attrs={'data-testid': 'precipPhrase'}).text
        print("Precipitation    :", Precipitation)
    except AttributeError:
        pass
    finally:
        try:
            p = soup.find('div', class_='_2xXSr').text
            print("Now              :", p)
        except AttributeError:
            pass
    print("Air quality index:", aqi+" - "+aqistatus)
    print("Feels like       :", fl)
    print("Sunrise at       :", sunrise)
    print("Sunset at        :", sunset)
    print("High/Low         :", hl)
    print("wind             :", wind)
    print("Humidity         :", UHumidity)
    print("Pressure Value   :", PressureValue)
    print("UV index         :", uvindex)
    print("Visibility Value :", VisibilityValue)
    if Precipitation == None:
        InputOutput.speak(
            f"Right now it's {temprature} and {p}, Today there will be forcasted high of {hl[:2]}° and low of {hl[4:6]}°. Due to the current Humidity feels like it's {fl}.")
    else:
        InputOutput.speak(
            f"Right now it's {temprature} and {p}, Today there will be {Precipitation} with forcasted high of {hl[:2]}° and low of {hl[4:6]}°. Due to the current Humidity feels like it's {fl}.")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    sleep(2)


def GooglecalenderEvents(text):
    MONTHS = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    DAYS = ["monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"]
    DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def Authenticate_google():

        creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        return service

    def get_events(day, service):
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end_date = end_date.astimezone(utc)

        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            InputOutput.speak('No upcoming events found.')
        else:
            InputOutput.speak(f"You have {len(events)} events on this day.")

            for event in events:
                start = event['start'].get(
                    'dateTime', event['start'].get('date'))
                InputOutput.PrintStr(start + event['summary']+"\n", 0.001)
                # get the hour the event starts
                start_time = str(start.split("T")[1].split("-")[0])
                # if the event is in the morning
                if int(start_time.split(":")[0]) < 12:
                    start_time = start_time + "am"
                else:
                    # convert 24 hour time to regular
                    start_time = str(int(start_time.split(
                        ":")[0])-12) + start_time.split(":")[1]
                    start_time = start_time + "pm"

                InputOutput.speak(event["summary"] + " at " + start_time)

    def get_date(text):
        text = text.lower()
        today = datetime.date.today()

        if text.count("today") > 0:
            return today

        day = -1
        day_of_week = -1
        month = -1
        year = today.year

        for word in text.split():
            if word in MONTHS:
                month = MONTHS.index(word) + 1
            elif word in DAYS:
                day_of_week = DAYS.index(word)
            elif word.isdigit():
                day = int(word)
            else:
                for ext in DAY_EXTENTIONS:
                    found = word.find(ext)
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass

        # if the month mentioned is before the current month set the year to the next
        if month < today.month and month != -1:
            year = year+1

        # This is slighlty different from the video but the correct version
        if month == -1 and day != -1:  # if we didn't find a month, but we have a day
            if day < today.day:
                month = today.month + 1
            else:
                month = today.month

        # if we only found a dta of the week
        if month == -1 and day == -1 and day_of_week != -1:
            current_day_of_week = today.weekday()
            dif = day_of_week - current_day_of_week

            if dif < 0:
                dif += 7
                if text.count("next") >= 1:
                    dif += 7

            return today + datetime.timedelta(dif)

        if day != -1:
            return datetime.date(month=month, day=day, year=year)
    SERVICE = Authenticate_google()
    get_events(get_date(text), SERVICE)


def news_headline():
    InputOutput.speak("News for today.. Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=556d8fb464f44228afed3a43ce962c57"  # for india
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']

    for article in arts:
        InputOutput.speak(article['title'])
        print(article['title'])
        InputOutput.speak("next  is")

    InputOutput.speak("Thanks for listening...")


