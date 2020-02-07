import math


def happyPrime(number):
    if number <= 1:
        return False

    if number == 2:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return len(list(str(number))) == len(set(list(str(number))))