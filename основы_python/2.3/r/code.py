n = int(input())
dx = []
k = 2
while k <= n ** 0.5:
    if n % k == 0:
        dx.append(k)
        n = n // k
    else:
        k += 1
if n > 1:
    dx.append(n)
print(' * '.join(str(s) for s in dx))
