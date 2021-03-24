# -*- coding: utf-8 -*-
import json #импортирование модуля для работы с json файлами

keyMenu = { #клавиатура с главным меню
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "☁Погода"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "📋Изменения в расписании"
                },
                "color": "positive"
            }],
        [{
            "action": {
                    "type": "text",
                    "label": "📌Важные даты"
                },
                "color": "primary"
        }],
        [{
            "action": {
                    "type": "open_link",
                    "link": "https://vk.com/app5748831_-186189504",
                    "label": "📰Новости школы"
                }
        }],
        [{
            "action": {
                    "type": "text",
                    "label": "⚠Особое"
                },
                "color": "secondary"
        },
        {
            "action": {
                    "type": "text",
                    "label": "🏫О школе",
                },
                "color": "secondary"
        },
        {
            "action": {
                    "type": "text",
                    "label": "⚙Настройки",
                },
                "color": "secondary"
        }]

    ]
}


keyMenuPRO = { #клавиатура с главным меню(PRO)
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "☁"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "label": "📋"
                },
                "color": "primary"
            },
        {
            "action": {
                    "type": "text",
                    "label": "📌"
                },
                "color": "primary"
        }],
        [{
            "action": {
                    "type": "open_link",
                    "link": "https://vk.com/app5748831_-186189504",
                    "label": "📰"
                }
        }],
        [{
            "action": {
                    "type": "text",
                    "label": "⚠"
                },
                "color": "positive"
        },
        {
            "action": {
                    "type": "text",
                    "label": "🏫",
                },
                "color": "positive"
        },
        {
            "action": {
                    "type": "text",
                    "label": "⚙",
                },
                "color": "positive"
        }]

    ]
}


keyStart = { #клавиатура при первом переходе к диалогу группы
    "one_time": True,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": {"command":"start"} ,
                    "label": "Начать"
                },
                "color": "primary"
            }]
    ]
}


keyTimers = { #клавиатура которая отсылается пользователю при команде "важные даты"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "☀Таймер до летних каникул"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "⏰Таймер до ближайших каникул"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
            
    ]
}

keyTimersPRO = { #клавиатура которая отсылается пользователю при команде "📌"(PRO)
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "☀"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "⏰"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
            
    ]
}


keyShedule = { #клавиатура для выбора дня
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "на сегодня"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "на завтра"
                },
                "color": "primary"
            }]
    ]
}


keySpecial = { #клавиатура которая отсылается пользователю при команде "⚠Особое"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "🦠Коронавирус"
                },
                "color": "negative"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "🃏Карточки"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "🎲Учить/Не учить"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "🕹Игры"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keySpecialPRO = { #клавиатура которая отсылается пользователю при команде "⚠"(PRO)
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "🦠"
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "label": "🃏"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "🎲"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}


keySchool_website ={ #клавиатура для перехода на сайт школы
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "open_link",
                    "link": "https://sevgym14.ru",
                    "label": "&#127760;На сайт" #знак интернета
                }  
            }]
    ]
}


keySchool_websitePRO ={ #клавиатура для перехода на сайт школы
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "open_link",
                    "link": "https://sevgym14.ru",
                    "label": "&#127760;" #знак интернета
                }  
            }]
    ]
}


keyCustomization = { #клавиатура которая отсылается пользователю при команде "⚙Настройки"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "🗿Standart"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "👑PRO"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keyCustomizationPRO = { #клавиатура которая отсылается пользователю при команде "⚙"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "🗿"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "👑"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keySettings = { #клавиатура которая отсылается пользователю при команде "⚙Настройки"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "⌨Вид клавиатуры"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "🌤Рассылка погоды"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keySettingsPRO = { #клавиатура которая отсылается пользователю при команде "⚙Настройки"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "⌨"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "🌤"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keyWeatherForUser= { #клавиатура которая отсылается пользователю при команде "⚙Настройки"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "✅Подписаться"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "❌Отписаться"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Коротко о рассылке погоды"
                },
                "color": "positive"
            }],
    ]
}

keyWeatherForUserPRO = { #клавиатура которая отсылается пользователю при команде "⚙Настройки"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "✅"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "❌"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Коротко о рассылке погоды"
                },
                "color": "positive"
            }],
    ]
}


keyCards = { #клавиатура для проверки себя
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Проверить себя"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Добавить карточку"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "secondary"
            },
            {
            
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Коротко о карточках"
                },
                "color": "positive"
            }]
            
    ]
}

check_Cards = { #клавиатура которая отправляется пользователю после команды "проверка знаний"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тАнглийский"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тБиология"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тАлгебра"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тИстория"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тЛитература"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "тМузыка"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тФизкультура"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тФранцузский"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тФизика"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тОбществознание"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тРусский"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "тХимия"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Следующая карточка"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "secondary"
            }
        ]

    ]
}


record_Cards = { #клавиатура которая отправляется пользователю после команды "Добавить карточку"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Английский"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Биология"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Алгебра"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "История"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Литература"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Музыка"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Физкультура"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Французский"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Физика"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Обществознание"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Русский"
                },
                "color": "primary"
            },{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Химия"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Назад"
                },
                "color": "secondary"
            }
        ]

    ]
}


keySchoolnews ={ #клавиатура для перехода на сайт школы
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/app5748831_-186189504",
                    "label": "Подписаться" #знак интернета
                }  
            }]
    ]
}


delete_a_card_and_farther = { #клавиатура для удаления карточки
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Удалить карточку"
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Следующая карточка"
                },
                "color": "primary"
            }
            ]
    ]
}


keyGames = { #клавиатура которая отсылается пользователю при команде "⚠Особое"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "Камень/Ножницы/Бумага"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "🔮Гадалка"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "🚪Двери"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keyKamen_Noznica_Bumaga = { #клавиатура которая отсылается пользователю при команде "⚠Особое"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "Камень"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Ножницы"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Бумага"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keyGadalka = { #клавиатура которая отсылается пользователю при команде "⚠Особое"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "🔮Погадать"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

keyDoor = { #клавиатура которая отсылается пользователю при команде "⚠Особое"
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "label": "1"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "2"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "label": "3"
                },
                "color": "primary"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Жизни"
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Счет"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Мой рекорд"
                },
                "color": "negative"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Таблица лидеров"
                },
                "color": "positive"
            },
            {
                "action": {
                    "type": "text",
                    "label": "Инструкция"
                },
                "color": "positive"
            }],
            [{
                "action": {
                    "type": "text",
                    "label": "Назад"
                },
                "color": "secondary"
            }]
    ]
}

#раскодировка клавиатур для дайнейшего использования

keyMenu = json.dumps(keyMenu, ensure_ascii=False).encode('utf-8')
keyMenu = str(keyMenu.decode('utf-8'))

keyStart = json.dumps(keyStart, ensure_ascii=False).encode('utf-8')
keyStart = str(keyStart.decode('utf-8'))

keyTimers = json.dumps(keyTimers, ensure_ascii=False).encode('utf-8')
keyTimers = str(keyTimers.decode('utf-8'))

keyShedule = json.dumps(keyShedule, ensure_ascii=False).encode('utf-8')
keyShedule = str(keyShedule.decode('utf-8'))

keySpecial = json.dumps(keySpecial, ensure_ascii=False).encode('utf-8')
keySpecial = str(keySpecial.decode('utf-8'))

keySchool_website = json.dumps(keySchool_website, ensure_ascii=False).encode('utf-8')
keySchool_website = str(keySchool_website.decode('utf-8'))

keyCustomization = json.dumps(keyCustomization, ensure_ascii=False).encode('utf-8')
keyCustomization = str(keyCustomization.decode('utf-8'))

keyMenuPRO = json.dumps(keyMenuPRO, ensure_ascii=False).encode('utf-8')
keyMenuPRO = str(keyMenuPRO.decode('utf-8'))

keyTimersPRO = json.dumps(keyTimersPRO, ensure_ascii=False).encode('utf-8')
keyTimersPRO = str(keyTimersPRO.decode('utf-8'))

keySpecialPRO = json.dumps(keySpecialPRO, ensure_ascii=False).encode('utf-8')
keySpecialPRO = str(keySpecialPRO.decode('utf-8'))

keySchool_websitePRO = json.dumps(keySchool_websitePRO, ensure_ascii=False).encode('utf-8')
keySchool_websitePRO = str(keySchool_websitePRO.decode('utf-8'))

keyCustomizationPRO = json.dumps(keyCustomizationPRO, ensure_ascii=False).encode('utf-8')
keyCustomizationPRO = str(keyCustomizationPRO.decode('utf-8'))

keySettings = json.dumps(keySettings, ensure_ascii=False).encode('utf-8')
keySettings = str(keySettings.decode('utf-8'))

keySettingsPRO = json.dumps(keySettingsPRO, ensure_ascii=False).encode('utf-8')
keySettingsPRO = str(keySettingsPRO.decode('utf-8'))

keyWeatherForUserPRO = json.dumps(keyWeatherForUserPRO, ensure_ascii=False).encode('utf-8')
keyWeatherForUserPRO = str(keyWeatherForUserPRO.decode('utf-8'))

keyWeatherForUser = json.dumps(keyWeatherForUser, ensure_ascii=False).encode('utf-8')
keyWeatherForUser = str(keyWeatherForUser.decode('utf-8'))

keyCards = json.dumps(keyCards, ensure_ascii=False).encode('utf-8')
keyCards = str(keyCards.decode('utf-8'))

check_Cards = json.dumps(check_Cards, ensure_ascii=False).encode('utf-8')
check_Cards = str(check_Cards.decode('utf-8'))

record_Cards = json.dumps(record_Cards, ensure_ascii=False).encode('utf-8')
record_Cards = str(record_Cards.decode('utf-8'))

delete_a_card_and_farther = json.dumps(delete_a_card_and_farther, ensure_ascii=False).encode('utf-8')
delete_a_card_and_farther = str(delete_a_card_and_farther.decode('utf-8'))

keySchoolnews = json.dumps(keySchoolnews, ensure_ascii=False).encode('utf-8')
keySchoolnews = str(keySchoolnews.decode('utf-8'))

keyGames = json.dumps(keyGames, ensure_ascii=False).encode('utf-8')
keyGames = str(keyGames.decode('utf-8'))

keyKamen_Noznica_Bumaga = json.dumps(keyKamen_Noznica_Bumaga, ensure_ascii=False).encode('utf-8')
keyKamen_Noznica_Bumaga = str(keyKamen_Noznica_Bumaga.decode('utf-8'))

keyGadalka = json.dumps(keyGadalka, ensure_ascii=False).encode('utf-8')
keyGadalka = str(keyGadalka.decode('utf-8'))

keyDoor = json.dumps(keyDoor, ensure_ascii=False).encode('utf-8')
keyDoor = str(keyDoor.decode('utf-8'))