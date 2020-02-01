def cubes(a):
    x = a[0]
    y = a[1]
    z = a[2]

    if 0 in x or 0 in y or 0 in z:
        return -1

    t = x[0] * x[1] * x[2]  + y[0] * y[1] * y[2] + z[0] * z[1] * z[2]

    m = round(t ** (1/3))

    if m ** 3 == t:
        return m

    return -1
