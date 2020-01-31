def turnRight(a):
    r = 0
    for i in range(2, len(a)):
        x = a[i - 2]
        y = a[i - 1]
        z = a[i]

        if x[0] == y[0] == (z[0] - 1) and y[1] == z[1] == (x[1] + 1):
            r = r + 1

        if y[0] == z[0] == (x[0] + 1) and x[1] == y[1] == (z[1] + 1):
            r = r + 1

        if x[0] == y[0] == (z[0] + 1) and y[1] == z[1] == (x[1] - 1):
            r = r + 1

        if y[0] == z[0] == (x[0] - 1) and x[1] == y[1] == (z[1] - 1):
            r = r + 1

    return r
