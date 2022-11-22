a = int(input())
blockchain_right = True
for i in range(a):
    if i == 0:
        h1 = 0
    else:
        h1 = h
    b = int(input())
    h = b % 256
    b //= 256
    r = b % 256
    b //= 256
    m = b
    if ((h != 37 * (m + r + h1) % 256) or (h >= 100)) and blockchain_right:
        print(i)
        blockchain_right = False
if blockchain_right:
    print('-1')
