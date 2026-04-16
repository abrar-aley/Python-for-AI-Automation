# task 1 simple calculator

num1= int(input('Enter num 1: '))
num2= int(input('Enter num 2: '))
print('1.Addition')
print('2.Subtraction')
print('3.Division')
print('4.Multiplication')
choise= int(input('Enter choise: '))
if choise==1:
    print(num1+num2)
elif choise== 2:
    print(num1-num2)
elif choise== 3:
    print(num1/num2)
elif choise== 4:
    print(num1*num2)
