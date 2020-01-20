def bricks2(a, b):
    p = a + b
    s = (a + 4) / 2

    delta = s * s - 4 * p
    if delta < 0:
        return [-1]

    x = (s - math.sqrt(delta)) / 2
    y = (s + math.sqrt(delta)) / 2
    return [int(x), int(y)]

