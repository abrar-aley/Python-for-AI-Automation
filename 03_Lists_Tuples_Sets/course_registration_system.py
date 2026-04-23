#task10 course registration sysytem mini project

# Departments with their respective courses

BBA= {'Intro to Business','Accounting','Finance','Business Ethics','Business Writting'}
BSE= {'PF','OOP','DSA','OS','Networking','SE-1','SE-2'}
BAI= {'PF','OOP','DSA','Agentic AI','Generative AI','Neural Networks'}
BFA= {'Intro to Arts','Classical Arts','Modern Arts','Practical Arts'}
BPH= {'Intro to Physics','Classical Physics','Quantum Mechanics','Applied Physics'}

while True:
    print('     ===MENU===')
    print('1.Register a student')
    print('2,End')

    choise= int(input('Enter your choise: '))

    if choise== 1:
        name= input('Enter student name: ')
        student_courses = set(input('Enter courses (comma separated): ').split(','))
        print('Which Department do you want to enroll in?')
        print('1.BBA')
        print('2.BSE')
        print('3.BAI')
        print('4.BFA')
        print('5.BPH')

        ch= int(input('Enter your choise: '))

        if ch==1:
           if BBA.issubset(student_courses):
               print('Registered!!')
           else:
               course_missing= BBA.difference(student_courses)
               print('The following corses are missing: ',course_missing)
               course_extra= student_courses.difference(BBA)
               print('The following courses are extra: ',course_extra)
               print('Enter required courses and try again..')

        elif ch==2:
            if  BSE.issubset(student_courses):
               print('Registered!!')
            else:
               course_missing= BSE.difference(student_courses)
               print('The following corses are missing: ',course_missing)
               course_extra= student_courses.difference(BSE)
               print('The following courses are extra: ',course_extra)
               print('Enter required courses and try again..')

        elif ch==3:
            if  BAI.issubset(student_courses):
               print('Registered!!')
            else:
               course_missing= BAI.difference(student_courses)
               print('The following corses are missing: ',course_missing)
               course_extra= student_courses.difference(BAI)
               print('The following courses are extra: ',course_extra)
               print('Enter required courses and try again..')

        elif ch==4:
            if  BFA.issubset(student_courses):
               print('Registered!!')
            else:
               course_missing= BFA.difference(student_courses)
               print('The following corses are missing: ',course_missing)
               course_extra= student_courses.difference(BFA)
               print('The following courses are extra: ',course_extra)
               print('Enter required courses and try again..')

        elif ch==5:
            if  BPH.issubset(student_courses):
               print('Registered!!')
            else:
               course_missing= BPH.difference(student_courses)
               print('The following corses are missing: ',course_missing)
               course_extra= student_courses.difference(BPH)
               print('The following courses are extra: ',course_extra)
               print('Enter required courses and try again..')

    elif choise==2:
       break