import random

#тут генирируется ответ пользователю ,учить ли ему
def teach_or_not_teach_random(): 
    random_number = random.randint(1,100)

    if random_number < 2:
        teach = "Тебе повезло)\nМожешь не учить🤐"
    else:
        teach = "Учи давай🙃\nУдачи🍀"
    
    return teach
