# -*- coding: utf-8 -*-
import datetime
import os
import os.path
import wget
import urllib.request as urllib2
from pdf2image import convert_from_path, convert_from_bytes
import requests
import fitz

def get_schedule(tomorrow):
    
    # получение настоящего времени
    now = datetime.datetime.now()
    year = now.year 
    mounth = now.month 
    day = now.day


    # преобразований данных для создание ссылки
    if mounth == 1: 
        mounth = "january"
    elif mounth == 2: 
        mounth = "february"
    elif mounth == 3: 
        mounth = "march"
    elif mounth == 4: 
        mounth = "april"
    elif mounth == 5: 
        mounth = "may"
    elif mounth == 6: 
        mounth = "june"
    elif mounth == 7: 
        mounth = "july"
    elif mounth == 8: 
        mounth = "august"
    elif mounth == 9: 
        mounth = "september"
    elif mounth == 10: 
        mounth = "october"
    elif mounth == 11: 
        mounth = "november"
    elif mounth == 12: 
        mounth = "december"
    
    if now.month < 10:
        mounth0 = "0" + str(now.month)
    else:
        mounth0 = str(now.month)

    if tomorrow:
        day = day + 1 
        if day < 10:
            day = "0" + str(day)
        day = str(day)
    else:
        if day < 10:
            day = "0" + str(day)
        day = str(day)

    # составление ссылки # поправить после каникул
    url = ("https://sevgym14.ru/" + mounth + "_" + str(year) + "/" + day + "_" + mounth0 + "_rasp.pdf")

    try:
        r = urllib2.urlopen(url)

    except urllib2.URLError as e:
        r = e

    if os.path.exists('shedule/' + day + '/shedule.pdf'):
        os.remove('shedule/' + day + '/shedule.pdf')
        print(1)

    if r.code in (200, 401):

        if tomorrow:
            wget.download(url, "shedule/tomorrow")  # скачивание pdf
            os.rename("shedule/tomorrow/" + day + "_" + mounth0 + "_rasp.pdf", "shedule/tomorrow/shedule.pdf")
        else:
            wget.download(url, "shedule/today")  # скачивание pdf
            os.rename("shedule/today" + day + "_" + mounth0 + "_rasp.pdf", "shedule/tomorrow/shedule.pdf")

        #os.path.exists("shedule/raspisanie_" + str(year - 1) + "_" + str(year) + "_" + str(now.month) + ".pdf")
        #images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())


def check_tomorrow(vk_session, vk_api, tomorrow):  # проверка того,что выбрал пользователь
    if tomorrow:
        day = "tomorrow"
    else:
        day = "today"

    if os.path.exists(r'shedule/' + day + '/shedule.pdf'):  # проверка на наличие фотографии

        pdffile = 'shedule/' + day + '/shedule.pdf'

        with fitz.open(pdffile) as doc:
            page = doc.loadPage(0)  # number of page
            pix = page.getPixmap()
            output = 'shedule/' + day + '/shedule.jpg'
            pix.writePNG(output)

        # загрузка фото во ВК
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages(photos="shedule/" + day + "/shedule.jpg")[0]
        attachments = []
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

        path1 = r'shedule/' + day + '/shedule.jpg'  # удаление фото с изменениями из папки
        os.remove(path1)

        path2 = r'shedule/' + day + '/shedule.pdf'  # удаление фото с изменениями из папки
        os.remove(path2)

        return attachments

