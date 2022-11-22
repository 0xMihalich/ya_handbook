num = input()
numlist = [int(num[0]), int(num[1]), int(num[2])]
numlist.sort()
if numlist[0] + numlist[2] == numlist[1] * 2:
    print('YES')
else:
    print('NO')
