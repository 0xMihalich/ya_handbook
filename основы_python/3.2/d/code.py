sem = set()
oat = set()
sem_num = int(input())
oat_num = int(input())
for i in range(sem_num):
    sem.add(input())
for i in range(oat_num):
    oat.add(input())
result = sem & oat
print(len(result) if result else 'Таких нет')
