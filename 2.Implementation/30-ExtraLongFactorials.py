def extraLongFactorials(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)

# OR

from math import factorial

def extraLongFactorials(n):
    print(factorial(n))