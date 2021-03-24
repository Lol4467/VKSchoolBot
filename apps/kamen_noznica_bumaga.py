import random


def player_vs_comp_normal(msg):

    comp = random.randint(1, 3)
    player = msg
    win = 0

    # определяем победителя
    if player == comp:
        win = 0
    elif player == "Камень" and comp == 2:
        win = 1
    elif player == "Камень" and comp == 3:
        win = 2
    elif player == "Ножницы" and comp == 1:
        win = 2
    elif player == "Ножницы" and comp == 3:
        win = 1
    elif player == "Бумага" and comp == 1:
        win = 1
    elif player == "Бумага" and comp == 2:
        win = 2
    
    if win == 0:
        answer = "Ничья!"
    elif win == 1:
        answer = "Вы победили!!!!🎊🎉"
    elif win == 2:
        answer = "Вы проиграли!🙃"

    if comp == 1:
        bot = "Бот выбрал камень!!!"
    elif comp == 2:
        bot = "Бот выбрал ножницы!!!"
    elif comp == 3:
        bot = "Бот выбрал бумагу!!!"
    
    return answer, bot


