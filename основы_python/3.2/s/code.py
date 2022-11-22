toys_set = set()
second_toys = set()
for i in range(int(input())):
    child, toys = input().split(': ')
    toys = toys.split(', ')
    for toy in toys:
        if toy in toys_set:
            second_toys.add(toy)
        toys_set.add(toy)
result = list(toys_set ^ second_toys)
result.sort()
for toy in result:
    print(toy)
