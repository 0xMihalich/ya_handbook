def is_prime(a):
    if a == 1:
        return False
    elif a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


result = 0
for i in range(int(input())):
    num = int(input())
    if is_prime(num):
        result += 1
print(result)
