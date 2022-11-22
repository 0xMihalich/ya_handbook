s1 = int(input())

for i in range(1, s1 + 1):
    for j in range(i, i * s1 + 1, i):
        print(j, end=' ')
    print()
