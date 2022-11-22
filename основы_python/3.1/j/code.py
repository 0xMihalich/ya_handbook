string_list = []
while (string := input()) != 'ФИНИШ':
    string_list += list(string.lower().replace(' ', ''))
check = list(set(string_list))
check.sort()
max_chk = 0
result = check[0]
for i in check:
    chk = string_list.count(i)
    if chk > max_chk:
        result = i
        max_chk = chk
print(result)
