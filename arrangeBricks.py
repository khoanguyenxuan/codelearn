def arrangeBricks(a):
    a = sorted(a, reverse=True)

    for i in range(0, len(a)):
        if i > len(a) - 1:
            break
        a = a[:a[i] + i + 1]
    return len(a)
