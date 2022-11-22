nods = []
for nod in range(int(input())):
    nods.append(int(input()))
nods.sort(reverse=True)
result = []
for b in nods[1:]:
    a = nods[0]
    while a != 0 and b != 0:
        if a > b: 
            a = a - b
        else: 
            b = b - a 
    result.append(max(a, b))
print(min(result))
