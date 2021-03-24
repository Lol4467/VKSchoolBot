# ls_config

#токен сообщества для работы с ботом (используеться в main)
token = 'b10473878154549000180f5a65525c710ad21ceb455a85429e448aab520076dd187a9abf7247959ece3fa'

#id группы(используеться в main)
group_id = '186189504'

#ссылка для рассылки сообщений
notifications = "https://vk.com/app5748831_-186189504" #это приложение вк

city = "severodvinsk" #выбор города для получения погоды(используется в weaather)

#текст который отправиться пользователю после вступления в группу(используется в main)
welcome_text = "Добро пожаловать!❤ \nПодпишись для получения уведомлений \n https://vk.com/app5748831_-186189504"

#текст который отправиться пользователю после выхода из группы(используется в main)
goodbye_text = "Жаль, что вы решили покинуть нас("

#текст который отправится пользователю ,если он напишеть Начать или начать(используется в response_form)
start_text = ", приятного пользования😎\n\nP.S что бы посмотреть на список команд напишите 'функционал'"

#текст который отправится пользователю ,если он напишеть Функционал или функционал(используется в response_form)
functional = "Вот наш функционал: \n\n☁Погода \n\n📋Изменения в расписании \n    ●  Изменения на сегодня \n    ●  Изменения на завтра\n\n📌Важные даты \n    ●  ☀Таймер до летних каникул\n    ●  ⏰Таймер до ближайших каникул\n\n📰Новости школы\n\n⚠Особое\n    ●  🦠Коронавирус\n    ●  🃏Карточки\n    ●  🎲Учить/Не учить\n\n🏫О школе\n\n⚙Настройки\n    ●  🗿Standart режим клавиатуры\n    ●  👑PRO режим клавиатуры\n\nP.S Что бы получать новости от сообщеста напишите 'Новости'"

#текст который отправиться если пользователь напишет 📰Новости школы (используется в response_form)
school_information = "Муниципальное бюджетное общеобразовательное учреждение «Северодвинская гимназия №14» \n\n Директор - Гришкова Елена Ивановна \n\nАдрес: г. Северодвинск, ул. Торцева, 59 \n\nКонтактный телефон - 8184569838 \n\nАдрес электронной почты – gym14@mail.ru \n\nРаботаем с 1963 года!\n\nБольше информации об образовательном учреждении можно посмотреть на официальном сайте"

#текст который отправиться если пользователь напишет ⚙Настройки (используется в response_form)
customization = "Здесь вы можете выбрать тип клавиатуры,всего их 2\n\n🗿Standart - режим клавиатуры установленный по умолчанию \n\n👑PRO - режим который вы можете выбрать (клавиатура будет состоять только из смайликов)\n\nПример PRO клавиатуры вы можете увидеть ниже"

keycards = "🃏Карточки - мини приложение для запоминания информации\n\nВо вкладке 'Добавить карточку' можно записать определенный вопрос и ответ на него, что бы вернуться к нему позже\n\n(Для этого ,перейдя в это вкладку, выберите предмет по которому хотите запомнить вопрос)\n\nВо вкладке 'Проверить себя' можно проверить себя на знание определенного вопроса, который вы уже записали\n\n(Для этого ,перейдя в это вкладку, выберите предмет по которому хотите проверить себя на знание верного ответа)" 

subscription_weather = "Подписавшись на эту рассылку вы будете получать сводку погоды каждый день в 7:00"

#текст который отправится пользователю ,если он напишеть на завтра (используется в response_form)
shedule_tomorrow_True_text_if_there_is = "Вот изменения на завтра"
shedule_tomorrow_True_text_if_not = "Изменений в расписании на завтра нет или их еще не объявили🤷‍♂"

#текст который отправится пользователю ,если он напишеть на сегодня (используется в response_form)
shedule_tomorrow_False_text_if_there_is = "Вот изменения на сегодня"
shedule_tomorrow_False_text_if_not = "Изменений в расписании на сегодня нет или их еще не объявили🤷‍♂"


#осение каникулы
beginning_autumn_holidays_month = 11 #начало осених каникул(месяц)(используется в timers)
beginning_autumn_holidays_day = 5 #начало осених каникул(день)(используется в timers)
end_autumn_holidays_month = 11 #конец осених каникул(месяц)(используется в timers)
end_autumn_holidays_day = 10 #конец осених каникул(день)(используется в timers)
#летние каникулы
beginning_summer_holidays_month = 6 #начало летних каникул(месяц)(используется в timers)
beginning_summer_holidays_day = 1 #начало летних каникул(день)(используется в timers)
end_summer_holidays_month = 8 #конец летних каникул(месяц)(используется в timers)
end_summer_holidays_day = 31 #конец летних каникул(день)(используется в timers)
#весенние каникулы
beginning_spring_holidays_month = 3 #начало весенних каникул(месяц)(используется в timers)
beginning_spring_holidays_day = 23 #начало весенних каникул(день)(используется в timers)
end_spring_holidays_month = 3 #конец весенних каникул(месяц)(используется в timers)
end_spring_holidays_day = 28 #конец весенних каникул(день)(используется в timers)
#зимние каникулы
beginning_winter_holidays_month = 12 #начало зимних каникул(месяц)(используется в timers)
beginning_winter_holidays_day = 30 #начало зимних каникул(день)(используется в timers)
end_winter_holidays_month = 1 #конец зимних каникул(месяц)(используется в timers)
end_winter_holidays_day = 11 #конец зимних каникул(день)(используется в timers)

# chat_config

#текст который отправится пользователю в чате ,если он напишеть команды (используется в response_form)
command_chat = "Доступные команды:\n\n&#128312; Погода\n&#128312; Изменения на сегодня\n&#128312; Таймер до лета\n&#128312; Таймер до ближайших каникул"