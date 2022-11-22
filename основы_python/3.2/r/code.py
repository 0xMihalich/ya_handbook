def symbols(c, d):
    if int(c) < 10:
        a = 0
    else:
        a = c[:-1]
    if int(d) < 10:
        b = 0
    else:
        b = d[:-1]
    e = str(a) + str(b)
    return (e)


dict = {}
lst = []
for i in range(int(input())):
    koord = input().split()
    a = symbols(koord[0], koord[1])
    if a in dict:
        dict[a] += 1
    else:
        dict.update({a: 1})
for i in dict:
    lst.append(dict[i])
lst.sort()
print(lst[-1])
