from math import ceil


n = int(input())
square = [[0] * n for i in range(n)]
num, row = 1, 0
square[n // 2][n // 2] = ceil(n / 2)
size = len(str(square[n // 2][n // 2]))
for v in range(n // 2):
    number = f'{num: >{size}}'
    for i in range(n - row):
        square[v][i + v] = number
    for i in range(v + 1, n - v):
        square[i][-v - 1] = number
    for i in range(v + 1, n - v):
        square[-v - 1][-i - 1] = number
    for i in range(v + 1, n - (v + 1)):
        square[-i - 1][v] = number
    row += 2
    num += 1
for col in square:
    print(*col)
