polskiu = []
 
 
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n
 
 
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
    elif x == '#':
        polskiu.append(polskiu[-1])
    elif x == '@':
        polskiu.append(polskiu[-2])
        polskiu.append(polskiu[-2])
        polskiu.append(polskiu[-5])
        del polskiu[-4]
        del polskiu[-4]
        del polskiu[-4]
    elif x == '/':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(z // g)
    elif x == '~':
        g = polskiu.pop()
        polskiu.append(-g)
    elif x == '!':
        g = polskiu.pop()
        polskiu.append(fac(g))
    else:
        polskiu.append(int(x))
print(polskiu[0])
