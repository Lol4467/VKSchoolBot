#отдельная БД для работы с карточками
import sys
sys.path.insert(1, '/apps')

import sqlite3 #импортирование модуля для работы с БД
import random #импортирование модуля для работы с псеворандомными числами
from apps import data_base
from apps import command

# промежуточная запись вопроса
def promo_question(msg,user_id,lesson_promo): 
    con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db')
    cur = con.cursor()
    
    cur.execute("INSERT INTO " +lesson_promo+" VALUES('%s', '%s','%s')" % (user_id,msg,"None"))
    con.commit()

    cur.close()
    con.close()

# запись вопроса и ответа
def question_answer(msg,user_id,lesson,lesson_promo): 
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()


    cur.execute("SELECT max_" + lesson + " from id" + str(user_id) + " where user_id = '%s'" % user_id)
    max_lesson = cur.fetchone()
    max_lesson = int(max_lesson[0])
    max_lesson += 1
    max_lesson = str(max_lesson)

    cur.close()
    con.close()

    con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db')
    cur = con.cursor()

    # получение вопроса
    cur.execute("SELECT question FROM " + lesson_promo + " WHERE Id = %d" % user_id)
    result = cur.fetchone()

    #получение колличества строк
    number = counting_the_number_of_rows(user_id,lesson)

    cur.execute("INSERT INTO " + lesson + " VALUES('%s', '%s', '%s', '%s')" % (user_id,result[0],msg,int(max_lesson)))
    con.commit()

    # очитстка таблицы для следующего цикла
    cur.execute("DELETE FROM " + lesson_promo + " WHERE Id=%d" % user_id)
    con.commit()

    cur.close()
    con.close()

    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    # что бы не мешало выполнению другим if
    cur.execute("UPDATE id"+str(user_id)+" SET LL_message='%s' WHERE user_id=%d" % ("удалено", user_id))
    con.commit()
    
    cur.execute("UPDATE id"+str(user_id)+" SET L_message='%s' WHERE user_id=%d" % ("удалено", user_id))
    con.commit()

    cur.execute("UPDATE id"+ str(user_id) +" SET max_"+ lesson +"='%s' WHERE user_id=%d" % (max_lesson, user_id))
    con.commit()

    cur.execute("SELECT masive_" + lesson + " from id" + str(user_id) + " where user_id = '%s'" % user_id)
    masive_lesson = cur.fetchone()

    try:
        masive_lesson = masive_lesson[0]
    except BaseException:
        print("какая то ошибка")

    if masive_lesson == "None":
        masive_lesson = "0"
    else:
        masive_lesson = list(masive_lesson)
        masive_lesson.append(max_lesson)
        masive_lesson_s = ''.join(masive_lesson)
        masive_lesson = masive_lesson_s

    cur.execute("UPDATE id"+ str(user_id) +" SET masive_"+ lesson +"='%s' WHERE user_id=%d" % (masive_lesson, user_id))
    con.commit()


    cur.close()
    con.close()


#получение колличество строк с определенным ID
def counting_the_number_of_rows(user_id,lesson): 
    con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db')
    cur = con.cursor()

    cur.execute("SELECT COUNT(Id) from " + lesson + " where Id = '%s'" % user_id)
    quantity = cur.fetchone()
    quantity = quantity[0] 

    cur.close()
    con.close()

    return quantity

#получение вопроса из БД
def questions(vk_session,user_id,msg,vk_api,lesson): 
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    number = counting_the_number_of_rows(user_id,lesson)
    number1 = number - 1 # что бы отсчет был от 0

    if number1 < 0:
        data_base.sequence(user_id,lesson_now = None)
        mistake = "Вы пока не записали вопросов по этому предмету"
        command.debugger1(vk_session,user_id,msg,vk_api,mistake)
    else:
        cur.execute("SELECT masive_" + lesson + " from id" + str(user_id) + " where user_id = '%s'" % user_id)
        masive_lesson = cur.fetchone()

        masive_lesson = masive_lesson[0]
        masive_lesson = list(masive_lesson)

        print(masive_lesson)

        cur.close()
        con.close()

        con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db')
        cur = con.cursor()
        
        random_number = 0

        if masive_lesson != []:

            random_number = int(random.choice(masive_lesson))
            
        

        if random_number > 0:
            cur.execute("SELECT question FROM " + lesson + " WHERE number = %d" % random_number)
            
            result = cur.fetchone()
            question = result

        else:
            question = "Вопросов по данному предмету больше нет"
        
        return question
    
    cur.close()
    con.close()
    
    
 #получение ответа на вопрос из БД
def answer(user_id,lesson,question):
    con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db')
    cur = con.cursor()
    
    if question is not None:
        question = question[0]

    cur.execute("SELECT answer FROM " + lesson + " WHERE question='%s' AND Id='%s'" % (question,user_id))
    answer = cur.fetchone()
    
    cur.close()
    con.close()
    return answer

#запись ответа в другую таблицу(base_USER),что бы не потерять
def receiving_and_memory_answer_and_question(question,answer,user_id):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    if question != None:
        question = question[0]
    
    cur.execute("UPDATE id"+str(user_id)+" SET answer='%s' WHERE user_id ='%s'" % (answer, user_id))
    con.commit() 

    cur.execute("UPDATE id"+str(user_id)+" SET question='%s' WHERE user_id ='%s'" % (question, user_id))
    con.commit() 

    cur.close()
    con.close()

#функция по удалению карточки
def delete_a_card(user_id,lesson):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT answer FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    answer = cur.fetchone()

    cur.execute("SELECT question FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    question = cur.fetchone()

    cur.execute("SELECT sequence FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    sequence = cur.fetchone()


    cur.execute("UPDATE id"+str(user_id)+" SET answer='%s' WHERE user_id ='%s'" % (None, user_id))
    con.commit() 

    cur.execute("UPDATE id"+str(user_id)+" SET question='%s' WHERE user_id ='%s'" % (None, user_id))
    con.commit() 

    cur.execute("UPDATE id"+str(user_id)+" SET sequence='%s' WHERE user_id ='%s'" % (None, user_id))
    con.commit() 

    question = question[0] 
    answer = answer[0] 
    sequence = sequence[0] 

    cur.execute("SELECT masive_" + lesson + " from id" + str(user_id) + " where user_id = '%s'" % user_id)
    masive_lesson = cur.fetchone()

    cur.close()
    con.close()

    if answer != None and question != None:

        con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db')
        cur = con.cursor()

        cur.execute("SELECT number FROM "+lesson+" WHERE Id='%s' AND question ='%s' AND answer = '%s'" % (user_id,question,answer))
        number = cur.fetchone()
        number = number[0] 

        cur.execute("DELETE FROM "+lesson+" WHERE Id='%s' AND question ='%s' AND answer = '%s'" % (user_id,question,answer))
        con.commit()
        
        if number != 0:
            masive_lesson = masive_lesson[0]
            masive_lesson = list(masive_lesson)
            masive_lesson.remove(str(number))
            masive_lesson_s = ''.join(masive_lesson)
            masive_lesson = masive_lesson_s
        else:
            masive_lesson = "None"

        cur.close()
        con.close()

        con = sqlite3.connect('./base_USER.db')
        cur = con.cursor()

        cur.execute("UPDATE id"+ str(user_id) +" SET masive_"+ lesson +"='%s' WHERE user_id=%d" % (masive_lesson, user_id))
        con.commit()

        answer = "удалено"
    else:
        answer = "нечего удалять"

    cur.close()
    con.close()
    
    return answer

 #получение ответа из таблицы для сравнения с msg
def getting_a_response(user_id):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT answer FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    answer = cur.fetchone()
    
    cur.close()
    con.close()
    
    return answer

def update_last_sesson(user_id,lesson):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("UPDATE id"+str(user_id)+" SET last_lesson='%s' WHERE user_id=%d" % (lesson, user_id))
    con.commit()

    cur.close()
    con.close()

def getting_last_lesson(user_id):
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()

    cur.execute("SELECT last_lesson FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    last_lesson = cur.fetchone()
    last_lesson = last_lesson[0]

    if last_lesson == "English": 
        last_lesson  = "тАнглийский"

    if last_lesson == "biology": 
        last_lesson = "тБиология"

    if last_lesson == "algebra":
        last_lesson = "тАлгебра"

    if last_lesson == "history":
        last_lesson = "тИстория"

    if last_lesson == "literature":
        last_lesson = "тЛитература"

    if  last_lesson == "music":
        last_lesson = "тМузыка"

    if  last_lesson == "physical_education":
        last_lesson = "тФизкультура"

    if  last_lesson == "French":
        last_lesson = "тФранцузский"

    if  last_lesson == "physics":
        last_lesson = "тФизика"

    if  last_lesson == "social_studies":
        last_lesson = "тОбществознание"

    if  last_lesson == "Russian":
        last_lesson = "тРусский"

    if  last_lesson == "chemistry":
        last_lesson = "тХимия"
        
    cur.close()
    con.close()

    return last_lesson

#удаление мешающих данных из таблицы,что бы не мешать другим if
def delite_message(user_id): 
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("UPDATE id"+str(user_id)+" SET L_message='%s' WHERE user_id=%d" % ("удалено", user_id))
    con.commit()

    cur.close()
    con.close()

#удаление мешающих данных из таблицы,что бы не мешать другим if
def checkanswerandquestion(user_id): 
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("SELECT answer FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    answer = cur.fetchone()
    
    cur.execute("SELECT question FROM id"+str(user_id)+" WHERE user_id='%s'" % user_id)
    question = cur.fetchone()

    cur.close()
    con.close()
    return answer,question

#удаление вопроса и ответа из БД(base_USER)
def del_answer_question(user_id): 
    con = sqlite3.connect('./base_USER.db')
    cur = con.cursor()
    
    cur.execute("UPDATE id"+str(user_id)+" SET answer='%s' WHERE user_id ='%s'" % (None, user_id))
    con.commit() 

    cur.execute("UPDATE id"+str(user_id)+" SET question='%s' WHERE user_id ='%s'" % (None, user_id))
    con.commit() 

    cur.close()
    con.close()