# -*- coding: utf-8 -*-
from vk_api.utils import get_random_id #получение рандомного id

#форма для отправки сообщений пользователю (в личные сообщения)
def private_send_message(vk_session, user_id, msg, attachments, keyboard):
    vk_session.method('messages.send', {'user_id': user_id,
                                        'random_id': get_random_id(),
                                        'message': msg,
                                        'attachment': attachments,
                                        'keyboard': keyboard})

#форма для отправки сообщений пользователю (в личные сообщения)
def private_send_message_karusel(vk_session, user_id, msg, template):
    vk_session.method('messages.send', {'user_id': user_id,
                                        'random_id': get_random_id(),
                                        'message': msg,
                                        'template': template})

#форма для отправки сообщений пользователю (в беседы)
def chat_send_message(vkapi,msg,peer_id,attachment):
    vkapi.messages.send(
                random_id   =   get_random_id(),
                peer_id     =   peer_id,
                message     =   msg,
                attachment  =   attachment
                )