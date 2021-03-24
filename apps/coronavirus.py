# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request





def coronovirus(): #парсинг с сайта стопкороновирус.рф

    url = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    convert = soup.findAll("div", {"class": "cv-countdown__item-value"})
    information = "ДАННЫЕ ПО РОССИИ \nПРЕДОСТАВЛЕНЫ САЙТОМ стопкоронавирус.рф\n"
    information += "\nПроведено тестов: " + convert[0].text
    information += "\nЗаболевших: " + convert[1].text
    information += "\nЗаболевших за сутки: " + convert[2].text
    information += "\nВыздоровело: " + convert[3].text
    information += "\nУмерло: " + convert[4].text
    return information
