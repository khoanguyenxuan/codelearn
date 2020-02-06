import math


def password(a, b):
    c = factorize(a)
    r = {}

    for k in c:
        n = c[k] * b + 1
        d = factorize(n)
        for j in d:
            if j not in r:
                r[j] = d[j]
            else:
                r[j] = r[j] + d[j]

    n = 1
    for k in r:
        n = n * (r[k] + 1)

    return n


def factorize(n):
    count = 0
    c = {}

    while not (n % 2 > 0):
        n >>= 1
        count += 1

    if count > 0:
        c[2] = count

    for i in range(3, int(math.sqrt(n)) + 1):
        count = 0
        while n % i == 0:
            count += 1
            n = int(n / i)
        if count > 0:
            c[i] = count
        i += 2

    if n > 2:
        c[n] = 1

    return c


print(password(12, 11))
