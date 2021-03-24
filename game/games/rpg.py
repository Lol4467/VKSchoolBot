from random import randint

#CLASS
class Dice:    
    def die(num):
        die=randint(1,num)
        return die

class Character:
    def __init__(self,name,hp,thaco,ac,inventory,exp):
        self.name=name
        self.hp=hp
        self.thaco=thaco
        self.ac=ac
        self.inventory=inventory
        self.exp=exp


class Fighter(Character):
    def __init__(self):
        super().__init__(name=input("Какое имя будет у твоего персонажа?"),thaco=20,ac=10,
                         hp=10,inventory={},exp=10)
    prof = "fighter"
    maxhp = 10
    level = 1
    hd = 10
    next_level = 20

class Cleric(Character):
    def __init__(self):
        super().__init__(name=input("Какое имя будет у твоего персонажа?"),thaco=20,ac=10,
                         hp=8,inventory={},exp=8)
    prof = "cleric"
    maxhp = 8
    level =1 
    hd = 8
    next_level = 15

class Mage(Character):
    def __init__(self):
        super().__init__(name=input("Какое имя будет у твоего персонажа?"),thaco=20,ac=10,
                         hp=4,inventory={},exp=4)
    prof = "mage"
    mana = 1
    maxmana = 1
    maxhp = 4
    level = 1
    hd = 4
    next_level = 10

class Goblin(Character):
    def __init__(self):
        super().__init__(name="goblin",
                         hp=7,thaco=20,
                         ac=6,inventory={},
                         exp=7)


class Orc(Character):
    def __init__(self):
        super().__init__(name="orc",
                         hp=8,thaco=18,
                         ac=6,inventory={},
                         exp=8)



#----------------------------------------------------------------------------------------------------------------------

def rpg():
    
    def profession():
        pclass = "Клерк"

        msg_for_user = ("Какого персанажа ты выбираешь?\nВоин\nКлерк\nМаг\n")
        print(msg_for_user)

        
        if pclass =="Воин":
            Prof = Fighter()
        elif pclass=="Клерк":
            Prof = Cleric()
        elif pclass == "Маг":
            Prof = Mage()

        return Prof

    def ranmob():
        mob = Goblin() if Dice.die(2)<2 else Orc()
        return mob


    def playerAttack():
        roll=Dice.die(20)   

        if roll>=hero.thaco-mob.ac:
            print("Есть попадание")

            if hero.prof=="fighter":
                rollD=Dice.die(10)

            if hero.prof=="cleric":
                rollD=Dice.die(6)

            if hero.prof=="mage":
                rollD=Dice.die(4)

            print("Ты нанес",rollD,"урона")

            mob.hp-=rollD

            print("у",mob.name,"осталось",mob.hp,"hp")

        else:
            print("Промах")

    def monsterAttack():
        roll=Dice.die(20)

        if roll>=mob.thaco-hero.ac:
            print("Монстер попал")

            if mob.name=="goblin":     
                rollD=Dice.die(4)

            elif mob.name=="orc":
                rollD=Dice.die(6)

            print(mob.name,"нанес",rollD,"урона")
            hero.hp-=rollD
            print("у",hero.name,"осталось",hero.hp,"hp")
        else:
            print("Монстер промазал")


    def levelUp():

        levelGain=False

        while hero.exp>=hero.next_level:

            hero.level+=1
            levelGain=True

            hero.next_level = hero.next_level*2

            if levelGain==True:

                hero.maxhp += Dice.die(hero.hd)
                hero.hp = hero.maxhp
                
                hero.thaco -= 1 #уворотливость падает с каждым уровнем

                if hero.prof == "mage":

                    hero.maxmana += 1
                    hero.mana = hero.maxmana

                print("Ты получил новый уровень","\n",'hp:',hero.hp,"\n",'уровень:',hero.level)
                


    def commands():

        if hero.prof == "fighter":
            print("Выберите действие")
            command = input()

            if command == "Удар":            
                playerAttack()
            
        if hero.prof == "cleric":

            print("Выберите действие")
            command = input()

            if command == "Удар":            
                playerAttack()

            elif command == "Лечение":

                if hero.hp < hero.maxhp:
                    hero.hp += Dice.die(8)   

                    if hero.hp > hero.maxhp:
                        hero.hp = hero.hp - (hero.hp - hero.maxhp)        

                    print("Сейчас у теюя:",hero.hp,"hp")

                else:

                    print("Твое здоровье полное")

                    commands()

            

        if hero.prof=="mage":

            print (" press f to fight",'\n',
                "press s for spells",'\n',
                "press m to generate mana",'\n',
                "press enter to pass")
            command=input("~~~~~~~~~Press a key to Continue.~~~~~~~")
            if command=="f":            
                playerAttack()
            elif command =="s":
                print("You have",hero.mana,"mana")
                if hero.mana>=1 and hero.mana<3:
                    print("press s for sleep",'\n',
                        "press m for magic missile")
                    command=input(">>>")
                    if command =="s":
                        print("You put the monster to sleep it is easy to kill now")
                        mob.hp-=mob.hp
                        hero.mana-=1
                    if command=="m":
                        if hero.mana<hero.maxmana:
                            hero.mana+=Dice.die(4)                
                            if hero.mana>hero.maxmana:
                                hero.mana-=(hero.mana-hero.maxmana)
                        dam =Dice.die(4)*hero.mana
                        mob.hp-=dam
                        print("You use all your mana! and do",dam,"damage!")
                        hero.mana-=hero.mana
                elif hero.mana>=3:
                    print("press s for sleep",'\n',
                        "press m for magic missile",'\n',
                        "press f for fireball")
                    command=input(">>>")
                    if command =="s":
                        print("You put the monster to sleep it is easy to kill now")
                        mob.hp-=mob.hp
                        hero.mana-=1
                    if command=="m":
                        dam=Dice.die(4)*hero.mana
                        mob.hp-=dam
                        print("You use all your mana! and do",dam,"damage!")
                        hero.mana-=hero.mana
                    if command=="f":
                        print("You are temporarily blinded by a feiry flash of light.")
                        dam=0
                        dam+=Dice.die(6)
                        dam+=Dice.die(6)
                        dam+=Dice.die(6)
                        mob.hp-=dam
                        print("You did",dam,"points of damage")

                        hero.mana-=3
                else:
                    print("Your mana is empty")
                    commands()
            elif command =="m":
                if hero.mana<hero.maxmana:
                    hero.mana+=1
                    print("You have",hero.mana,"mana")
                elif hero.mana>=hero.maxmana:
                    print("Your mana is full.")
                    print("You have",hero.mana,"mana")
                    commands()

            elif command=="":
                pass

    mob=ranmob()
    hero=profession()

    while True:

        if mob.hp <= 0:
            print(mob.name,'погиб!')        
            hero.exp += mob.exp

            print('Опыт игрока',hero.exp)

            mob=ranmob()

        if hero.hp <= 0:

            print('Вы погибли!')
             
            hero=profession()
            

        levelUp()


        print("Впереди тебя",mob.name+",",mob.name,"с",mob.hp,"hp.")

        if hero.hp > 0:
            commands()

        if mob.hp > 0:                
            monsterAttack()

rpg()