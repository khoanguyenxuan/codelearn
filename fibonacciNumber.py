def fibonacciNumber(n):
    previous, current = 0, 1

    if n == 0:
        return 0

    for i in range(n - 1):
        previous, current = current, current + previous

    return current % (10 ** 9 + 7)
