http_list = []
for i in range(int(input())):
    http_list.append(input())
word = input().lower()
for i in http_list:
    if word in i.lower():
        print(i)
