def numberOfBits(n):
    ones=0
    zeros=0
    while(n):
        if(n&1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print("\n\ number of 1's: ",ones)

number=int(input("enter a number: "))
numberOfBits(number)
