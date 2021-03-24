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
        super().__init__(name=input("What is your characters name?"),thaco=20,ac=10,
                         hp=10,inventory={},exp=10)
    prof = "fighter"
    maxhp=10
    level=1
    hd=10
    level2=20

class Cleric(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"),thaco=20,ac=10,
                         hp=8,inventory={},exp=8)
    prof= "cleric"
    maxhp=8
    level=1
    hd=8
    level2=15

class Mage(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"),thaco=20,ac=10,
                         hp=4,inventory={},exp=4)
    prof= "mage"
    mana=1
    maxmana=1
    maxhp=4
    level=1
    hd=4
    level2=10

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