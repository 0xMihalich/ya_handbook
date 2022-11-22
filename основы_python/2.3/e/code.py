total = 0
while (summ := float(input())) != 0:
    if summ >= 500:
        summ = summ * (1 - 10 / 100)
    total += summ
print(total)
