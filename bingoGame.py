def bingoGame(a, b):
    m = [[False for x in range(5)] for y in range(5)]

    for c in b:
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == c:
                    m[i][j] = True
                    if isOk(m):
                        return b.index(c)


def isOk(a):
    for i in range(len(a)):
        ok = True
        for j in range(len(a[0])):
            if not a[i][j]:
                ok = False
                break
        if ok:
            return True

    for j in range(len(a[0])):
        ok = True
        for i in range(len(a)):
            if not a[i][j]:
                ok = False
                break
        if ok:
            return True

    ok = True
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j and not a[i][j]:
                ok = False
    if ok:
        return True

    ok = True
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j == 4 - i and not a[i][j]:
                ok = False
    if ok:
        return True

    return False


a = [[21, 1, 2, 20, 18], [23, 7, 5, 3, 14], [13, 16, 8, 25, 17], [6, 11, 4, 24, 12], [22, 19, 9, 15, 10]]
b = [13, 2, 10, 8, 19, 9, 15, 6, 4, 7, 24, 20, 21, 23, 17, 11, 22, 12, 18, 14, 25, 3, 16, 1, 5]

print (bingoGame(a, b))