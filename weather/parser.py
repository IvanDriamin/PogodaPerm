from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/perm?lat=58.018558&lon=56.282341'
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
mas = []
dict = []
mas.append(bs.find('span', 'temp__value temp__value_with-unit')) #tempDay1
mas.append(bs.find('strong', 'forecast-details__day-number')) #tempDay2
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

#dict.append(bs.find('', '')) #weatherDay1
#dict.append(bs.find('', '')) #weatherDay2
#dict.append(bs.find('', '')) #weatherDay3
#dict.append(bs.find('', '')) #weatherDay4
#dict.append(bs.find('', '')) #weatherDay5
#dict.append(bs.find('', '')) #weatherDay6
#dict.append(bs.find('', '')) #weatherDay7

#dict.append(bs.find('', '')) #weatherNight1
#dict.append(bs.find('', '')) #weatherNight2
#dict.append(bs.find('', '')) #weatherNight3
#dict.append(bs.find('', '')) #weatherNight4
#dict.append(bs.find('', '')) #weatherNight5
#dict.append(bs.find('', '')) #weatherNight6
#dict.append(bs.find('', '')) #weatherNight7

#dict.append(bs.find('', '')) #windDirection1
#dict.append(bs.find('', '')) #windDirection2
#dict.append(bs.find('', '')) #windDirection3
#dict.append(bs.find('', '')) #windDirection4
#dict.append(bs.find('', '')) #windDirection5
#dict.append(bs.find('', '')) #windDirection6
#dict.append(bs.find('', '')) #windDirection7
mas.append(333)
dict.append("CLOSED")
i = 0
while mas[i] != 333:
    print(mas[i])
    i += 1
j = 0
while dict[j] != "CLOSED":
    print(dict[j])
    j += 1
