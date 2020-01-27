def isValidGuestPassword(password):
    l = []
    for p in password:
        if len(p) != 8 or len(set(p)) != 8:
            return False
        l.append(''.join(sorted(p)))
    return len(set(l)) == 5

isValidGuestPassword(["ab123456","bcgh4567","c3d451gf","bcgl4567","c3d4n3gf"])
