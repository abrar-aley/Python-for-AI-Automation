import random

while True:
    print('=== MENU ===')
    print('1. Rolling dice')
    print('2. Random Day')
    print('3. Shuffle')
    print('4. Exit')

    choise= int(input('Enter the choise: '))

    if choise==1:
        print('Random dies= ',random.randint(1,6))

    elif choise==2:
        Days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        print('Random day= ',random.choice(Days))

    elif choise==3:
        deck=[1,2,3,4,5,6,7,8,9,10]
        random.shuffle(deck)
        print(deck)
    elif choise==4:
        break

    else:
        print('Invalid choise')

