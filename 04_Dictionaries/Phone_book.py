#task 6 phone book

contact= {'Abrar':923405152680,'Karrar':923555465642,'Raza':923475440717,'Mahdi':923091213105,'Taqi':923555890776}

while True:
    print('      =====  MENU ====')
    print('1. Search Contact')
    print('2. Add Contact')
    print('3. Delete Contacts')
    print('4. Display Contact')
    print('5. End')

    choise= int(input('Enter your choise: '))
    if choise==1:

      name= input('Enter name to search contact: ')
      print(contact.get(name, 'contact not found'))

    elif choise==2:
       
       name= input('Enter name: ')
       number= int(input('Enter number: '))
       contact.update({name:number})
       print('Contact added')

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
       
       




