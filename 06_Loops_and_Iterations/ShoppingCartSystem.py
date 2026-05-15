#shopping cart system

shoppings={}

while True:
    print('----------MENU----------')
    print('1.Add Item')
    print('2.Remove Item')
    print('3.View Cart')
    print('4.Checkout')
    print('5.Exit')
    print()

    choise= int(input('Enter Choise: '))

    if choise==1:
        name=input('Enter Item Name: ')
        price=int(input('Enter Price: '))
        shoppings.update({name:price})
        print('Item added successfully!!')

    elif choise==2:
        Ritem= input('Enter item name to remove: ')
        if Ritem in shoppings:
           del shoppings[Ritem]
           print('Item Removed Successfully!!')
        else:
            print('Item not found!!')

    elif choise==3:
        for key,value in shoppings.items():
            print(key,':',value)

    elif choise==4:
        total=0
        for value in shoppings.values():
            total+=value
        print('Total bill: Rs.',total)

    elif choise==5:
        break
    else:
        print('Incorrect Choise!!!')

