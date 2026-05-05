#task 12 Student Grade Reporter

Students={'Abrar':[20,13,11],'Hassan':[26,13,7],'Awais':[23,14,11],'Moeez':[30,15,15],'Ali':[10,15,20]}

heighest_marks=0
topper='null'
for key,value in Students.items():
    sum=0
    for i in range(0,3):
        sum+=value[i]

    if sum>heighest_marks:
        heighest_marks=sum
        topper=key

    avg=sum//3
    print(key)
    print('Average marks: ',avg)

    if avg>=25 and avg<=30:
        print('Grade A')

    elif avg>=20 and avg<=24:
        print('Grade B')

    elif avg>=15 and avg<= 19:
        print('Grade C')

    elif avg>=10 and avg<=14:
        print('Grade D')

    elif avg<10:
        print('Grade F')

    else:
        print('Error')
    print()
        
print('The topper is ',topper,' with total ',heighest_marks,' marks.')