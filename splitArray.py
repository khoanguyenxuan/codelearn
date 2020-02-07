def splitArray(arr):
    if len(arr) % 2 == 0:
        return False
    if arr[0] % 2 == 0 or arr[-1] % 2 == 0:
        return False
    return True