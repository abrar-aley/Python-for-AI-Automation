#Budjet Tracker

salary= float(input('Enter your monthly salary: '))
bonus= float(input("Enter this month's bonus: "))
expense= float(input('Enter total expence of this month: '))
print('Total Income: ', salary+bonus)
print('Remaining baance: ', (salary+bonus)-expense)

