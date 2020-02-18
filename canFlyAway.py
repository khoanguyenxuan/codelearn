def canFlyAway(h, arr):
    if min(arr) < h:
        return False

    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) > 1000:
            return False
    return True
