#task 7 number search

numbers=[5,7,3,13,55,77,59,10,20,4]

num= int(input('Enter a number to search: '))

for number in numbers:
    if number==num:
        print('Number found at index ',numbers.index(number))
        break

else:
    print('Number not found!!')
