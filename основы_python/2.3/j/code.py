x = 0
y = 0

while (coordinate := input()) != "СТОП":
    num = int(input())
    if coordinate == 'СЕВЕР':
        x += num
    elif coordinate == 'ЮГ':
        x -= num
    elif coordinate == 'ВОСТОК':
        y += num
    elif coordinate == 'ЗАПАД':
        y -= num

print(x)
print(y)
