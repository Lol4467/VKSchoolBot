# -*- coding: utf-8 -*-

import sys

from apps import command
from apps import data_base
from apps import data_door
from apps.kamen_noznica_bumaga import player_vs_comp_normal
from apps import door

sys.path.insert(0, '/apps')


def private_message(vk_session, user_id, msg, vk_api, vkapi, L_message):
    available_command = data_base.check_available_command(user_id)
    role = data_base.check_role(user_id)
    msg_save = msg
    msg = msg.lower()

    if msg == "Назад":
        command.back(vk_session, user_id, available_command)

    elif msg == "Начать" or msg == "Start":
        command.start(vk_session, user_id, vkapi)

    elif available_command == "avaible_standart":

        if msg == "на завтра" or msg == "на сегодня":
            command.message_shedule(vk_session, user_id, msg, vk_api)

        elif msg == "☁погода":
            command.message_weather(vk_session, user_id)
        
        elif msg == "📌важные даты":
            command.message_important_date(vk_session, user_id)

        elif msg == "⏰таймер до ближайших каникул":
            command.timer_until_the_next_vacation(vk_session, user_id)

        elif msg == "☀таймер до летних каникул":
            command.the_countdown_till_summer_vacation(vk_session, user_id)

        elif msg == "📰новости школы":
            command.notifications(vk_session, user_id)

        elif msg == "📋изменения в расписании":
            command.keyShedule(vk_session, user_id)

        elif msg == "⚠особое":
            command.special(vk_session, user_id)

        elif msg == "🏫о школе":
            command.information_about_the_school(vk_session, user_id, vk_api)

        elif msg == "🦠коронавирус":
            command.coronovirus(vk_session, user_id)

        elif msg == "🎲учить/не учить":
            command.teach_or_not(vk_session, user_id)

        elif msg == "🕹игры":
            command.keyGames(vk_session, user_id)
        
        elif msg == "камень/ножницы/бумага":
            command.keyKamen_Noznica_Bumaga(vk_session, user_id, "Kamen_Noznica_Bumaga")
        
        elif msg == "🔮гадалка":

            command.keyGadalka(vk_session, user_id, "Gadalka")

        elif msg == "🚪двери":
            data_door.registracion(user_id)
            NEW_GAME = data_door.start(user_id)
            command.keyDoor(vk_session, user_id, "Door")

            if NEW_GAME:
                command.doorstart(vk_session, user_id)

        elif role == "admin":
            print(L_message)
            if msg == "срочное сообщение":
                command.urgent_message_part1(vk_session, user_id)

            elif L_message == "срочное сообщение":
                command.urgent_message_part2(vk_session, msg_save)


    elif available_command == "Kamen_Noznica_Bumaga":
        if msg == 'камень' or msg == "ножницы" or msg == "бумага":
            answer, bot = player_vs_comp_normal(msg)
            command.message_Kamen_Noznica_Bumaga(vk_session, user_id, bot, answer)

    elif available_command == "Gadalka":
        if msg == "🔮погадать":
            command.Gadalka_instrukcion(vk_session, user_id)

        elif msg != "🔮погадать" and msg != "назад" and msg != "🔮гадалка":
            command.message_Gadalka(vk_session, user_id)

    elif available_command == "Door":
        if msg == "1" or msg == "2" or msg == "3":
            NEW_GAME = data_door.start(user_id)
            
            if NEW_GAME:
                command.doorstart(vk_session, user_id)

            event, lives_score = door.three_door(msg, user_id)
            command.message_Door(vk_session, user_id, event, lives_score)
            
        elif msg == "счет":
            NEW_GAME = data_door.start(user_id)

            if NEW_GAME:
                command.doorstart(vk_session, user_id)

            score = data_door.getting_score(user_id)
            command.DoorScore(vk_session, user_id, score)

        elif msg == "жизни":
            NEW_GAME = data_door.start(user_id)
            
            if NEW_GAME:
                command.doorstart(vk_session, user_id)

            lives = data_door.getting_health(user_id)
            command.DoorLives(vk_session, user_id, lives)

        elif msg == "мой рекорд":
            my_record = data_door.getting_my_record(user_id)
            command.Door_record(vk_session, user_id, my_record)

        elif msg == "таблица лидеров":
            one, two, three, four, five = data_door.board_liders()
            leaders = data_door.getting_leaders(one, two, three, four, five) 
            command.Board_liders_Door(vk_session, user_id, leaders)

        elif msg == "инструкция":
            command.Door_instrukcion(vk_session, user_id)





