from sys import stdin


result = 0
for line in stdin:
    for num in line.split():
        result += int(num)
print(result)
