# task 7 Leap Year checker

year= int(input('Enter year to check: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")