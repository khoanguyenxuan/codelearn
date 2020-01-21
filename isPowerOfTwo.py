def isPowerOfTwo(n):
    b = bin(n).split('b')[1]
    for i in range(1, len(b)):
        if b[i] == '1':
            return False
    return True

print (isPowerOfTwo(0))