import sqlite3
import re

import vk_api
import config

vk_session = vk_api.VkApi(token=config.token) # получение vk_session
vkapi = vk_session.get_api() # получение vkapi

def registracion(user_id):

    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Door (user_id TEXT, health TEXT, score TEXT, my_record TEXT)')

    cur.execute("SELECT user_id FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    result = cur.fetchone()

    if result is None:
        cur.execute("INSERT INTO Door VALUES('%s','%s','%s','%s')" % (user_id,0,0,0))
        con.commit()

    cur.close()
    con.close()

def start(user_id):
    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("SELECT health FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    result1 = cur.fetchone()
    result1 = result1[0]

    cur.execute("SELECT score FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    result2 = cur.fetchone()
    result2 = result2[0]

    NEW_GAME = False

    if result1 == '0' and result2 == '0':
        cur.execute("UPDATE Door SET health='%s' WHERE user_id ='%s'" % (3, user_id))
        con.commit()

        NEW_GAME = True
    
    elif result1 == '0' and result2 != '0':
        
        cur.execute("UPDATE Door SET health='%s' WHERE user_id ='%s'" % (3, user_id))
        con.commit()

        cur.execute("UPDATE Door SET score='%s' WHERE user_id ='%s'" % (0, user_id))
        con.commit()

        NEW_GAME = True

    cur.close()
    con.close()

    return NEW_GAME

def dragon_water(user_id,health,score):
    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("UPDATE Door SET health='%s' WHERE user_id ='%s'" % (health, user_id))
    con.commit()

    cur.execute("UPDATE Door SET score='%s' WHERE user_id ='%s'" % (score, user_id))
    con.commit()


    cur.close()
    con.close()

def empty_gameower(user_id,score):
    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()


    cur.execute("UPDATE Door SET score='%s' WHERE user_id ='%s'" % (score, user_id))
    con.commit()


    cur.close()
    con.close()

def getting_health_score(user_id):

    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("SELECT health FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    lives = cur.fetchone()
    lives = lives[0]

    cur.execute("SELECT score FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    score = cur.fetchone()
    score = score[0]

    cur.close()
    con.close()
    
    return lives,score

def getting_health(user_id):

    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("SELECT health FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    lives = cur.fetchone()
    lives = lives[0]

    cur.close()
    con.close()

    return lives

def getting_score(user_id):

    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("SELECT score FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    score = cur.fetchone()
    score = score[0]

    cur.close()
    con.close()

    return score

def getting_my_record(user_id):

    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("SELECT my_record FROM Door WHERE user_id = '%s'" % user_id) #проверка на наличие информации о пользователе в таблице
    my_record = cur.fetchone()
    my_record = my_record[0]

    cur.close()
    con.close()

    return my_record

def new_my_record(user_id,score):
    my_record = getting_my_record(user_id)
    
    my_record = int(my_record)

    if my_record < score:
        con = sqlite3.connect('./base_games/base_Door.db')
        cur = con.cursor()

        cur.execute("UPDATE Door SET my_record='%s' WHERE user_id ='%s'" % (score, user_id))
        con.commit()

        cur.close()
        con.close()


def counting_the_number_of_rows(): 
    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    cur.execute("SELECT COUNT(user_id) FROM Door")
    quantity = cur.fetchone()
    quantity = quantity[0] 

    cur.close()
    con.close()

    return quantity



def board_liders():
    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()
    
    one = None
    two = None
    three = None
    four = None
    five = None



    masive =[]

    quantity = counting_the_number_of_rows()
    
    for x in range(quantity):

        cur.execute("SELECT my_record FROM Door") #проверка на наличие информации о пользователе в таблице
        my_record = cur.fetchall()

        world_record = my_record[x]

        red = re.compile('')
        for z in world_record:
            world_record = red.sub('', z)
            world_record = int(world_record)

            masive.append(world_record)

        
    for x in range(quantity):        

        if x == 0:
            one = max(masive)
            masive.remove(one)

        if x == 1:
            two = max(masive)
            masive.remove(two)

        if x == 2:
            three = max(masive)
            masive.remove(three)
            
        if x == 3:
            four = max(masive)
            masive.remove(four)
            
        if x == 4:
            five = max(masive)
            masive.remove(five)
            
    
    cur.close()
    con.close()
    
    return one, two, three, four, five
    
def information_user(user_id): #получение имени пользователя
    user = vkapi.users.get(user_id=user_id)
    name_user = (user[0]['first_name'])
    fam_name = (user[0]['last_name'])
    return name_user,fam_name


def getting_leaders(one, two, three, four, five):
    con = sqlite3.connect('./base_games/base_Door.db')
    cur = con.cursor()

    leaders = "⭐МИРОВЫЕ ЗВЕЗДЫ⭐\n\n"

    if one is not None:
        cur.execute("SELECT user_id FROM Door WHERE my_record = '%s'" % one) #проверка на наличие информации о пользователе в таблице
        one_leader = cur.fetchone()
        one_leader = one_leader[0]

        name_user,fam_name = information_user(one_leader)

        leaders +=  "1 место🏅занимает " + "[id" + one_leader + "|" + fam_name + " " + name_user + "]" + "\nОн(а) сумел(а) набрать " + str(one) + " баллов\n\n"

    if two is not None:
        cur.execute("SELECT user_id FROM Door WHERE my_record = '%s'" % two) #проверка на наличие информации о пользователе в таблице
        two_leader = cur.fetchone()
        two_leader = two_leader[0]

        name_user,fam_name = information_user(two_leader)

        leaders +=  "2 место🥈занимает " + "[id" + two_leader + "|" + fam_name + " " + name_user + "]" + "\nОн(а) сумел(а) набрать " + str(two) + " баллов\n\n"

    if three is not None:
        cur.execute("SELECT user_id FROM Door WHERE my_record = '%s'" % three) #проверка на наличие информации о пользователе в таблице
        three_leader = cur.fetchone()
        three_leader = three_leader[0]

        name_user,fam_name = information_user(three_leader)

        leaders +=  "3 место🥉занимает " + "[id" + three_leader + "|" + fam_name + " " + name_user + "]" + "\nОн(а) сумел(а) набрать " + str(three) + " баллов\n\n"

    if four is not None:
        cur.execute("SELECT user_id FROM Door WHERE my_record = '%s'" % four) #проверка на наличие информации о пользователе в таблице
        four_leader = cur.fetchone()
        four_leader = four_leader[0]

        name_user,fam_name = information_user(four_leader)

        leaders +=  "4 место 🍫 занимает " + "[id" + four_leader + "|" + fam_name + " " + name_user + "]" + "\nОн(а) сумел(а) набрать " + str(four) + " баллов\n\n"
    
    if five is not None:
        cur.execute("SELECT user_id FROM Door WHERE my_record = '%s'" % five) #проверка на наличие информации о пользователе в таблице
        five_leader = cur.fetchone()
        five_leader = five_leader[0]

        name_user,fam_name = information_user(five_leader)

        leaders +=  "5 место занимает " + "[id" + five_leader + "|" + fam_name + " " + name_user + "]" + "\nОн(а) сумел(а) набрать " + str(five) + " баллов\n\n"



    cur.close()
    con.close()

    return leaders