def promotion(x, y, s):
    if x + y > s and x < s:
        return x

    m = int(s / (x + y))
    c = m * x + (s - m * (x + y))

    return c
