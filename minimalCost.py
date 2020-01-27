def minimalCost(c, a):
    b = {}
    s = []

    for i in range(len(a)):
        d = [i + 1]
        t = i
        while a[t] not in d:
            d.append(a[t])
            t = a[t] - 1
        b[d[0]] = d[-1]

    cy = []

    for k in b:
        if b[k] == k:
            s.append(k)
        else:
            m = [k]
            d = b[k]
            while d not in m:
                m.append(d)
                if d not in b:
                    break
                d = b[d]
            cy.append(m)

    dup = {}

    for i in range(len(cy)):
        for j in range(len(cy)):
            if i == j or len(cy[i]) != len(cy[j]):
                continue
            eq = True
            for k in range(len(cy[i])):
                if cy[i][k] not in cy[j]:
                    eq = False
                    break
            if eq:
                dup[i] = j
    fn = []

    for i in range(len(cy)):
        if i not in dup:
            fn.append(cy[i])
    cm = []
    fmm = []
    for i in dup.copy().keys():
        if i in cm or dup[i] in cm:
            continue
        fmm.append(cy[i])
        t = dup[i]
        cm.append(i)
        while t in dup and t not in cm:
            cm.append(t)
            t = dup[t]
    for k in fn:
        al = False
        for f in fmm:
            if k[-1] in f:
                al = True
                break
        if al:
            continue

        if k[-1] not in s:
            s.append(k[-1])

    for k in fmm:
        m = 1000000
        j = -1
        for i in k:
            if c[i - 1] < m:
                m = c[i - 1]
                j = i
        s.append(j)

    s = list(set(s))

    r = 0
    for i in s:
        r = r + c[i - 1]

    return r

c = [6,9,1,1,1,10,2,4,9,6]
a = [5,3,4,2,6,8,9,1,10,7]


print(minimalCost(c, a))
