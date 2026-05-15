# args practice

def total(*args):
    sum=0
    for n in args:
        sum+=n

    return sum

print('Total= ',total(5,8))
print('Total= ',total(2,8,10,15,30))
print('Total= ',total(1,2,3,4,5,6,7,8,9,10))