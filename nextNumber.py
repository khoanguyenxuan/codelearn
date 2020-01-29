def nextNumber(a):
    c1 = a[1]
    c2 = a[2]

    a1 = a[0]
    a2 = a[1]

    b1 = 1
    b2 = 1

    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    if D == 0:
        return a[-1]

    m = Dx / D
    n = Dy / D

    return int(m * a[-1] + n)


a = [0, 0, 0]

print(nextNumber(a))
