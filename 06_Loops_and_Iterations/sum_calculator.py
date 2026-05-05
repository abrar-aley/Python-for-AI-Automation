# taskk 3 summ calculator

numbers=[3,5,4,8,7,6,6,9,10,3]

sum=0

for i in range(10):
    sum+=numbers[i]

print(sum)

index=0
while index==9:
    sum+=numbers[index]
    index+=1

print(sum)