# -*- coding: utf-8 -*-
import json

keyMenu = {
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
        }]

    ]
}


keyStart = {
    "one_time": True,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": {"command": "start"},
                    "label": "Начать"
                },
                "color": "primary"
            }]
    ]
}


keyTimers = {  # клавиатура которая отсылается пользователю при команде "важные даты"
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

keyAdmin = {  # клавиатура которая отсылается пользователю при команде "Админ-панель"
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "label": "Срочное сообщение (текст)"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "label": "Срочное сообщение (текст и изображение)"
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


keyShedule = {  # клавиатура для выбора дня
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


keySpecial = {  # клавиатура которая отсылается пользователю при команде "⚠Особое"
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
                    "label": "Админ-панель"
                },
                "color": "secondary"
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


keySchool_website = {  # клавиатура для перехода на сайт школы
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "open_link",
                    "link": "https://sevgym14.ru",
                    "label": "&#127760;На сайт"  # знак интернета
                }  
            }]
    ]
}


keySchoolnews = {  # клавиатура для перехода на сайт школы
    "inline": True,
    "buttons": [
        [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/app5748831_-186189504",
                    "label": "Подписаться"  # знак интернета
                }  
            }]
    ]
}


keyGames = {  # клавиатура которая отсылается пользователю при команде "⚠Особое"
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


keyKamen_Noznica_Bumaga = {
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


keyGadalka = {
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


keyDoor = {
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


# раскодировка клавиатур для дайнейшего использования

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

keyAdmin = json.dumps(keyAdmin, ensure_ascii=False).encode('utf-8')
keyAdmin = str(keyAdmin.decode('utf-8'))