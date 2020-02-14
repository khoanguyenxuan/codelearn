def encodePhoneMessage(s):
    d = {
        '0': ' 0',
        '1': '.,?!1',
        '2': 'abc2',
        '3': 'def3',
        '4': 'ghi4',
        '5': 'jkl5',
        '6': 'mno6',
        '7': 'pqrs7',
        '8': 'tuv8',
        '9': 'wxyz9'
    }

    r = ''

    for c in s:
        for k in d:
            if c in d[k]:
                if len(r) > 0:
                    if k == r[-1]:
                        r = r + '-'
                r = r + k * (d[k].index(c) + 1)
    return r

print (encodePhoneMessage('code'))