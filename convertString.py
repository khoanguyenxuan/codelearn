def convertString(a, b):
    a = list(a.lower())
    b = list(b.lower())

    prev = -1
    for c in b:
        try:
            idx = a.index(c)
        except:
            return 'NO'

        if idx == -1 or idx < prev:
            return 'NO'
        a[idx] = '_'
        prev = idx

    return 'YES'
