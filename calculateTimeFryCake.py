def calculateTimeFryCake(n, k):
    t = int(n / k) * 5
    if n % k == 0:
        return t * 2
    t = t + 5
    n = n - (k - n % k)
    t = t + int(n / k) * 5 + (1 if n % k > 0 else 0) * 5
    return t
