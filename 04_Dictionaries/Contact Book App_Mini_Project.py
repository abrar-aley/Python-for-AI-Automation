# task 9 contact book app mini project

contact={}

while True:
    print('*******  MENU  ********')
    print('1.Add contact')
    print('2.Search contact')
    print('3.Delete contact')
    print('4.Show all contact')
    print('5.Exit')

    choise= int(input('Enter your choise: '))

    if choise==1:
        name= input('Enter name: ')
        phno=int(input('Enter Phone number: '))
        contact.update({name:phno})
        print('Contact added successfully')

    elif choise==2:
        name=input('Enter name to search: ')
        print(contact.get(name, 'contact not found'))

    elif choise==3:
        name= input('Enter name to delete contact: ')
        del contact[name]
        print('Contact Deleted')

    elif choise==4:
         print(contact)

    elif choise==5:
       break

    else:
       print('Invalid choise')