# task9 contact book mini project

c1 = ('Ali', 923497535663)
c2 = ('Ahmed', 923507575660)
c3 = ('Hassan', 92349732166)
c4 = ('Daood', 923497535468)
c5 = ('Kashif', 923557995699)
c6 = ('Haider', 923477512664)
c7 = ('Awais', 923507535230)
c8 = ('Raza', 923447535688)
c9 = ('Kaleem', 923497535773)

Contacts = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

while True:
    print('=== MENU ===')
    print('1. Add Contact')
    print('2. Remove Contact')
    print('3. Search by Name')
    print('4. Display Contacts')
    print('5. End')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter Name: ')
        number = int(input('Enter Number: '))
        new_contact = (name, number)
        Contacts.append(new_contact)
        print('Contact added')

    elif choice == 2:
        c_remove = input('Enter contact name to remove: ')
        found = False

        for contact in Contacts:
            if contact[0] == c_remove:   
                Contacts.remove(contact)
                print('Contact removed')
                found = True
                break

            else:
                print('Contact not found')

    elif choice == 3:
        c_search = input('Enter contact to search: ')
        found = False

        for contact in Contacts:
            if contact[0] == c_search:   
                print('Contact found!!')
                print(contact)
                found = True

            else:
                print('Contact not found')

    elif choice == 4:
        print('=== CONTACTS ===')
        for con in Contacts:
            print(con)

    elif choice == 5:
        print('Exiting...')
        break

    else:
        print('Invalid choice')