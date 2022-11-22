weight = int(input())
height = int(input())
square = [str(j) for j in range(1, weight * height + 1)]
lens = len(square[-1])
for i in range(weight):
    print(' '.join(' ' * (lens - len(j)) + j for j in square[:height]))
    square = square[height:]
