filename = input()
line = int(input())

with open(filename, 'r', encoding="UTF-8") as f_in:
    result = [string.replace('\n', '') for string in f_in.readlines()]

for string in result[-line:]:
    print(string)
