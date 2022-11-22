first = f'{int(input()):03d}'[-3:]
second = f'{int(input()):03d}'[-3:]
result = ''
for i in range(3):
    result += str(int(first[i]) + int(second[i]))[-1]
result = int(result)
print(result)
