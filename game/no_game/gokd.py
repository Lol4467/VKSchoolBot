from sys import exit

def start():
       print("You are in an old temple.")
       print("There is a door to your right and left or you can walk forwad.")
       print("Which one do you take?")

       choice = input("> ")

       if choice == "left":
           gold_room()
       elif choice == "right":
           trap_room()
       elif choice == "forward":
           monster_room()
       else:
           dead("you got caught by the ancient gods and you must be killed.")


def monster_room():
       print("you're in a room with a monster. what you gonna do?")

       choice = input("> ")
       if "left" in choice:
           print("you are going to the gold room")
           gold_room()
       elif "right" in choice:
           print("you are going to the trap room")
           trap_room()
       else:
           dead("couldn't understand what did you say so you are dead!")


def gold_room():
       print("you chose the left room. now you are in a room with a pot of gold!")
       print("you can take the pot.")
       print("or you can just rob the money in it.")
       print("or you go go to other rooms.")

       choice = input("> ")

       if choice == "take the pot":
           print("you are a millionaire from now on!!!")
       elif choice == "rob the money":
           dead("you will never rest in piece!")
       elif choice == "another room":
           monster_room()


def trap_room():
       print("you are now in a trap room.")
       print("there is a hidden trap in this room.")
       print("be careful!")
       print("you can go back to the  monster room")
       print("or you can find the trap")

       choice = input("> ")

       if "find" in choice:
           start()
       elif "back" in choice:
           gold_room()


def dead(why):
       print(why, "rekt!")
       exit(0)

start()