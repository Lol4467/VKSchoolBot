from random import shuffle
from apps import data_door


def three_door(msg,user_id):

    if msg == "1" or msg == "2" or msg == "3":
        msg = int(msg)

        doors = ['dragon','dragon', 'water', 'empty', 'empty']
        shuffle(doors)
        
        lives,score = data_door.getting_health_score(user_id)

        lives = int(lives)
        score = int(score)

        event = None
        lives_score = None

        if doors[msg - 1] == 'dragon':
            score += 100
            lives -= 1

            health = lives
            data_door.dragon_water(user_id,health,score)

            event = '\nВы попали в комнату с драконом\n-1 ❤'
            lives_score = "\n\nУ вас осталось: " + str(lives) + " ❤\nВаш счет: " + str(score) + "\n"
            
            
        elif doors[msg - 1] == 'water':
            score += 100
            lives += 1

            health = lives
            data_door.dragon_water(user_id,health,score)

            event = '\nВы попали в комнату с живой водой\n+1 ❤'
            lives_score = "\n\nУ вас осталось: " + str(lives) + " ❤\nВаш счет: " + str(score) + "\n"

        else:
            score += 100
            data_door.empty_gameower(user_id,score)

            event = '\nВы попали в пустую комнату\nНичего не произошло'
            lives_score = "\n\nУ вас осталось: " + str(lives) + " ❤\nВаш счет: " + str(score) + "\n"

        if lives == 0:

            my_record = data_door.getting_my_record(user_id)
            my_record = int(my_record)
            data_door.new_my_record(user_id,score)

            if my_record > score:

                raznica = my_record - score
                event = '\nВы попали в комнату с драконом\n-1 ❤\n\nВы погибли от лапок дракона\nВаш финальный счет: '+ str(score) +'\n\nВам не хватило '+str(raznica)+' баллов до вашего рекорда'
            
            elif my_record == score:
                event = '\nВы попали в комнату с драконом\n-1 ❤\n\nВы погибли от лапок дракона\nВаш финальный счет: '+ str(score) +'\n\nВы почти побили свой рекорд, так держать'
            
            elif my_record < score:
                event = '\nВы попали в комнату с драконом\n-1 ❤\n\nВы погибли от лапок дракона\nВаш финальный счет: '+ str(score) +'\n\nВы побили свой рекорд, но всегда можно достичь большего'
            
            lives_score = None

            score = 0
            data_door.empty_gameower(user_id,score)
        
        return event, lives_score