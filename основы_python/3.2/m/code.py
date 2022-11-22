dishes = set()
for i in range(int(input())):
    dishes.add(input())
for i in range(int(input())):
    for j in range(int(input())):
        dishes.discard(input())
dishes = list(dishes)
dishes.sort()
if not dishes:
    print('Готовить нечего')
else:
    for dish in dishes:
        print(dish)
