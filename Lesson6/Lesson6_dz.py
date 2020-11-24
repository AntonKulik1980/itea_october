# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.


import requests
from bs4 import BeautifulSoup

from ip2geotools.databases.noncommercial import DbIpCity
import socket
#
# a= socket.gethostname()
# ip= str(socket.gethostbyname(a))
# response = DbIpCity.get('195.66.160.36', api_key='free')
# print(response)
#
# # 192.168.56.1

url='https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BF%D0%BE%D0%B4%D0%B3%D0%BE%D1%80%D0%B8%D1%86%D0%B0/2020-11-20'
page = requests.get(url)
print(page)
soup =  BeautifulSoup(page.content,'html.parser')

p1 = soup.findAll("div", {"class": "weather__content_tab-temperature"})
# soup.select('weather__article_main_temp')
print(p1)

# <div class="weather__article_main_temp">
# 			                        +13°<span>C</span></div>

# /html/body/div/div[4]/main/div[1]/div[2]/div/div/div[1]/div[3]/text()