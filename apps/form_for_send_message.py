# -*- coding: utf-8 -*-
from vk_api.utils import get_random_id


def private_send_message(vk_session, user_id, msg, attachments, keyboard):
    vk_session.method('messages.send', {'user_id': user_id,
                                        'random_id': get_random_id(),
                                        'message': msg,
                                        'attachment': attachments,
                                        'keyboard': keyboard})
