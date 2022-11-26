rows = int(input())
cols = int(input())
for i in range(1, rows + 1):
    result = '|'.join(f'{j:^{cols}}' for j in range(i, i * rows + 1, i))
    print(result)
    if i < rows:
        print('-' * len(result))
