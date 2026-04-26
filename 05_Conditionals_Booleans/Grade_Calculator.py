# task 6 grade caculator

marks= int(input('Enter you marks out of 100: '))

if marks>=90 and marks<100:
    print('A+')

elif marks>=80 and marks<100:
    print('A')

elif marks>=70 and marks<100:
    print('B+')

elif marks>= 60 and marks<100:
    print('B')

elif marks>=50 and marks<100:
    print('C+')

elif marks>=40 and marks<100:
    print('C')

elif marks< 40 and marks>0:
    print('F')

else:
    print('Put correct marks!!')
    