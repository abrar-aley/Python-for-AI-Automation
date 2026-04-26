#task 10 triangle checker

side1= int(input('Enter side 1 of triangle: '))
side2= int(input('Enter side 2 of triangle: '))
side3= int(input('Enter side 3 of triangle: '))

if (side1==0 or side1<0) or (side2==0 or side2<0) or (side3==0 or side3<0):
    print('Not a Triangle!!!')

if side1==side2 and side1==side3 and side2==side3:
    print('Equilateral Triangle')

elif side1==side2 or side1==side3 or side2==side3:
    print('Isosceles Triangle')

elif side1!=side2 and side1!=side3 and side2!=side3:
    print('Scalene Triangle')

else:
    ('Input eror')
