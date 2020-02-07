import math

def cutTheRope(wood):
    if wood <= 10:
        return 0

    n = int(wood / 10)
    if wood % 10 != 0:
        n = n + 1

    return int(math.ceil(math.log2(n)))
