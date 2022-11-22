def is_prime(a):
    if a == 1:
        return False
    elif a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


result = is_prime(int(input()))
print('YES' if result else 'NO')
