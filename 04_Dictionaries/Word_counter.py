# task 5 word counter

sentence= 'bots and cats and dogs and bots and cats'

words= sentence.split()

words_count={}

for word in words:
    if word in words_count:
        words_count[word]= words_count[word]+1

    else:
        words_count[word]= 1

for word in words_count:
    print(word,' : ',words_count[word])