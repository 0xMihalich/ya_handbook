from sys import stdin


for line in stdin:
    comm = line.find('#')
    if comm == 0:
        continue
    print(line[:comm])
