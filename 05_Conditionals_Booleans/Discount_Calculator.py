#Discount Calculator Mini project

amount=float(input('Enter Purchase Amount: '))
discount=0.0
final_price=0.0
mem_disc=0

if amount>=10000.0:
    discount= (amount/100)*20
    final_price= amount-discount
    print('20 percent discout granted!!')

elif amount>= 5000.0:
    discount= (amount/100)*10
    final_price= amount-discount
    print('10 percent discout granted!!')

elif amount>= 2000.0:
    discount= (amount/100)*5
    final_price= amount-discount
    print('5 percent discout granted!!')

else:
    final_price=amount
    print('No discount below Rs.2000.0')

choise=input('Do you have membership card??(Y/N): ')

if choise=='y' or choise=='Y':
    mem_disc=(amount/100)*5
    final_price-=mem_disc
    print('5 percent membership discount added!!')

elif choise=='n' or choise=='N':
    print('No member ship discounts')

print('Original Price= ',amount)
print('Discount applied= ',discount+mem_disc)
print('Final Price= ',final_price)



