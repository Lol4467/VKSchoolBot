health = 100
coins = 0
tutorial = True
gameStart = True
death  = False
spawn = True
livingRoom = False
Bathroom = False
Bedroom = False
Kitchen = False
wardrobeSpawn = False
spawnStart = True
telev = False


def countCoins():
    print("\n")
    print("You have: " + str(coins) + " coins")


while gameStart == True:
    if spawn == True:
        if spawnStart == True:
            print("\n")
            print("You wake up in a room you don't recognise, with no idea how you got there")
            print("\n")
            print("You look around and see a wardrobe and a door")
            spawnStart = False
        elif spawnStart == False:
            print("\n")
            spawnIn = input("")
            spawnIn = spawnIn.lower()
            if spawnIn == "coins":
                countCoins()
                spawnStart = False
            elif spawnIn == "wardrobe":
                if wardrobeSpawn == False:
                    print("\n")
                    print ("The wardrobe seems quite empty, but you do find a coin in the far left corner, you put it in your pocket")
                    print("\n")
                    coins += 1
                    wardrobeSpawn = True
                    spawnStart = False
                elif wardrobeSpawn == True:
                    print ("This wardrobe looks oddly familiar, you have already explored it")
                    print("\n")
                    spawnStart = False
            elif spawnIn == "door":
                print("\n")
                print ("You walk out the door")
                print("\n")
                spawn = False
                livingRoom = True
            elif spawnIn == "look":
                print("You look around and see a wardrobe and a door")
                print("\n")
                spawnStart = False
            else:
                print("That is an unvalid command. Try again")
                print("\n")
                spawnStart = False