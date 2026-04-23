#task 99 password strength checker

password= input('Enter a password: ')

hasDecimal= False
hasUpper= False
for c in password:
       if c.isdecimal():
              hasDecimal= True
for c in password:
       if c.isupper():
              hasUpper= True

if len(password)> 7:
           if hasDecimal==True:
                  if hasUpper== True:
                         print('Strong Password!')
                  else: 
                         print('Weak Password!')                
           else:
                  print('Weak Password!')
else:
   print('Weak Password!')