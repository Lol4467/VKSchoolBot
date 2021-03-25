import sys

from apps import keyboards
from apps import data_base

from apps.form_for_send_message import private_send_message

sys.path.insert(1, '/apps')


def start(vk_session, user_id, vkapi):  # "начать"
    import config

    user_name = data_base.information_user(vkapi, user_id)

    data_base.now_Keyboard(user_id, keyboard="keyMenu")  # запись в БД клавиатуру пользователя
    private_send_message(vk_session, user_id, user_name + config.start_text, None, keyboards.keyMenu)


def message_shedule(vk_session, user_id, msg, vk_api):  # 'на завтра', 'на сегодня'
    from apps import shedule
    import config

    tomorrow = False
    if msg == "на завтра":
        tomorrow = True

    shedule.get_schedule(tomorrow)  # получение и загрузка изменений
    attachments = shedule.check_tomorrow(vk_session, vk_api, tomorrow)  # получение изменений в виде картинке
    
    if tomorrow:
        if attachments == None:  # проверка на наличие изменений
            private_send_message(vk_session, user_id, config.shedule_tomorrow_True_text_if_not, None, None)
        else:
            private_send_message(vk_session, user_id, config.shedule_tomorrow_True_text_if_there_is, attachments, None)
    else:
        if attachments == None:
            private_send_message(vk_session, user_id, config.shedule_tomorrow_False_text_if_not, None, None)
        else:
            private_send_message(vk_session, user_id, config.shedule_tomorrow_False_text_if_there_is, attachments, None)


def message_weather(vk_session, user_id):  # 'Погода'
    from apps import weather

    temp, wind_speed, cloudiness = weather.get_weather()  # получение состояния погоды

    data_base.now_Keyboard(user_id, keyboard="keyMenu")
    private_send_message(vk_session, user_id, "Температура: " + temp + "\n" + cloudiness + "\n" + "Скорость ветра: "
                         + wind_speed + "м/с", None, keyboards.keyMenu)


def message_important_date(vk_session, user_id):  # 'Важные даты'

    data_base.now_Keyboard(user_id, keyboard="keyTimers")
    private_send_message(vk_session, user_id, "Самое главное⚠", None, keyboards.keyTimers)


def timer_until_the_next_vacation(vk_session, user_id):  # '⏰Таймер до ближайших каникул'
    from apps import timers

    data_base.now_Keyboard(user_id, keyboard="keyTimers")
    remained_until_holidays = timers.identification_holidays()  # поиск ближайщих каникул
    private_send_message(vk_session, user_id, remained_until_holidays, None, keyboards.keyTimers)


def the_countdown_till_summer_vacation(vk_session, user_id):  # '☀Таймер до лених каникул'
    from apps import timers

    data_base.now_Keyboard(user_id, keyboard="keyTimers")
    summer = timers.the_countdown_till_summer()  # высчитывание времени до летних каникул
    private_send_message(vk_session, user_id, summer, None, keyboards.keyTimers)


def back(vk_session, user_id, available_command):  # 'Назад'
    keyboard = data_base.Back(user_id)  # выбор клавиатура, которая отправиться пользователю
    data_base.record_available_command(user_id, "avaible_standart")

    if keyboard == "Не доступно":  # проверка возможен ли ход назад
        private_send_message(vk_session, user_id, "Не доступно\nP.S если у вас что то работает, то напишите 'Начать'",
                             None, None)
    
    elif keyboard == "keyMenu":
        private_send_message(vk_session, user_id, "Главное меню", None, keyboards.keyMenu)
    
    elif keyboard == "keySpecial":
        private_send_message(vk_session, user_id, "⚠Особое", None, keyboards.keySpecial)
    
    elif keyboard == "keyGames":
        private_send_message(vk_session, user_id, '🕹Игры', None, keyboards.keyGames)


def notifications(vk_session, user_id):  # "📰новости школы"

    data_base.now_Keyboard(user_id, keyboard="keyMenu")
    private_send_message(vk_session, user_id,
                         "Что бы получать новости нужно подписаться на них", None, keyboards.keySchoolnews)


def keyShedule(vk_session, user_id):  # '📋Изменения в расписании'

    data_base.now_Keyboard(user_id, keyboard="keyMenuPRO")
    private_send_message(vk_session, user_id, "Изменения в расписании...\n ", None, keyboards.keyShedule)


def special(vk_session, user_id):  # "Особое"

    data_base.now_Keyboard(user_id, keyboard="keySpecial")
    private_send_message(vk_session, user_id, "⚠Особое", None, keyboards.keySpecial)


def coronovirus(vk_session, user_id):  # "Короновирус"
    import requests
    from bs4 import BeautifulSoup

    url = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    convert = soup.findAll("div", {"class": "cv-countdown__item-value"})
    information = "ДАННЫЕ ПО РОССИИ \nПРЕДОСТАВЛЕНЫ САЙТОМ стопкоронавирус.рф\n"
    information += "\nПроведено тестов: " + convert[0].text
    information += "\nЗаболевших: " + convert[1].text
    information += "\nЗаболевших за сутки: " + convert[2].text
    information += "\nВыздоровело: " + convert[3].text
    information += "\nУмерло: " + convert[4].text

    data_base.now_Keyboard(user_id, keyboard="keySpecial")
    private_send_message(vk_session, user_id, information, None, keyboards.keySpecial)


def information_about_the_school(vk_session, user_id, vk_api):  # "О школе"
    import config
    attachments = []

    data_base.now_Keyboard(user_id, keyboard="keyMenu")
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_messages(photos="images/school.jpg")[0]
    attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
    private_send_message(vk_session, user_id, config.school_information, attachments, keyboards.keySchool_website)


def keyGames(vk_session, user_id):
    data_base.now_Keyboard(user_id, keyboard="keyGames")
    private_send_message(vk_session, user_id, "🕹Игры", None, keyboards.keyGames)


def keyKamen_Noznica_Bumaga(vk_session, user_id, available_command):
    data_base.record_available_command(user_id, available_command)
    data_base.now_Keyboard(user_id, keyboard="keyKamen_Noznica_Bumaga")
    private_send_message(vk_session, user_id, "Вас приветствует игра под названием КАМЕНЬ НОЖНИЦЫ БУМАГА!!!\n\n"
                                              "Для начала игры выбирите за что вы будите играть", None,
                                              keyboards.keyKamen_Noznica_Bumaga)


def message_Kamen_Noznica_Bumaga(vk_session, user_id, bot, answer):
    private_send_message(vk_session, user_id, "3!!!", None, None)
    private_send_message(vk_session, user_id, "2!!!", None, None)
    private_send_message(vk_session, user_id, "1!!!", None, None)

    private_send_message(vk_session, user_id, bot, None, None)
    private_send_message(vk_session, user_id, answer, None, None)


def keyGadalka(vk_session, user_id, available_command):
    data_base.record_available_command(user_id, available_command)
    data_base.now_Keyboard(user_id, keyboard="keyGadalka")
    private_send_message(vk_session, user_id, "🔮Гадалка", None, keyboards.keyGadalka)


def Gadalka_instrukcion(vk_session, user_id):
    private_send_message(vk_session, user_id, "Напиши вопрос который тебе не дает покоя \n\nИ Я "
                                              "ВАСИЛИСА ПЕТРОВНА - ВЕЛИЧАЙЩАЯ ГАДАЛКА НА СИЕ ШАРЕ "
                                              "дам на него ответ!!!", None, None)


def message_Gadalka(vk_session, user_id):
    import random

    answers = ["Абсолютно точно!", "Да", "Нет", "Скорее да, чем нет", "Не уверена...", "Однозначно нет!",
               "Если ты не фанат аниме", "у тебя все получится!", "Можешь быть уверен в этом",
               "Перспективы не очень хорошие", "А как же иначе?", "Да, но если только ты не смотришь аниме",
               "Знаки говорят — «да»", "Не знаю", "Мой ответ — «нет»", "Весьма сомнительно",
               "Не могу дать точный ответ"]

    private_send_message(vk_session, user_id, "🔮" + random.choice(answers), None, None)


def keyDoor(vk_session, user_id, available_command):
    data_base.record_available_command(user_id, available_command)
    data_base.now_Keyboard(user_id, keyboard="keyDoor")
    private_send_message(vk_session, user_id, "🚪Двери", None, keyboards.keyDoor)


def message_Door(vk_session, user_id, event, lives_score):
    if lives_score is None:
        private_send_message(vk_session, user_id, event, None, None)
    else:
        private_send_message(vk_session, user_id, event + lives_score, None, None)


def doorstart(vk_session, user_id):
    private_send_message(vk_session, user_id, 'Новая игра', None, None)


def DoorScore(vk_session, user_id, score):
    private_send_message(vk_session, user_id, 'Ваш счет: ' + str(score), None, None)


def DoorLives(vk_session, user_id, lives):
    private_send_message(vk_session, user_id, "У вас осталось: " + str(lives) + " ❤", None, None)


def Door_record(vk_session, user_id, my_record):  # "Мой рекорд"
    private_send_message(vk_session, user_id, "Ваш рекорд: " + str(my_record) + " баллов", None, None)


def Door_instrukcion(vk_session, user_id):  # "Инструкция"
    private_send_message(vk_session, user_id, "🚪Двери - это игра которая переносит тебя в подземелье в котором "
                                              "находится бесконечное количество комнат и из каждой есть по 3 выхода в "
                                              "следующую комнату, но не стоит радоваться, в каждой комнате ты можешь "
                                              "открыть лишь 1 дверь и обратного пути не будет, со старта у тебя есть 3"
                                              " жизни, они обозначаются сердечками и проходя через каждую комнату ,не"
                                              " важно что в ней находилось тебе будет начисляться по 100 очков ,по "
                                              "окончанию игры максимальное значение твоих балов будет записано в 'Мой"
                                              " рекорд', если ты набрал очень много балов, то ты можешь поискать себя "
                                              "в списке лидеров, кто знает, вдруг ты стал мировым чемпионом по "
                                              "открыванию дверей 😉", None, None)


def Board_liders_Door(vk_session, user_id, leaders):  # "Таблица лидеров"
    private_send_message(vk_session, user_id, leaders, None, None)


def teach_or_not(vk_session, user_id):  # "🎲Учить/Не учить"
    import random

    random_number = random.randint(1, 100)

    if random_number < 2:
        teach = "Тебе повезло)\nМожешь не учить🤐"
    else:
        teach = "Учи давай🙃\nУдачи🍀"

    private_send_message(vk_session, user_id, teach, None, None)
