def expressionFill(s):
    import re
    letters = re.sub('[^a-z]+', '', s)

    letters = list(set(letters))
    letters = sorted(letters)

    i = 0
    for c in ['a', 'b', 'c', 'd', 'e', 'f']:
        if i < len(letters):
            s = s.replace(letters[i], c)
            i = i + 1

    n = len(letters)

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for a in range(0, 10):

        if n == 1:
            data = {
                'a': a,
                'b': b,
                'c': c,
                'd': d,
                'e': e,
                'f': f,
            }
            if evaluate(s, data):
                return build_result(s, data)
            continue

        for b in range(0, 10):

            if n == 2 and len({a, b}) == 2:
                data = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'd': d,
                    'e': e,
                    'f': f,
                }
                if evaluate(s, data):
                    return build_result(s, data)
                continue

            for c in range(0, 10):
                if n == 3 and len({a, b, c}) == 3:
                    data = {
                        'a': a,
                        'b': b,
                        'c': c,
                        'd': d,
                        'e': e,
                        'f': f,
                    }
                    if evaluate(s,data ):
                        return build_result(s, data)
                    continue

                for d in range(0, 10):
                    if n == 4 and len({a, b, c, d}) == 4:
                        data = {
                            'a': a,
                            'b': b,
                            'c': c,
                            'd': d,
                            'e': e,
                            'f': f,
                        }
                        if evaluate(s, data):
                            return build_result(s, data)
                        continue

                    for e in range(0, 10):
                        if n == 5 and len({a, b, c, d, e}) == 5:
                            data = {
                                'a': a,
                                'b': b,
                                'c': c,
                                'd': d,
                                'e': e,
                                'f': f,
                            }
                            if evaluate(s, data):
                                return build_result(s, data)
                            continue
                        for f in range(0, 10):
                            if n == 6 and len({a, b, c, d, e, f}) == 6:
                                data = {
                                    'a': a,
                                    'b': b,
                                    'c': c,
                                    'd': d,
                                    'e': e,
                                    'f': f,
                                }
                                if evaluate(s, data):
                                    return build_result(s, data)
                                continue
    return 'undefined'


def fill(s, d):
    v = s.replace('a', str(d['a']))
    v = v.replace('b', str(d['b']))
    v = v.replace('c', str(d['c']))
    v = v.replace('d', str(d['d']))
    v = v.replace('e', str(d['e']))
    v = v.replace('f', str(d['f']))
    return v


def evaluate(s, d):
    s1 = s.split('=')[0]
    s2 = s.split('=')[1]

    s1 = fill(s1, d)
    s2 = fill(s2, d)

    try:
        v1 = int(eval(s1))
        v2 = int(eval(s2))
    except:
        return False

    if v1 == v2:
        if len(s2) > 1 and s2[0] == '0':
            return False

        for c in ['+', '-', '*', '/']:
            if len(s1.split(c)) == 2:
                if len(s1.split(c)[0]) > 1 and s1.split(c)[0][0] == '0':
                    return False
                if len(s1.split(c)[1]) > 1 and s1.split(c)[1][0] == '0':
                    return False

        return True


def build_result(s, d):
    return fill(s, d)


print (expressionFill('ab*d=d'))
print (expressionFill("ab+cb=abb"))
