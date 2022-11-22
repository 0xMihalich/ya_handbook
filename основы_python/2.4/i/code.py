num = ''
for i in range(int(input())):
    num += f'{max(int(j) for j in list(input()))}'
print(num)
