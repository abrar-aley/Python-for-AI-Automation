#task 10 shopping cart

Shoppings = {}

while True:
    print('*******  MENU  ********')
    print('1.Add items')
    print('2.Remove items')
    print('3.Total bill')
    print('4.Print receipt')
    print('5.Exit')

    choise = int(input('Enter your choise: '))

    if choise == 1:
        name = input('Enter item name: ')
        price = int(input('Enter item price: '))
        Shoppings.update({name: price})
        print('Item added to cart!!')
        print('')

    elif choise == 2:
        name = input('Enter item to remove: ')
        del Shoppings[name]
        print('Item removed!!')
        print('')
       
    elif choise == 3:
        total = 0
        for value in Shoppings.values():   # fixed
            total += value
        print('Total bill: PKR.', total)   # fixed
        print('')
        
    elif choise == 4:
        total = 0
        for value in Shoppings.values():   # fixed
            total += value

        print('--------------------')
        print('|     RECIEPT      |')
        print('--------------------')
        print(' ITEMS:    ')
        for key in Shoppings:
            print(key)
        print('--------------------')    
        print(' Total Bill:')
        print('PKR.', total)
        print('--------------------')
        print('')

    elif choise == 5:
        break

    else:
        print('Invalid choise')