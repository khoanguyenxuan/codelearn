def checkOutRangeChar(s, r):
    p = 0
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i - 1])) >= r:
            p = p + 1
    return p