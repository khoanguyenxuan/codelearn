def funnyString(s):
    a1 = []
    a2 = []

    for i in range(1, len(s)):
        a1.append(abs(ord(s[i]) - ord(s[i - 1])))

    for i in range(len(s) - 1, 0, -1):
        a2.append(abs(ord(s[i]) - ord(s[i - 1])))

    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return 'Not Funny'
    return 'Funny'
