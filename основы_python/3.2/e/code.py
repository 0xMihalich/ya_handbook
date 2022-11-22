result = set()
sem_num = int(input())
oat_num = int(input())
for i in range(sem_num + oat_num):
    child = input()
    if child in result:
        result.discard(child)
    else:
        result.add(child)
print(len(result) if result else 'Таких нет')
