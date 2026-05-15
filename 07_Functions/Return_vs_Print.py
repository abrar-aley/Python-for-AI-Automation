# Return vs Print

def square(n):
    print(n)

def square_return(n):
    return n

result= square(2)+5      # It gives error

result= square_return(2)+5   # It works
