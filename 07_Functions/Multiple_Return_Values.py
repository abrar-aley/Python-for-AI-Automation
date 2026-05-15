# Multiple return values

def min_max(numbers):
    max=0
    min=0
    for n in numbers:
        if n>max:
            max=n
            min=max

    for n in numbers:
        if n<min:
            min=n

    return max,min

list1=[4,6,8,10,12,1,16,3,2,7]
list2=[400,100,700,300,500,900,200]

print('Maximum and minimum in list1 are respectively: ',min_max(list1))

print('Maximum and minimum in list2 are respectively: ',min_max(list2))
