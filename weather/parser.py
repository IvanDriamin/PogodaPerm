from bs4 import BeautifulSoup
import requests

url = 'https://yandex.ru/pogoda/perm?lat=58.018558&lon=56.282341'
response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
mas = []
mas.append(temp1 = bs.find('span', 'temp__value temp__value_with-unit'))
mas.append(temp2 = bs.find('', ''))
mas.append(temp3 = bs.find('', ''))
mas.append(temp4 = bs.find('', ''))
mas.append(temp5 = bs.find('', ''))
mas.append(temp6 = bs.find('', ''))
mas.append(temp7 = bs.find('', ''))
print(mas[0].text)