drop = int(input())
end = '...'
for i in range(int(input())):
    string = input()
    if len(string) > drop:
        string = string[:drop - 3] + end
    print(string)
