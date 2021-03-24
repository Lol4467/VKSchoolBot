print("Welcome!\nThink of one integer number from 1 to 100\nI will try to guess it! ")
up_b=100
low_b=1
number=100
tries=1
guess=input("Is it {}\nWrite 'l' if lower, and 'h' if higher, and 'c' if correct ".format(number))
guess=guess.lower()
while guess!="c":
    if guess=="h":
       low_b=number
       number=int((up_b-low_b)/2+low_b)
     
    elif guess=="l":
       up_b=number
       number=int((up_b-low_b)/2+low_b)
     
    elif guess=="c":
       break
    else:
       print('Please write correct letter')
    guess = input("Is it {}\nWrite 'l' if lower, and 'h' if higher, and 'c' if correct".format(number))
    guess = guess.lower()
    tries+=1
print('I guessed! It was {}. This took {} tries'.format(number, tries))