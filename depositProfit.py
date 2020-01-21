import math
def depositProfit(deposit, rate, threshold):
    return math.ceil(math.log(threshold / deposit, rate / 100 + 1))
