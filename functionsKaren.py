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


def wikipediaSearch():
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


def weather(quary):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    URL="https://google.com/search?q=%s" % quary
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content,'lxml')
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
    Precipitation = soup.find('div', class_='RBVJT').text
    fl = soup.find('span', class_='_2aogo').text
    wind = soup.find('span', class_='_1Va1P undefined').text
    sunrise = soup.find('p', class_='_2nwgx').text
    sunset = soup.find('div', class_='_2_gJb _2ATeV').text
    aqi=soup.find('text',class_ ='k2Z7I').text
    aqistatus = soup.find('span', class_='_1VMr2').text
    UHumidity=soup.find('span',attrs={'data-testid':'PercentageValue'}).text
    VisibilityValue=soup.find('span',attrs={'data-testid':'VisibilityValue'}).text
    uvindex=soup.find('span',attrs={'data-testid':'UVIndexValue'}).text
    PressureValue=soup.find('span',attrs={'data-testid':'PressureValue'}).text

    print("temprature       :",temprature)
    print("Location         :",Location)
    print("Today            :",Today)
    print("Precipitation    :",Precipitation)
    print("Air quality index:",aqi+" - "+aqistatus)
    print("Feels like       :", fl)
    print("Sunrise at       :", sunrise)
    print("Sunset at        :", sunset)
    print("High/Low         :",hl)
    print("wind             :", wind)
    print("Humidity         :",UHumidity)
    print("Pressure Value   :",PressureValue)
    print("UV index         :",uvindex)
    print("Visibility Value :",VisibilityValue)
    InputOutput.speak(f"Right now it's {temprature} and {Today}, Today there will be {Precipitation} with forcasted high of {hl[:2]}° and low of {hl[4:6]}°. Due to the current Humidity feels like it's {fl}.")
