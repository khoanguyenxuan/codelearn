def sequenceFixing(s):
    t = 0
    p = 0

    for c in s:
        if c == ')' and p > 0:
            p = p - 1
            continue
        if c == ')' and p == 0:
            t = t + 1
            continue
        if c == '(':
            p = p + 1
    t = t + p
    return t
