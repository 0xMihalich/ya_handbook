def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mcd(n, m):
    return (n / gcd(n, m)) * m  


n = int(input())
m = int(input())
print(int(mcd(n, m)))
