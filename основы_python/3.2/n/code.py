foods = set()
dishes = {}
for i in range(int(input())):
    foods.add(input())
for i in range(int(input())):
    dish = input()
    food = set()
    for j in range(int(input())):
        food.add(input())
    dishes.update({dish: food})
result = []
for dish, food in dishes.items():
    if food <= foods:
        result.append(dish)
result.sort()
if not result:
    print('Готовить нечего')
else:
    for i in result:
        print(i)
