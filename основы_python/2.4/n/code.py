weight = int(input())
height = int(input())
square = [str(j) for j in range(1, weight * height + 1)]
lens = len(square[-1])
for i in range(weight):
    result = square[:height]
    if i % 2:
        result = reversed(result)
    square = square[height:]
    print(' '.join(' ' * (lens - len(j)) + j for j in result))
