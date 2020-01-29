def checkMax(s):
    m = -1
    for c in s:
        if ord(c) > m:
            m = ord(c)
    return m
