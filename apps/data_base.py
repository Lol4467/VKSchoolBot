# -*- coding: utf-8 -*-

import sys
import sqlite3

sys.path.insert(1, '/base_lessons_folder')


def information_user(vkapi, user_id):  # получение имени пользователя
    user = vkapi.users.get(user_id=user_id)
    name_user = (user[0]['first_name'])
    return name_user


def checking_for_a_user(user_id, vkapi):  # проверка на наличие пользователя в БД
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    name_user = information_user(vkapi, user_id)
    
    # регестрация пользователя,если он раньше не регестрировался
    cur.execute('CREATE TABLE IF NOT EXISTS id' + str(user_id) + '(user_id TEXT, user_name TEXT, L_message TEXT, '
                                                                 'LL_message TEXT, LLL_message TEXT '
                                                                 ', keyboard TEXT, keyboard_type TEXT,'
                                                                 'available_command TEXT)')
    
    # проверка на наличие информации о пользователе в таблице
    cur.execute("SELECT user_id FROM id"+ str(user_id) + " WHERE user_id = '%s'" % user_id)
    result = cur.fetchone()


    # заполнение информации о пользователе,если он толко что зарегестрировался
    if result is None:
        cur.execute("INSERT INTO id" + str(user_id) + " VALUES('%s', '%s', '%s', '%s','%s','%s','%s','%s')"
                    % (user_id, name_user, None, None, None, None, "standart", "avaible_standart"))

        con.commit()

        user_txt(user_id)

    cur.close()
    con.close()


def user_txt(user_id):
    f = open('base_user_txt/user.txt', 'a')
    try:
        f.writelines("id" + str(user_id) + "\n")
    finally:
        f.close()


def L_message_and_LL_message(user_id, L_message):  # запись в таблицу прошлого и позопрошлого сообщения
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    LLL_message = geting_LL_message(user_id)  # получение позопозопрошлого сообщени
    LL_message = geting_L_message(user_id)  # получение позопрошлого сообщения

    # обновление значений прошлого и позопрошлого сообщения
    cur.execute("UPDATE id"+str(user_id)+" SET L_message='%s' WHERE user_id ='%s'" % (L_message, user_id))
    con.commit()
    cur.execute("UPDATE id"+str(user_id)+" SET LL_message='%s' WHERE user_id ='%s'" % (LL_message, user_id))
    con.commit()
    cur.execute("UPDATE id"+str(user_id)+" SET LLL_message='%s' WHERE user_id ='%s'" % (LLL_message, user_id))
    con.commit()

    cur.close()
    con.close()
    

def geting_L_message(user_id):  # получение последнего сообщеия
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT L_message FROM id" + str(user_id)+" WHERE user_id = %d" % user_id)
    result = cur.fetchone()
    
    if result is None:
        result = "нет сообщений в базе"
        return result
    else:
        return result[0]

    cur.close()
    con.close()


def geting_LL_message(user_id):  # получение позапрошлого сообщения
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT LL_message FROM id" + str(user_id) + " WHERE user_id = %d" % user_id)
    result = cur.fetchone()

    if result is None:
        result = "нет сообщений в базе"
        return result
    else:
        return result[0]

    cur.close()
    con.close()


def geting_LLL_message(user_id):  # получение позапозапрошлого сообщения
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT LLL_message FROM id" + str(user_id) + " WHERE user_id = %d" % user_id)
    result = cur.fetchone()

    if result is None:
        result = "нет сообщений в базе"
        return result
    else:
        return result[0]

    cur.close()
    con.close()


def now_Keyboard(user_id, keyboard):  # запись в БД клаыитатуры которая сейчас у пользователя
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("UPDATE id" + str(user_id) + " SET keyboard='%s' WHERE user_id ='%s'" % (keyboard, user_id))
    con.commit()

    cur.close()
    con.close()


def Back(user_id):  # "Назад"
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    # получение клавиатуры, которая находиться сейчас у пользователя
    cur.execute("SELECT keyboard FROM id" + str(user_id) + " WHERE user_id = '%s'" % user_id)
    result = cur.fetchone()
    result = result[0]

    # какая клавиатура будет если сделать шаг назад
    if not result:
        keyboard = "Не доступно"
        now_Keyboard(user_id, keyboard)
    elif result == "keyTimers":
        keyboard = "keyMenu"
        now_Keyboard(user_id, keyboard)
    elif result == "keyMenu":
        keyboard = "Не доступно"
        now_Keyboard(user_id, keyboard)
    elif result == "keySpecial":
        keyboard = "keyMenu"
        now_Keyboard(user_id, keyboard)
    elif result == "keySettings":
        keyboard = "keyMenu"
        now_Keyboard(user_id, keyboard)
    elif result == "keyCustomization":
        keyboard = "keySettings"
        now_Keyboard(user_id, keyboard)
    elif result == "keyWeatherForUser":
        keyboard = "keySettings"
        now_Keyboard(user_id, keyboard)
    elif result == "keyGames":
        keyboard = "keySpecial"
        now_Keyboard(user_id, keyboard)
    elif result == "keyKamen_Noznica_Bumaga":
        keyboard = "keyGames"
        now_Keyboard(user_id, keyboard)
    elif result == "keyGadalka":
        keyboard = "keyGames"
        now_Keyboard(user_id, keyboard)
    elif result == "keyDoor":
        keyboard = "keyGames"
        now_Keyboard(user_id, keyboard)
    elif result == "keyCards":
        keyboard = "keySpecial"
        now_Keyboard(user_id, keyboard)
    elif result == "check_Cards":
        keyboard = "keyCards"
        now_Keyboard(user_id, keyboard)
    elif result == "record_Cards":
        keyboard = "keyCards"
        now_Keyboard(user_id, keyboard)
    elif result == "Не доступно":
        keyboard = "keyMenu"
        now_Keyboard(user_id, keyboard)
    else:
        keyboard = "Не доступно"

    cur.close()
    con.close() 

    return keyboard


# проверка какой у пользователя вид клавиатуры
def check_key(user_id):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("SELECT keyboard_type FROM id" + str(user_id) + " WHERE user_id = '%s'" % user_id)
    result = cur.fetchone()
    result = result[0]
    
    cur.close()
    con.close()
    return result


# запись переменной котороя говорит боту ,какие команды может выполнить пользователь
def record_available_command(user_id, available_command):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("UPDATE id" + str(user_id) + " SET available_command='%s' WHERE user_id ='%s'" %
                (available_command, user_id))

    con.commit()

    cur.close()
    con.close()


# проверка переменной котороя говорит боту ,какие команды может выполнить пользователь
def check_available_command(user_id):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT available_command FROM id" + str(user_id) + " WHERE user_id = '%s'" % user_id)
    result = cur.fetchone()
    result = result[0]

    cur.close()
    con.close()
    return result


def record_last_command(user_id, last_command):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("UPDATE id"+str(user_id) + " SET last_command='%s' WHERE user_id ='%s'" % (last_command, user_id))
    con.commit()

    cur.close()
    con.close()


def getting_last_command(user_id):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("SELECT last_command FROM id" + str(user_id)+" WHERE user_id='%s'" % user_id)
    answer = cur.fetchone()

    cur.close()
    con.close()
    return answer


# основной цикл(выполняеться каждый раз,когда пользователь присылает сообщение)
def main_loop(user_id, message, vkapi):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    # проверка на наличие пользователей
    checking_for_a_user(user_id, vkapi)
    
    # получение последнего сообщения пользователя
    #L_message = geting_L_message(user_id)
    
    # получение позапрошлого сообщения
    #LL_message = geting_LL_message(user_id)

    # получение позапозапрошлого сообщения
    #LLL_message = geting_LLL_message(user_id)

    # запись последих сообщений 
    #L_message_and_LL_message(user_id, message)

    cur.close()
    con.close()

    #return L_message, LL_message, LLL_message
