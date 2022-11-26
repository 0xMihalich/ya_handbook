def gcd(a, b):
    while max(a, b) % min(a, b) != 0:
        if a > b:
            a = a % b
        elif a < b:
            b = b % a
    return min(a, b)
