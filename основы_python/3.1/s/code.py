polskiu = []
s = input().split()
for x in s:
    if x == '+':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(g + z)
    elif x == '-':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(z - g)
    elif x == '*':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(g * z)
    else:
        polskiu.append(int(x))
print(polskiu[0])
