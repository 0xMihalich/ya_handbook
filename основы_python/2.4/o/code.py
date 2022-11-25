cols = int(input())
rows = int(input())
result = [[] for i in range(cols)]
size = len(str(cols * rows))
nums = [f'{j:>{size}}' for j in range(1, rows * cols + 1)]
reverse = 1
for col in [nums[i:i + cols] for i in range(0, len(nums), cols)]:
    for n, row in enumerate(col[::reverse]):
        result[n].append(row)
    reverse = -reverse
for row in result:
    print(' '.join(row))
