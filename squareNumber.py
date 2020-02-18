import math

def squareNumber(n):
    if n == 0:
        return 1

    m = int(math.sqrt(n))

    for i in range(m, 1, -1):
        if int(n % (i ** 2)) == 0:
            return int(n / (i ** 2))
    return n
print (squareNumber(100))
