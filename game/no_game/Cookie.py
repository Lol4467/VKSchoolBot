""" A text game "Bob, the Cookie Cooker". """

import random

COINS_FOR_WIN        = 1000000
FINE_COOKIE_PRICE    =      30
POOR_COOKIE_PRICE    =      10
PRICE_DEVIATION      =       5
HUGE_DOUGH_AMOUNT    =    1000
DOUGH_PRICE          =      10
MAX_LOAN             =   10000
LOAN_PRICE           =     100
TICKET_PRICE         =       1
LOTTERY_PRIZE        =       2
BEG_MONEY            =       8
TIME_COOKIE_COOK     =       1
TIME_BIG_DEAL        =      60
TIME_SMALL_DEAL      =      30
TIME_GRANDMA         =      60
TIME_BANK_SERVICE    =       5
TIME_LOTTERY         =       1
TIME_BEGGING         =    1440
CHANCE_LOTTERY       =    1000
CHANCE_SKILL_COOK    =    1000
CHANCE_SKILL_GRANDMA =     100

cookies = 0
minutes = 0
skill   = 0
coins   = 0
dough   = 0
bribe   = 1
debt    = 0
term    = 0

def main():
       """ The main function. """
       intro()
       while menu():
           if check_for_end():
               break

def intro():
       """ Print's out a welcoming string. """
       print ( """
                                       .--,--.
                                       '.  ,.'          Bob,
                                        |___|    the Cookie Cooker
                                        :o o:   O      
                                       _'~^~'_  |  
                                     /'   ^   '\=)
                                   .'  _______ '~|
                                   '(<=|     |= /'
                                       |     |
                                       |_____|
                                ~~~~~~~ ===== ~~~~~~~~
               """ )
       print ("\tWelcome, my dear player! I am Bob, the Cookie Cooker! I dream to")
       print ("\tcook my way to the top.  But I am not a smart guy, so that's why")
       print ("\tI'm talking to You. I need your guidance. Please, turn me into a")
       print ("\tCookie Master!  Help me to become rich and famous!  So let's go!")
       print ()

def menu():
       """ Player selects action he/she wants to do. """
       methods = { 1: work, 2: buy, 3: grandma, 4: bank, 5: lottery, 6: beg}
       print ("Cookies made: {}. Game-time spent: {}.".format(cookies, minutes))
       print ("Skill: {}%. Coins: {}. Dough: {} kg.".format(skill, coins, dough))
       print ( """
                    Action:
                            1. Go to work.
                            2. Go to supermarket.
                            3. Visit grandma.
                            4. Visit bank.
                            5. Buy a lottery ticket.
                            6. Beg for money.
                            7. Exit.
               """ )
       selection = get_valid_int(1, 7)
       if selection != 7:
           methods[selection]()
           return True
       else:
           return False

def get_valid_int(min_bound, max_bound):
       """ Prompts input until a positive integer in provided range is entered. """
       while True:
           user_input = input(">> ")
           if is_int(user_input):
               user_input = int(user_input)
               if min_bound != None and user_input < min_bound:
                   print ("Number is too small.")
                   continue
               if max_bound != None and user_input > max_bound:
                   print ("Number is too big.")
                   continue
               break
       return user_input

def is_int(string):
       """ Returns if string can be converted into a positive integer or 0. """
       try:
           value = int(string)
           return True
       except ValueError:
           print ("Input is not n integer.")
           return False

def work():
       """ Player cooks & sells specified amount of cookies. """
       print ("How many cookies do you want to cook?")
       amount = get_valid_int(0, None)
       cookie_loop(amount)

def cookie_loop(amount):
       """ Tries to cook and sell the specified amount of cookies. """
       global minutes
       for i in range(amount):
           minutes += TIME_COOKIE_COOK
           if dough > 0:
               cook_cookie(i)
           else:
               be_confused(i)

def cook_cookie(i):
       """ Cooks and sells a cookie. """
       global cookies, skill, coins, dough
       cookies += 1
       dough   -= 1
       price = random.randrange(PRICE_DEVIATION)
       if random.randrange(101) > skill:
           # A poor cookie is cooked
           price += POOR_COOKIE_PRICE
           print ("You sell a poor cookie #{} for {} coins.".format(i+1, price))
       else:
           # A fine cookie is cooked
           price += FINE_COOKIE_PRICE
           print ("You sell a FINE cookie #{} for {} coins.".format(i+1, price))
       coins += price
       # There's a 1 in a CHANCE_SKILL_COOK to improve your skill by 1%:
       if random.randrange(CHANCE_SKILL_COOK) == 42 and skill < 100:
           skill += 1

def be_confused(i):
       """ Stands confused for no dough is left. """
       print ("Minute #{} passes. You're confused - no dough is left.".format(i+1))

def buy():
       """ Player visits the supermarket to buy dough. """
       global minutes, coins, dough
       print ("Hello! We are the biggest supermarket in town. We only sell dough.")
       print ("How much would you like?")
       offer = get_valid_int(0, None)
       if offer == 0:
           print ("Well, okay then.")
       elif offer > HUGE_DOUGH_AMOUNT and offer * (DOUGH_PRICE / 2) <= coins:
           # Big deals come 50% off
           print ("Wow. That's a big deal! It's 50% for big clients. Here you go!")
           coins -= int (offer * (DOUGH_PRICE / 2) )
           minutes += TIME_BIG_DEAL
       elif offer * DOUGH_PRICE <= coins:
           # Standart deals for standart clients
           print ("Thank you for using our services. Come again!")
           coins -= int (offer * DOUGH_PRICE)
           minutes += TIME_SMALL_DEAL
       else:
           print ("I appreciate your intentions, but you don't have enough money.")
           return
       dough += offer

def grandma():
       global minutes, skill, coins, bribe
       """ Player visits grandma to get some cookie cooking experience. """
       print ("Gradma: howdy son! Me sees ya wanna get some tips, so tell me ")
       print ("how much ya hearts says you shoulda give me.")
       offer = get_valid_int(0, coins)
       if offer < bribe:
           print ("Ya greedy bastard! You think wisdom comes for free?")
           print ("Me teach ya a lesson and take your money for nothin'.")
       else:
           bribe += offer
           print ("Grandma tells you a secret cookie cooking secret.")
           if random.randrange(CHANCE_SKILL_GRANDMA) == 7 and skill <= 95:
               # There's 1 in CHANCE_SKILL_GRANDMA to increase your skill by 5%
               skill += 5
       minutes += TIME_GRANDMA
       coins -= offer

def bank():
       """ Player goes to bank to loan some coins or to repay his debts. """
       print ("Bank: we loan up to {} for {} coins.".format(MAX_LOAN, LOAN_PRICE))
       print ("Don't forget that we find everyone who doesn't repay in time.")
       print ("Enter '1' to request a loan.")
       print ("Enter '2' to repay your debt.")
       print ("Enter '3' for a term reminder.")
       print ("Enter '4' to exit the bank.")
       selection = get_valid_int(1, 4)
       if selection == 1:
           take_a_loan()
       elif selection == 2:
           repay_debt()
       elif selection == 3:
           if debt == 0:
               print ("You've got no debts!")
           else:
               print ("Repay your debts before minute #{}.".format(term))
       else:
           print ("Bank says you a cold official good bye.")

def take_a_loan():
       """ Player tries to take a loan at bank. """
       global minutes, coins, term, debt
       if debt != 0:
           print ("We can't give you another loan. You already have debts.")
       elif coins < LOAN_PRICE:
           print ("You don't have enough yellows to purchase a loan.")
       else:
           debt = get_valid_int(0, MAX_LOAN)
           if debt > 0:
               minutes += TIME_BANK_SERVICE
               term = int (minutes + debt / 2)
               coins += debt
               print ("Thank you for using our services. Repay in time.")
               print ("You have to repay the debt before minute #{}.".format(term))

def repay_debt():
       """ Player tries to repay debt at bank. """
       global minutes, coins, term, debt
       if debt == 0:
           print ("You've got no debt to repay.")
       elif coins >= debt:
           minutes += TIME_BANK_SERVICE
           coins -= debt
           debt = 0
           term = 0
           print ("Thank you. Come again.")
       else:
           print ("You don't have enough money to repay your debt.")

def lottery():
       """ Player plays lottery. """
       global minutes, coins
       print ("Enter nothing to purchase a lottery ticket, anything else to exit.")
       while input(">> ") == "":
           if coins >= TICKET_PRICE:
               minutes += TIME_LOTTERY
               coins -= TICKET_PRICE
               print ("You bug a ticket for {}.".format(TICKET_PRICE))
               if random.randrange(CHANCE_LOTTERY) == 666:
                   # There's 1 in CHANCE_LOTTERY to win a lottery
                   coins += LOTTERY_PRIZE
                   print ("You won {}.".format(LOTTERY_PRIZE))
               else:
                   print ("You didn't win.")
           else:
               print ("You don't have enough money to purchase a lottery ticket.")
               break

def beg():
       """ Player goes on the streets begging people for coins. """
       global minutes, coins
       beg_money = random.randrange(BEG_MONEY)
       print ("You beg people for money on the streets for whole day.")
       print ("People give you this many coins: {}.".format(beg_money))
       minutes += TIME_BEGGING
       coins += beg_money

def check_for_end():
       """ Checks if player won or lost. """
       if term > minutes:
           print ("GAME OVER. You forgot to pay your debt and bank got you.")
           return True
       elif coins > COINS_FOR_WIN:
           print ("GAME OVER. You won in {} minutes.".format(minutes))
           return True
       else:
           return False

if __name__ == "__main__":
       main()