def digitalNumber(lightStatus):
    patterns = {
        '****.**.**.****': '0',
        '..*..*..*..*..*': '1',
        '***..*****..***': '2',
        '***..****..****': '3',
        '*.**.****..*..*': '4',
        '****..***..****': '5',
        '****..****.****': '6',
        '***..*.**..*..*': '7',
        '****.*****.****': '8',
        '****.****..****': '9',
    }

    s = []

    for i in range(int(len(lightStatus[0]) / 3)):
        c = lightStatus[0][i * 3: i * 3 + 3]
        c = c + lightStatus[1][i * 3: i * 3 + 3]
        c = c + lightStatus[2][i * 3: i * 3 + 3]
        c = c + lightStatus[3][i * 3: i * 3 + 3]
        c = c + lightStatus[4][i * 3: i * 3 + 3]
        s.append(patterns[c])

    return ''.join(s)

