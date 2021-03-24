import sqlite3 #импортирования модуля для работы с БД
def base_lesson_user(user_id):
    con = sqlite3.connect('./base_lessons_folder/users/'+str(user_id)+'.db') #подключение к БД
    cur = con.cursor() #подключение курсора

    # проверка на наличие таблицы с физикой
    cur.execute('CREATE TABLE IF NOT EXISTS physics(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для физики
    cur.execute('CREATE TABLE IF NOT EXISTS physics_promo(Id TEXT, question TEXT,answer TEXT)')
        
    # проверка на наличие таблицы с английским
    cur.execute('CREATE TABLE IF NOT EXISTS English(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для английским
    cur.execute('CREATE TABLE IF NOT EXISTS English_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с биологией
    cur.execute('CREATE TABLE IF NOT EXISTS biology(Id TEXT, question TEXT, answer TEXT, number TEXTT)')
    # проверка на наличие промежуточной таблицы для биологии
    cur.execute('CREATE TABLE IF NOT EXISTS biology_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с информатикой
    cur.execute('CREATE TABLE IF NOT EXISTS informatics(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для информатикой
    cur.execute('CREATE TABLE IF NOT EXISTS informatics_promo(Id TEXT, question TEXT,answer TEXT)')
        
    # проверка на наличие таблицы с историей
    cur.execute('CREATE TABLE IF NOT EXISTS history(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для истории
    cur.execute('CREATE TABLE IF NOT EXISTS history_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с литературой
    cur.execute('CREATE TABLE IF NOT EXISTS literature(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для литературы
    cur.execute('CREATE TABLE IF NOT EXISTS literature_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с музыкой
    cur.execute('CREATE TABLE IF NOT EXISTS music(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для музыки
    cur.execute('CREATE TABLE IF NOT EXISTS music_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с немецким
    cur.execute('CREATE TABLE IF NOT EXISTS German(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для немецкого
    cur.execute('CREATE TABLE IF NOT EXISTS German_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с французским
    cur.execute('CREATE TABLE IF NOT EXISTS French(Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для французского
    cur.execute('CREATE TABLE IF NOT EXISTS French_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с ОБЖ
    cur.execute('CREATE TABLE IF NOT EXISTS OBJ (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для ОБЖ
    cur.execute('CREATE TABLE IF NOT EXISTS OBJ_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с обществознанием
    cur.execute('CREATE TABLE IF NOT EXISTS social_studies (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для обществознания
    cur.execute('CREATE TABLE IF NOT EXISTS social_studies_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с русским
    cur.execute('CREATE TABLE IF NOT EXISTS Russian (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для русского
    cur.execute('CREATE TABLE IF NOT EXISTS Russian_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с технологией
    cur.execute('CREATE TABLE IF NOT EXISTS technology (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для технологии
    cur.execute('CREATE TABLE IF NOT EXISTS technology_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с физрой
    cur.execute('CREATE TABLE IF NOT EXISTS physical_education (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для физры
    cur.execute('CREATE TABLE IF NOT EXISTS physical_education_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с химией
    cur.execute('CREATE TABLE IF NOT EXISTS chemistry (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для химии
    cur.execute('CREATE TABLE IF NOT EXISTS chemistry_promo(Id TEXT, question TEXT,answer TEXT)')

    # проверка на наличие таблицы с алгеброй
    cur.execute('CREATE TABLE IF NOT EXISTS algebra (Id TEXT, question TEXT, answer TEXT, number TEXT)')
    # проверка на наличие промежуточной таблицы для алгебры
    cur.execute('CREATE TABLE IF NOT EXISTS algebra_promo(Id TEXT, question TEXT,answer TEXT)')

    cur.close() #отключение курсора
    con.close() #отключение от БД