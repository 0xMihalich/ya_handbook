result = 0
for i in range(int(input())):
    for j in input().split():
        if j == 'зайка':
            result += 1
print(result)
