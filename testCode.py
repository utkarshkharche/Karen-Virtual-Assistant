import urllib
import requests
from bs4 import BeautifulSoup
query="datala maharashtra weather"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
URL="https://google.com/search?q=%s" % query
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
# print(results)
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
aqi=soup.find('text',class_ ='k2Z7I').text
aqistatus = soup.find('span', class_='_1VMr2').text
UHumidity=soup.find('span',attrs={'data-testid':'PercentageValue'}).text
VisibilityValue=soup.find('span',attrs={'data-testid':'VisibilityValue'}).text
uvindex=soup.find('span',attrs={'data-testid':'UVIndexValue'}).text
PressureValue=soup.find('span',attrs={'data-testid':'PressureValue'}).text
Precipitation=None
print("temprature       :",temprature)
print("Location         :",Location)
try:
    Precipitation = soup.find('div', attrs={'data-testid':'precipPhrase'}).text
    print("Precipitation    :",Precipitation)
except AttributeError:
    pass
finally:
    try:
        p=soup.find('div',class_='_2xXSr').text
        print("Now              :",p)
    except AttributeError:
        pass
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
if Precipitation==None:
    print(f"Right now it's {temprature} and {p}, Today there will be forcasted high of {hl[:2]}° and low of {hl[4:6]}°. Due to the current Humidity feels like it's {fl}.")
else:
    print(f"Right now it's {temprature} and {p}, Today there will be {Precipitation} with forcasted high of {hl[:2]}° and low of {hl[4:6]}°. Due to the current Humidity feels like it's {fl}.")


