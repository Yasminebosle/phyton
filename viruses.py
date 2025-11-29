number=int(input("Input your numbeer: "))
digits=len(str(number))
result=0
temp=number
while temp > 0:
    digit =temp %10
    result +=digit ** digits
    temp // 10

if number == result:
        print(number,"is an Armstrong number")
else:
        print(number,"is not an Armstrong number")