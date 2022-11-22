num = list(range(1, 1001))
separate = (len(num) // 2) - 1
print(num[separate])
while (command := input()) != "Угадал!":
    if command == "Меньше":
        num = num[:separate]
    elif command == "Больше":
        num = num[separate:]
    separate = len(num) // 2
    print(num[separate])
