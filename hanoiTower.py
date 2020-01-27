a = 0
b = 0
c = 0
tn = 0
s = 0

def hanoiTower(n, k):
    global a, b, c, tn
    tn = k
    a = n
    chuyen(n, 'A', 'B', 'C')
    return [a, b, c]


def chuyen(x, f, t, m):
    global a, b, c, s, tn
    if s == tn:
        return

    if x == 1:
        s = s + 1
        if f == 'A':
            a = a - 1
        if f == 'B':
            b = b - 1
        if f == 'C':
            c = c - 1
        if t == 'A':
            a = a + 1
        if t == 'B':
            b = b + 1
        if t == 'C':
            c = c + 1

        return

    chuyen(x - 1, f, m, t)
    chuyen(1, f, t, m)
    chuyen(x - 1, m, t, f)


print(hanoiTower(3, 1))
