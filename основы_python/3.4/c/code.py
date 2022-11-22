from itertools import count


start, stop, step = (float(num) for num in input().split())
for value in count(start, step):
    if value <= stop:
        print(f'{value: .2f}')
    else:
        break
