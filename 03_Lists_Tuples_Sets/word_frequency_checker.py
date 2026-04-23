#task 7 word frequency checker

sentence= 'Hey i am Abrar Ali and i am a student i am a passionate lerner'
words= sentence.split()

unique_words= set(words)
check= 'am'
count= words.count(check)

print('Sentence: '+sentence)
print('Word list :', words)
print('Print unique words: ', unique_words)
print('Count of am: ',count)