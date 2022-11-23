col = int(input())
for row in (list(str(j) for j in range(1 * i, (col + 1) * i, i)) for i in range(1, col + 1)):
    print(' '.join(row))
