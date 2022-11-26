def num_definition(num):
    even = 0
    odd = 0
    for i in num:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        return 0
    elif even < odd:
        return 1
    elif even == odd:
        return 2


filename = input()
even_odd_eq_files = [open(input(), 'w', encoding="UTF-8") for i in range(3)]

with open(filename, 'r', encoding="UTF-8") as f_in:
    for line in f_in.readlines():
        even_odd_eq = [[], [], []]
        for num in line.split():
            even_odd_eq[num_definition(num)].append(num)
        for n in range(3):
            even_odd_eq_files[n].write(' '.join(even_odd_eq[n]) + '\n')
for file in even_odd_eq_files:
    file.close()
