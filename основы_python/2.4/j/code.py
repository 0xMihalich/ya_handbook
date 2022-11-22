juice = int(input())
print('А Б В')
for a in range(1, juice + 1):
    for b in range(1, juice):
        for c in range(1, juice - 1):
            if a + b + c == juice:
                print(a, b, c)
