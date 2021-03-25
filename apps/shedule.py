# -*- coding: utf-8 -*-
import datetime
import os
import os.path
import wget
import urllib.request as urllib2

from pdf2image import convert_from_path


def get_schedule(tomorrow):
    
    # получение настоящего времени
    now = datetime.datetime.now()
    year = now.year 
    mounth = now.month 
    day = now.day
    
    # преобразований данных для создание ссылки
    if mounth == 1: 
        mounth = "January"
    elif mounth == 2: 
        mounth = "February"
    elif mounth == 3: 
        mounth = "March"
    elif mounth == 4: 
        mounth = "April"
    elif mounth == 5: 
        mounth = "May"
    elif mounth == 6: 
        mounth = "June"
    elif mounth == 7: 
        mounth = "July"
    elif mounth == 8: 
        mounth = "August"
    elif mounth == 9: 
        mounth = "September"
    elif mounth == 10: 
        mounth = "October"
    elif mounth == 11: 
        mounth = "November"
    elif mounth == 12: 
        mounth = "December"
    
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
    url = ("https://sevgym14.ru/raspisanie_" + str(year - 1) + "_" + str(year) + "_" + str(now.month) + ".pdf")

    try:
        r = urllib2.urlopen(url)
    except urllib2.URLError as e:
        r = e
    if r.code in (200, 401) and not \
            os.path.exists("shedule/raspisanie_" + str(year - 1) + "_" + str(year) + "_" + str(now.month) + ".pdf"):

        wget.download(url, "shedule")  # скачивание pdf

        pages = convert_from_path("shedule/raspisanie_" + str(year - 1) + "_" + str(year) + "_" + str(now.month) + ".pdf", 500)
        for page in pages:
            page.save('shedule/out.jpg', 'JPEG')


def check_tomorrow(vk_session, vk_api, tomorrow):  # проверка того,что выбрал пользователь
    if tomorrow:
        day = "tomorrow"
    else:
        day = "today"

    if os.path.exists(r'shedule/' + day + '/shedule.jpg'):  # проверка на наличие фотографии

        # загрузка фото во ВК
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages(photos="shedule/" + day + "/shedule.jpg")[0]
        attachments = []
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

        path = r'shedule/' + day + '/shedule.jpg'  # удаление фото с изменениями из папки
        os.remove(path)
        return attachments 
