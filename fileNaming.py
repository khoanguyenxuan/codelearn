def fileNaming(names):
    d = {}
    dm = {}
    r = []

    for n in names:
        if n not in d:
            d[n] = 0
            dm[n] = 1
        else:
            dm[n] = dm[n] + 1

    for n in names:
        if n in r and d[n] == 0:
            d[n] = 1
            r.append('%s(%d)' % (n, d[n]))
            d[n] = d[n] + 1
            continue

        if dm[n] == 1:
            r.append(n)
            continue

        if d[n] == 0:
            r.append(n)
            d[n] = d[n] + 1
        else:
            while True:
                x = '%s(%d)' % (n, d[n])
                if x not in r:
                    r.append(x)
                    break
                d[n] = d[n] + 1
    return r
