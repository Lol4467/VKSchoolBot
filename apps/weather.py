# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '/apps')

import urllib.request #импортирование модуля для парсинга
from bs4 import BeautifulSoup #тоже для парсинга

import config #импортирование настроек для бота
import datetime
import re


def get_weather(): #действие которые выполняются после написания команды "погода"
    html = urllib.request.urlopen('https://yandex.ru/weather/'+config.city) #парсировка сайта с погодой (yandex)
    soup = BeautifulSoup(html, "html.parser")

    temp =  soup.find('div', class_='fact__hour-temp').get_text().encode('utf-8').decode('utf-8', 'ignore') #получение температура на данный момент
    try:
        wind_speed = soup.find('span', class_='wind-speed').get_text().encode('utf-8').decode('utf-8', 'ignore') #получение скорости ветра на данный момент
    except BaseException:
        wind_speed = "0 "
    cloudiness =  soup.find('div', class_='link__condition day-anchor i-bem').get_text().encode('utf-8').decode('utf-8', 'ignore') #получение состояния погоды в целом на данный момент

    
    #добовление к строчке о погоде в целом смайлика для дикорации
    if cloudiness == "Облачно с прояснениями":
        cloudiness += "&#9925;" #смайлик облоко с солнышком
    elif cloudiness == "Ясно":
        cloudiness += "&#9728;" #смайлик солнце
    elif cloudiness == "Малооблачно":
        cloudiness += "&#127780;" #смайлик солнце с облочком
    elif cloudiness == "Пасмурно":
        cloudiness += "&#9729;" #смайлик облоко
    elif cloudiness == "Дождь" or cloudiness == "Небольшой дождь":
        cloudiness += "&#127783;" #смайлик тучка с дождем
    
    return temp, wind_speed, cloudiness #возвращение температуры,скорости ветра и общего состояния погоды

