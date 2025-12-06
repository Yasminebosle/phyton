from math import sqrt
number=int(input("enter a number to discover the square root"))

print('\n')
if number > 1:
    for i in range(2, int(sqrt(number)) + 1):
        if (number % i) == 0:
           print(f"{number} it isn't a prime number.")
           print(f"{i} times {number // i} is {number}.")
           break
        else:
            print(f"{number} is a prime number.")
            break

else:
    print(f"{number} is not a prime number")