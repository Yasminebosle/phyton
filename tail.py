def tail(n):
    if(n!=0):
        print(n)
        tail(n-1)
x=10
tail(x)