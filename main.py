# -*- coding: utf-8 -*-

import sys
sys.path.insert(1, '/apps')


import vk_api #импортирование vk_api
import  subprocess

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType #получение лонгпола и получение событий
from vk_api.utils import get_random_id #получение случайного id

from apps.form_for_send_message import private_send_message  #получение формы для отправки личного сообщения
from apps.response_form import private_message  #полчение ответа на определенное сообщение


#import config # импортирование настроек для бота
#import keyboards # импортирование клавиатур для разных событий
#import data_base # импортирование БД
from apps import keyboards,data_base
import config

#параметры token и group_id изменяются в файле config.py
vk_session = vk_api.VkApi(token=config.token) # получение vk_session
longpoll = VkBotLongPoll(vk_session, config.group_id) # получение longpoll
vkapi = vk_session.get_api() # получение vkapi

#subprocess.Popen(['python3', 'send_weather_at_7am.py'])

for event in longpoll.listen(): #прослушка лонгпола

    if event.type == VkBotEventType.MESSAGE_NEW and event.from_user: #проверка пришло ли личное сообщенеи от пользователя
        
        L_message , LL_message , LLL_message= data_base.main_loop(event.obj.from_id, event.obj.text,vkapi) #получение прошлого и позопрошлого сообщения
        private_message(vk_session,event.obj.from_id, event.obj.text,vk_api,vkapi,L_message,LL_message,LLL_message) #отправка личного сообщения
    

    elif event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        try:
            chatbot(vk_session,vk_api,event.object.text.lower(),vkapi,event.obj.peer_id)
        except BaseException:
            print("какая то ошибка")
            
    elif event.type == VkBotEventType.GROUP_JOIN: #проверка вступил ли пользоваттель в группу
        try:
            private_send_message(vk_session, event.obj.user_id, config.welcome_text, None, None) #отправка личного сообщения
        except BaseException:
            print("какая то ошибка")
                    
    elif event.type == VkBotEventType.GROUP_LEAVE: #проверка вышел ли пользователь из группы
        try:
            private_send_message(vk_session, event.obj.user_id, config.goodbye_text, None, None) #отправка личного сообщения
        except BaseException:
            print("какая то ошибка")
    