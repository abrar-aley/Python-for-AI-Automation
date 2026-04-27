#task 11 ATM Machine mini project

password='pakistan1947'
balance= 50000.00

print('********* CITY BANK ATM *********')

for i in range(3):
    
    pas= input('Enter Password to progress: ')

    if pas==password:
        while True:
            print('1.Check Balance')
            print('2.Deposit Balance')
            print('3.Withdraw Balance')
            print('Exit')

            choise= int(input('Enter you choise: '))

            if choise==1:
                print('Balance: Rs.',balance)

            elif choise==2:
                amountD= float(input('Enter amount to deposit: '))
                balance+=amountD
                print('Rs.',amountD,' deposited successfully!! ')

            elif choise==3:
                amountW= float(input('Enter amount to withdraw: '))
                balance-=amountW
                print('Rs.',amountW,' withdrawn successfully!! ')

            elif choise==4:
                break

            else:
                print('Invalid choise')

        break

    else:
        print('Wrong password')

