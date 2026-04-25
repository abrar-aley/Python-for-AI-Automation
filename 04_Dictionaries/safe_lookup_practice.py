#task 2 safe look up

Countries= {'Pakistan':'Islamabad','India':'Dehli','Afghanistan':'Kabul','China':'Bejing','Iran':'Tehran'}

name= input('Enter a country name: ')

print(Countries.get(name, 'Country not found in dictionary'))