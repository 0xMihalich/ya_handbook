babylist = {}
for i in range(int(input())):
    name = input()
    num = 0
    for j in list(input()):
        num += int(j)
    babylist.update({num: name})
print(babylist[max(babylist)])
