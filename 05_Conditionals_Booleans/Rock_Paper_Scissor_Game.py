# rock paper scissor game

import random

choices=['rock','paper','scissor']

your_choise=input('Enter your choise :').lower()

if your_choise not in choices:
    print('Invalid user choise!!')

else:
    computer_choise= random.choice(choices).lower()
    print('Computer choise: ',computer_choise)

    if computer_choise==your_choise:
        print('Draw!')

    elif (computer_choise==choices[0] and your_choise==choices[1]) or \
    (computer_choise==choices[1] and your_choise==choices[2]) or \
    (computer_choise==choices[2]and your_choise==choices[0]):
        print('You won!!')

    else:
        print('You lost!!')
                                                                