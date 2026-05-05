#task 11 number guessing game

import random

num= random.randint(1,100)

while True:
    guess= int(input('Guess the number: '))
    if guess>num:
        print('Too High')

    elif guess<num:
        print('Too Low')

    elif guess==num:
        print('You won!!')
        Choise= input('Do you want to paly again? (Y/N)')
        if Choise=='y'or Choise=='Y':
            num= random.randint(1,100)
        elif Choise==n or Choise==N:
            break
        else:
            print('Error')

    else:
        print('Error')

       