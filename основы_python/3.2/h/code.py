childs = {}
for i in range(int(input())):
    child = input().split()
    childs.update({child[0]: child[1:]})
search = input()
result = []
for k, v in childs.items():
    if search in v:
        result.append(k)
if not result:
    print('Таких нет')
else:
    result.sort()
    for child in result:
        print(child)
