from itertools import combinations


digits = input()

digitlist = []

for num_1, num_2 in list(combinations(digits, 2)):
    first = int(num_1 + num_2)
    second = int(num_2 + num_1)
    for num in (first, second):
        if num >= 10:
            digitlist.append(num)

digitlist.sort()

print(digitlist[0], digitlist[-1])
