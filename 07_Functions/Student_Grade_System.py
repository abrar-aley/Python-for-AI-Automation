# Student Grading System

def getAverage(marks):
    avg=0
    for m in marks:    
        avg+=m
    avg/=len(marks)
    return avg
        

def getGrade(avg):
    if avg>= 80:
        return 'A'
    elif avg>=70:
        return 'B'
    elif avg>=60:
        return 'C'
    elif avg>=50:
        return 'D'
    else:
        return 'F'

def getResult(name,marks):
    print('***** ',name,' *****')
    print('Average marks= ',getAverage(marks))
    print('Grade= ',getGrade(getAverage(marks)))
    print()

Student_Grades={'Hamza':[50,70,75,40,88],'Asif':[44,70,88,75,75],'Hannan':[30,35,60,52,44],'Asad':[50,55,52,59,60],'Moiz':[88,80,90,79,92]}

for key,value in Student_Grades.items():
    getResult(key,value)