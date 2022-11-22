result = 0
surnames = []
for i in range(int(input())):
    surnames.append(input())
for i in set(surnames):
    count = surnames.count(i)
    if count > 1:
        result += count
print(result)
