def fibonacciIndex(n):
    previous, current = 0, 1
    m = 10 ** (n - 1)

    if n == 1:
        return 0

    for i in range(10 ** 3):
        previous, current = current, current + previous

        if int(current / m) > 0:
            return i + 2

print (fibonacciIndex(1))
