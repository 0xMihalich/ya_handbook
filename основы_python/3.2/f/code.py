result = set()
sem_num = int(input())
oat_num = int(input())
for i in range(sem_num + oat_num):
    child = input()
    if child in result:
        result.discard(child)
    else:
        result.add(child)
result = list(result)
result.sort()
if not result:
    print('Таких нет')
else:
    for child in result:
        print(child)
