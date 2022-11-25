from sys import stdin


search = []
for line in stdin:
    search.append(line.replace('\n', ''))
for line in search[:-1]:
    if search[-1].lower() in line.lower():
        print(line)
