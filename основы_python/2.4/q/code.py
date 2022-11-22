result = 0
for i in range(int(input())):
    if (num := input()) == num[::-1]:
        result += 1
print(result)
