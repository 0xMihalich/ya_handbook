result = []
surnames = []
for i in range(int(input())):
    surnames.append(input())
check = list(set(surnames))
check.sort()
for i in check:
    count = surnames.count(i)
    if count > 1:
        result += [f'{i} - {count}']
if not result:
    print('Однофамильцев нет')
else:
    for i in result:
        print(i)
