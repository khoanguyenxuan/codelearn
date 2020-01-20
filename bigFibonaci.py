def bigFibonaci(n):
    n = n % 482776

    previous, current = 0, 1

    for i in range(n - 1):
        previous, current = current, previous + current

    return current % (10 ** 6 + 7)
