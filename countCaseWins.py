def countCaseWins(n):
    k = int((n - 1) / 2) + 1
    k_gt = 1
    n_gt = 1

    for i in range(1, k + 1):
        k_gt = k_gt * i

    for i in range(n - k + 1, n + 1):
        n_gt = n_gt * i

    return int(n_gt / k_gt)


print(countCaseWins(3))
