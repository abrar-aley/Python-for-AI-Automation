#task 4 login system

user_name= 'abrar-aley'
password= 'tcs446@skardu'

user= input('Enter User Name: ')
pas= input('Enter Password: ')

if user==user_name and pas==password:
    print('Logged in Successfully!!')

elif user==user_name and pas != password:
    print('Incorrect password !!')

elif user!=user_name and pas==password:
    print('Incorrect Username !!')

else:
    print('Incorrect user name or password !!')
    
