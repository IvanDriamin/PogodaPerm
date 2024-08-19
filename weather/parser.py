from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/perm?lat=58.018558&lon=56.282341'
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
mas = []
dict = []
tempDay1 = bs.find('div', 'temp forecast-briefly__temp forecast-briefly__temp_day')
mas.append(tempDay1.text)
tempDay2 = bs.find('div', 'temp forecast-briefly__temp forecast-briefly__temp_day')
mas.append(tempDay2.text)
tempDay3 = bs.find('div', 'temp forecast-briefly__temp forecast-briefly__temp_day')
mas.append(tempDay3.text)
#mas.append(bs.find('', '')) #tempDay3
#mas.append(bs.find('', '')) #tempDay4
#mas.append(bs.find('', '')) #tempDay5
#mas.append(bs.find('', '')) #tempDay6
#mas.append(bs.find('', '')) #tempDay7

#mas.append(bs.find('', '')) #tempNight1
#mas.append(bs.find('', '')) #tempNight2
#mas.append(bs.find('', '')) #tempNight3
#mas.append(bs.find('', '')) #tempNight4
#mas.append(bs.find('', '')) #tempNight5
#mas.append(bs.find('', '')) #tempNight6
#mas.append(bs.find('', '')) #tempNight7

#mas.append(bs.find('', '')) #humidity1
#mas.append(bs.find('', '')) #humidity2
#mas.append(bs.find('', '')) #humidity3
#mas.append(bs.find('', '')) #humidity4
#mas.append(bs.find('', '')) #humidity5
#mas.append(bs.find('', '')) #humidity6
#mas.append(bs.find('', '')) #humidity7

#mas.append(bs.find('', '')) #windSpeed1
#mas.append(bs.find('', '')) #windSpeed2
#mas.append(bs.find('', '')) #windSpeed3
#mas.append(bs.find('', '')) #windSpeed4
#mas.append(bs.find('', '')) #windSpeed5
#mas.append(bs.find('', '')) #windSpeed6
#mas.append(bs.find('', '')) #windSpeed7

#mas.append(bs.find('', '')) #pressure1
#mas.append(bs.find('', '')) #pressure2
#mas.append(bs.find('', '')) #pressure3
#mas.append(bs.find('', '')) #pressure4
#mas.append(bs.find('', '')) #pressure5
#mas.append(bs.find('', '')) #pressure6
#mas.append(bs.find('', '')) #pressure7

#mas.append(bs.find('', '')) #weatherDay1
#mas.append(bs.find('', '')) #weatherDay2
#mas.append(bs.find('', '')) #weatherDay3
#mas.append(bs.find('', '')) #weatherDay4
#mas.append(bs.find('', '')) #weatherDay5
#mas.append(bs.find('', '')) #weatherDay6
#mas.append(bs.find('', '')) #weatherDay7

#mas.append(bs.find('', '')) #weatherNight1
#mas.append(bs.find('', '')) #weatherNight2
#mas.append(bs.find('', '')) #weatherNight3
#mas.append(bs.find('', '')) #weatherNight4
#mas.append(bs.find('', '')) #weatherNight5
#mas.append(bs.find('', '')) #weatherNight6
#mas.append(bs.find('', '')) #weatherNight7

#mas.append(bs.find('', '')) #windDirection1
#mas.append(bs.find('', '')) #windDirection2
#mas.append(bs.find('', '')) #windDirection3
#mas.append(bs.find('', '')) #windDirection4
#mas.append(bs.find('', '')) #windDirection5
#mas.append(bs.find('', '')) #windDirection6
#mas.append(bs.find('', '')) #windDirection7
mas.append(333)
i = 0
while mas[i] != 333:
    print(mas[i])
    i += 1
j = 0
