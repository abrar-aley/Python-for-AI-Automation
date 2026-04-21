# task 3 score tracker

scores= [94, 55, 70, 75, 90, 43, 88, 74, 32, 65]
print('Maximum score: ',max(scores))
print('Minimum score: ',min(scores))
print('Sum of score: ',sum(scores))
scores.sort()
scores.reverse()

for index , score in enumerate(scores):
    print(index+1, score)

