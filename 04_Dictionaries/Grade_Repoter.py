# task 7 graed reporter

Marks= {'Saqib':23,'Ali':90,'Hussain':74,'Murtaza':55,'Ahsan':87,'Hassam':70,'Kamil':98,'Raqeeb':82}

for key,value in Marks.items():

    if value>= 90:
        print('Name: ',key,' Marks: ',value,' Grade: A+')

    elif value>= 80:
        print('Name: ',key,' Marks: ',value,' Grade: A')
    
    elif value>= 70:
        print('Name: ',key,' Marks: ',value,' Grade: B+')

    elif value>= 60:
        print('Name: ',key,' Marks: ',value,' Grade: B')

    elif value>= 50:
        print('Name: ',key,' Marks: ',value,' Grade: C')

    else:
        print('Name: ',key,' Marks: ',value,' Grade: F')


    
    
