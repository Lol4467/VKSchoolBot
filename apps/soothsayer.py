# -*- coding: utf-8 -*-

import random


def Gadalka_3000():
# Инициализируем возможные ответы
    answers = '''Абсолютно точно!
Да
Нет
Скорее да, чем нет
Не уверена...
Однозначно нет!
Если ты не фанат аниме, у тебя все получится!
Можешь быть уверен в этом
Перспективы не очень хорошие
А как же иначе?
Да, но если только ты не смотришь аниме
Знаки говорят — «да»
Не знаю
Мой ответ — «нет»
Весьма сомнительно
Не могу дать точный ответ
'''.splitlines()



    answer = "🔮" + random.choice(answers)
    return answer
