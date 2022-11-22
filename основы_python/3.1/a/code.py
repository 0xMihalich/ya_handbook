strings = []
for i in range(int(input())):
    strings.append(input())
if all(string[0] in ('а', 'б', 'в') for string in strings):
    print('YES')
else:
    print('NO')
