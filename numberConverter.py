def numberConverter(n):
    d = 2
    s = []
    t = 1
    o = n
    while n > 1 and t < o:
        if n % d == 0:
            s.append(d)
            n = n / d
            t = t * d
        else:
            d = d + 1
    return max(s)

print (numberConverter(234))