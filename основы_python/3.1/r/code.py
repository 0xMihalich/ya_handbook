num = input()
result = 0
first = num[0]
for i in num:
    if i == first:
        result += 1
    elif i != first:
        print(first, result)
        first, result = i, 1
        continue
print(first, result)
