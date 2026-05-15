# Combined Parameters

def display_StudentInfo(name,*args,**kwargs):
    print('Name: ',name)

    print('Courses:')
    for c in args:
        print(c)

    print('Extra Info:')
    for key,value in kwargs.items():
        print(key,' : ',value)


display_StudentInfo('Arsalan','OOP','DSA','Calculus',University='Comsats Isb',Department='CS',gpa=3.5)
