def numberOfViewsAtOnce(a):
    l = [0] * (10 ** 5)

    for v in a:
        for i in range(v[0], v[1] + 1):
            l[i] = l[i] + 1
    return max(l)
