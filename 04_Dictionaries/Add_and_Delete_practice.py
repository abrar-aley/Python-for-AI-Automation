# task 4 add and delete practice

Grocery= {'Eggs':12,'Soap':5,'Detergent':'SurfExel'}

print(Grocery.keys())

Grocery.update({'Chicken':'2kg','Bananas':12})

print(Grocery.keys())

del Grocery['Chicken']

print(Grocery.keys())

item= Grocery.pop('Eggs')
print(item)
