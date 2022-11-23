from itertools import accumulate


for item in accumulate(input().split(), lambda *args: ' '.join(args)):
    print(item)
