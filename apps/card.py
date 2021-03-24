import sys
sys.path.insert(0, '/apps')

from apps import data_base
from apps import data_lessons
from apps.form_for_send_message import private_send_message
from apps import keyboards


#генерация вопроса с ответом
def generating_a_question_with_an_answer(vk_session,user_id,msg,vk_api,lesson):
    question = data_lessons.questions(vk_session,user_id,msg,vk_api,lesson)
    answer = data_lessons.answer(user_id,lesson,question)
    if answer is not None:       
        answer = answer[0]
    data_lessons.update_last_sesson(user_id,lesson)
    return answer, question

#запись в БД ответа и вопроса
def question1(user_id,lesson,vk_session,msg,vk_api):
    answer ,question= generating_a_question_with_an_answer(vk_session,user_id,msg,vk_api,lesson)
    data_lessons.receiving_and_memory_answer_and_question(question,answer,user_id)
    if question is not None:
        private_send_message(vk_session, user_id, question, None, keyboards.check_Cards)
    
#проверка ответил ли пользователь верно
def question2(user_id,msg,vk_session):
    answer = data_lessons.getting_a_response(user_id)
    if answer is not None:
        answer = answer[0]
    if msg == answer and answer != "None":
        private_send_message(vk_session, user_id, "Вы ответили верно🎉🎊", None, keyboards.delete_a_card_and_farther)
    elif msg != answer and answer != "None":
        private_send_message(vk_session, user_id, "Вы не правы🤷‍♂\nПравильный ответ: "+answer, None, keyboards.delete_a_card_and_farther)
        #data_lessons.delite_message(user_id)
    if answer == "None":
        answer = "yes"
    else:
        answer = "no"

    return answer

def cards(vk_session,user_id, msg, L_message, LL_message):

    lesson_now = data_base.getting_a_sequence(user_id)
    if lesson_now is not None:
        lesson_now = lesson_now[0]
    else:
        lesson_now = "None"

    #Физика 
    if LL_message == "Физика" and lesson_now == "Физика2" and msg != "Назад":
        lesson = "physics"
        lesson_promo = "physics_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "Физика" and lesson_now == "Физика3" and msg != "Назад":
            lesson_promo = "physics_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Физика2"
            data_base.sequence(user_id,lesson_now)
        else:
            if msg == "Физика" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Физика3"
                data_base.sequence(user_id,lesson_now)
    
        
    #Английский
    if LL_message == "Английский" and lesson_now == "Английский2" and msg != "Назад":
        lesson = "English"
        lesson_promo = "English_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "Английский" and lesson_now == "Английский3" and msg != "Назад":
            lesson_promo = "English_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Английский2"
            data_base.sequence(user_id,lesson_now)
        else:
            if msg == "Английский" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Английский3"
                data_base.sequence(user_id,lesson_now)
    
    #Биология
    if LL_message == "Биология" and lesson_now == "Биология2" and msg != "Назад":
        lesson = "biology"
        lesson_promo = "biology_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "Биология" and lesson_now == "Биология3"  and msg != "Назад":
            lesson_promo = "biology_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Биология2"
            data_base.sequence(user_id,lesson_now)
                
        else:
            if msg == "Биология" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Биология3"
                data_base.sequence(user_id,lesson_now)

    
    #История
    if LL_message == "История" and lesson_now == "История2" and msg != "Назад":
        lesson = "history"
        lesson_promo = "history_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "История" and lesson_now == "История3" and msg != "Назад":
            lesson_promo = "history_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "История2"
            data_base.sequence(user_id,lesson_now)
        else:
            if msg == "История" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "История3"
                data_base.sequence(user_id,lesson_now)

    #Литература
    if LL_message == "Литература" and lesson_now == "Литература2" and msg != "Назад":
        lesson = "literature"
        lesson_promo = "literature_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "Литература" and lesson_now == "Литература3" and msg != "Назад":
            lesson_promo = "literature_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Литература2"
            data_base.sequence(user_id,lesson_now)

        else:
            if msg == "Литература" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Литература3"
                data_base.sequence(user_id,lesson_now)

    #музыка
    if LL_message == "Музыка"and lesson_now == "Музыка2" and msg != "Назад":
        lesson = "music"
        lesson_promo = "music_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "Музыка" and lesson_now == "Музыка3" and msg != "Назад":
            lesson_promo = "music_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Музыка2"
            data_base.sequence(user_id,lesson_now)    
        else:
            if msg == "Музыка" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Музыка3"
                data_base.sequence(user_id,lesson_now)

    #Французский
    if LL_message == "Французский" and lesson_now == "Французский2" and msg != "Назад":
        lesson = "French"
        lesson_promo = "French_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now)
    else:
        if L_message == "Французский" and lesson_now == "Французский3" and msg != "Назад":
            lesson_promo = "French_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Французский2"
            data_base.sequence(user_id,lesson_now)   
    
        else:
            if msg == "Французский" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Французский3"
                data_base.sequence(user_id,lesson_now)   


    
    #Обществознаение
    if LL_message == "Обществознаение" and lesson_now == "Обществознаение2" and msg != "Назад":
        lesson = "social_studies"
        lesson_promo = "social_studies_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now) 
    else:
        if L_message == "Обществознаение" and lesson_now == "Обществознаение3" and msg != "Назад":
            lesson_promo = "social_studies_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Обществознаение2"
            data_base.sequence(user_id,lesson_now)     
        else:
            if msg == "Обществознаение" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Обществознаение3"
                data_base.sequence(user_id,lesson_now) 
    
    #Русский
    if LL_message == "Русский" and lesson_now == "Русский2" and msg != "Назад":
        lesson = "Russian"
        lesson_promo = "Russian_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now) 
    else:
        if L_message == "Русский" and lesson_now == "Русский3" and msg != "Назад":
            lesson_promo = "Russian_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Русский2"
            data_base.sequence(user_id,lesson_now) 
    
        else:
            if msg == "Русский" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Русский3"
                data_base.sequence(user_id,lesson_now) 


    #Физкультура
    if LL_message == "Физкультура" and lesson_now == "Физкультура2" and msg != "Назад":
        lesson = "physical_education"
        lesson_promo = "physical_education_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now) 
    else:
        if L_message == "Физкультура" and lesson_now == "Физкультура3" and msg != "Назад":
            lesson_promo = "physical_education_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Физкультура2"
            data_base.sequence(user_id,lesson_now)     
        else:
            if msg == "Физкультура" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Физкультура3"
                data_base.sequence(user_id,lesson_now) 
        
    #Химия
    if LL_message == "Химия" and lesson_now == "Химия2" and msg != "Назад":
        lesson = "chemistry"
        lesson_promo = "chemistry_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now) 
    else:
        if L_message == "Химия" and lesson_now == "Химия3" and msg != "Назад":
            lesson_promo = "chemistry_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Химия2"
            data_base.sequence(user_id,lesson_now)  
        else:
            if msg == "Химия" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопрос", None, keyboards.record_Cards)
                lesson_now = "Химия3"
                data_base.sequence(user_id,lesson_now) 
    #Алгебра
    if LL_message == "Алгебра" and lesson_now == "Алгебра2" and msg != "Назад":
        lesson = "algebra"
        lesson_promo = "algebra_promo"
        data_lessons.question_answer(msg,user_id,lesson,lesson_promo)
        private_send_message(vk_session, user_id, "Записано👍", None, keyboards.record_Cards)
        lesson_now = None
        data_base.sequence(user_id,lesson_now) 
    else:
        if L_message == "Алгебра" and lesson_now == "Алгебра3" and msg != "Назад":
            lesson_promo = "algebra_promo"
            data_lessons.promo_question(msg,user_id,lesson_promo)
            private_send_message(vk_session, user_id, "Напишите ответ", None, keyboards.record_Cards)
            lesson_now = "Алгебра2"
            data_base.sequence(user_id,lesson_now) 
        else:
            if msg == "Алгебра" and lesson_now == "None":
                private_send_message(vk_session, user_id, "Напишите вопросы", None, keyboards.record_Cards)
                lesson_now = "Алгебра3"
                data_base.sequence(user_id,lesson_now) 



def checking_the_answer(user_id, msg, L_message,vk_session,vk_api):

    lesson = data_base.getting_a_sequence(user_id)

    if lesson is not None:
        lesson = lesson[0]
    else:
        lesson = "None"


    if msg == "тФизика" or L_message == "тФизика" and msg != "Назад":
        if lesson == "physics" or lesson == "None":
            if L_message == "тФизика" and lesson == "physics":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тФизика" and lesson == "None":
                lesson = "physics"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer
            
            else:
                if msg == "тФизика":
                    lesson = "physics"
                    question1(user_id,lesson,vk_session,msg,vk_api)
    
    if msg == "тАнглийский" or L_message == "тАнглийский" and msg != "Назад":
        if lesson == "English" or lesson == "None":
            if L_message == "тАнглийский" and lesson == "English":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тАнглийский" and lesson == "None":
                lesson = "English"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer
            
            else:
                if msg == "тАнглийский":
                    lesson = "English"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    if msg == "тЛитература" or L_message == "тЛитература" and msg != "Назад":
        if lesson == "literature" or lesson == "None":
            if L_message == "тЛитература" and lesson == "literature":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тЛитература" and lesson == "None":
                lesson = "literature"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тЛитература":
                    lesson = "literature"
                    question1(user_id,lesson,vk_session,msg,vk_api)
    


    if msg == "тБиология" or L_message == "тБиология" and msg != "Назад":
        if lesson == "biology" or lesson == "None":
            if L_message == "тБиология" and lesson == "biology":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тБиология" and lesson == "None":
                lesson = "biology"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тБиология":
                    lesson = "biology"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    if msg == "тМузыка" or L_message == "тМузыка" and msg != "Назад":
        if lesson == "music" or lesson == "None":
            if L_message == "тМузыка" and lesson == "music":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тМузыка" and lesson == "None":
                lesson = "music"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer
            
            else:
                if msg == "тМузыка":
                    lesson = "music"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    if msg == "тОбществознание" or L_message == "тОбществознание" and msg != "Назад":
        if lesson == "social_studies" or lesson == "None":
            if L_message == "тОбществознание" and lesson == "social_studies":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тОбществознание" and lesson == "None":
                lesson = "social_studies"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer
            
            else:
                if msg == "тОбществознание":
                    lesson = "social_studies"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    if msg == "тФизкультура" or L_message == "тФизкультура" and msg != "Назад":
        if lesson == "physical_education" or lesson == "None":
            if L_message == "тФизкультура" and lesson == "physical_education":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тФизкультура" and lesson == "None":
                lesson = "physical_education"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тФизкультура":
                    lesson = "physical_education"
                    question1(user_id,lesson,vk_session,msg,vk_api)
    

    
    if msg == "тРусский" or L_message == "тРусский" and msg != "Назад":
        if lesson == "Russian" or lesson == "None":
            if L_message == "тРусский" and lesson == "Russian":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer   

            if msg == "тРусский" and lesson == "None":
                lesson = "Russian"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тРусский":
                    lesson = "Russian"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    if msg == "тХимия" or L_message == "тХимия" and msg != "Назад":
        if lesson == "chemistry" or lesson == "None":
            if L_message == "тХимия" and lesson == "chemistry":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тХимия" and lesson == "None":
                lesson = "chemistry"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тХимия":
                    lesson = "chemistry"
                    question1(user_id,lesson,vk_session,msg,vk_api)
    
    if msg == "тИстория" or L_message == "тИстория" and msg != "Назад":
        if lesson == "history" or lesson == "None":
            if L_message == "тИстория" and lesson == "history":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тИстория" and lesson == "None":
                lesson = "history"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тИстория":
                    lesson = "history"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    if msg == "тФранцузский" or L_message == "тФранцузский" and msg != "Назад":
        if lesson == "French" or lesson == "None":
            if L_message == "тФранцузский" and lesson == "French":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тФранцузский" and lesson == "None":
                lesson = "French"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тФранцузский":
                    lesson = "French"
                    question1(user_id,lesson,vk_session,msg,vk_api)

    
    if msg == "тАлгебра" or L_message == "тАлгебра" and msg != "Назад":
        if lesson == "algebra" or lesson == "None":
            if L_message == "тАлгебра" and lesson == "algebra":
                answer = question2(user_id,msg,vk_session)
                lesson = None
                data_base.sequence(user_id,lesson)
                return answer

            if msg == "тАлгебра" and lesson == "None":
                lesson = "algebra"
                data_base.sequence(user_id,lesson)
                question1(user_id,lesson,vk_session,msg,vk_api)
                answer = "yes"
                return answer

            else:
                if msg == "тАлгебра":
                    lesson = "algebra"
                    question1(user_id,lesson,vk_session,msg,vk_api)


    else:
        answer ,question = data_lessons.checkanswerandquestion(user_id)
        answer = answer[0]
        question = question[0]
        if question == "None" and answer == "None":
            data_lessons.del_answer_question(user_id)


#фикс кучи ошибок
def grebanaya_proverka_12if(msg,L_message,user_id):
    lesson_now = None

    if msg == "тАнглийский":
        if L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
        
    elif msg == "тБиология":
        if L_message == "тБиология" or L_message == "тАнглийский" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)

    elif msg == "тАлгебра":
        if L_message == "тАлгебра" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
    
    elif msg == "тИстория":
        if L_message == "тИстория" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
    
    elif msg == "тЛитература":
        if L_message == "тЛитература" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
        
    elif msg == "тМузыка":
        if L_message == "тМузыка" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
        
    elif msg == "тФизкультура":
        if L_message == "тФизкультура" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
        
    elif msg == "тФранцузский":
        if L_message == "тФранцузский" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
    
    elif msg == "тФизика":
        if L_message == "тФизика" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тОбществознание" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
        
    elif msg == "тОбществознание":
        if L_message == "тОбществознание" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тРусский" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
    
    elif msg == "тРусский":
        if L_message == "тРусский" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тХимия":
            data_base.sequence(user_id,lesson_now)
        
    elif msg == "тХимия":
        if L_message == "тХимия" or L_message == "тАлгебра" or L_message == "тАнглийский" or L_message == "тБиология" or L_message == "тАлгебра" or L_message == "тИстория" or L_message == "тЛитература" or L_message == "тМузыка" or L_message == "тФизкультура" or L_message == "тФранцузский" or L_message == "тФизика" or L_message == "тОбществознание" or L_message == "тРусский":
            data_base.sequence(user_id,lesson_now)
            