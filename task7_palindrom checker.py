#task7 palindrom checker

text= input('Enter string to check: ')

if text==text[::-1]:
    print('Palindrom')
else:
    print('Not Palindrom')
