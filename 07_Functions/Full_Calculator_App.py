# full calculator

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def power(num1,num2):
    return num1**num2

def Modulus(num1,num2):
    return num1%num2

while True:

    print('Enter Two Numbers:')
    num1=int(input('First Number= '))
    num2=int(input('Second Number= '))

    print('--------- MENU ---------')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Power')
    print('6. Modulus')
    print('7. Exit')
    print()

    choise= int(input('Enter your choise: '))

    if choise==1:
        print('Sum= ',add(num1,num2))

    elif choise==2:
        print('Difference= ',subtract(num1,num2))

    elif choise==3:
        print('Product= ',multiply(num1,num2))

    elif choise==4:
        if num2==0:
            print('Can not be divided by zero!!')

        else:
            print('Quotient= ',divide(num1,num2))

    elif choise==5:
        print('Exponent= ',power(num1,num2))

    elif choise==6:
        print('Modulus= ',Modulus(num1,num2))

    elif choise==7:
        break

    else:
        print('Input error!!')

    

    

