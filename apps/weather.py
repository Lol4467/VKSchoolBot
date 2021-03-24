# -*- coding: utf-8 -*-

import sys
import config
import urllib.request
from bs4 import BeautifulSoup

sys.path.insert(1, '/apps')


def get_weather():  # "погода"
    html = urllib.request.urlopen('https://yandex.ru/weather/'+config.city)  # парсировка сайта с погодой (yandex)
    soup = BeautifulSoup(html, "html.parser")

    # получение температура
    temp = soup.find('div', class_='fact__hour-temp').get_text().encode('utf-8').decode('utf-8', 'ignore')
    try:
        # получение скорости ветра
        wind_speed = soup.find('span', class_='wind-speed').get_text().encode('utf-8').decode('utf-8', 'ignore')
    except BaseException:
        wind_speed = "0 "

    # получение состояния погоды в целом
    cloudiness = soup.find('div', class_='link__condition day-anchor i-bem').\
        get_text().encode('utf-8').decode('utf-8', 'ignore')

    # добовление смайлика для дикорации
    if cloudiness == "Облачно с прояснениями":
        cloudiness += "&#9925;"  # смайлик облоко с солнышком
    elif cloudiness == "Ясно":
        cloudiness += "&#9728;"  # смайлик солнце
    elif cloudiness == "Малооблачно":
        cloudiness += "&#127780;"  # смайлик солнце с облочком
    elif cloudiness == "Пасмурно":
        cloudiness += "&#9729;"  # смайлик облоко
    elif cloudiness == "Дождь" or cloudiness == "Небольшой дождь":
        cloudiness += "&#127783;"  # смайлик тучка с дождем
    
    return temp, wind_speed, cloudiness

