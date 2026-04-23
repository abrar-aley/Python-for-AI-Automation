# task 1 shopping list manager

grocery= ['rice', 'vegees', 'chicken', 'cooking oil']
print('Grocery:', grocery)
grocery.append('fruits')
print('Grocery:',grocery)
grocery.insert(1, 'garins')
print('Grocery:',grocery)
grocery.remove('rice')
print('Grocery:',grocery)
print('Last item:', grocery.pop())

grocery2= ['shampoo', 'conditioner', 'facewash']
grocery.extend(grocery2)
print('Grocery:', grocery)
grocery.sort()
print('Grocery Sorted:',grocery)
