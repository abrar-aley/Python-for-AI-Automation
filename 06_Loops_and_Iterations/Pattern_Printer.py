# pattern printer

while True:
    print('-------MENU-------')
    print('1.Rightangle Triangle')
    print('2.Square')
    print('3.Pyramid')
    print('4.Exit')
    print()

    choise= int(input('Choose a shape to print: '))

    if choise==1:
        for i in range(5):
            for j in range(i+1):
                print('* ',end='')
            print()

    elif choise==2:
        for i in range(5):
            print('* * * * *')

    elif choise == 3:
        for i in range(5):
            for j in range(5 - i - 1):
                print(' ', end='')
            for k in range(i + 1):
                print('* ', end='')
            print()
            
    elif choise==4:
        break

    else:
        print('Enter Coorrect choise!!')
           

            
                
            
