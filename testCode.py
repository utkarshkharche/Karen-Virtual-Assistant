import urllib
import requests
from bs4 import BeautifulSoup
#enter location here in query
query="weather banglore"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
URL="https://google.com/search?q=%s" % query
#  URL = "https://www.google.com/search?source=hp&ei=siBgX_i3C-qf4-EPw9mruAU&q=weather+report&oq=whth&gs_lcp=CgZwc3ktYWIQARgFMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKOgIIADoICAAQsQMQgwE6BQgAELEDOgUILhCxAzoHCAAQsQMQClCYEFimL2CyWmgAcAB4AIABmgGIAcgEkgEDMC40mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab#spf=1600135358332"
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
temprature = soup.find('span', class_='_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--tempValue--3KcTQ').text
Location = soup.find('h1', class_='_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--location--1Ayv3').text
Today = soup.find('div', class_='_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--2xXSr').text
hl = soup.find('div', class_='_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--tempHiLoValue--A4RQE').text
Precipitation = soup.find('div', class_='_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--precipValue--RBVJT').text
Precipitation = soup.find('div', class_='_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--precipValue--RBVJT').text
fl = soup.find('span', class_='_-_-node_modules-@wxu-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2aogo').text
wind = soup.find('span', class_='_-_-node_modules-@wxu-components-src-atom-WeatherData-Wind-Wind--windWrapper--1Va1P undefined').text
sunrise = soup.find('div', class_='_-_-node_modules-@wxu-components-src-molecule-SunriseSunset-SunriseSunset--sunriseDateItem--2ATeV').text
sunset = soup.find('div', class_='_-_-node_modules-@wxu-components-src-molecule-SunriseSunset-SunriseSunset--sunsetDateItem--2_gJb _-_-node_modules-@wxu-components-src-molecule-SunriseSunset-SunriseSunset--sunriseDateItem--2ATeV').text
aqi=soup.find('text',class_ ='_-_-node_modules-@wxu-components-src-molecule-DonutChart-DonutChart--innerValue--k2Z7I').text
aqistatus = soup.find('span', class_='_-_-node_modules-@wxu-components-src-molecule-AirQualityText-AirQualityText--severity--1VMr2').text
Humidity=soup.find('div', class_='_-_-node_modules-@wxu-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--23DP5')
print("temprature       :",temprature)
print("Location         :",Location)
print("Today            :",Today)
print("High/Low         :",hl)
print("Precipitation    :",Precipitation)
print("Feels like       :", fl)
print("wind             :", wind)
for i in Humidity:
    for j in soup.find('span', attrs={'data-testid': 'PercentageValue'}):
        print("Humidity         :", j)
        break
    break
print("Sunrise at       :", sunrise)
print("Sunset at        :", sunset)
print("Air quality index:",aqi+" - "+aqistatus)
print(hl[:2])
print(hl[3:5])