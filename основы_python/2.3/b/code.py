num = 0
while (string := input()) != "Приехали!":
    if "зайка" in string:
        num += 1
print(num)
