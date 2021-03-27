# -*- coding: utf-8 -*-

import config
import vk_api
import sys

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from apps.form_for_send_message import private_send_message
from apps.response_form import private_message
from apps import data_base

sys.path.insert(1, '/apps')

vk_session = vk_api.VkApi(token=config.token)
longpoll = VkBotLongPoll(vk_session, config.group_id)
vkapi = vk_session.get_api()

for event in longpoll.listen():  # проверка на наличие событий
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:

        L_message = data_base.main_loop(event.obj.from_id, vkapi, event.obj.text.lower())
        private_message(vk_session, event.obj.from_id, event.obj.text.lower(), vk_api, vkapi, L_message)
            
    elif event.type == VkBotEventType.GROUP_JOIN:
        private_send_message(vk_session, event.obj.user_id, config.welcome_text, None, None)

