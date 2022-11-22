N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

total = N * M
result1 = []
result2 = []
for i in range(N):
    num = i + 1
    result1.append(num * K1)
    result2.append(num * K2)
for num1, k1 in enumerate(result1):
    for num2, k2 in enumerate(result2):
        if (k1 + k2) == total:
            if (num1 + num2 + 2) == N:
                print(num1 + 1, num2 + 1)
                break
