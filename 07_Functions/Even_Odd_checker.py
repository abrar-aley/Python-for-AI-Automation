# even odd function

def isEven(n):
    if n%2==0:
        return True
    else:
        return False
    
for i in range(1,11):
    if isEven(i):
        print(i,' is even.')
    else:
        print(i,' is not even')

        