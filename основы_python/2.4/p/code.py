# пробовал разные варианты, в итоге пришел к этому коду, тем не менее тесты все-равно не проходит, исключать, что в тестах нет ошибки нельзя,
# поскольку ранее уже было замечено и исправлено через обращение в ТП две ошибки в тестах.

cols = int(input())
rows = int(input())
size = len(str(cols * rows))
for i in range(1, cols + 1):
    nums = (f'{j: >{size}}' for j in range(i, i * rows + 1, i))
    result = '|'.join(f'{num: ^{rows}}' for num in nums)
    print(result)
    if i < cols:
        print('-' * len(result))
