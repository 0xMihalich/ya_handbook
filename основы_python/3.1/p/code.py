long = int(input())
end = '...'
for n in range(int(input())):
    string = input()
    if long == 0:
        continue
    if len(string) + len(end) >= long:
        string = string[:long - len(end)] + end
    long -= len(string)
    print(string)
