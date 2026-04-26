# task 3 largest of three numbers

num1=int(input('Enter first Nummber: '))
num2=int(input('Enter Second Nummber: '))
num3=int(input('Enter Third Nummber: '))

if num1>num2 and num1>num3:
    print('Largest number is: ',num1)

elif num2>num1 and num2>num3:
    print('Largest number is: ',num2)

elif num3>num1 and num3>num2:
    print('Largest number is: ',num3)

elif num1==num2 and num1==num3 and num2==num3:
    print('All are equal!!')

else:
    print('Error')
