# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/apps')

from apps import command #импортирование дейвстий, которые будут выполнятся при определеных командах (из функции private_message) 
from apps import data_base
from apps import data_lessons
from apps import data_door
from apps.card import cards #импортирование фунции cards из файла card
from apps.card import checking_the_answer
from apps.card import grebanaya_proverka_12if
from apps.kamen_noznica_bumaga import player_vs_comp_normal
from apps import door


def private_message(vk_session,user_id,msg,vk_api,vkapi,L_message, LL_message,LLL_message): #функция с командами
    available_command = data_base.check_available_command(user_id)
    
    if available_command == "avaible_standart":

        #действие которые выполняются после написания команды "начать"
        if msg == "Начать" or msg == "начать" or msg == "Start":
            available_command = "avaible_standart"
            command.msgstart(vk_session,user_id,msg,vk_api,vkapi,available_command)
        
        #действие которые выполняются после написания команды "hepl"
        #elif msg == "Help" or msg == "help":
        #    available_command = "avaible_standart"
        #    command.Help(vk_session,user_id,msg,vk_api,available_command)

        #большая часть кода в shedule
        elif msg == "на завтра" or msg == "На завтра" or msg == "на сегодня" or msg == "На сегодня":
            available_command = "avaible_standart"
            command.msgshedule(vk_session,user_id,msg,vk_api,available_command)

        #большая часть кода в weather
        elif msg == "☁Погода" or msg == "☁":
            available_command = "avaible_standart"
            command.msgweather(vk_session,user_id,msg,vk_api,available_command)
        
        elif msg == "📌Важные даты" or msg == "📌":
            available_command = "avaible_standart"
            command.msgimportant_date(vk_session,user_id,msg,vk_api,available_command)
        
        #большая часть кода в timers
        elif msg == "⏰Таймер до ближайших каникул" or msg == "⏰":
            available_command = "avaible_standart"
            command.timer_until_the_next_vacation(vk_session,user_id,msg,vk_api,available_command)

        #большая часть кода в timers
        elif msg == "☀Таймер до летних каникул" or msg == "☀":
            available_command = "avaible_standart"
            command.the_countdown_till_summer_vacation(vk_session,user_id,msg,vk_api,available_command)

        #пользователю просто присылаеться ссылка ,перейдя по которой он может подписаться на рассылку в отдельном приложении (приложение вк)    
        elif msg == "📰Новости школы" or msg == "📰" or msg == "Новости" or msg == "новости":
            available_command = "avaible_standart"
            command.notifications(vk_session,user_id,msg,vk_api,available_command)

        #даеться выбрать на кокой день посмотреть изменения(сегодня/завтра)
        elif msg == "📋Изменения в расписании" or msg == "📋":
            available_command = "avaible_standart"
            command.keyShedule(vk_session,user_id,msg,vk_api,available_command)

        #переход во вкладку "особое" 
        elif msg == "⚠Особое" or msg == "⚠":
            available_command = "avaible_standart"
            command.special(vk_session,user_id,msg,vk_api,available_command)
        
        #можно посмотреть информации о школе и перейти на сайт 
        elif msg == "🏫О школе" or msg == "🏫":
            available_command = "avaible_standart"
            command.information_about_the_school(vk_session,user_id,msg,vk_api,available_command)

        #присылаеться последняя статистика по короновирусу в России
        elif msg == "🦠Коронавирус" or msg == "🦠":
            available_command = "avaible_standart" 
            command.coronovirus(vk_session,user_id,msg,vk_api,available_command)
        
        #сделать настройки(идея)
        elif msg == "⚙Настройки" or msg == "⚙":
            available_command = "avaible_standart"
            command.settings(vk_session,user_id,msg,vk_api,available_command)

        elif msg == "🗿Standart" or msg == "🗿":
            key = "standart"
            available_command = "avaible_standart"
            command.keyCustomization(vk_session,user_id,msg,vk_api,key,available_command)
        
        elif msg == "👑PRO" or msg == "👑":
            key = "pro"
            available_command = "avaible_standart"
            command.keyCustomization(vk_session,user_id,msg,vk_api,key,available_command)

        elif msg == "🃏Карточки" or msg == "🃏":
            available_command = "avaible_standart"
            command.cards(vk_session,user_id,msg,vk_api,available_command)

        elif msg == "Коротко о карточках":
            available_command = "avaible_standart"
            command.briefly_about_cards(vk_session,user_id,msg,vk_api,available_command)

        elif msg == "🎲Учить/Не учить" or msg == "🎲":
            available_command = "avaible_standart"
            command.teach_or_not(vk_session,user_id,msg,vk_api,available_command)

        elif msg == "функционал" or msg == "Функционал":
            available_command = "avaible_standart"
            command.functional(vk_session,user_id,msg,vk_api,vkapi,available_command)

        elif msg == "⌨Вид клавиатуры" or msg == "⌨":
            available_command = "avaible_standart"
            command.customization(vk_session,user_id,msg,vk_api,available_command)

        elif msg == "🌤Рассылка погоды" or msg == "🌤":
            available_command = "avaible_standart"
            command.WeatherForUser(vk_session,user_id,msg,vk_api,available_command)
        
        elif msg == "✅Подписаться" or msg == "✅":
            available_command = "avaible_standart"
            command.subscription_for_weather(vk_session,vk_api,user_id)
        
        elif msg == "❌Отписаться" or msg == "❌":
            available_command = "avaible_standart"
            command.delite_subscription_for_weather(vk_session,vk_api,user_id)
        
        elif msg == "Коротко о рассылке погоды":
            available_command = "avaible_standart"
            command.subscription_weather(vk_session,user_id,vk_api)

        elif msg == "🕹Игры":
            available_command = "avaible_standart"
            command.keyGames(vk_session,user_id,vk_api)
        
        elif msg == "Камень/Ножницы/Бумага":
            available_command = "Kamen_Noznica_Bumaga"
            command.keyKamen_Noznica_Bumaga(vk_session,user_id,vk_api,available_command)
        
        elif msg == "🔮Гадалка":
            available_command = "Gadalka"
            command.keyGadalka(vk_session,user_id,vk_api,available_command)

        elif msg == "🚪Двери":
            available_command = "Door"
            data_door.registracion(user_id)
    
            NEW_GAME = data_door.start(user_id)
                
            command.keyDoor(vk_session,user_id,vk_api,available_command)
            if NEW_GAME == True:
                command.doorstart(vk_session,user_id,vk_api)
        
        elif msg == "Проверить себя":
            available_command = "available_only_cards_check"
            command.check_Cards(vk_session,user_id,msg,vk_api,available_command)

        elif msg == "Добавить карточку":
            available_command = "available_only_cards_record"
            command.record_Cards(vk_session,user_id,msg,vk_api,available_command)
            

    if available_command == "available_only_cards_check":
        available_command = "available_only_cards_check"
        if msg == "Удалить карточку" or msg == "Следующая карточка" or L_message == "Следующая карточка" or LL_message == "Следующая карточка" :
                if msg == "Удалить карточку":
                    command.delete_a_card(vk_session,user_id,LL_message)
                else:
                    last_lesson = data_lessons.getting_last_lesson(user_id)
                    if last_lesson != "None":
                        if msg == "Следующая карточка":
                            msg = last_lesson
                        if L_message == "Следующая карточка":
                            L_message = last_lesson
                        grebanaya_proverka_12if(msg,L_message,user_id)
                        checking_the_answer(user_id, msg, L_message,vk_session,vk_api)
                        answer = "все ок"
                        command.next_card(vk_session,user_id,msg,vk_api,available_command,answer)
                    else:
                        answer = "сейчас это недоступно"
                        command.next_card(vk_session,user_id,msg,vk_api,available_command,answer)

        elif msg == "тФизика" or L_message == "тФизика" or msg == "тАнглийский" or L_message == "тАнглийский" or msg == "тЛитература" or L_message == "тЛитература" or msg == "тОБЖ" or L_message == "тОБЖ" or msg == "тБиология" or L_message == "тБиология" or msg == "тМузыка" or L_message == "тМузыка" or msg == "тОбществознание" or L_message == "тОбществознание" or msg == "тФизкультура" or L_message == "тФизкультура" or msg == "тИнформатика" or L_message == "тИнформатика" or msg == "тНемецкий" or L_message == "тНемецкий" or msg == "тРусский" or L_message == "тРусский" or msg == "тХимия" or L_message == "тХимия" or msg == "тИстория" or L_message == "тИстория" or msg == "тФранцузский" or L_message == "тФранцузский" or msg == "тТехнология" or L_message == "тТехнология" or msg == "тАлгебра" or L_message == "тАлгебра":
            grebanaya_proverka_12if(msg,L_message,user_id)
            checking_the_answer(user_id, msg, L_message,vk_session,vk_api)
        
        elif msg == "Удалить карточку":
            command.delete_a_card(vk_session,user_id,LL_message)


    if available_command == "available_only_cards_record":
        available_command = "available_only_cards_record"
        if msg == "Английский" or msg == "Биология" or msg == "Информатика" or msg == "История" or msg == "Литература" or msg == "Музыка" or msg == "Немецкий" or msg == "Французский" or msg == "ОБЖ" or msg == "Обществознание" or msg == "Русский" or msg == "Технология" or msg == "Физика" or msg == "Физкультура" or msg == "Химия" or msg == "Алгебра" or L_message == "Английский" or L_message == "Биология" or L_message == "Информатика" or L_message == "История" or L_message == "Литература" or L_message == "Музыка" or L_message == "Немецкий" or L_message == "Французский" or L_message == "ОБЖ" or L_message == "Обществознание" or L_message == "Русский" or L_message == "Технология" or L_message == "Физика" or L_message == "Физкультура" or L_message == "Химия" or L_message == "Алгебра" or LL_message == "Английский" or LL_message == "Биология" or LL_message == "Информатика" or LL_message == "История" or LL_message == "Литература" or LL_message == "Музыка" or LL_message == "Немецкий" or LL_message == "Французский" or LL_message == "ОБЖ" or LL_message == "Обществознание" or LL_message == "Русский" or LL_message == "Технология" or LL_message == "Физика" or LL_message == "Физкультура" or LL_message == "Химия" or LL_message == "Алгебра":
            cards(vk_session,user_id, msg, L_message, LL_message)

    if available_command == "Kamen_Noznica_Bumaga":
        if msg == 'Камень' or msg == "Ножницы" or msg == "Бумага":
            answer,bot = player_vs_comp_normal(msg)
            command.msgKamen_Noznica_Bumaga(vk_session,user_id,vk_api,bot,answer)

    if available_command == "Gadalka":
        if msg == "🔮Погадать":
            command.Gadalka_instrukcion(vk_session,user_id,vk_api)
        elif msg != "🔮Погадать" and msg != "Назад" and msg != "🔮Гадалка":
            command.msgGadalka(vk_session,user_id,vk_api)

    if available_command == "Door":
        if msg == "1" or msg == "2" or msg == "3":
            NEW_GAME = data_door.start(user_id)
            
            if NEW_GAME == True:
                command.doorstart(vk_session,user_id,vk_api)

            event, lives_score = door.three_door(msg,user_id)
            command.msgDoor(vk_session,user_id,vk_api,event, lives_score)
            
        elif msg == "Счет":
            NEW_GAME = data_door.start(user_id)

            if NEW_GAME == True:
                command.doorstart(vk_session,user_id,vk_api)

            score = data_door.getting_score(user_id)
            command.DoorScore(vk_session,user_id,vk_api,score)

        elif msg == "Жизни": 
            NEW_GAME = data_door.start(user_id)
            
            if NEW_GAME == True:
                command.doorstart(vk_session,user_id,vk_api)

            lives = data_door.getting_health(user_id)
            command.DoorLives(vk_session,user_id,vk_api,lives)

        elif msg == "Мой рекорд": 
            my_record = data_door.getting_my_record(user_id)
            command.Door_record(vk_session,user_id,vk_api,my_record)

        elif msg == "Таблица лидеров":
            one, two, three, four, five = data_door.board_liders()
            leaders = data_door.getting_leaders(one, two, three, four, five) 
            command.Board_liders_Door(vk_session,user_id,vk_api,leaders)

        elif msg == "Инструкция":
            command.Door_instrukcion(vk_session,user_id,vk_api)

    #большая часть кода в data_base
    if msg == "Назад":
        available_command = "avaible_standart"
        sequence = command.debugger2(user_id)
        sequence = sequence[0]
        if sequence == "None":
            command.back(vk_session,user_id,msg,vk_api,available_command)
            mistake = "все ок"
            command.debugger1(vk_session,user_id,msg,vk_api,mistake)
        else: 
            lesson_now = None
            data_base.sequence(user_id,lesson_now)
            mistake = "cards"
            command.debugger1(vk_session,user_id,msg,vk_api,mistake)
   
    
    #просмотр фоточек школы(идея)
    #elif msg == "п":
        #command.inline(vk_session,user_id,msg,vk_api)

def chatbot(vk_session,vk_api,chat_msg,vkapi,chat_peer_id):
    
    if chat_msg == "команды":
        command.command_help_chat(vkapi,chat_peer_id)
    
    elif chat_msg == "таймер до лета":
        command.the_countdown_till_summer_chat(vkapi,chat_peer_id)
    
    elif chat_msg == "таймер до следующих каникул":
        command.identification_holidays_chat(vkapi,chat_peer_id)

    elif chat_msg == "изменения на завтра":
        command.shedule_chat_tomorrow(vk_session,vk_api,vkapi,chat_peer_id)
    
    elif chat_msg == "изменения на сегодня":
        command.shedule_chat_today(vk_session,vk_api,vkapi,chat_peer_id)
    
    elif chat_msg == "погода":
        command.msgweather_chat(vkapi,chat_peer_id)


