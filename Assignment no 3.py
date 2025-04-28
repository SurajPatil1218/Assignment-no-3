## Task no 1

a = int(input("Entre the No : "))
def factorial(a):
    if a < 2:
        return 1 
    else:
        return (a * factorial(a-1))
result=factorial(a)
print(result)

Output :
Entre the No :  5
120

## Task no 2

import math
n = int(input("Entre the number : "))
print("Square Root of :",math.sqrt(n))
print("Logarithm of :",math.log10(n))
print("Sin of :",math.sin(n))

Output :
Entre the number :  5
Square Root of : 2.23606797749979
Logarithm of : 0.6989700043360189
Sin of : -0.9589242746631385