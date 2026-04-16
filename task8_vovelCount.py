#task8 vovel counter

text=input('Enter text: ')
vovel= 'AEIOUaeiou'
count= 0
for char in text:
    if char in vovel:
        count+=1

print('No of vovels: ', count)
space= text.count(' ')
print('Spaces: ', space)
print('No of consonants: ', len(text)-count-space)


