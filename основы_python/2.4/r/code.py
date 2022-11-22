num_list = [str(i + 1) for i in range(int(input()))]
string_list = []
range_start = 1
while True:
    if not num_list:
        break
    string_list.append(' '.join(num_list[:range_start]))
    num_list = num_list[range_start:]
    range_start += 1
lenstr = len(string_list[-1])
for string in string_list:
    print(f'{string:^{lenstr}}')
