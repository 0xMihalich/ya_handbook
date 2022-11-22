num = input()

numlist = [int(num[1]) + int(num[2]), int(num[0]) + int(num[1])]
numlist.sort(reverse=True)
print(f'{numlist[0]}{numlist[1]}')
