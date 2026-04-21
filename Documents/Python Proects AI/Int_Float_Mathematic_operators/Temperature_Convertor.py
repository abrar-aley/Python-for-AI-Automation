# temperature convertor

temp= int(input('Enter a temperature: '))
print('1.Celcious to Farenhiet')
print('2.Farenheit to Celcious')
choise= int(input('Enter choise: '))
if choise== 1:
    print((temp*9/5)+32)
elif choise== 2:
    print((temp-32)*5/8)
