def isIPv4Address(inputString):
    parts = inputString.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        if not 0 <= int(item) <= 255:
            return False
    return True
