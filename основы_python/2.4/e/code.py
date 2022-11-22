result = 0
for strings in range(int(input())):
    string = []
    while (word := input()) != 'ВСЁ':
        string.append(word)
    if 'зайка' in string:
        result += 1
print(result)
