#task 6 student grade book

students= ['Ali','Ahmed','Hassan','Daood','Kashif']
marks= [89,90,56,72,55]

print('Class Average: ', sum(marks)/len(marks))
print('Max score: ', max(marks))
if marks[0]==max(marks):
    print('Max scorer is Ali' )
elif marks[1]==max(marks):
    print('Max scorer is Ahmed' )
elif marks[2]==max(marks):
    print('Max scorer is Hassan' )
elif marks[3]==max(marks):
    print('Max scorer is Daood' )
elif marks[4]==max(marks):
    print('Max scorer is Kashif' )

print('Min Score: ',min(marks))
if marks[0]==min(marks):
    print('Min scorer is Ali' )
elif marks[1]==min(marks):
    print('Min scorer is Ahmed' )
elif marks[2]==min(marks):
    print('Min scorer is Hassan' )
elif marks[3]==min(marks):
    print('Min scorer is Daood' )
elif marks[4]==min(marks):
    print('Min scorer is Kashif' )

for index, mark in enumerate(marks):
    print(index+1, mark)




