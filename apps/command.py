import sys
sys.path.insert(1, '/apps')

import vk_api
import config
import datetime
import re
import time

from apps import keyboards
from apps import shedule
from apps import weather
from apps import data_base
from apps import data_lessons
from apps import timers
from apps import template
from apps import coronavirus
from apps import teach_or_not_teach
from apps import soothsayer

from apps.form_for_send_message import private_send_message

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#начальное сообщение ,которое отправляется после нажатия пользователем кнопки 'начать'
def msgstart(vk_session,user_id,msg,vk_api,vkapi,available_command): #действие которые выполняются после написания команды "начать"
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    user_name = data_base.information_user(vkapi,user_id)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyMenu") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, user_name + config.start_text, None, keyboards.keyMenu) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyMenuPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, user_name + config.start_text, None, keyboards.keyMenuPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'функционал'
def functional(vk_session,user_id,msg,vk_api,vkapi,available_command): 
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "keyMenu") #запись в БД клавиатуры котороя в данный момент у пользователя
    private_send_message(vk_session, user_id, config.functional, None, keyboards.keyMenu) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Коротко о карточках'
def briefly_about_cards(vk_session,user_id,msg,vk_api,available_command): 
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "keyCards") #запись в БД клавиатуры котороя в данный момент у пользователя
    private_send_message(vk_session, user_id, config.keycards, None, keyboards.keyCards) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение или изменения ,которые отправляются после команды 'на завтра','на сегодня'
def msgshedule(vk_session,user_id,msg,vk_api,available_command): #действие которые выполняются после написания команды "расписание"
    data_base.record_available_command(user_id,available_command)
    if msg == "на завтра" or msg == "На завтра": #завтра ли выбрал пользователь
        tomorrow = True
    else:
        tomorrow = False

    shedule.get_schedule(tomorrow) #получение и загрузка изменений,если они есть
    attachments = shedule.check_tomorrow(vk_session,vk_api,tomorrow) #получение изменений в виде картинке(если они есть)
    
    if tomorrow == True: # проверка завтра ли выбрал пользователь
        if attachments == None: #проверка на наличие изменений
            private_send_message(vk_session, user_id, config.shedule_tomorrow_True_text_if_not, None, None) #отправка личного сообщения
        else:
            private_send_message(vk_session, user_id, config.shedule_tomorrow_True_text_if_there_is, attachments, None) #отправка личного сообщения
    else:
        if attachments == None: #проверка на наличие изменений
            private_send_message(vk_session, user_id, config.shedule_tomorrow_False_text_if_not, None, None) #отправка личного сообщения
        else:
            private_send_message(vk_session, user_id, config.shedule_tomorrow_False_text_if_there_is, attachments, None) #отправка личного сообщения
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Погода'
def msgweather(vk_session,user_id,msg,vk_api,available_command): #действие которые выполняются после написания команды "погода"
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    temp, wind_speed, cloudiness = weather.get_weather() #получение состояния погоды
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyMenu") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "Температура: " + temp + "\n" + cloudiness + "\n" + "Скорость ветра: " + wind_speed +"м/с" , None, keyboards.keyMenu) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyMenuPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "Температура: " + temp + "\n" + cloudiness + "\n" + "Скорость ветра: " + wind_speed +"м/с" , None, keyboards.keyMenuPRO) #отправка личного сообщения

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение и изменение клавиатуры,которое отправляется после команды 'Важные даты'
def msgimportant_date(vk_session,user_id,msg,vk_api,available_command): #действие которые выполняются после написания команды "важные даты"
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyTimers") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "Самое главное⚠", None, keyboards.keyTimers) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyTimersPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "Самое главное⚠", None, keyboards.keyTimersPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды '⏰Таймер до ближайших каникул'
def timer_until_the_next_vacation(vk_session,user_id,msg,vk_api,available_command): #действие которые выполняются после написания команды "Таймер до ближайших каникул"
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyTimers")
        remained_until_holidays = timers.identification_holidays() #высчитывание ближайщий к настоящему моменту времени каникул
        private_send_message(vk_session, user_id, remained_until_holidays, None, keyboards.keyTimers) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyTimersPRO")
        remained_until_holidays = timers.identification_holidays() #высчитывание ближайщий к настоящему моменту времени каникул
        private_send_message(vk_session, user_id, remained_until_holidays, None, keyboards.keyTimersPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды '☀Таймер до лених каникул'
def the_countdown_till_summer_vacation(vk_session,user_id,msg,vk_api,available_command): #действие которые выполняются после написания команды "Таймер до лених каникул"
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyTimers")
        summer = timers.the_countdown_till_summer() #высчитывание времени до летних каникул
        private_send_message(vk_session, user_id, summer, None, keyboards.keyTimers) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyTimersPRO")
        summer = timers.the_countdown_till_summer() #высчитывание времени до летних каникул
        private_send_message(vk_session, user_id, summer, None, keyboards.keyTimersPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение и изменение клавиатуры ,которое отправляется после команды 'Назад'
def back(vk_session,user_id,msg,vk_api,available_command): #действие которые выполняются после написания команды "назад"
    keyboard = data_base.Back(user_id) #выбор клавиатура ,которая отправиться пользователю
    data_base.record_available_command(user_id,available_command)
    
    if keyboard == "Не доступно": # проверка возможен ли ход назад
        private_send_message(vk_session, user_id, "Не доступно\nP.S если у вас что то работает, то напишите 'Начать'", None, None) #отправка личного сообщения
    
    elif keyboard == "keyMenu" or keyboard == "keyMenuPRO":
        key = data_base.check_key(user_id)
        if key == "standart":
            private_send_message(vk_session, user_id, "Главное меню", None, keyboards.keyMenu) #отправка личного сообщения
        elif key == "pro":
            private_send_message(vk_session, user_id, "Главное меню", None, keyboards.keyMenuPRO) #отправка личного сообщения
    
    elif keyboard == "keySpecialPRO" or keyboard == "keySpecial":
        key = data_base.check_key(user_id)
        if key == "standart":
            private_send_message(vk_session, user_id, "⚠Особое", None, keyboards.keySpecial) #отправка личного сообщения
        elif key == "pro":
            private_send_message(vk_session, user_id, "⚠Особое", None, keyboards.keySpecialPRO) #отправка личного сообщения
    
    elif keyboard == "keySettingsPRO" or keyboard == "keySettings":
        key = data_base.check_key(user_id)
        if key == "standart":
            private_send_message(vk_session, user_id, "⚙Настройки", None, keyboards.keySettings) #отправка личного сообщения
        elif key == "pro":
            private_send_message(vk_session, user_id, "⚙Настройки", None, keyboards.keySettingsPRO) #отправка личного сообщения

    elif keyboard == "keyCards":
        private_send_message(vk_session, user_id, '🃏Карточки', None, keyboards.keyCards) #отправка личного сообщения
    
    elif keyboard == "keyGames":
        private_send_message(vk_session, user_id, '🕹Игры', None, keyboards.keyGames) #отправка личного сообщения
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Новости'
def notifications(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyMenu") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "Что бы получать новости нужно подписаться на них", None, keyboards.keySchoolnews) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyMenuPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "Что бы получать новости нужно подписаться на них", None, keyboards.keySchoolnews) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды '📋Изменения в расписании'
def keyShedule(vk_session,user_id,msg,vk_api,available_command):
    data_base.now_Keyboard(user_id,keyboard = "keyMenuPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
    private_send_message(vk_session, user_id, "Изменения в расписании...\n ", None, keyboards.keyShedule) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение и изменение клавиатуры, которое отправляется после команды 'Особое'
def special(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keySpecial") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "⚠Особое", None, keyboards.keySpecial) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keySpecialPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "⚠Особое", None, keyboards.keySpecialPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Короновирус'
def coronovirus(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keySpecial") #запись в БД клавиатуры котороя в данный момент у пользователя
        information = coronavirus.coronovirus()
        private_send_message(vk_session, user_id, information, None, keyboards.keySpecial) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keySpecialPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        information = coronavirus.coronovirus()
        private_send_message(vk_session, user_id, information, None, keyboards.keySpecialPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'О школе'
def information_about_the_school(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)

    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyMenu") #запись в БД клавиатуры котороя в данный момент у пользователя
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages(photos="images/school.jpg")[0]
        attachments = []
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
        private_send_message(vk_session, user_id, config.school_information , attachments, keyboards.keySchool_website) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyMenuPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages(photos="images/school.jpg")[0]
        attachments = []
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
        private_send_message(vk_session, user_id, config.school_information , attachments, keyboards.keySchool_websitePRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Настройки'
def settings(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)

    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keySettings") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "⚙Настройки", None, keyboards.keySettings) #отправка личного сообщения
    
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keySettingsPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "⚙Настройки", None, keyboards.keySettingsPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#сообщение ,которое отправляется после команды 'Настройки'
def customization(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)
    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyCustomization") #запись в БД клавиатуры котороя в данный момент у пользователя
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages(photos="images/PROkey.jpg")[0]
        attachments = []
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
        private_send_message(vk_session, user_id, config.customization, attachments, keyboards.keyCustomization) #отправка личного сообщения
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyCustomizationPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_messages(photos="images/PROkey.jpg")[0]
        attachments = []
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
        private_send_message(vk_session, user_id, config.customization, attachments, keyboards.keyCustomizationPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение и изменение режима клавиатуры,которое отправляется после команды 'PRO',"standart"
def keyCustomization(vk_session,user_id,msg,vk_api,key,available_command):
    answer = data_base.Customization(user_id,key)
    data_base.record_available_command(user_id,available_command)
    if key == "standart" and answer == "Standart режим установлен🎉🎊":
        data_base.now_Keyboard(user_id,keyboard = "keyMenu") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, answer, None, keyboards.keyMenu) #отправка личного сообщения
    elif key == "pro" and answer == "PRO режим установлен🎉🎊":
        data_base.now_Keyboard(user_id,keyboard = "keyMenuPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, answer, None, keyboards.keyMenuPRO) #отправка личного сообщения
    else:
        if key == "standart":
            data_base.now_Keyboard(user_id,keyboard = "keyCustomization")
            private_send_message(vk_session, user_id, answer, None, None) #отправка личного сообщения
        elif key == "pro":
            data_base.now_Keyboard(user_id,keyboard = "keyCustomizationPRO")
            private_send_message(vk_session, user_id, answer, None, None) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Карточки'
def cards(vk_session,user_id,msg,vk_api,available_command):
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "keyCards")
    private_send_message(vk_session, user_id, "🃏Карточки", None, keyboards.keyCards) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Проверить себя'
def check_Cards(vk_session,user_id,msg,vk_api,available_command):#действие которые выполняются после написания команды "Проверить себя"
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "check_Cards") #запись в БД клавиатуры котороя в данный момент у пользователя
    private_send_message(vk_session, user_id, "Выберите предмет по которому хотите проверить себя\n(т - ТЕСТ)", None, keyboards.check_Cards) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'Добавить карточку'
def record_Cards(vk_session,user_id,msg,vk_api,available_command):
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "record_Cards") #запись в БД клавиатуры котороя в данный момент у пользователя
    private_send_message(vk_session, user_id, "Выберите предмет по которому вы хотели бы запомнить ответ на вопрос", None, keyboards.record_Cards) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#исправление ошибок
def debugger1(vk_session,user_id,msg,vk_api,mistake):
    if mistake == "В данный момент это не возможно":
        private_send_message(vk_session, user_id, mistake, None, None) #отправка личного сообщения
    if mistake == "Вы пока не записали вопросов по этому предмету":
        private_send_message(vk_session, user_id, mistake, None, keyboards.check_Cards) #отправка личного сообщения
    if mistake == "cards":
        available_command = "avaible_standart"
        data_base.record_available_command(user_id,available_command)
        data_base.now_Keyboard(user_id,keyboard = "keyCards")
        private_send_message(vk_session, user_id, config.keycards, None, keyboards.keyCards) #отправка личного сообщения
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#исправление ошибок
def debugger2(user_id):
    sequence = data_base.getting_a_sequence(user_id)
    return sequence

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#удаление карточки
def delete_a_card(vk_session,user_id,LL_message):
    
    last_lesson = data_lessons.getting_last_lesson(user_id)
    if last_lesson != "None":
        if LL_message == "Следующая карточка":
            LL_message = last_lesson
            
    if LL_message == "тФизика" or LL_message == "тАнглийский" or LL_message == "тБиология" or LL_message == "тАлгебра" or LL_message == "тИстория" or LL_message == "тЛитература" or LL_message == "тМузыка" or LL_message == "тФизкультура" or LL_message == "тФранцузский" or LL_message == "тОбществознание" or LL_message == "тРусский" or LL_message == "тХимия":
        if LL_message == "тФизика":
            lesson = "physics"
        if LL_message == "тАнглийский":
            lesson = "English"
        if LL_message == "тБиология":
            lesson = "biology"
        if LL_message == "тАлгебра":
            lesson = "algebra"
        if LL_message == "тИстория":
            lesson = "history"
        if LL_message == "тЛитература":
            lesson = "literature"
        if LL_message == "тМузыка":
            lesson = "music"
        if LL_message == "тФизкультура":
            lesson = "physical_education"
        if LL_message == "тФранцузский":
            lesson = "French"
        if LL_message == "тОбществознание":
            lesson = "social_studies"
        if LL_message == "тРусский": 
            lesson = "Russian"
        if LL_message == "тХимия":
            lesson = "chemistry"
            
        answer = data_lessons.delete_a_card(user_id,lesson)
        private_send_message(vk_session, user_id, answer, None, keyboards.check_Cards) #отправка личного сообщения
    else:
        private_send_message(vk_session, user_id, "сейчас это недоступно", None, keyboards.check_Cards) #отправка личного сообщения


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#сообщение ,которое отправляется после команды '🎲Учить/Не учить'
def teach_or_not(vk_session,user_id,msg,vk_api,available_command):
    data_base.record_available_command(user_id,available_command)
    teach = teach_or_not_teach.teach_or_not_teach_random()
    private_send_message(vk_session, user_id, teach, None, None) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def next_card(vk_session,user_id,msg,vk_api,available_command,answer):
    data_base.record_available_command(user_id,available_command)
    if answer == "сейчас это недоступно":
        private_send_message(vk_session, user_id, "сейчас это недоступно", None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Идеи для реализации пока что не используется
def karusel(vk_session,user_id,msg,vk_api):
    private_send_message_karusel(vk_session, user_id, config.help4, template.template) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def send_weather_at_7am_for_user(vk_session,user_id,vk_api,temp, wind_speed, cloudiness):
    private_send_message(vk_session, user_id, "Температура: " + temp + "\n" + cloudiness + "\n" + "Скорость ветра: " + wind_speed +"м/с", None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def WeatherForUser(vk_session,user_id,msg,vk_api,available_command):
    key = data_base.check_key(user_id)
    data_base.record_available_command(user_id,available_command)

    if key == "standart":
        data_base.now_Keyboard(user_id,keyboard = "keyWeatherForUser") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "🌤Рассылка погоды", None, keyboards.keyWeatherForUser) #отправка личного сообщения
    
    elif key == "pro":
        data_base.now_Keyboard(user_id,keyboard = "keyWeatherForUserPRO") #запись в БД клавиатуры котороя в данный момент у пользователя
        private_send_message(vk_session, user_id, "🌤Рассылка погоды", None, keyboards.keyWeatherForUserPRO) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def delite_subscription_for_weather(vk_session,vk_api,user_id):
    key = data_base.check_key(user_id)
    

    with open('base_user_txt/user_weather.txt') as f:
        lines = f.readlines()

    user_id_weather = "id" + str(user_id)
    pattern = re.compile(re.escape(user_id_weather))

    msg_for_user = "Вы и так не подписаны 🤷‍♂"

    with open('base_user_txt/user_weather.txt', 'w') as f:
        
        for line in lines:
            result = pattern.search(line)

            if result is None:
                f.write(line)

            elif result is not None:
                msg_for_user = "Вы отписались ☹"

    
    private_send_message(vk_session, user_id, msg_for_user, None, None) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscription_for_weather(vk_session,vk_api,user_id):

    with open('base_user_txt/user_weather.txt') as f:
        lines = f.readlines()

    user_id_weather = "id" + str(user_id)
    pattern = re.compile(re.escape(user_id_weather))
    msg_for_user = None

    with open('base_user_txt/user_weather.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            f.write(line)
            if result is not None:
                msg_for_user = " Вы и так подписаны 🤷‍♂"
    
    if msg_for_user == None:

        with open('base_user_txt/user_weather.txt', 'a') as f:
            f.writelines(user_id_weather + "\n")
            f.close()

        msg_for_user = "Теперь вы подписаны на рассылку🎉🎊"
    
    private_send_message(vk_session, user_id, msg_for_user, None, None) #отправка личного сообщения

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def subscription_weather(vk_session,user_id,vk_api):
    private_send_message(vk_session, user_id, config.subscription_weather , None, None)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def keyGames(vk_session,user_id,vk_api):
    data_base.now_Keyboard(user_id,keyboard = "keyGames")
    private_send_message(vk_session, user_id, "🕹Игры" , None, keyboards.keyGames)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def keyKamen_Noznica_Bumaga(vk_session,user_id,vk_api,available_command):
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "keyKamen_Noznica_Bumaga")
    private_send_message(vk_session, user_id, "Вас приветствует игра под названием КАМЕНЬ НОЖНИЦЫ БУМАГА!!!\n\nДля начала игры выбирите за что вы будите играть" , None, keyboards.keyKamen_Noznica_Bumaga)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def msgKamen_Noznica_Bumaga(vk_session,user_id,vk_api,bot,answer):
    private_send_message(vk_session, user_id, "3!!!" , None, None)
    time.sleep(1)
    private_send_message(vk_session, user_id, "2!!!" , None, None)
    time.sleep(1)
    private_send_message(vk_session, user_id, "1!!!" , None, None)
    time.sleep(1)
    private_send_message(vk_session, user_id, "1 c половинкой!!!" , None, None)
    time.sleep(1)
    private_send_message(vk_session, user_id, "1 c паунтинкой!!!" , None, None)
    private_send_message(vk_session, user_id, bot , None, None)
    private_send_message(vk_session, user_id, answer , None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def keyGadalka(vk_session,user_id,vk_api,available_command):
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "keyGadalka")
    private_send_message(vk_session, user_id, "🔮Гадалка" , None, keyboards.keyGadalka)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def Gadalka_instrukcion(vk_session,user_id,vk_api):
    private_send_message(vk_session, user_id, "Напиши вопрос который тебе не дает покоя \n\nИ Я ВАСИЛИСА ПЕТРОВНА - ВЕЛИЧАЙЩАЯ ГАДАЛКА НА СИЕ ШАРЕ дам на него ответ!!!" , None, None)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def msgGadalka(vk_session,user_id,vk_api):
    answer = soothsayer.Gadalka_3000()
    private_send_message(vk_session, user_id, answer, None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def keyDoor(vk_session,user_id,vk_api,available_command):
    data_base.record_available_command(user_id,available_command)
    data_base.now_Keyboard(user_id,keyboard = "keyDoor")
    private_send_message(vk_session, user_id, "🚪Двери" , None, keyboards.keyDoor)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def msgDoor(vk_session,user_id,vk_api,event, lives_score):
    if lives_score is None :
        private_send_message(vk_session, user_id, event , None, None)
    else:
        private_send_message(vk_session, user_id, event + lives_score , None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def doorstart(vk_session,user_id,vk_api):
    private_send_message(vk_session, user_id, 'Новая игра' , None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def DoorScore(vk_session,user_id,vk_api,score):
    private_send_message(vk_session, user_id, 'Ваш счет: '  + str(score) , None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def DoorLives(vk_session,user_id,vk_api,lives):
    private_send_message(vk_session, user_id,"У вас осталось: " + str(lives) + " ❤" , None, None)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def Door_record(vk_session,user_id,vk_api,my_record):
    private_send_message(vk_session, user_id,"Ваш рекорд: " + str(my_record) + " баллов" , None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def Door_instrukcion(vk_session,user_id,vk_api):
    private_send_message(vk_session, user_id,"🚪Двери - это игра которая переносит тебя в подземелье в котором находится бесконечное количество комнат и из каждой есть по 3 выхода в следующую комнату, но не стоит радоваться, в каждой комнате ты можешь открыть лишь 1 дверь и обратного пути не будет, со старта у тебя есть 3 жизни, они обозначаются сердечками и проходя через каждую комнату ,не важно что в ней находилось тебе будет начисляться по 100 очков ,по окончанию игры максимальное значение твоих балов будет записано в 'Мой рекорд', если ты набрал очень много балов, то ты можешь поискать себя в списке лидеров, кто знает, вдруг ты стал мировым чемпионом по открыванию дверей 😉" , None, None)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def Board_liders_Door(vk_session,user_id,vk_api,leaders):

    private_send_message(vk_session, user_id,leaders , None, None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#CHAT command

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды 'таймер до лета'
def the_countdown_till_summer_chat(vkapi,chat_peer_id):
    summer = timers.the_countdown_till_summer()
    chat_send_message(vkapi,summer,chat_peer_id,None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды "команды"
def command_help_chat(vkapi,chat_peer_id):
    chat_send_message(vkapi,config.command_chat ,chat_peer_id,None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды "таймер до следующих каникул"
def identification_holidays_chat(vkapi,chat_peer_id):
    holidays = timers.identification_holidays()()
    chat_send_message(vkapi,holidays,chat_peer_id,None)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды "изменения на завтра"
def shedule_chat_tomorrow(vk_session,vk_api,vkapi,chat_peer_id):
    shedule.get_schedule(tomorrow=True)
    attachments = shedule.check_tomorrow(vk_session,vk_api,tomorrow=False)
    if attachments == None:
        chat_send_message(vkapi,config.shedule_tomorrow_True_text_if_not,chat_peer_id,None)
    else:
        chat_send_message(vkapi,config.shedule_tomorrow_True_text_if_there_is,chat_peer_id,attachments)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды "изменения на сегодня"
def shedule_chat_today(vk_session,vk_api,vkapi,chat_peer_id):
    shedule.get_schedule(tomorrow=False)
    attachments = shedule.check_tomorrow(vk_session,vk_api,tomorrow=False)
    if attachments == None:
        chat_send_message(vkapi,config.shedule_tomorrow_True_text_if_not,chat_peer_id,None)
    else:
        chat_send_message(vkapi,config.shedule_tomorrow_True_text_if_there_is,chat_peer_id,attachments)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#сообщение ,которое отправляется после команды "погода"
def msgweather_chat(vkapi,chat_peer_id): #действие которые выполняются после написания команды "погода"
    temp, wind_speed, cloudiness = weather.get_weather() #получение состояния погоды
    chat_send_message(vkapi, "Температура: " + temp + "\n" + cloudiness + "\n" + "Скорость ветра: " + wind_speed +"м/с" , chat_peer_id, None) #отправка личного сообщения
